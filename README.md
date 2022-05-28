# ega

Ego but female, because all AI assistants are female.

The goal is to implement tools that

1. Collect data about yourself (Google Search, YouTube, books, what you see, at least what can be captured by mobile computer sensors, i.e. your inputs)
2. Process and analyze data, build AI models, assistants, UI, etc.

See [issues](https://github.com/louis030195/ega/issues) for discussing ideas.

## Why?

- No software exists to collect private data.
- Thus, softwares cannot use private data to build AI models.

## Features

Regularly export desktop Chrome history as a [Huggingface dataset](https://huggingface.co/datasets) hosted on Google Cloud storage and as a [Google Cloud BigQuery](https://cloud.google.com/bigquery) table.

## Usage

```bash
gcloud projects list
gcloud config set project MY_PROJECT
# generate service account key file for owner
OWNER=$(gcloud iam service-accounts list --filter="displayName:owner" --format="value(email)")
gcloud iam service-accounts keys create key.json --iam-account=${OWNER}
export GOOGLE_APPLICATION_CREDENTIALS=key.json
python3 main.py --logs_path=None
```

![bigquery](docs/bigquery.png)

### MacOS script on boot

https://stackoverflow.com/questions/6442364/running-script-upon-login-mac

Using a [Automator](https://support.apple.com/en-au/guide/automator/welcome/mac) script

```bash
GOOGLE_APPLICATION_CREDENTIALS="PATH_TO_MY_JSON_SERVICE_ACCOUNT" GOOGLE_CLOUD_PROJECT="MY_GCP_PROJECT" PATH_TO_MY_VIRTUALENV_BIN/python3 PATH_TO_MY_EGA_DIR/main.py --bucket_name="MY_BUCKET" &> PATH_TO_LOGS/ega.log
```

### Linux cron

Something similar to above but in cron 😇

### Windows

We are in 2022 guys.

## Analytics

```bash
pip install plotly==5.6.0
```

```python
import gcsfs
from datasets import load_from_disk

gcs = gcsfs.GCSFileSystem() 

dataset = load_from_disk('my-bucket',fs=gcs)  
import plotly.express as px
import pandas as pd
import re
df = dataset.to_pandas()
websites = pd.Series([re.sub(r'^https?://(www\.)?', '', url).split("/")[0] for url in df['url']]).value_counts().rename_axis('websites').reset_index(name='visits')
fig = px.bar(
    websites.head(50),
    x="websites", y="visits", color="visits", title="History distribution")
fig.show()
fig.write_html("file.html")
```
