# Project 15: Wormhole

**Tier:** Expert | **Complexity Level:** 15/20
**Primary Focus:** Cost Optimisation

## 📝 Overview
Build a pipeline to analyze cloud warehouse usage and automate cost reductions.

## 🏗️ Architecture Diagram
```mermaid
graph TD
    A[(Snowflake Query History)] --> B[Cost Analysis Script]
    B --> C{Unused Tables / Heavy Queries?}
    C -->|Yes| D[Auto-suspend Warehouses]
    C -->|Yes| E[Alert Data Owners]
```

## 🛠️ Tech Stack
* FinOps tools

## 📂 Directory Structure
* `/src` - Core processing scripts
* `/tests` - Data quality and unit tests
* `/dags` - Orchestration logic
* `/infrastructure` - IaC and Docker setups
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [Cloud Billing](https://www.google.com/search?q=Cloud+Billing)
* **Goal:** Set up infrastructure, ingest raw data, and implement **Cost Optimisation**.

## 🚀 Quick Start
```bash
make setup
make up
make run
```
