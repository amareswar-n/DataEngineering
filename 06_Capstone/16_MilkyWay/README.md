# Project 16: MilkyWay

**Tier:** Expert | **Complexity Level:** 16/20
**Primary Focus:** Reliability Engineering

## 📝 Overview
Perform chaos engineering on clusters to ensure pipeline resilience.

## 🏗️ Architecture Diagram
```mermaid
graph LR
    A[Kubernetes Cluster] --> B(Kafka Pods)
    A --> C(Spark Pods)
    D{Chaos Mesh} -->|Inject Network Delay| B
    D -->|Kill Pod| C
    E[Monitoring] -->|Verifies Auto-recovery| A
```

## 🛠️ Tech Stack
* Chaos Mesh, K8s

## 📂 Directory Structure
* `/src` - Core processing scripts
* `/tests` - Data quality and unit tests
* `/dags` - Orchestration logic
* `/infrastructure` - IaC and Docker setups
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [Streaming Pipeline](https://www.google.com/search?q=Streaming+Pipeline)
* **Goal:** Set up infrastructure, ingest raw data, and implement **Reliability Engineering**.

## 🚀 Quick Start
```bash
make setup
make up
make run
```
