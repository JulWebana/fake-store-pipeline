# Fake Store Ingestion Pipeline

This repository contains a Python pipeline to:

- Extract product data from the [Fake Store API](https://fakestoreapi.com/)
- Save it as CSV in a local data/ directory
- Upload the file to a Google Cloud Storage bucket


## Tech Stack
- Python
- Google Cloud Storage (GCS)
- Fake Store API
- virtualenv

## Project Structure

```
fake-store-pipeline/
├── .venv/                  # Virtual environment
├── data/                   # Folder to store CSVs
├── ingestion/
│   ├── config.py           # Contains GCS bucket config
│   └── fetch_products.py   # Script to fetch data from API and upload to GCS
├── requirements.txt 
└── README.md        # Python dependencies
```

## How to Run it :

```bash
# 1. Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the ingestion pipeline
python ingestion/fetch_products.py
```

## Output
The script fetches data from https://fakestoreapi.com/products

Saves it locally as data/products.csv

Uploads it to your configured GCS bucket


## Author
Julien T.W AGA 

Junior Data Engineer & Analytics Enthusiast – 2025

