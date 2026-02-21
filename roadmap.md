# WIP -- DO NOT USE --- 

https://roadmap.sh/data-engineer

*This roadmap uses my core curriculum as the foundation, enriched with deep-dive technical sub-topics from industry leaders (Codebasics, Seattle Data Guy, Sumit Mittal, Data with Baraa, and Roadmap.sh). Every topic is scoped to a 1-week sprint.*

## 🧭 **Exploration** _*.. clarity not any skill*_

Before learning anything, make sure you understand the role. Data engineering is not about flashy visuals—it’s about systems, pipelines, fixing issues, and working behind the scenes. It’s about **building the data foundation** that everything else depends on.

### 📈 Maturity Ladder
| Level | Focus |
| --- | --- |
| **Junior** | Pipelines, SQL, debugging, Python basics |
| **Mid** | Distributed systems, cloud orchestration, CI/CD |
| **Senior** | Architecture, reliability, cost optimisation (FinOps) |
| **Staff** | Platform design, data mesh, governance, strategy |

---

## 🗺️ The Interactive 24-Week Learning Path
*Click to expand each Phase, Step, and 1-Week Sprint to track your progress.*

<details>
<summary><h2>🏗️ Phase 1: Foundation (Weeks 1-4)</h2></summary>
<i>Base: System navigation, version control, and programming mastery.</i>

<details>
<summary><h3>Step 1: System Navigation & Version Control</h3></summary>

* **Week 1: Linux, CLI Basics & Shell Scripting**
    * [ ] Navigate systems using Bash commands (ls, cd, grep, awk, sed).
    * [ ] OS Concepts: Processes, Threads, Memory, and Cron jobs.
    * 📚 *Book:* The Linux Command Line
* **Week 2: Git, GitHub & Networking**
    * [ ] Version control (clone, commit, push, branch, merge, resolve conflicts).
    * [ ] Networking Protocols: HTTP/HTTPS, TCP/IP, SSH, REST, and GraphQL APIs.
    * 📚 *Book:* Pro Git
</details>

<details>
<summary><h3>Step 2: Programming Mastery</h3></summary>

* **Week 3: Python Core**
    * [ ] Data structures, loops, conditionals, and functions.
    * [ ] Object-Oriented Programming (OOP) and error handling.
    * [ ] *Awareness:* How Python compares to JVM languages (Java/Scala) in Big Data.
    * 📚 *Book:* Fluent Python
* **Week 4: Python for Data Processing**
    * [ ] Pandas & NumPy essentials (filtering, aggregations, merges).
    * [ ] Parsing serialization formats: JSON, XML, CSV, Parquet, Avro.
</details>

</details>

---

<details>
<summary><h2>💾 Phase 2: Data Storage & Design (Weeks 5-10)</h2></summary>
<i>Base: Databases, dimensional modeling, distributed systems concepts, and analytical storage.</i>

<details>
<summary><h3>Step 3: Databases & Distributed Systems Theory</h3></summary>

* **Week 5: RDBMS & Distributed Concepts (Roadmap.sh Integration)**
    * [ ] Relational DB concepts, ACID properties, Indexing (B-Trees, Hash).
    * [ ] Distributed DB Theory: CAP Theorem, BASE, Sharding, Replication, Consensus.
    * 📚 *Book:* Database System Concepts
* **Week 6: Advanced SQL & NoSQL**
    * [ ] SQL Mastery: CTEs, Window Functions, Subqueries, Execution Plans.
    * [ ] NoSQL paradigms: Document (MongoDB), Key-Value (Redis), Wide-Column (Cassandra), Graph (Neo4j), Time-Series (InfluxDB).
    * 📚 *Book:* SQL Performance Explained
</details>

<details>
<summary><h3>Step 4: Modeling & Warehousing</h3></summary>

* **Week 7: Data Modelling Concepts**
    * [ ] Kimball Methodology: Fact vs. Dimension tables.
    * [ ] Star Schema vs. Snowflake Schema.
    * [ ] Slowly Changing Dimensions (SCD Type 1, 2, and 3).
    * 📚 *Book:* Data Modeling Made Simple
* **Week 8: Object Storage, Warehousing & Lakehouses**
    * [ ] Cloud Object Storage basics (AWS S3, GCS, Azure Blob).
    * [ ] Cloud Warehouses (Snowflake, BigQuery): Columnar storage, RBAC. *Awareness:* ClickHouse for real-time OLAP.
    * [ ] Lakehouse Concepts: Delta Lake, Apache Iceberg, Apache Hudi.
    * 📚 *Book:* Data Warehouse Toolkit / Lakehouse Architecture
</details>

<details>
<summary><h3>Step 5: Metadata & Transformations</h3></summary>

* **Week 9: Analytics Engineering with dbt**
    * [ ] Setting up dbt; writing modular SQL models and macros.
    * [ ] Testing and documenting models natively in dbt.
    * 📚 *Book:* Analytics Engineering
* **Week 10: Data Discovery, Contracts & Cataloging**
    * [ ] Managing schema evolution and ensuring Data Contracts.
    * [ ] Data Catalogs & Lineage (Concepts behind DataHub, Amundsen, or Collibra).
</details>

</details>

---

<details>
<summary><h2>⚙️ Phase 3: Data Processing & Pipelines (Weeks 11-16)</h2></summary>
<i>Base: Integration, distributed compute, and streaming architectures.</i>

<details>
<summary><h3>Step 6: Integration & Orchestration</h3></summary>

* **Week 11: APIs, ETL/ELT & Reverse ETL**
    * [ ] Batch vs. Streaming paradigms.
    * [ ] Building robust ETL/ELT pipelines and Reverse ETL workflows.
* **Week 12: Workflow Scheduling & Orchestration**
    * [ ] Apache Airflow: DAGs, Tasks, Operators, XComs, Catchup.
    * [ ] *Awareness:* Modern alternative orchestrators (Prefect, Dagster, Mage).
    * 📚 *Book:* Data Pipelines Pocket Reference
</details>

<details>
<summary><h3>Step 7: Distributed Compute</h3></summary>

* **Week 13: Hadoop Legacy to Spark Modernity**
    * [ ] Context: MapReduce, HDFS, and YARN (understanding the history).
    * [ ] Spark architecture (Driver, Executors, Cluster Manager).
    * [ ] PySpark: RDDs vs. DataFrames, Transformations vs. Actions.
    * 📚 *Book:* Spark Definitive Guide
* **Week 14: Spark Optimizations**
    * [ ] Handling Data Skew and Out of Memory (OOM) errors.
    * [ ] Broadcast Joins, Partitioning, Bucketing, and reading the Spark UI DAG.
</details>

<details>
<summary><h3>Step 8: Real-Time Streaming</h3></summary>

* **Week 15: Message Brokers & Event Streaming**
    * [ ] Apache Kafka architecture: Topics, Partitions, Brokers.
    * [ ] *Awareness:* RabbitMQ, Apache Pulsar, AWS Kinesis, GCP Pub/Sub.
    * [ ] Stream Processing engines (Apache Flink vs Spark Streaming).
    * 📚 *Book:* Kafka in Action
* **Week 16: CDC (Change Data Capture)**
    * [ ] Capturing operational DB changes via binlogs.
    * [ ] Setting up Debezium to stream database changes.
</details>

</details>

---

<details>
<summary><h2>☁️ Phase 4: Infrastructure & Reliability (Weeks 17-20)</h2></summary>
<i>Base: Cloud ecosystems, containerization, observability, and FinOps.</i>

<details>
<summary><h3>Step 9: Cloud & Provisioning</h3></summary>

* **Week 17: Cloud Ecosystems, Security & IAM**
    * [ ] Managed Data Services (AWS Glue/Athena vs GCP Dataflow/BigQuery).
    * [ ] Identity and Access Management (IAM) and Cloud Security basics.
    * 📚 *Book:* Cloud Architecture Patterns
* **Week 18: IaC & Cost Optimisation (FinOps)**
    * [ ] Infrastructure as Code: Terraform basics, state files. (*Awareness:* Pulumi, AWS CDK).
    * [ ] FinOps: Tracking compute costs and optimizing cloud warehouse bills.
    * 📚 *Book:* Cloud FinOps
</details>

<details>
<summary><h3>Step 10: DevOps & Observability</h3></summary>

* **Week 19: Containerization & CI/CD**
    * [ ] Docker basics (Images, Containers, Dockerfiles, `docker-compose`).
    * [ ] CI/CD Pipelines (GitHub Actions / GitLab CI).
    * 📚 *Book:* Docker Deep Dive
* **Week 20: Observability, Debugging & Quality**
    * [ ] Data Quality: Great Expectations, Soda.
    * [ ] Monitoring & Metrics: Prometheus, Grafana, Datadog.
    * 📚 *Book:* Observability Engineering
</details>

</details>

---

<details>
<summary><h2>🚀 Phase 5: Advanced Platform & Architecture (Weeks 21-24)</h2></summary>
<i>Base: Enterprise-scale data platform design and modern architectural paradigms.</i>

<details>
<summary><h3>Step 11: Enterprise Architecture Patterns</h3></summary>

* **Week 21: Medallion Architecture**
    * [ ] Designing Bronze (Raw), Silver (Cleaned), and Gold (Business-ready) layers in a Lakehouse.
    * 📚 *Book:* Designing Data Platforms
* **Week 22: Advanced Streaming Architecture**
    * [ ] Designing robust event-driven architectures (Lambda vs. Kappa architectures).
    * 📚 *Book:* Streaming Systems
</details>

<details>
<summary><h3>Step 12: Platform Scale & Reliability</h3></summary>

* **Week 23: Data Mesh & Domain Ownership**
    * [ ] Decentralized domain ownership vs. Data Fabric vs. centralized data teams.
    * 📚 *Book:* Data Mesh — Zhamak Dehghani
* **Week 24: Platform Engineering & SLAs/SLOs**
    * [ ] Building self-service data infrastructure.
    * [ ] Multi-cloud routing and defining strict reliability SLAs/SLOs.
    * 📚 *Book:* Site Reliability Engineering
</details>

</details>

---

## 🎯 **UDIM - Capstone Project: 20-Project Workspace**

This is where learning stops being theoretical. Projects are how you turn concepts, tools, and code into **real understanding**.

Instead of a single project, I have built a **20-Tier Progressive Capstone Workspace** to execute these weekly learnings in isolated, production-grade environments.

👉 **[Enter the 06_Capstone Directory to view the 20 Projects & Architecture Gallery](./06_Capstone/README.md)**

---

## 💼 **Interview Prep**

At this point, you won’t know 100% of data engineering, and that’s completely normal. You already have the skills needed to start applying. 

👉 **[Access the Interview Prep Bank & Templates](./07_Interview_Prep)**

---

## 📖 How to use this repository

1. **Fork** this repository.
2. Expand the phases and mark your progress by checking the `[ ]` boxes week by week.
3. Commit your notes or small practice scripts to folders `01` through `05` as you learn.
4. **Execute in the Capstone:** Navigate to `06_Capstone` to start building real pipelines based on the week's topic.
