# Project 05: Asteroid

**Tier:** Intermediate | **Complexity Level:** 05/20
**Primary Focus:** Lakehouse Architecture

## 📝 Overview
Establish a local or cloud-based Lakehouse to store large volumes of structured and semi-structured data.

## 🛠️ Tech Stack
* Apache Iceberg/Delta Lake, AWS S3

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
* **Primary Data Source:** [Global Weather Data](https://www.google.com/search?q=Global+Weather+Data)
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Lakehouse Architecture**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
