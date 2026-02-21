# Welcome to the Data Engineering Capstone directory. This repository contains 20 progressive projects spanning from foundational data extraction to elite-level enterprise platform engineering. 

## 📂 Project Roadmap & Directory Index

| # | Project | Domain | Description | Complexity | Architecture | Diagram | Status |
|---|---|---|---|---|---|---|---|
| 1 | [01_Meteor](./01_Meteor) | Aerospace | Build a daily batch ETL script to extract, clean, and load raw CSVs. | Beginner | Python, Pandas, PostgreSQL | [preview](./01_Meteor/docs/architecture.png) | ⬜ |
| 2 | [02_Comet](./02_Comet) | Astronomy | Design a simple star schema data warehouse and load dimensional data. | Beginner | PostgreSQL, Bash, Cron | [preview](./02_Comet/docs/architecture.png) | ⬜ |
| 3 | [03_Satellite](./03_Satellite) | Geospatial | Schedule API pulls of ISS locations and dump raw JSON to cloud storage. | Beginner | Apache Airflow, Python, S3/GCS | [preview](./03_Satellite/docs/architecture.png) | ⬜ |
| 4 | [04_Orbit](./04_Orbit) | Analytics | Transform raw asteroid data into clean, analytical views in a cloud warehouse. | Beginner | dbt Core, Snowflake/BigQuery | [preview](./04_Orbit/docs/architecture.png) | ⬜ |
| 5 | [05_Asteroid](./05_Asteroid) | Meteorology | Establish a Lakehouse to store large volumes of structured/semi-structured data. | Intermediate | Apache Iceberg/Delta Lake, AWS S3 | [preview](./05_Asteroid/docs/architecture.png) | ⬜ |
| 6 | [06_Eclipse](./06_Eclipse) | Transportation | Process massive datasets focusing on optimal partitioning and bucketing. | Intermediate | PySpark, AWS S3/HDFS | [preview](./06_Eclipse/docs/architecture.png) | ⬜ |
| 7 | [07_Nebula](./07_Nebula) | E-commerce | Build a deep Kimball dimensional model (Fact/Dimensions, SCD Type 2). | Intermediate | dbt, Kimball Methodology | [preview](./07_Nebula/docs/architecture.png) | ⬜ |
| 8 | [08_Pulsar](./08_Pulsar) | IoT Sensors | Integrate data quality testing to halt pipelines upon anomaly detection. | Intermediate | Great Expectations, Airflow | [preview](./08_Pulsar/docs/architecture.png) | ⬜ |
| 9 | [09_Quasar](./09_Quasar) | Telemetry | Build a lambda architecture handling real-time streams and batch reconciliations. | Advanced | Apache Kafka, Spark Streaming | [preview](./09_Quasar/docs/architecture.png) | ⬜ |
| 10 | [10_Nova](./10_Nova) | Transactions | Capture Change Data (CDC) from an operational database to stream to a warehouse. | Advanced | Debezium, Kafka, Snowflake | [preview](./10_Nova/docs/architecture.png) | ⬜ |
| 11 | [11_Constellation](./11_Constellation) | FinTech | Orchestrate a complex DAG triggering external compute and dbt transformations. | Advanced | Airflow, Databricks, dbt | [preview](./11_Constellation/docs/architecture.png) | ⬜ |
| 12 | [12_Galaxy](./12_Galaxy) | Internal Ops | Implement data observability to automatically track freshness and schema changes. | Advanced | Monte Carlo / Databand, dbt | [preview](./12_Galaxy/docs/architecture.png) | ⬜ |
| 13 | [13_Supernova](./13_Supernova) | Platform Eng | Monitor the infrastructure of the data platform itself (CPU, memory, DAGs). | Expert | Prometheus, Grafana, Airflow StatsD | [preview](./13_Supernova/docs/architecture.png) | ⬜ |
| 14 | [14_BlackHole](./14_BlackHole) | Global Identity | Deploy a highly available data architecture spanning multiple geographic regions. | Expert | Terraform, AWS/GCP Multi-region | [preview](./14_BlackHole/docs/architecture.png) | ⬜ |
| 15 | [15_Wormhole](./15_Wormhole) | FinOps | Build a pipeline to analyze cloud warehouse usage and automate cost reductions. | Expert | FinOps tools, Snowflake/BigQuery | [preview](./15_Wormhole/docs/architecture.png) | ⬜ |
| 16 | [16_MilkyWay](./16_MilkyWay) | SRE | Perform chaos engineering on clusters to ensure pipeline resilience. | Expert | Chaos Mesh, Kubernetes | [preview](./16_MilkyWay/docs/architecture.png) | ⬜ |
| 17 | [17_Cosmos](./17_Cosmos) | Enterprise Data | Design decentralized data domains with cross-domain federated querying. | Elite | AWS Lake Formation, Trino | [preview](./17_Cosmos/docs/architecture.png) | ⬜ |
| 18 | [18_Andromeda](./18_Andromeda) | Multi-cloud Ops | Orchestrate data movement and processing across 3 major cloud providers. | Elite | Azure Data Factory, GCP BigQuery, AWS S3 | [preview](./18_Andromeda/docs/architecture.png) | ⬜ |
| 19 | [19_EventHorizon](./19_EventHorizon) | Governance | Create a self-service platform with metadata management and strict SLAs. | Elite | DataHub, Terraform, SLA alerting | [preview](./19_EventHorizon/docs/architecture.png) | ⬜ |
| 20 | [20_Singularity](./20_Singularity) | AI/Enterprise | Governed, self-service, hybrid architecture supporting BI and ML simultaneously. | Ultimate | Medallion + Mesh, Real-time + ML, Data Contracts | [preview](./20_Singularity/docs/architecture.png) | ⬜ |

---
*Note: Click on any project name to view its specific README, detailed instructions, and setup guides.*
