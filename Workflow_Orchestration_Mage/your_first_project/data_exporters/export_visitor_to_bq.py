from google.cloud import bigquery

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    client = bigquery.Client()


    table_id = "generated-amusement-park.testing_eu3.visitor123"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
    )
    uri = "gs://amusement-park-bucket/visitor/visitor_date=2023-01-02/77e8c9a6e2c74667bf37a45f7c499883-0.parquet"

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))


