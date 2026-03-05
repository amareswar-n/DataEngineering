### How Spark Distributed Joins Work

```mermaid
flowchart TB

%% --------------------------------
%% 1. Spark Reading Data from S3
%% --------------------------------

subgraph S3["Source: Amazon S3"]
A["Data Files"]
end

subgraph Partitions["Logical Partitions (~128MB each)"]
P1["Partition 0"]
P2["Partition 1"]
P3["Partition 2"]
end

A --> P1
A --> P2
A --> P3

subgraph Scheduler["Spark Scheduler"]
T1["Task 0"]
T2["Task 1"]
T3["Task 2"]
end

P1 --> T1
P2 --> T2
P3 --> T3

subgraph Executors["Executors"]
E1["Executor 1"]
E2["Executor 2"]
end

T1 --> E1
T2 --> E2
T3 --> E1


%% --------------------------------
%% 2. Why Data Must Move Before Join
%% --------------------------------

subgraph Customers["Customers Dataset"]
C1["Partition 0<br>ID:101<br>ID:19"]
C2["Partition 1<br>ID:66<br>ID:56"]
C3["Partition 2<br>ID:42<br>ID:13"]
end

subgraph Orders["Orders Dataset"]
O1["Partition 0<br>ID:972<br>ID:245"]
O2["Partition 1<br>ID:56<br>ID:501"]
O3["Partition 2<br>ID:15<br>ID:458"]
end

Customers --> H["Hash(customer_id)"]
Orders --> H

H --> JP1["Target Partition 0"]
H --> JP2["Target Partition 1"]
H --> JP3["Target Partition 2"]


%% --------------------------------
%% 3. Shuffle Stage
%% --------------------------------

subgraph ShuffleSource["Source Partitions"]
S1["Partition 0"]
S2["Partition 1"]
end

subgraph Shuffle["Shuffle (Network + Disk I/O)"]
X["Shuffle Exchange"]
end

subgraph ShuffleTarget["Repartitioned Data"]
R1["Partition 0"]
R2["Partition 1"]
R3["Partition 2"]
end

S1 --> X
S2 --> X
X --> R1
X --> R2
X --> R3


%% --------------------------------
%% 4. Executor Join Operation
%% --------------------------------

subgraph ExecutorTask["Executor Join Task"]
B["Build Side Rows"]
HT["Hash Table (in memory)"]
P["Probe Side Rows"]
J["Joined Output"]
end

B --> HT
P --> HT
HT --> J
