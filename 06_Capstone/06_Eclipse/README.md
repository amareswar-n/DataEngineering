# Project 06: Eclipse

**Tier:** Intermediate | **Complexity Level:** 06/20
**Primary Focus:** Partitioning

## 📝 Overview
Process massive datasets using PySpark, focusing on optimal partitioning and bucketing strategies.

## 🛠️ Tech Stack
* PySpark, AWS S3/HDFS

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
* **Primary Data Source:** [NY TLC Trip Data (simulating telemetry)](https://www.google.com/search?q=NY+TLC+Trip+Data+(simulating+telemetry))
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Partitioning**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
