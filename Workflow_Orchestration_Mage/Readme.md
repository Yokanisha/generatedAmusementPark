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

`First pipeline:` This pipeline involves taking the `csv.gz file` via URL, transforming it, and exporting it to `Google Cloud Storage`.

`Second pipeline:` In this pipeline, we retrieve the files from `Google Cloud Storage` and export them to `Google Cloud BigQuery`.

Note: We are performing these actions with `visitor.csv.gz` and `action.csv.gz`.

## First pipeline - action.csv.gz
In this pipeline, we take the csv.gz file via URL, define the schema, and pass it to the next two transformers. The first transformer filters out rows where the values are positive (including zero), while the second transformer removes leading and trailing spaces from the values.

`Note:` These two transformers may not be necessary since we generated these files ourselves. However, if we were to retrieve data from an API or in real-world scenarios such as sensor data, the data might not be as clean. Therefore, for practice and to account for potential data cleanliness issues, we have included them.

Finally, we `partition` the data after a `certain number of records`. For every 10,000 records, we partition it and export it to Google Cloud Storage. Partitioning the data helps in faster uploading as it reduces memory consumption.

To automatically trigger the next pipeline, we add a trigger pipeline at the end, which executes the next pipeline named visitor_gcs.

Here the pipeline: 

![action_pipeline](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Images/pipeline_action_gcs.PNG?raw=true)

## Second pipeline - action.csv.gz
This pipeline is not much different from the first one. Here, we take the csv.gz file via URL, define the schema, and pass it to the next two transformers. The first transformer filters out rows where the values are positive (including zero), while the second transformer removes leading and trailing spaces from the values. In contrast to the first pipeline, we also have higher values which have the data type string. For that reason, we introduce a third transformer to ensure that all values in the string column are in lower case.

`Note:` Similarly to the first pipeline, these three transformers may not be necessary since we generated these files ourselves.

Finally, we `partition` the data after the `column entry_date`, which is of `type datetime`. We partition it based on entry_date and export it to Google Cloud Storage. Partitioning the data helps in faster uploading as it reduces memory consumption.

It automatically triggers the next pipeline named action_bq.

Here the pipeline: 

![visitor_pipeline](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Images/pipeline_visitor_gcs.PNG?raw=true)

## Pipeline - from gcs to bigquery

In this pipeline, we will first create a block that creates a partitioned table in BigQuery. Then, we will transfer the Parquet files from our storage into BigQuery as a table.

For visitor data, we create a partitioned table `partitioned by DAY`. For action data, we create a partitioned table partitioned by Integer range.

After executing the pipeline, we will have all the data in BigQuery that we need for the data modeling in dbt.

`Note:` At the end of the pipeline, the pipeline named action_bq triggers the pipeline named visitor_bq. After this step, all necessary files are stored in Google Cloud Storage and Google Cloud BigQuery.

| action_bq  | visitor_bq  |
|-----------------------------|--------------------------------|
| ![action_pipeline_bq](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Images/pipeline_action_bq.PNG?raw=true) | ![visitor_pipeline_bq](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Images/pipeline_visitor_bq.PNG?raw=true)|                                  |

## Schedule and trigger
As you are aware, we generate our own data and upload it to GitHub, where we retrieve the data using `mage-ai`. This means that if you intend to schedule the pipeline daily, monthly, etc., you also need to update the files daily, monthly, etc.

To simplify this process, instead of creating a schedule, we opt to trigger it `once`. This means that if you want to execute the entire project, simply execute the pipeline named `action_gcs`. With the trigger blocks, it will sequentially execute the other necessary pipelines.

Here is the trigger flow:
```
action_gcs -> visitor_gcs -> action_bq -> visitor_bq
```
![Pipelines](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Images/Pipelines.PNG?raw=true)
If you wish to create a schedule, follow these steps:

Navigate to Triggers -> New Triggers -> Schedule.

Adjusting the schedule is straightforward. Ensure that only the pipeline named action_gcs is scheduled because it will trigger the other necessary pipelines.
