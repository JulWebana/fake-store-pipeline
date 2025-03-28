# Import necessary libraries

import requests                                        # To make an HTTP request to the Fake Store API
import pandas as pd                                    # For manipulating data as DataFrames
from google.cloud import storage                       # To interact with Google Cloud Storage (GCS)
from pathlib import Path                               # For handling file paths
from config import BUCKET_NAME, DESTINATION_BLOB_NAME  # GCS config from external file


print("Script has started...")


def fetch_product_data():
    """
    Retrieves product data from the Fake Store API.

    """

    url = "https://fakestoreapi.com/products"

    response = requests.get(url)         # Send GET request

    response.raise_for_status()          # Raise an error if the HTTP status is not 200
    
    return response.json()               # Return data as JSON



def save_to_csv(data, file_path):
    """
    Saves JSON product data into a local CSV file.
    """
    df = pd.DataFrame(data)              # Convert JSON to pandas DataFrame

    df.to_csv(file_path, index=False)    # Save DataFrame to CSV without index

    print(f"Data saved locally : {file_path}")
    return file_path



def upload_to_gcs(local_file_path, bucket_name, destination_blob_name):
    """
    Uploads a local file to a Google Cloud Storage bucket.
    """
    client = storage.Client(project="copper-site-454601-i7")   # Initializes GCS client

    bucket = client.bucket(bucket_name)                        # Retrieve the bucket

    blob = bucket.blob(destination_blob_name)                  # Create a blob (GCS object)

    blob.upload_from_filename(local_file_path)                 # Upload the local file to GCS

    print(f"File uploaded to: gs://{bucket_name}/{destination_blob_name}")


if __name__ == "__main__":
    data_dir = Path("data")                               # Define local data directory

    data_dir.mkdir(exist_ok=True)                         # Create it if it doesn't exist

    local_file = data_dir / "products.csv"                # Define local file path


    print("Fetching data from Fake Store API...")
    product_data = fetch_product_data()                   # API call
    

    print("Saving data locally...")
    save_to_csv(product_data, local_file)                 # Save to CSV
    

    print("Uploading to Google Cloud Storage...")
    upload_to_gcs(str(local_file), BUCKET_NAME, DESTINATION_BLOB_NAME)  # Upload to GCS