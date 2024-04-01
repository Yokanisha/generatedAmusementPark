from google.cloud import bigquery
from google.api_core.exceptions import NotFound

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    client = bigquery.Client()

    table_id = "generated-amusement-park.testing_123.action123"

    try:
        existing_table = client.get_table(table_id)
        print("Table already exists.")
    except NotFound:
        schema = [
            bigquery.SchemaField("identification_card_id", "INTEGER"),
            bigquery.SchemaField("ice_cream_parlor", "INTEGER"),
            bigquery.SchemaField("french_fries", "INTEGER"),
            bigquery.SchemaField("drink", "INTEGER"),
            bigquery.SchemaField("souvenir", "INTEGER"),
            bigquery.SchemaField("__index_level_0__", "INTEGER"),
        ]

        table = bigquery.Table(table_id, schema=schema)
        table.range_partitioning = bigquery.RangePartitioning(
            field="identification_card_id",
            range_=bigquery.PartitionRange(start=0, end=100000, interval=10),
        )
        table = client.create_table(table)  # Make an API request.
        print(
            "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
        )


