import os
from pathlib import Path

# --- 1. Project Definitions ---
# Ordered 1 to 20 (Beginner -> Ultimate) based on your provided roadmap
projects = [
    # BEGINNER
    {"name": "01_Meteor", "tier": "Beginner", "theme": "Batch ETL", "tech": "Python, Pandas, PostgreSQL", "data": "Kaggle Space Missions Dataset", "desc": "Build a daily batch ETL script to extract raw CSVs, clean them, and load them into a local Postgres database."},
    {"name": "02_Comet", "tier": "Beginner", "theme": "Simple Warehouse", "tech": "PostgreSQL, Bash, Cron", "data": "NASA Exoplanet Archive (CSV)", "desc": "Design a simple star schema data warehouse and load dimensional data."},
    {"name": "03_Satellite", "tier": "Beginner", "theme": "Basic Airflow", "tech": "Apache Airflow, Python, S3/GCS", "data": "Open Notify API (ISS Location)", "desc": "Use Airflow to schedule API pulls of the ISS location every 10 minutes and dump raw JSON to cloud storage."},
    {"name": "04_Orbit", "tier": "Beginner", "theme": "Basic dbt", "tech": "dbt Core, Snowflake/BigQuery", "data": "Public Asteroid Dataset", "desc": "Connect dbt to a cloud warehouse to transform raw asteroid data into clean, analytical views."},
    
    # INTERMEDIATE
    {"name": "05_Asteroid", "tier": "Intermediate", "theme": "Lakehouse Architecture", "tech": "Apache Iceberg/Delta Lake, AWS S3", "data": "Global Weather Data", "desc": "Establish a local or cloud-based Lakehouse to store large volumes of structured and semi-structured data."},
    {"name": "06_Eclipse", "tier": "Intermediate", "theme": "Partitioning", "tech": "PySpark, AWS S3/HDFS", "data": "NY TLC Trip Data (simulating telemetry)", "desc": "Process massive datasets using PySpark, focusing on optimal partitioning and bucketing strategies."},
    {"name": "07_Nebula", "tier": "Intermediate", "theme": "Data Modelling Depth", "tech": "dbt, Kimball Methodology", "data": "E-commerce/Retail dataset", "desc": "Build a deep Kimball dimensional model (Fact/Dimensions, SCD Type 2) using dbt."},
    {"name": "08_Pulsar", "tier": "Intermediate", "theme": "Quality Checks", "tech": "Great Expectations, Airflow", "data": "Messy Sensor Data", "desc": "Integrate data quality testing into your pipelines to halt processing if anomalies are detected."},
    
    # ADVANCED
    {"name": "09_Quasar", "tier": "Advanced", "theme": "Streaming + Batch Hybrid", "tech": "Apache Kafka, Spark Structured Streaming", "data": "Simulated IoT Telemetry", "desc": "Build a lambda architecture handling both real-time streams and nightly batch reconciliations."},
    {"name": "10_Nova", "tier": "Advanced", "theme": "CDC Pipelines", "tech": "Debezium, Kafka, Snowflake", "data": "Transactional OLTP DB (MySQL)", "desc": "Capture Change Data (CDC) from an operational database and stream it to a data warehouse."},
    {"name": "11_Constellation", "tier": "Advanced", "theme": "Multi-stage Orchestration", "tech": "Airflow, Databricks, dbt", "data": "Financial Market Data", "desc": "Orchestrate a complex DAG that triggers external compute clusters and subsequent dbt transformations."},
    {"name": "12_Galaxy", "tier": "Advanced", "theme": "Observability", "tech": "Monte Carlo / Databand, dbt", "data": "Internal Company Data", "desc": "Implement data observability to track data freshness, volume, and schema changes automatically."},
    
    # EXPERT
    {"name": "13_Supernova", "tier": "Expert", "theme": "Platform Observability", "tech": "Prometheus, Grafana, Airflow StatsD", "data": "Pipeline Metadata", "desc": "Monitor the infrastructure of the data platform itself (CPU, memory, DAG runtimes)."},
    {"name": "14_BlackHole", "tier": "Expert", "theme": "Multi-region Architecture", "tech": "Terraform, AWS/GCP Multi-region", "data": "Global User Data", "desc": "Deploy a highly available data architecture spanning multiple geographic regions using IaC."},
    {"name": "15_Wormhole", "tier": "Expert", "theme": "Cost Optimisation", "tech": "FinOps tools, Snowflake/BigQuery", "data": "Cloud Billing Exports", "desc": "Build a pipeline to analyze cloud warehouse usage and recommend/automate cost reductions."},
    {"name": "16_MilkyWay", "tier": "Expert", "theme": "Reliability Engineering", "tech": "Chaos Mesh, Kubernetes", "data": "Streaming Pipeline", "desc": "Perform chaos engineering on your Kafka/Airflow clusters to ensure pipeline resilience."},
    
    # ELITE
    {"name": "17_Cosmos", "tier": "Elite", "theme": "Data Mesh", "tech": "AWS Lake Formation, Trino", "data": "Multi-domain enterprise data", "desc": "Design decentralized data domains with cross-domain federated querying."},
    {"name": "18_Andromeda", "tier": "Elite", "theme": "Multi-cloud", "tech": "Azure Data Factory, GCP BigQuery, AWS S3", "data": "Inter-cloud transfers", "desc": "Build a pipeline that seamlessly orchestrates data movement and processing across 3 major cloud providers."},
    {"name": "19_EventHorizon", "tier": "Elite", "theme": "Platform Engineering & SLAs", "tech": "DataHub, Terraform, SLA alerting", "data": "Platform Metrics", "desc": "Create a self-service platform with metadata management and strict SLO/SLA enforcement."},
    
    # ULTIMATE
    {"name": "20_Singularity", "tier": "Ultimate", "theme": "Full Enterprise Platform", "tech": "Medallion + Mesh, Real-time + ML, Data Contracts, Gov Automation", "data": "Enterprise-scale synthetic data", "desc": "The culmination project: A governed, self-service, hybrid architecture supporting BI and ML simultaneously."}
]

# --- 2. Production Sub-directories ---
sub_dirs = [
    "src",                  # Core code (Python, Scala, SQL)
    "tests",                # Unit and integration tests
    "dags",                 # Airflow DAGs
    "dbt",                  # dbt models and configurations
    "infrastructure",       # Terraform, Docker, CloudFormation
    "docs",                 # Architecture diagrams, data dictionaries
    "config",               # YAML/JSON config files
    ".github/workflows"     # CI/CD pipelines
]

# --- 3. README Template ---
readme_template = """# Project {id}: {space_name}

**Tier:** {tier} | **Complexity Level:** {id}/20
**Primary Focus:** {theme}

## 📝 Overview
{desc}

## 🛠️ Tech Stack
* {tech}

## 📂 Directory Structure
This project follows a production-grade structure:
* `/src` - Core extraction and transformation scripts
* `/tests` - Unit and data quality tests
* `/dags` - Orchestration logic
* `/dbt` - Analytical transformations
* `/infrastructure` - Infrastructure as Code (IaC) / Docker setups
* `/docs` - Architecture diagrams
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [{data}](https://www.google.com/search?q={data_query})
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **{theme}**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
"""

def create_capstone():
    base_dir = Path("Capstone")
    base_dir.mkdir(exist_ok=True)
    
    for i, proj in enumerate(projects, 1):
        # Format the directory name properly
        folder_name = proj['name']
        proj_dir = base_dir / folder_name
        proj_dir.mkdir(exist_ok=True)
        
        # Create subdirectories
        for sub in sub_dirs:
            (proj_dir / sub).mkdir(parents=True, exist_ok=True)
            # Add a .gitkeep so empty folders can be committed to Git
            (proj_dir / sub / ".gitkeep").touch()
            
        # Create standard files
        (proj_dir / "requirements.txt").touch()
        (proj_dir / ".gitignore").touch()
        
        # Format and write the README
        readme_content = readme_template.format(
            id=str(i).zfill(2),
            space_name=folder_name.split("_")[1],
            tier=proj["tier"],
            theme=proj["theme"],
            desc=proj["desc"],
            tech=proj["tech"],
            data=proj["data"],
            data_query=proj["data"].replace(" ", "+")
        )
        
        with open(proj_dir / "README.md", "w", encoding="utf-8") as f:
            f.write(readme_content)
            
        print(f"✅ Created: {folder_name} ({proj['tier']})")

if __name__ == "__main__":
    print("🚀 Launching Capstone setup...")
    create_capstone()
    print("✨ All 20 projects successfully generated in the 'Capstone' directory!")