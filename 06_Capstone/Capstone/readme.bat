@echo off

set projects=SuperNova-00 BlackHole-01 Nebula-02 Quasar-03 Pulsar-04 EventHorizon-05 CosmicWeb-06 Singularity-07 DarkMatter-08 Wormhole-09 Helios-10 Atlas-11 Orion-12 Vega-13 Aurora-14 Polaris-15 Zenith-16 Hypernova-17 Magnetar-18 GalacticCore-19

:: Tech stack pools (pseudo-random assignment)
set clouds=AWS GCP Azure
set compute=Spark Flink Databricks
set stream=Kafka Pulsar Kinesis
set orchestrators=Airflow Prefect Dagster
set warehouses=Snowflake BigQuery Redshift

set i=0

for %%p in (%projects%) do (

    mkdir %%p
    mkdir %%p\ingestion
    mkdir %%p\streaming
    mkdir %%p\transformation\dbt_project
    mkdir %%p\orchestration\airflow_dags
    mkdir %%p\warehouse
    mkdir %%p\quality
    mkdir %%p\observability
    mkdir %%p\infra\terraform
    mkdir %%p\docs

    :: README with storytelling
    (
        echo # %%p
        echo.
        echo ## Data Domain
        echo Random enterprise domain (IoT / Finance / Gaming / Retail / Health)
        echo.
        echo ## High-Level Requirements
        echo - Real-time + batch ingestion
        echo - Medallion architecture
        echo - Data quality validation
        echo - Observability and alerting
        echo - CI/CD deployment
        echo.
        echo ## Tech Stack
        echo Cloud: AWS/GCP/Azure
        echo Compute: Spark/Flink
        echo Streaming: Kafka
        echo Orchestration: Airflow
        echo Warehouse: Snowflake/BigQuery
        echo IaC: Terraform
        echo Containers: Docker
        echo.
        echo ## Interview Story
        echo Demonstrates platform ownership, reliability engineering, cost optimisation, and architecture design.
    ) > %%p\README.md

    :: Terraform scaffold
    (
        echo provider "aws" {}
        echo resource "aws_s3_bucket" "data_lake" {}
    ) > %%p\infra\terraform\main.tf

    :: Airflow DAG starter
    (
        echo from airflow import DAG
        echo from airflow.operators.python import PythonOperator
        echo from datetime import datetime
        echo.
        echo with DAG("%%p_pipeline", start_date=datetime(2024,1,1), schedule="@daily") as dag:
        echo     pass
    ) > %%p\orchestration\airflow_dags\dag.py

    :: dbt scaffold
    (
        echo name: %%p
        echo version: 1.0
    ) > %%p\transformation\dbt_project\dbt_project.yml

    :: Observability scaffold
    (
        echo # Observability
        echo Logging + Metrics + Alerts
    ) > %%p\observability\README.md

    :: Architecture diagram
    (
        echo ```mermaid
        echo flowchart LR
        echo API-->Kafka-->Spark-->Lakehouse-->Warehouse
        echo ```
    ) > %%p\docs\architecture.md
)

echo ✅ Enterprise random projects generated
pause