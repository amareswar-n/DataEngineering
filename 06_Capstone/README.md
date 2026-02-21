# 🚀 Space-Themed Data Engineering Capstone

Welcome to the Data Engineering Capstone directory. This repository contains 20 progressive projects spanning from foundational data extraction to elite-level enterprise platform engineering. 

Each project is contained within its own directory with a production-grade structure (src, dbt, dags, tests, etc.) and its own specific requirements.

## 📂 Project Roadmap & Directory Index

| # | Project Name | Description | Architecture |
|---|---|---|---|
| 1 | [01_Meteor](./01_Meteor) | Build a daily batch ETL script to extract, clean, and load raw CSVs. | Python, Pandas, PostgreSQL |
| 2 | [02_Comet](./02_Comet) | Design a simple star schema data warehouse and load dimensional data. | PostgreSQL, Bash, Cron |
| 3 | [03_Satellite](./03_Satellite) | Schedule API pulls of ISS locations and dump raw JSON to cloud storage. | Apache Airflow, Python, S3/GCS |
| 4 | [04_Orbit](./04_Orbit) | Transform raw asteroid data into clean, analytical views in a cloud warehouse. | dbt Core, Snowflake/BigQuery |
| 5 | [05_Asteroid](./05_Asteroid) | Establish a Lakehouse to store large volumes of structured/semi-structured data. | Apache Iceberg/Delta Lake, AWS S3 |
| 6 | [06_Eclipse](./06_Eclipse) | Process massive datasets focusing on optimal partitioning and bucketing. | PySpark, AWS S3/HDFS |
| 7 | [07_Nebula](./07_Nebula) | Build a deep Kimball dimensional model (Fact/Dimensions, SCD Type 2). | dbt, Kimball Methodology |
| 8 | [08_Pulsar](./08_Pulsar) | Integrate data quality testing to halt pipelines upon anomaly detection. | Great Expectations, Airflow |
| 9 | [09_Quasar](./09_Quasar) | Build a lambda architecture handling real-time streams and batch reconciliations. | Apache Kafka, Spark Streaming |
| 10 | [10_Nova](./10_Nova) | Capture Change Data (CDC) from an operational database to stream to a warehouse. | Debezium, Kafka, Snowflake |
| 11 | [11_Constellation](./11_Constellation) | Orchestrate a complex DAG triggering external compute and dbt transformations. | Airflow, Databricks, dbt |
| 12 | [12_Galaxy](./12_Galaxy) | Implement data observability to automatically track freshness and schema changes. | Monte Carlo / Databand, dbt |
| 13 | [13_Supernova](./13_Supernova) | Monitor the infrastructure of the data platform itself (CPU, memory, DAGs). | Prometheus, Grafana, StatsD |
| 14 | [14_BlackHole](./14_BlackHole) | Deploy a highly available data architecture spanning multiple geographic regions. | Terraform, AWS/GCP Multi-region |
| 15 | [15_Wormhole](./15_Wormhole) | Build a pipeline to analyze cloud warehouse usage and automate cost reductions. | FinOps tools, Snowflake/BigQuery |
| 16 | [16_MilkyWay](./16_MilkyWay) | Perform chaos engineering on clusters to ensure pipeline resilience. | Chaos Mesh, Kubernetes |
| 17 | [17_Cosmos](./17_Cosmos) | Design decentralized data domains with cross-domain federated querying. | AWS Lake Formation, Trino |
| 18 | [18_Andromeda](./18_Andromeda) | Orchestrate data movement and processing across 3 major cloud providers. | Azure Data Factory, GCP BigQuery, AWS S3 |
| 19 | [19_EventHorizon](./19_EventHorizon) | Create a self-service platform with metadata management and strict SLAs. | DataHub, Terraform, SLA Alerting |
| 20 | [20_Singularity](./20_Singularity) | Governed, self-service, hybrid architecture supporting BI and ML simultaneously. | Medallion + Mesh, Real-time + ML, Data Contracts |

---
*Note: Navigate to each respective directory to view detailed instructions, required datasets, and setup guides.*
