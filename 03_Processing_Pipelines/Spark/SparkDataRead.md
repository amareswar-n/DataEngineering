## How Spark Distributed Joins Work

```mermaid
flowchart LR

%% DATA SOURCE
A["Amazon S3<br>Data Files"]

%% PARTITIONS
subgraph Partitioning["Spark Logical Partitions (~128MB)"]
P1["Partition 0"]
P2["Partition 1"]
P3["Partition 2"]
end

A --> P1
A --> P2
A --> P3

%% TASK SCHEDULING
subgraph Scheduler["Spark Scheduler"]
T1["Task 0"]
T2["Task 1"]
T3["Task 2"]
end

P1 --> T1
P2 --> T2
P3 --> T3

%% EXECUTORS
subgraph Executors["Executors (Workers)"]
E1["Executor 1"]
E2["Executor 2"]
end

T1 --> E1
T2 --> E2
T3 --> E1

%% DATASETS
subgraph Datasets["Datasets to Join"]
C["Customers Dataset"]
O["Orders Dataset"]
end

%% HASH PARTITION
H["Hash(customer_id)"]

C --> H
O --> H

%% SHUFFLE
subgraph Shuffle["Shuffle (Network + Disk I/O)"]
S1["Repartition"]
S2["Repartition"]
S3["Repartition"]
end

H --> S1
H --> S2
H --> S3

%% JOIN EXECUTION
subgraph Join["Executor Join Task"]
B["Build Side"]
HT["Hash Table"]
P["Probe Side"]
J["Joined Output"]
end

B --> HT
P --> HT
HT --> J
```
