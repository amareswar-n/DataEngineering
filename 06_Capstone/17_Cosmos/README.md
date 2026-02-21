# Project 17: Cosmos

**Tier:** Elite | **Complexity Level:** 17/20
**Primary Focus:** Data Mesh

## 📝 Overview
Design decentralized data domains with cross-domain federated querying.

## 🏗️ Architecture Diagram
```mermaid
graph TD
    A[(Finance Domain S3)] --> C[Trino / Starburst (Federated Query)]
    B[(HR Domain S3)] --> C
    C --> D[BI Dashboard]
```

## 🛠️ Tech Stack
* AWS Lake Formation

## 📂 Directory Structure
* `/src` - Core processing scripts
* `/tests` - Data quality and unit tests
* `/dags` - Orchestration logic
* `/infrastructure` - IaC and Docker setups
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [Multi-domain](https://www.google.com/search?q=Multi-domain)
* **Goal:** Set up infrastructure, ingest raw data, and implement **Data Mesh**.

## 🚀 Quick Start
```bash
make setup
make up
make run
```
