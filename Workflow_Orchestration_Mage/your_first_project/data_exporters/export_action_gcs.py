from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path
import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/KEYS/my-creds.json"

bucket_name = 'amusement-park-bucket'
project_id = 'generated-amusement-park'
table_name = "action_new"
root_path = f'{bucket_name}/{table_name}'

# Funktion zum Partitionieren der Daten
def partition_data(data):
    num_rows = len(data)
    num_partitions = max(1, num_rows // 10000)  # Anzahl der Partitionen berechnen (mindestens 1)
    partitioned_data = []
    partition_size = num_rows // num_partitions
    partition_boundaries = [i * partition_size for i in range(num_partitions)]
    partition_boundaries.append(num_rows)
    for i in range(num_partitions):
        partition_data = data.iloc[partition_boundaries[i]:partition_boundaries[i+1]]
        partitioned_data.append(partition_data)
    return partitioned_data

@data_exporter
def export_data_to_google_cloud_storage(data, **kwargs) -> None:
    # Partitionieren der Daten
    partitioned_data = partition_data(data)

    # Schreiben der partitionierten Daten in Google Cloud Storage
    for i, partition in enumerate(partitioned_data):
        partition_path = f'{root_path}/partition_{i}'
        table = pa.Table.from_pandas(partition)
        gcs = pa.fs.GcsFileSystem()
        pq.write_to_dataset(table, root_path=partition_path, filesystem=gcs)

