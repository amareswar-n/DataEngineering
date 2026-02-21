# Project 09: Quasar

**Tier:** Advanced | **Complexity Level:** 09/20
**Primary Focus:** Streaming + Batch Hybrid

## 📝 Overview
Build a lambda architecture handling both real-time streams and nightly batch reconciliations.

## 🛠️ Tech Stack
* Apache Kafka, Spark Structured Streaming

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
* **Primary Data Source:** [Simulated IoT Telemetry](https://www.google.com/search?q=Simulated+IoT+Telemetry)
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Streaming + Batch Hybrid**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
