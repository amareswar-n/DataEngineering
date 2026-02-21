# This repository contains 20 progressive projects spanning from foundational data extraction to elite-level enterprise platform engineering. 

## 📂 Project Roadmap & Directory Index

| # | Project | Domain | Description | Complexity | Architecture | Diagram | Status |
|---|---|---|---|---|---|---|---|
| 1 | [01_Meteor](./01_Meteor) | Aerospace | Build a daily batch ETL script to extract, clean, and load raw CSVs. | Beginner | Python, Pandas, PostgreSQL | [preview](./01_Meteor/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 2 | [02_Comet](./02_Comet) | Astronomy | Design a simple star schema data warehouse and load dimensional data. | Beginner | PostgreSQL, Bash, Cron | [preview](./02_Comet/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 3 | [03_Satellite](./03_Satellite) | Geospatial | Schedule API pulls of ISS locations and dump raw JSON to cloud storage. | Beginner | Apache Airflow, Python, S3/GCS | [preview](./03_Satellite/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 4 | [04_Orbit](./04_Orbit) | Analytics | Transform raw asteroid data into clean, analytical views in a cloud warehouse. | Beginner | dbt Core, Snowflake/BigQuery | [preview](./04_Orbit/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 5 | [05_Asteroid](./05_Asteroid) | Meteorology | Establish a Lakehouse to store large volumes of structured/semi-structured data. | Intermediate | Apache Iceberg/Delta Lake, AWS S3 | [preview](./05_Asteroid/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 6 | [06_Eclipse](./06_Eclipse) | Transportation | Process massive datasets focusing on optimal partitioning and bucketing. | Intermediate | PySpark, AWS S3/HDFS | [preview](./06_Eclipse/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 7 | [07_Nebula](./07_Nebula) | E-commerce | Build a deep Kimball dimensional model (Fact/Dimensions, SCD Type 2). | Intermediate | dbt, Kimball Methodology | [preview](./07_Nebula/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 8 | [08_Pulsar](./08_Pulsar) | IoT Sensors | Integrate data quality testing to halt pipelines upon anomaly detection. | Intermediate | Great Expectations, Airflow | [preview](./08_Pulsar/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 9 | [09_Quasar](./09_Quasar) | Telemetry | Build a lambda architecture handling real-time streams and batch reconciliations. | Advanced | Apache Kafka, Spark Streaming | [preview](./09_Quasar/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 10 | [10_Nova](./10_Nova) | Transactions | Capture Change Data (CDC) from an operational database to stream to a warehouse. | Advanced | Debezium, Kafka, Snowflake | [preview](./10_Nova/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 11 | [11_Constellation](./11_Constellation) | FinTech | Orchestrate a complex DAG triggering external compute and dbt transformations. | Advanced | Airflow, Databricks, dbt | [preview](./11_Constellation/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 12 | [12_Galaxy](./12_Galaxy) | Internal Ops | Implement data observability to automatically track freshness and schema changes. | Advanced | Monte Carlo / Databand, dbt | [preview](./12_Galaxy/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 13 | [13_Supernova](./13_Supernova) | Platform Eng | Monitor the infrastructure of the data platform itself (CPU, memory, DAGs). | Expert | Prometheus, Grafana, Airflow StatsD | [preview](./13_Supernova/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 14 | [14_BlackHole](./14_BlackHole) | Global Identity | Deploy a highly available data architecture spanning multiple geographic regions. | Expert | Terraform, AWS/GCP Multi-region | [preview](./14_BlackHole/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 15 | [15_Wormhole](./15_Wormhole) | FinOps | Build a pipeline to analyze cloud warehouse usage and automate cost reductions. | Expert | FinOps tools, Snowflake/BigQuery | [preview](./15_Wormhole/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 16 | [16_MilkyWay](./16_MilkyWay) | SRE | Perform chaos engineering on clusters to ensure pipeline resilience. | Expert | Chaos Mesh, Kubernetes | [preview](./16_MilkyWay/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 17 | [17_Cosmos](./17_Cosmos) | Enterprise Data | Design decentralized data domains with cross-domain federated querying. | Elite | AWS Lake Formation, Trino | [preview](./17_Cosmos/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 18 | [18_Andromeda](./18_Andromeda) | Multi-cloud Ops | Orchestrate data movement and processing across 3 major cloud providers. | Elite | Azure Data Factory, GCP BigQuery, AWS S3 | [preview](./18_Andromeda/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 19 | [19_EventHorizon](./19_EventHorizon) | Governance | Create a self-service platform with metadata management and strict SLAs. | Elite | DataHub, Terraform, SLA alerting | [preview](./19_EventHorizon/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |
| 20 | [20_Singularity](./20_Singularity) | AI/Enterprise | Governed, self-service, hybrid architecture supporting BI and ML simultaneously. | Ultimate | Medallion + Mesh, Real-time + ML, Data Contracts | [preview](./20_Singularity/README.md#%EF%B8%8F-architecture-diagram) | ⬜ |





|#|Project|Domain|Complexity|Signal|Architecture|Diagram|Status|
|---|---|---|---|---|---|---|---|
|1|[00_Aurora](./00_Aurora)|Finance|Beginner|⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|2|[01_Polaris](./01_Polaris)|Retail|Beginner|⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|3|[02_Vega](./02_Vega)|Retail|Beginner|⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|4|[03_Orion](./03_Orion)|Logs|Beginner+|⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|5|[04_Nebula](./04_Nebula)|IoT|Intermediate|⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|6|[05_GalacticCore](./05_GalacticCore)|AdTech|Intermediate|⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|7|[06_CosmicWeb](./06_CosmicWeb)|MultiDomain|Intermediate+|⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|8|[07_Atlas](./07_Atlas)|CDC|Intermediate+|⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|9|[08_Pulsar](./08_Pulsar)|IoT|Advanced|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|10|[09_Quasar](./09_Quasar)|Gaming|Advanced|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|11|[10_Hypernova](./10_Hypernova)|Hybrid|Advanced+|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|12|[11_Magnetar](./11_Magnetar)|Telecom|Advanced+|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|13|[12_DarkMatter](./12_DarkMatter)|Observability|Expert|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|14|[13_EventHorizon](./13_EventHorizon)|MultiRegion|Expert|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|15|[14_Wormhole](./14_Wormhole)|MultiCloud|Expert+|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|16|[15_BlackHole](./15_BlackHole)|Reliability|Expert+|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|17|[16_Singularity](./16_Singularity)|Mesh|Elite|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|18|[17_NovaPipeline](./17_NovaPipeline)|Platform|Elite|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|19|[18_StellarForge](./18_StellarForge)|Lakehouse|Elite+|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
|20|[19_SuperNova](./19_SuperNova)|Enterprise|Ultimate|⭐⭐⭐⭐⭐|Python, dbt, Spark|preview|⬜|
