# Data Pipelines

## Project Introduction
A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.
They have decided to bring you into the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.
The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

## Project Overview
This project will introduce you to the core concepts of Apache Airflow. To complete the project, you will need to create your own custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data as the final step.
We have provided you with a project template that takes care of all the imports and provides four empty operators that need to be implemented into functional pieces of a data pipeline. The template also contains a set of tasks that need to be linked to achieve a coherent and sensible data flow within the pipeline.
You'll be provided with a helpers class that contains all the SQL transformations. Thus, you won't need to write the ETL yourselves, but you'll need to execute it with your custom operators.

## Description of Project Files
`udac_example_dag.py` is the main DAG file. It contains all the taks definations and their dependencies.<br />
`create_tables.sql` contains the SQL queries used to create all the required tables in Redshift.<br />
`stage_redshift.py` contains defination of `StageToRedshiftOperator`. This operator copies data from s3 path to redshift table.<br />
`load_fact.py` contains defination of `LoadFactOperator`. This simple operator copies data using a select statement into a destination table.<br />
`load_dimension.py` contains defination of `LoadDimensionOperator`. It works like `LoadFactOperator`.<br />
`data_quality.py` contains  of `DataQualityOperator`. This operator checks the quality of the data. For simplicity, I have limited this operator to just verify the counts of records in a table. It takes an SQL count statement and verifies the returned value with an expected value.<br />
`sql_queries.py` contains the SQL queries used in the ETL process.<br />

## Pre-Requisite (Configurations)
Define following connections on Airflow's connection page.
- AWS Credentials
    - `Conn Id`: *aws_credentials*.
    - `Conn Type`: *Amazon Web Services*.
    - `Login`: Enter your Access key ID from the IAM User credentials.
    - `Password`: Enter your Secret access key from the IAM User credentials.
- Redshift Credentials
    - `Conn Id`: *redshift*.
    - `Conn Type`: *Postgres*.
    - `Host`: *Endpoint of your Redshift cluster, excluding the port at the end*.
    - `Schema`: This is the Redshift database you want to connect to.
    - `Login`: Username of the redshift user.
    - `Password`: *Enter the password you created when launching your Redshift cluster*.
    - `Port`: *5439*.

### Note that `Conn Id` parameterd must have exact names as mentioned above.
