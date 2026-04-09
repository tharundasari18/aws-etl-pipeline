AWS Serverless ETL Pipeline (S3 + Lambda + Glue + Athena)

**Overview

This project demonstrates a complete serverless ETL pipeline built using AWS services. The pipeline ingests raw CSV data, processes and partitions it using Lambda, optimizes it into Parquet format using AWS Glue, and enables querying using Amazon Athena.

Architecture

S3 (Raw Data)
→ Lambda (Data Cleaning + Partitioning)
→ S3 (Processed Data)
→ Glue Job (CSV → Parquet Conversion)
→ S3 (Parquet Data)
→ Athena (Query Layer)

Technologies Used

* Amazon S3
* AWS Lambda (Python, boto3)
* AWS Glue (ETL + Parquet conversion)
* AWS Glue Crawler (Schema detection)
* Amazon Athena (SQL queries)

Workflow Explanation

1. Raw CSV data is uploaded to S3
2. Lambda function is triggered automatically
3. Data is cleaned and partitioned by year
4. Processed data is stored in S3 in partitioned folders
5. Glue job converts CSV data into Parquet format
6. Glue crawler detects schema and creates table
7. Athena queries the data using SQL

Features

* Serverless architecture
* Event-driven ETL pipeline
* Partitioning for faster queries
* Parquet optimization for cost and performance
* Schema-on-read using Athena

⚠️ Issues Faced & Fixes

### 1. IAM Permission Error

* Issue: Glue job failed with AccessDenied error
* Fix: Added AmazonS3FullAccess policy to Glue IAM role

### 2. Partition Not Detected

* Issue: Athena was not showing any data
* Fix: Used MSCK REPAIR TABLE to load partitions

### 3. Schema Mismatch

* Issue: Columns were showing NULL values
* Fix: Corrected column names and mapping between CSV and Athena table

### 4. Data Not Updating

* Issue: Old parquet files were mixing with new data
* Fix: Deleted old data from S3 before rerunning Glue job

### 5. CSV Header Issue

* Issue: First row treated as data
* Fix: Used TBLPROPERTIES ("skip.header.line.count"="1")

>Key Learnings

* Difference between partitioning and file format optimization
* Importance of schema alignment in ETL pipelines
* Handling IAM permissions in AWS
* Performance benefits of Parquet over CSV
* Real-world debugging in data pipelines

💼 Interview Summary

Built a serverless ETL pipeline using AWS S3, Lambda, Glue, and Athena to process and optimize data. Implemented partitioning and Parquet conversion to improve query performance and reduce cost.
