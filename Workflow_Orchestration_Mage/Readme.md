# Configure Mage Ai

## How to Install mage ai and using Docker

The recommended way to install the latest version of Mage is through Docker with the following command:

`docker pull mageai/mageai:latest`

```bash
git clone https://github.com/mage-ai/compose-quickstart.git Workflow_Orchestration_Mage
cd Workflow_Orchestration_Mage
cp dev.env .env
rm dev.env
docker compose up
```

# What pipelines do we need
There are two types of pipelines we need.

First pipeline: This pipeline involves taking the csv.gz file via URL, transforming it, and exporting it to Google Cloud Storage.

Second pipeline: In this pipeline, we retrieve the files from Google Cloud Storage and export them to Google Cloud BigQuery.

Note: We are performing these actions with visitor.csv.gz and action.csv.gz.

## First pipeline - action.csv.gz
In this pipeline, we take the csv.gz file via URL, define the schema, and pass it to the next two transformers. The first transformer filters out rows where the values are positive (including zero), while the second transformer removes leading and trailing spaces from the values.

Note: These two transformers may not be necessary since we generated these files ourselves. However, if we were to retrieve data from an API or in real-world scenarios such as sensor data, the data might not be as clean. Therefore, for practice and to account for potential data cleanliness issues, we have included them.

Finally, we partition the data after a certain number of records. For every 10,000 records, we partition it and export it to Google Cloud Storage. Partitioning the data helps in faster uploading as it reduces memory consumption.

Here the pipeline: 
PICTURE <action_gcs.PNG>

## Second pipeline - action.csv.gz
This pipeline is not much different from the first one. Here, we take the csv.gz file via URL, define the schema, and pass it to the next two transformers. The first transformer filters out rows where the values are positive (including zero), while the second transformer removes leading and trailing spaces from the values. In contrast to the first pipeline, we also have higher values which have the data type string. For that reason, we introduce a third transformer to ensure that all values in the string column are in lower case.

Note: Similarly to the first pipeline, these three transformers may not be necessary since we generated these files ourselves.

Finally, we partition the data after the column entry_date, which is of type datetime. We partition it based on entry_date and export it to Google Cloud Storage. Partitioning the data helps in faster uploading as it reduces memory consumption.

Here the pipeline: 
PICTURE <visitor_gcs.PNG>
