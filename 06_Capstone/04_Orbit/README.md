# Project 04: Orbit

**Tier:** Beginner | **Complexity Level:** 04/20
**Primary Focus:** Basic dbt

## 📝 Overview
Connect dbt to a cloud warehouse to transform raw data into analytical views.

## 🏗️ Architecture Diagram
```mermaid
graph LR
    A[(Raw Data in Snowflake)] -->|dbt run| B(Staging Models)
    B -->|dbt test/run| C(Core Models)
    C --> D[(Analytical Marts)]
```

## 🛠️ Tech Stack
* dbt Core, Snowflake

## 📂 Directory Structure
* `/src` - Core processing scripts
* `/tests` - Data quality and unit tests
* `/dags` - Orchestration logic
* `/infrastructure` - IaC and Docker setups
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [Public Asteroid Dataset](https://www.google.com/search?q=Public+Asteroid+Dataset)
* **Goal:** Set up infrastructure, ingest raw data, and implement **Basic dbt**.

## 🚀 Quick Start
```bash
make setup
make up
make run
```
