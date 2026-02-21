# Project 08: Pulsar

**Tier:** Intermediate | **Complexity Level:** 08/20
**Primary Focus:** Quality Checks

## 📝 Overview
Integrate data quality testing to halt pipelines upon anomaly detection.

## 🏗️ Architecture Diagram
```mermaid
graph TD
    A[Airflow Task: Extract] --> B[Airflow Task: Load Staging]
    B --> C{Great Expectations Suite}
    C -->|Pass| D[Transform Data]
    C -->|Fail| E[Halt Pipeline & Alert Slack]
```

## 🛠️ Tech Stack
* Great Expectations, Airflow

## 📂 Directory Structure
* `/src` - Core processing scripts
* `/tests` - Data quality and unit tests
* `/dags` - Orchestration logic
* `/infrastructure` - IaC and Docker setups
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [Sensor Data](https://www.google.com/search?q=Sensor+Data)
* **Goal:** Set up infrastructure, ingest raw data, and implement **Quality Checks**.

## 🚀 Quick Start
```bash
make setup
make up
make run
```
