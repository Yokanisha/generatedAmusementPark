# Generated Amusement Park Project

This project was created for the final project of DataEngineering-ZoomCamp-2024.

The goal of this project is to demonstrate the ability to develop an end-to-end project after completing the ZoomCamp. It was important to utilize certain technologies that are of great significance to a Data Engineer. Since I couldn't find suitable data of personal interest in a short amount of time, nor suitable data models to develop, I decided to generate my own data.

## Overview
In this project, we received data from a new amusement park in Germany that has been operating for over a year. To obtain a clear overview of all the generated data, an end-to-end project was created to visualize the data and provide a comprehensive overview. The data is stored in GitHub. First, an overview of the data model will be provided, followed by the process from data extraction to visualization. The goal is to automate everything once the project is set up. For this purpose, the following technologies and tools were used:

Cloud - [Google Cloud Platform](https://cloud.google.com/?hl=de)

Containerization - [Docker](https://www.docker.com/)

Data build tool - [Dbt_cloud](https://www.getdbt.com/product/what-is-dbt)

Data Lake - [Google Cloud Storage](https://cloud.google.com/storage?hl=de)

Data Visualization - [Looker Studio](https://lookerstudio.google.com/navigation/reporting)

Data Warehouse - [BigQuery](https://cloud.google.com/bigquery/?hl=de&utm_source=google&utm_medium=cpc&utm_campaign=emea-de-all-de-dr-bkws-all-all-trial-e-gcp-1707574&utm_content=text-ad-none-any-DEV_c-CRE_554507997073-ADGP_Hybrid+%7C+BKWS+-+EXA+%7C+Txt+-+Data+Analytics+-+BigQuery-KWID_43700072687751150-kwd-12297987241-userloc_9044716&utm_term=KW_big%20query-NET_g-PLAC_&&gad_source=1&gclid=CjwKCAjw_LOwBhBFEiwAmSEQASbDWmL37ZnYTiF1i6c2uAxtPjz_p1DwuqN0-AvAHBjXPHmeu-SgBRoCYSEQAvD_BwE&gclsrc=aw.ds)

Infrastructure as Code software (IaC) - [Terraform](https://www.terraform.io/)

Language - [Python](https://www.python.org/)

Workflow Orchestration - [mage-ai](https://www.mage.ai/)

## Amusement Park Architecture

![Architecture](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Images/Architecture.png?raw=true)

The architecture (above) illustrates how the process operates. We integrate the Orchestrator-Workflow Mage-AI into Docker. Terraform is utilized to create tables for Google Cloud Storage and Google Cloud BigQuery. However, in this project, we will use Terraform solely for creating a table in Google Cloud Storage. For Google Cloud BigQuery, we will follow best practices and utilize Python for implementation.

Our approach involves creating an ETL pipeline in Mage-AI from a URL to Google Cloud Storage. We ensure that the data is transferred to Google Cloud Storage, the schema is correct, and the data is clean. With another pipeline, we create a staged table and export it to Google Cloud BigQuery. The data in BigQuery has not yet been modeled. Additionally, we have multiple tables, of which only one is required for visualization. Initially, we perform data modeling to gain an overview of our data:

![Data_modell](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Images/Data_model.png?raw=true)

Now, we have an overview and also the information on how to consolidate all data into one table.

For this process, we utilize dbt to transform the raw data into transformed data. Additionally, for practice, we manually import the seed files into DBT, which could also automatically handle two GZ files. Here is the result of the DAG:

![Data_modell](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Images/dbt-dag_white.png?raw=true)


## Analytics Dashboard


## Information about Each Technology

- To get information on how the data is generated, click [here](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Data_generator/Readme.md)
- For instructions on installing Mage-AI and detailed information on how the pipeline works, click [here](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Workflow_Orchestration_Mage/Readme.md)
- For a better overview of dbt, click [here](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Dbt/Readme.md)
- To learn about Terraform, click [here](https://github.com/Yokanisha/generatedAmusementPark/blob/main/Terraform/Readme.md)












