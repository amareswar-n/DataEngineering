# Project 02: Comet

**Tier:** Beginner | **Complexity Level:** 02/20
**Primary Focus:** Simple Warehouse

## 📝 Overview
Design a simple star schema data warehouse and load dimensional data.

## 🛠️ Tech Stack
* PostgreSQL, Bash, Cron

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
* **Primary Data Source:** [NASA Exoplanet Archive (CSV)](https://www.google.com/search?q=NASA+Exoplanet+Archive+(CSV))
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Simple Warehouse**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
