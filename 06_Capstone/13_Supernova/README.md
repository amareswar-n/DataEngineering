# Project 13: Supernova

**Tier:** Expert | **Complexity Level:** 13/20
**Primary Focus:** Platform Observability

## 📝 Overview
Monitor the infrastructure of the data platform itself.

## 🏗️ Architecture Diagram
```mermaid
graph TD
    A[Airflow Nodes] -->|StatsD / JMX| B(Prometheus Scraper)
    C[Spark Cluster] -->|Metrics API| B
    B --> D[Grafana Dashboard]
    D -->|High CPU Alert| E[DevOps Team]
```

## 🛠️ Tech Stack
* Prometheus, Grafana

## 📂 Directory Structure
* `/src` - Core processing scripts
* `/tests` - Data quality and unit tests
* `/dags` - Orchestration logic
* `/infrastructure` - IaC and Docker setups
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [Pipeline Metadata](https://www.google.com/search?q=Pipeline+Metadata)
* **Goal:** Set up infrastructure, ingest raw data, and implement **Platform Observability**.

## 🚀 Quick Start
```bash
make setup
make up
make run
```
