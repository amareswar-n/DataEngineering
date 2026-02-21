# Project 19: EventHorizon

**Tier:** Elite | **Complexity Level:** 19/20
**Primary Focus:** Platform Engineering & SLAs

## 📝 Overview
Create a self-service platform with metadata management and strict SLO/SLA enforcement.

## 🛠️ Tech Stack
* DataHub, Terraform, SLA alerting

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
* **Primary Data Source:** [Platform Metrics](https://www.google.com/search?q=Platform+Metrics)
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Platform Engineering & SLAs**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
