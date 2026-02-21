# Project 01: Meteor

**Tier:** Beginner | **Complexity Level:** 01/20
**Primary Focus:** Batch ETL

## 📝 Overview
Build a daily batch ETL script to extract raw CSVs, clean them, and load them into a local Postgres database.

## 🛠️ Tech Stack
* Python, Pandas, PostgreSQL

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
* **Primary Data Source:** [Kaggle Space Missions Dataset](https://www.google.com/search?q=Kaggle+Space+Missions+Dataset)
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Batch ETL**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
