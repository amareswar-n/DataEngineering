# Project 16: MilkyWay

**Tier:** Expert | **Complexity Level:** 16/20
**Primary Focus:** Reliability Engineering

## 📝 Overview
Perform chaos engineering on your Kafka/Airflow clusters to ensure pipeline resilience.

## 🛠️ Tech Stack
* Chaos Mesh, Kubernetes

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
* **Primary Data Source:** [Streaming Pipeline](https://www.google.com/search?q=Streaming+Pipeline)
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Reliability Engineering**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
