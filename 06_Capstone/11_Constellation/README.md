# Project 11: Constellation

**Tier:** Advanced | **Complexity Level:** 11/20
**Primary Focus:** Multi-stage Orchestration

## 📝 Overview
Orchestrate a complex DAG triggering external compute and dbt transformations.

## 🏗️ Architecture Diagram
```mermaid
graph TD
    A((Airflow)) -->|API Trigger| B[Databricks Spark Job (ETL)]
    B --> C{Sensor Check}
    C -->|Success| D[dbt Cloud Job (Transform)]
    D --> E[BI Refresh Alert]
```

## 🛠️ Tech Stack
* Airflow, Databricks, dbt

## 📂 Directory Structure
* `/src` - Core processing scripts
* `/tests` - Data quality and unit tests
* `/dags` - Orchestration logic
* `/infrastructure` - IaC and Docker setups
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [Market Data](https://www.google.com/search?q=Market+Data)
* **Goal:** Set up infrastructure, ingest raw data, and implement **Multi-stage Orchestration**.

## 🚀 Quick Start
```bash
make setup
make up
make run
```
