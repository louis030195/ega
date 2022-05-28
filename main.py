from typing import Optional, Tuple
from history import get_browserhistory
import schedule
import time
import fire
import logging
from datasets import Dataset, DatasetInfo
import gcsfs
import os
from google.cloud import storage
from google.cloud import bigquery
import pandas as pd


def _setup_big_query() -> Tuple[bigquery.Client, bigquery.Table]:
    """
    Setup BigQuery for a new integration.
    """
    client = bigquery.Client()
    project = client.project
    dataset_id = f"{project}.ega"
    try:
        dataset = client.get_dataset(dataset_id)
        print(f"Dataset {dataset_id} already exists")
    except Exception as e:
        print(e)
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "EU"
        dataset = client.create_dataset(dataset, timeout=30)
        print(f"Created dataset {client.project}.{dataset.dataset_id}")

    table_id = "ega"
    table_ref = dataset.table(table_id)
    table = bigquery.Table(table_ref)
    try:
        table = client.create_table(table)
    except Exception as e:
        print(e)
    return client, table


def publish(
    bucket_name: str = "ega-030195",
    frequency_in_hours: int = 10,
    logs_path: Optional[str] = "~/Desktop/ega.log",
):
    """
    Regularly fetch and publish your Google Chrome history
    :param bucket_name: Name of the GCS bucket to publish to
    :param frequency_in_hours: How often to fetch and publish
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename=os.path.expanduser(logs_path) if logs_path else None,
    )

    logging.info("Synchronizing Google Chrome history")
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    if not bucket.exists():
        logging.info(f"Bucket {bucket_name} does not exist, creating")
        storage_client.create_bucket(bucket_name)

    gcs = gcsfs.GCSFileSystem()

    bigquery_client, bigquery_table = _setup_big_query()

    def job():
        try:
            history = get_browserhistory()
            # turn [[url,title,date]] into {"url": [urls], "title": [titles], "date": [dates]}
            history_ds = {
                "url": [],
                "title": [],
                "date": [],
                "browser": [],
            }
            for k, v in history.items():
                for url, title, date in v:
                    history_ds["url"].append(url)
                    history_ds["title"].append(title)
                    history_ds["date"].append(date)
                    history_ds["browser"].append(k)

            logging.info(f"Found {len(history_ds['url'])} history entries")
            gcs_path = f"gcs://{bucket_name}"
            version = "0.0.1"
            try:
                # TODO: append history
                raise NotImplementedError
                # dataset = load_from_disk(bucket_name, fs=gcs)
                # append rows to existing dataset and update version
                # dataset.add_item(history_ds)
                # dataset.version = version
            except Exception as e:
                logging.warning(
                    f"Could not load dataset from {gcs_path} {e}, creating new dataset"
                )
                dataset = Dataset.from_dict(
                    history_ds,
                    info=DatasetInfo(
                        version=version,
                    ),
                )
            dataset.save_to_disk(gcs_path, fs=gcs)
            logging.info(f"Synced dataset with Google Cloud")

            job = bigquery_client.load_table_from_dataframe(
                pd.DataFrame(history_ds),
                bigquery_table.reference,
                job_config=bigquery.LoadJobConfig(
                    schema_update_options=["ALLOW_FIELD_ADDITION"]
                ),
            )
            result = job.result()
            logging.info(f"Loaded {result.output_rows} rows to BigQuery")

        except Exception as e:
            logging.error(e)
    schedule.every(frequency_in_hours).hours.do(job)
    schedule.run_all()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    fire.Fire(publish)
