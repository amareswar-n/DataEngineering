# Project 04: Orbit

**Tier:** Beginner | **Complexity Level:** 04/20
**Primary Focus:** Basic dbt

## 📝 Overview
Connect dbt to a cloud warehouse to transform raw asteroid data into clean, analytical views.

## 🛠️ Tech Stack
* dbt Core, Snowflake/BigQuery

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
* **Primary Data Source:** [Public Asteroid Dataset](https://www.google.com/search?q=Public+Asteroid+Dataset)
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Basic dbt**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
