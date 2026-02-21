# Project 06: Eclipse

**Tier:** Intermediate | **Complexity Level:** 06/20
**Primary Focus:** Partitioning

## 📝 Overview
Process massive datasets using PySpark, focusing on optimal partitioning.

## 🏗️ Architecture Diagram
```mermaid
graph LR
    A[(Large Unpartitioned CSVs)] -->|PySpark Read| B(Spark Cluster Workers)
    B -->|Shuffle & Sort| C(Optimized DataFrame)
    C -->|Write Parquet| D[(S3 Partitioned by Year/Month)]
```

## 🛠️ Tech Stack
* PySpark, S3

## 📂 Directory Structure
* `/src` - Core processing scripts
* `/tests` - Data quality and unit tests
* `/dags` - Orchestration logic
* `/infrastructure` - IaC and Docker setups
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [NY TLC Trip Data](https://www.google.com/search?q=NY+TLC+Trip+Data)
* **Goal:** Set up infrastructure, ingest raw data, and implement **Partitioning**.

## 🚀 Quick Start
```bash
make setup
make up
make run
```
