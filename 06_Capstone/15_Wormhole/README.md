# Project 15: Wormhole

**Tier:** Expert | **Complexity Level:** 15/20
**Primary Focus:** Cost Optimisation

## 📝 Overview
Build a pipeline to analyze cloud warehouse usage and recommend/automate cost reductions.

## 🛠️ Tech Stack
* FinOps tools, Snowflake/BigQuery

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
* **Primary Data Source:** [Cloud Billing Exports](https://www.google.com/search?q=Cloud+Billing+Exports)
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Cost Optimisation**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
