# Data Engineer Roadmap

## 0. What is Data Engineering
* Data Engineering vs Data Science
* Skills and Responsibilities
* Data Engineering Lifecycle
* Choosing the right Techniques
* Decide is data engineering right for you?

## 1. Foundations: Learn the Basics
Before specializing, you must master these core pillars as shown in the foundational roadmap.

* **Programming Skills**
    * **Languages**:
      *   Python <sub>(Recommended)</sub>
      *   Java
      *   Scala
      *   Go
    * **Advanced Techniques**: Functional programming in Scala, JVM tuning for Java/Scala.
* **Data Structures and Algorithms**
    * **Core Concepts**: Arrays, Linked Lists, Stacks, Queues.
    * **Advanced**: Hash Maps, Trees, Graphs, and Sorting/Searching efficiency (Big O).
* **Git and GitHub**
    * **Version Control**: Branching, Merging, Pull Requests, and Conflict Resolution.
* **Linux Basics**
    * **Environment**: File systems, Permissions, Package Management.
    * **Scripting**: Bash/Zsh scripting, Vim/Nano, Cron jobs for automation.
* **Networking Fundamentals**
    * **Protocols**: TCP/IP, HTTP/S, DNS.
    * **Concepts**: Load Balancing, Firewalls, and API communication.
* **Distributed Systems Basics**
    * **Principles**: Consistency vs. Availability (CAP Theorem), Partitioning, Sharding.
    * **Architecture**: Master-Worker patterns, Consensus algorithms.

---

## 2. Data Lifecycle
Following the roadmap flow, these are the high-level stages of data movement.

* **Data Generation**
    * **Sources**: APIs, Log files, Mobile apps, IoT telemetry.
* **Data Storage**
    * **Concepts**: Data Lakes, Data Warehousing, Cold vs. Hot storage.
* **Data Ingestion**
    * **Methods**: Batch (Airbyte, Fivetran), Streaming (Kafka, Kinesis), CDC (Change Data Capture).
* **Data Serving**
    * **Output**: BI Tools (Tableau, Power BI), REST APIs (FastAPI), Feature Stores.
 **Data Management**
    * **Governance**: Data Quality, Data Lineage. Metadata, Interoperability
    * **Security**: 
    * **Pivacy**: GDPR, ECPA, EU AI Act 
 
--- 

## 3.1 Data Generation
* Messaging Systems
   * What and why use them
   * Aync vs Sync
   * Messages Vs Streams
      * Apache Kafka
      * Aws SQS
      * AWS SNS       

--- 

## 3.2 Data Storage

### 3.2.1 Databases, Data Modeling
something about databases.

* Centralised Storage: NFS, FTP
* Distributed Storage: HDFS
* Cloud Storage: S3, DataBlock
* **Database Fundamentals**
* **Relational (SQL)**: PostgreSQL, MySQL, SQL Server, Oracle
* **NoSQL**
   *    Document: MongoDB,
   *    Columnar:Cassandra
   *    Graph: Neo4j
   *    Key-Value: Redis
* Data Normalisation
* SCD
* Star vs snoflake
* Data Modelling Techniques
* **Modeling**: Kimball vs. Inmon, Star & Snowflake Schemas, SCD Types.
* CAP Theorem
* OLTP Vs OLAP
* Horizontal Vs Vertical Scaling
* Introduction to cloud Computing


### 3.2.2 Datawarehousing

* Data Warehousing
* Data Warehousing Architectures
   * Data Mart
   * Data Mesh
   * Data Fabric
   * Data Hub
   * Metadata-first Architecture
   * Serverless options
* Datawarehouse
   * Snowflake
   * Redshift
   * Google BigQuery
* Data Lake
   * Databricks
   * Snowflake
   * oneHouse

--- 

## 3.3 Data Ingestion
* Types of Data Ingestion
   * Batch
   * Hybrid
   * Realtime
   * 
### 3.3.1 Data Pipelines

* Data Pipelines
   * ETL
      * Extract
      * Trasnform
      * Load
   * Pipeline Tools
      * **Orchestration**
         * Apache Airflow
         * DBT
         * Prefect
      * **Processing**
         * Centralised Computing
         * Distributed Computing
         * Cloud Computing


 --- 

## 3.4 Data Serving
* Data Analytics
* Business Intelligence
* BI Tools
   * Power BI
   * Tableau 


------ 

## 4. Cloud Computing
somthing about cloud computing

* **Cloud Architecture**
   * AWS
   * Azure
   * GCP
  
---

## 5. Infrastructure & DataOps
* **Containers**: Docker, Kubernetes (K8s).
* **IaC**: Terraform, Ansible, AWS CDK.
* **CI/CD**: GitHub Actions, Jenkins.
* **Monitoring**: Datadog
* **Quality**: Great Expectations, DataHub (Metadata).
