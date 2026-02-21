# Project 10: Nova

**Tier:** Advanced | **Complexity Level:** 10/20
**Primary Focus:** CDC Pipelines

## 📝 Overview
Capture Change Data (CDC) from an operational database to stream to a warehouse.

## 🏗️ Architecture Diagram
```mermaid
graph LR
    A[(MySQL Binlog)] -->|Debezium Connector| B(Kafka CDC Topic)
    B -->|Kafka Connect / Snowpipe| C[(Snowflake Raw Landing)]
    C -->|Stream/Task| D[(Snowflake Target Tables)]
```

## 🛠️ Tech Stack
* Debezium, Kafka, Snowflake

## 📂 Directory Structure
* `/src` - Core processing scripts
* `/tests` - Data quality and unit tests
* `/dags` - Orchestration logic
* `/infrastructure` - IaC and Docker setups
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [MySQL DB](https://www.google.com/search?q=MySQL+DB)
* **Goal:** Set up infrastructure, ingest raw data, and implement **CDC Pipelines**.

## 🚀 Quick Start
```bash
make setup
make up
make run
```
