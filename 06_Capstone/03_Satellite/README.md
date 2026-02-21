# Project 03: Satellite

**Tier:** Beginner | **Complexity Level:** 03/20
**Primary Focus:** Basic Airflow

## 📝 Overview
Use Airflow to schedule API pulls of the ISS location every 10 minutes and dump raw JSON to cloud storage.

## 🛠️ Tech Stack
* Apache Airflow, Python, S3/GCS

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
* **Primary Data Source:** [Open Notify API (ISS Location)](https://www.google.com/search?q=Open+Notify+API+(ISS+Location))
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Basic Airflow**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
