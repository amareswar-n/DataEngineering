# Project 12: Galaxy

**Tier:** Advanced | **Complexity Level:** 12/20
**Primary Focus:** Observability

## 📝 Overview
Implement data observability to track freshness and schema changes automatically.

## 🏗️ Architecture Diagram
```mermaid
graph LR
    A[(Data Warehouse)] -->|Metadata APIs| B(Observability Platform)
    B -->|ML Anomaly Detection| C{Volume/Freshness Drop?}
    C -->|Yes| D[PagerDuty Alert & Lineage Graph]
    C -->|No| E[Monitor Logs]
```

## 🛠️ Tech Stack
* Monte Carlo, dbt

## 📂 Directory Structure
* `/src` - Core processing scripts
* `/tests` - Data quality and unit tests
* `/dags` - Orchestration logic
* `/infrastructure` - IaC and Docker setups
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [Internal Data](https://www.google.com/search?q=Internal+Data)
* **Goal:** Set up infrastructure, ingest raw data, and implement **Observability**.

## 🚀 Quick Start
```bash
make setup
make up
make run
```
