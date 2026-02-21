# Project 10: Nova

**Tier:** Advanced | **Complexity Level:** 10/20
**Primary Focus:** CDC Pipelines

## 📝 Overview
Capture Change Data (CDC) from an operational database and stream it to a data warehouse.

## 🛠️ Tech Stack
* Debezium, Kafka, Snowflake

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
* **Primary Data Source:** [Transactional OLTP DB (MySQL)](https://www.google.com/search?q=Transactional+OLTP+DB+(MySQL))
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **CDC Pipelines**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
