How Spark Moves 10GB Just to Join Two Columns

Let’s strip away the buzzwords and watch what actually happens

You have two tables:
Customers (5GB)
Orders (5GB)

You run a join on customer_id.

Now Spark goes to work.

First, it reads both tables from S3 or HDFS. That 10GB doesn’t move as one giant blob. Spark splits it into smaller chunks called partitions. If we assume 128MB per partition, that’s roughly 80 partitions in total.

Each partition becomes a task.
Tasks are what executors actually run.

Executors don’t “store” the data permanently. They just execute tasks that process one partition at a time. Think of them as workers handling assigned chunks.

Then comes the hard part.

Spark cannot join yet because matching customer IDs might live in completely different partitions across the cluster. So it reorganizes the data.

It takes every row and computes:

partition_id = hash(customer_id) % N

This sends rows across the network so that all records with the same customer_id end up in the same shuffle partition.

That movement across machines is called the shuffle.
It’s the most expensive part of a distributed join.

After the shuffle, something beautiful happens.

Inside each executor, the join becomes a local problem.

Spark picks the smaller side (called the build side) and creates an in-memory hash table:

Key → customer_id
Value → the row

That hash table lives inside the executor’s memory.

Then Spark scans the other table (the probe side). For every row, it computes the hash and checks if that key exists in the hash table. If it does, the rows are joined.

No more network traffic.
Just memory lookups.

Finally, each executor outputs its joined partition, and Spark combines them into the final result.

So the full journey looks like this:

Read → Partition → Shuffle → Build Hash Table → Probe → Match → Output

Under the hood, a distributed systems problem is solved first (moving data), and only then the actual join happens.
