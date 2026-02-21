# Project 14: BlackHole

**Tier:** Expert | **Complexity Level:** 14/20
**Primary Focus:** Multi-region Architecture

## 📝 Overview
Deploy a highly available data architecture spanning multiple geographic regions.

## 🏗️ Architecture Diagram
```mermaid
graph LR
    A[us-east-1 Storage] <-->|Cross-Region Replication| B[eu-west-1 Storage]
    C[Global Route53] -->|Latency Routing| D[API Gateway US]
    C -->|Latency Routing| E[API Gateway EU]
```

## 🛠️ Tech Stack
* Terraform, AWS Multi-region

## 📂 Directory Structure
* `/src` - Core processing scripts
* `/tests` - Data quality and unit tests
* `/dags` - Orchestration logic
* `/infrastructure` - IaC and Docker setups
* `/config` - Pipeline configurations

## 📊 Data Sources & Requirements
* **Primary Data Source:** [Global Data](https://www.google.com/search?q=Global+Data)
* **Goal:** Set up infrastructure, ingest raw data, and implement **Multi-region Architecture**.

## 🚀 Quick Start
```bash
make setup
make up
make run
```
