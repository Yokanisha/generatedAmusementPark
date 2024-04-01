from google.cloud import bigquery
from google.api_core.exceptions import NotFound

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):

    client = bigquery.Client()

    table_id = "generated-amusement-park.testing_eu3.visitor123"

    try:
        existing_table = client.get_table(table_id)
        print("Table already exists.")

    except NotFound:
        schema = [
            bigquery.SchemaField("entry_date", "TIMESTAMP"),
            bigquery.SchemaField("country", "STRING"),
            bigquery.SchemaField("entry_id", "INT64"),
            bigquery.SchemaField("identification_card_id", "INT64"),
            bigquery.SchemaField("__index_level_0__", "INT64")
        ]

    table = bigquery.Table(table_id, schema=schema)
    table.time_partitioning = bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field="entry_date",  # name of column to use for partitioning
        expiration_ms=1000 * 60 * 60 * 24 * 90,
    )  # 90 days

    table = client.create_table(table)

    print(
        f"Created table {table.project}.{table.dataset_id}.{table.table_id}, "
        f"partitioned on column {table.time_partitioning.field}."
    )

