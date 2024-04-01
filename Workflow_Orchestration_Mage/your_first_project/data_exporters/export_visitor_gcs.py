import pyarrow as pa
import pyarrow.parquet as pq
import os
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/KEYS/my-creds.json"

config_path = path.join(get_repo_path(), 'io_config.yaml')
config_profile = 'default'

bucket_name = 'amusement-park-bucket'
table_name = "visitor_new"

root_path = f'{bucket_name}/{table_name}'


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:


    df['visitor_date'] = df['entry_date'].dt.date

    table = pa.Table.from_pandas(df)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols = ['visitor_date'],
        filesystem = gcs,
        use_deprecated_int96_timestamps=True
    )
