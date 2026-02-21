# Project 20: Singularity

**Tier:** Ultimate | **Complexity Level:** 20/20
**Primary Focus:** Full Enterprise Platform

## 📝 Overview
The culmination project: A governed, self-service, hybrid architecture supporting BI and ML simultaneously.

## 🛠️ Tech Stack
* Medallion + Mesh, Real-time + ML, Data Contracts, Gov Automation

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
* **Primary Data Source:** [Enterprise-scale synthetic data](https://www.google.com/search?q=Enterprise-scale+synthetic+data)
* **Requirements:**
  1. Set up the local/cloud environment using files in `/infrastructure`.
  2. Ingest raw data from the provided source.
  3. Apply the core concept of **Full Enterprise Platform**.
  4. Ensure all tests in `/tests` pass via CI/CD.

## 📖 Useful Documentation
* [Data Engineering Zoomcamp (Reference)](https://github.com/DataTalksClub/data-engineering-zoomcamp)
* [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
