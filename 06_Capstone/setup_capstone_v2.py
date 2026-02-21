import os
from pathlib import Path

# --- 1. Project Definitions ---
projects = [
    {"name": "01_Meteor", "tier": "Beginner", "theme": "Batch ETL", "tech": "Python, Pandas, PostgreSQL", "data": "Kaggle Space Missions Dataset", "desc": "Build a daily batch ETL script to extract raw CSVs, clean them, and load them into a local Postgres database.", "diagram": "graph LR\n    A[Raw CSV File] -->|Python/Pandas| B(Data Cleaning & Transfomation)\n    B -->|SQLAlchemy| C[(PostgreSQL DB)]"},
    {"name": "02_Comet", "tier": "Beginner", "theme": "Simple Warehouse", "tech": "PostgreSQL, Bash, Cron", "data": "NASA Exoplanet Archive", "desc": "Design a simple star schema data warehouse and load dimensional data.", "diagram": "graph LR\n    A[(OLTP Postgres)] -->|Cron + Bash Script| B(Data Processing)\n    B -->|SQL Insert| C[(OLAP Star Schema)]"},
    {"name": "03_Satellite", "tier": "Beginner", "theme": "Basic Airflow", "tech": "Apache Airflow, Python, S3", "data": "Open Notify API (ISS Location)", "desc": "Use Airflow to schedule API pulls of the ISS location every 10 minutes and dump raw JSON to cloud storage.", "diagram": "graph TD\n    A((Airflow Scheduler)) -->|Triggers DAG| B[Python Operator]\n    B -->|GET Request| C(REST API)\n    C -->|JSON Payload| B\n    B -->|Boto3 Upload| D[(AWS S3 Bucket)]"},
    {"name": "04_Orbit", "tier": "Beginner", "theme": "Basic dbt", "tech": "dbt Core, Snowflake", "data": "Public Asteroid Dataset", "desc": "Connect dbt to a cloud warehouse to transform raw data into analytical views.", "diagram": "graph LR\n    A[(Raw Data in Snowflake)] -->|dbt run| B(Staging Models)\n    B -->|dbt test/run| C(Core Models)\n    C --> D[(Analytical Marts)]"},
    {"name": "05_Asteroid", "tier": "Intermediate", "theme": "Lakehouse Architecture", "tech": "Apache Iceberg, AWS S3", "data": "Global Weather Data", "desc": "Establish a Lakehouse to store large volumes of structured and semi-structured data.", "diagram": "graph TD\n    A[Raw Data Streams] --> B[(S3 Raw Zone)]\n    B -->|Spark| C[(Iceberg Tables / Silver)]\n    C -->|Spark SQL| D[(Iceberg Marts / Gold)]\n    D --> E[Trino / Athena Query Engine]"},
    {"name": "06_Eclipse", "tier": "Intermediate", "theme": "Partitioning", "tech": "PySpark, S3", "data": "NY TLC Trip Data", "desc": "Process massive datasets using PySpark, focusing on optimal partitioning.", "diagram": "graph LR\n    A[(Large Unpartitioned CSVs)] -->|PySpark Read| B(Spark Cluster Workers)\n    B -->|Shuffle & Sort| C(Optimized DataFrame)\n    C -->|Write Parquet| D[(S3 Partitioned by Year/Month)]"},
    {"name": "07_Nebula", "tier": "Intermediate", "theme": "Data Modelling Depth", "tech": "dbt, Kimball", "data": "Retail dataset", "desc": "Build a deep Kimball dimensional model (Fact/Dimensions, SCD Type 2).", "diagram": "erDiagram\n    FACT_SALES ||--o{ DIM_CUSTOMER : \"purchased by\"\n    FACT_SALES ||--o{ DIM_PRODUCT : \"includes\"\n    FACT_SALES ||--o{ DIM_DATE : \"occurred on\""},
    {"name": "08_Pulsar", "tier": "Intermediate", "theme": "Quality Checks", "tech": "Great Expectations, Airflow", "data": "Sensor Data", "desc": "Integrate data quality testing to halt pipelines upon anomaly detection.", "diagram": "graph TD\n    A[Airflow Task: Extract] --> B[Airflow Task: Load Staging]\n    B --> C{Great Expectations Suite}\n    C -->|Pass| D[Transform Data]\n    C -->|Fail| E[Halt Pipeline & Alert Slack]"},
    {"name": "09_Quasar", "tier": "Advanced", "theme": "Streaming + Batch Hybrid", "tech": "Kafka, Spark Streaming", "data": "IoT Telemetry", "desc": "Build a lambda architecture handling real-time streams and batch reconciliations.", "diagram": "graph LR\n    A[IoT Devices] --> B(Kafka Topic)\n    B -->|Real-time| C[Spark Streaming]\n    B -->|Daily| D[Batch Spark Job]\n    C --> E[(Speed Layer DB)]\n    D --> F[(Batch Layer Warehouse)]"},
    {"name": "10_Nova", "tier": "Advanced", "theme": "CDC Pipelines", "tech": "Debezium, Kafka, Snowflake", "data": "MySQL DB", "desc": "Capture Change Data (CDC) from an operational database to stream to a warehouse.", "diagram": "graph LR\n    A[(MySQL Binlog)] -->|Debezium Connector| B(Kafka CDC Topic)\n    B -->|Kafka Connect / Snowpipe| C[(Snowflake Raw Landing)]\n    C -->|Stream/Task| D[(Snowflake Target Tables)]"},
    {"name": "11_Constellation", "tier": "Advanced", "theme": "Multi-stage Orchestration", "tech": "Airflow, Databricks, dbt", "data": "Market Data", "desc": "Orchestrate a complex DAG triggering external compute and dbt transformations.", "diagram": "graph TD\n    A((Airflow)) -->|API Trigger| B[Databricks Spark Job (ETL)]\n    B --> C{Sensor Check}\n    C -->|Success| D[dbt Cloud Job (Transform)]\n    D --> E[BI Refresh Alert]"},
    {"name": "12_Galaxy", "tier": "Advanced", "theme": "Observability", "tech": "Monte Carlo, dbt", "data": "Internal Data", "desc": "Implement data observability to track freshness and schema changes automatically.", "diagram": "graph LR\n    A[(Data Warehouse)] -->|Metadata APIs| B(Observability Platform)\n    B -->|ML Anomaly Detection| C{Volume/Freshness Drop?}\n    C -->|Yes| D[PagerDuty Alert & Lineage Graph]\n    C -->|No| E[Monitor Logs]"},
    {"name": "13_Supernova", "tier": "Expert", "theme": "Platform Observability", "tech": "Prometheus, Grafana", "data": "Pipeline Metadata", "desc": "Monitor the infrastructure of the data platform itself.", "diagram": "graph TD\n    A[Airflow Nodes] -->|StatsD / JMX| B(Prometheus Scraper)\n    C[Spark Cluster] -->|Metrics API| B\n    B --> D[Grafana Dashboard]\n    D -->|High CPU Alert| E[DevOps Team]"},
    {"name": "14_BlackHole", "tier": "Expert", "theme": "Multi-region Architecture", "tech": "Terraform, AWS Multi-region", "data": "Global Data", "desc": "Deploy a highly available data architecture spanning multiple geographic regions.", "diagram": "graph LR\n    A[us-east-1 Storage] <-->|Cross-Region Replication| B[eu-west-1 Storage]\n    C[Global Route53] -->|Latency Routing| D[API Gateway US]\n    C -->|Latency Routing| E[API Gateway EU]"},
    {"name": "15_Wormhole", "tier": "Expert", "theme": "Cost Optimisation", "tech": "FinOps tools", "data": "Cloud Billing", "desc": "Build a pipeline to analyze cloud warehouse usage and automate cost reductions.", "diagram": "graph TD\n    A[(Snowflake Query History)] --> B[Cost Analysis Script]\n    B --> C{Unused Tables / Heavy Queries?}\n    C -->|Yes| D[Auto-suspend Warehouses]\n    C -->|Yes| E[Alert Data Owners]"},
    {"name": "16_MilkyWay", "tier": "Expert", "theme": "Reliability Engineering", "tech": "Chaos Mesh, K8s", "data": "Streaming Pipeline", "desc": "Perform chaos engineering on clusters to ensure pipeline resilience.", "diagram": "graph LR\n    A[Kubernetes Cluster] --> B(Kafka Pods)\n    A --> C(Spark Pods)\n    D{Chaos Mesh} -->|Inject Network Delay| B\n    D -->|Kill Pod| C\n    E[Monitoring] -->|Verifies Auto-recovery| A"},
    {"name": "17_Cosmos", "tier": "Elite", "theme": "Data Mesh", "tech": "AWS Lake Formation", "data": "Multi-domain", "desc": "Design decentralized data domains with cross-domain federated querying.", "diagram": "graph TD\n    A[(Finance Domain S3)] --> C[Trino / Starburst (Federated Query)]\n    B[(HR Domain S3)] --> C\n    C --> D[BI Dashboard]"},
    {"name": "18_Andromeda", "tier": "Elite", "theme": "Multi-cloud", "tech": "ADF, BigQuery, S3", "data": "Inter-cloud", "desc": "Orchestrate data movement across 3 major cloud providers.", "diagram": "graph LR\n    A[(AWS S3)] -->|Azure Data Factory| B[(Azure ADLS)]\n    B -->|GCP Omni| C[(Google BigQuery)]"},
    {"name": "19_EventHorizon", "tier": "Elite", "theme": "Platform Engineering", "tech": "DataHub", "data": "Platform Metrics", "desc": "Create a self-service platform with metadata management.", "diagram": "graph TD\n    A[All Data Sources] -->|Push Metadata| B(DataHub Catalog)\n    B --> C[Self-Service UI]\n    C -->|User Requests Access| D[Terraform Provisioning]"},
    {"name": "20_Singularity", "tier": "Ultimate", "theme": "Full Enterprise Platform", "tech": "Medallion, Real-time + ML", "data": "Enterprise data", "desc": "Governed, self-service, hybrid architecture supporting BI and ML simultaneously.", "diagram": "graph TD\n    A[Ingestion Layer] --> B[(Bronze)]\n    B --> C[(Silver / Data Contracts)]\n    C --> D[(Gold / BI Marts)]\n    C --> E[(Feature Store)]\n    E --> F[ML Inference Models]"}
]

sub_dirs = ["src", "tests", "dags", "dbt", "infrastructure", "docs", "config", ".github/workflows"]

gitignore_content = """__pycache__/\n*.py[cod]\n.env\nvenv/\n.pytest_cache/\ndata/\n*.csv\n*.parquet\n.terraform/\nterraform.tfstate*"""
makefile_content = """.PHONY: setup test run up down\n\nsetup:\n\tpython -m venv venv\n\tvenv/bin/pip install -r requirements.txt\n\ntest:\n\tpytest tests/\n\nup:\n\tdocker-compose -f infrastructure/docker-compose.yml up -d\n\ndown:\n\tdocker-compose -f infrastructure/docker-compose.yml down\n\nrun:\n\tpython src/main.py"""

# The Project README template now includes the "Back to Home" button
readme_template = """[🔙 Back to Main Capstone Index](../../README.md)

# Project {id}: {space_name}

**Tier:** {tier} | **Complexity Level:** {id}/20
**Primary Focus:** {theme}

## 📝 Overview
{desc}

## 🏗️ Architecture Diagram
{ticks}mermaid
{diagram}
{ticks}

## 🛠️ Tech Stack