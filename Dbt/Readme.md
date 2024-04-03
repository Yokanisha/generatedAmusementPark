# Data Build Tool (dbt)
This repository contains a data pipeline project for processing data from various sources for the Generated Amusement Park. The pipeline utilizes the dbt (Data Build Tool) framework for data transformation and enables the creation of analysis tables for visualization in Looker Studio.

## DAG Overview
The DAG (Directed Acyclic Graph) diagram illustrates the flow direction and dependencies between various data processing steps in the pipeline. The key steps include:

**Manual Formatting of Sed Files:** Data from the 5 Sed files were manually formatted into CSV files to prepare them for further processing.

**Data Type Conversion and Column Renaming:** After loading the CSV files, data types were correctly converted, and column names were adjusted to ensure a uniform data structure.

**Data Integration from BigQuery:** Data for the `staging.action` and `staging.visitor` tables were loaded from BigQuery. Here too, data types were correctly converted, and column naming was adjusted if necessary.

**Dimension Tables:** Several dimension tables such as `dim_drink`, `dim_french_fries`, `dim_icecream`, and `dim_souvenir` were created. These were connected to the corresponding staging tables (`staging.action` and `staging.visitor`) to enable comprehensive analysis.

**Creation of Analysis Tables:** The `action` and `visitor` tables were merged to create a single table used for visualization in Looker Studio.

## Using dbt
The **Data Build Tool (dbt)** is used in this project to define the data pipeline and automate the transformation processes. Dbt facilitates easy management of data models, versioning of transformation steps, and integration into existing data infrastructures.

## Installation and Execution

To set up and run this project, we utilized dbt Cloud. To create an account and utilize the service, please visit the dbt [Cloud website](https://www.getdbt.com/product/dbt-cloud) and follow the [instructions](https://docs.getdbt.com/guides) to create an account. Once your account is set up, you can access detailed guidelines and documentation on how to proceed with dbt Cloud on the dbt Cloud documentation page. These resources offer comprehensive guidance on setting up and managing projects within dbt Cloud. After creating your account, integrate this repository into dbt Cloud to obtain the code directly. Follow the instructions provided in the dbt Cloud user interface or utilize the dbt CLI to clone the repository and configure it as necessary. Utilize the features of dbt Cloud to compile and execute your models, monitoring the progress of execution and troubleshooting any issues as needed. Once the models have been successfully executed, you can use the created analysis tables in Looker Studio to generate data visualizations and reports. For assistance with setting up your dbt Cloud account or utilizing the platform, feel free to reach out to the dbt Cloud support team. Additionally, extensive resources are available in the dbt community to provide support and exchange best practices.
