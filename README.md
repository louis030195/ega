# ega

Ego but female, because all AI assistants are female.

The goal is to implement tools that

1. Collect data about yourself (Google Search, YouTube, books, what you see, at least what can be captured by mobile computer sensors, i.e. your inputs)
2. Process and analyze data, build AI models, assistants, UI, etc.

See [issues](https://github.com/louis030195/ega/issues) for discussing ideas.

## Why?

- No software exists to collect private data.
- Thus, softwares cannot use private data to build AI models.

## Usage

```bash
gcloud projects list
gcloud config set project MY_PROJECT
```

### MacOS script on boot

https://stackoverflow.com/questions/6442364/running-script-upon-login-mac

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
