# Project 11: Constellation

**Tier:** Advanced | **Complexity Level:** 11/20
**Primary Focus:** Multi-stage Orchestration

## 📝 Overview
Orchestrate a complex DAG that triggers external compute clusters and subsequent dbt transformations.

## 🛠️ Tech Stack
* Airflow, Databricks, dbt

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
* **Primary Data Source:** [Financial Market Data](https://www.google.com/search?q=Financial+Market+Data)
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Multi-stage Orchestration**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
