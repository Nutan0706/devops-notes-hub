# 🧠 AWS DynamoDB — Interview Questions (With Hints)

A well-structured set of **40 DynamoDB interview questions** categorized by difficulty with hints.

---

## 📚 Table of Contents
- [10 Commonly Asked Questions](#-10-commonly-asked-questions)
- [10 Moderate Level Questions](#-10-moderate-level-questions)
- [10 Advanced Questions](#-10-advanced-questions)
- [10 Scenario Based Questions](#-10-scenario-based-questions)

---

<details>
<summary><h2>✅ 10 Commonly Asked Questions</h2></summary>

| No. | Question | Hint |
|-----|-----------|-------|
| 1 | What is DynamoDB? | Fully managed NoSQL key-value/document store |
| 2 | Difference between RDS and DynamoDB? | SQL vs NoSQL + scaling |
| 3 | What is a Partition Key? | Determines data distribution |
| 4 | What is Sort Key used for? | Sorts items within same PK |
| 5 | What are RCU and WCU? | Read/Write capacity units |
| 6 | What is DynamoDB On-Demand capacity mode? | Pay per request |
| 7 | What is a DynamoDB Item & Attribute? | Row & column equivalent |
| 8 | What is eventually consistent vs strongly consistent read? | Consistency models |
| 9 | What is TTL in DynamoDB? | Auto-delete item after time |
| 10 | What is DynamoDB Stream? | Change log of item-level modifications |

</details>

---

<details>
<summary><h2>📈 10 Moderate Level Questions</h2></summary>

| No. | Question | Hint |
|-----|-----------|-------|
| 1 | What is a GSI and why do we use it? | Query with different PK/SK |
| 2 | Explain LSI and its limitation. | Must be created at table creation |
| 3 | What is DAX? | In-memory caching layer |
| 4 | Difference between Scan and Query? | Query is efficient, Scan scans full table |
| 5 | What is a hot partition in DynamoDB? | Too many requests to same PK |
| 6 | How does DynamoDB auto-scaling work? | Adjusts RCU/WCU |
| 7 | What are conditional writes? | Write only if condition meets |
| 8 | What is PartiQL? | SQL-like query language for DynamoDB |
| 9 | What is BatchGetItem & BatchWriteItem? | Bulk operations |
| 10 | What is Global Table in DynamoDB? | Multi-region replication |

</details>

---

<details>
<summary><h2>🚀 10 Advanced Questions</h2></summary>

| No. | Question | Hint |
|-----|-----------|-------|
| 1 | How does DynamoDB maintain performance at scale? | Partitioning + adaptive capacity |
| 2 | Explain Adaptive Capacity. | Auto redistributes throughput |
| 3 | How does DynamoDB ensure high availability? | Multi-AZ replication |
| 4 | Describe strategies to prevent hot partitions. | Randomize PK, write sharding |
| 5 | Difference between GSI vs LSI (deep explanation)? | Re-indexing, consistency, storage |
| 6 | How does DynamoDB Streams integrate with Lambda? | Trigger on change events |
| 7 | How does DynamoDB handle transactional operations? | ACID transactions support |
| 8 | Explain item size limits & best practices. | 400 KB limit |
| 9 | When would you use Single-table design? | High-scale, flexible schema |
| 10 | Compare DynamoDB vs MongoDB vs Cassandra. | Architecture + scaling tradeoffs |

</details>

---

<details>
<summary><h2>🎯 10 Scenario Based Questions</h2></summary>

| Scenario | Question | Hint |
|-----------|-------------|--------|
| E-commerce Orders | You need to fetch all orders of a user sorted by date. How will you design PK & SK? | PK = UserID, SK = OrderDate |
| Chat App | Support chat messages sorted by timestamp. Table structure? | PK = ChatRoomID, SK = Timestamp |
| Leaderboard | Need top 10 players globally. How do you design? | Use GSI on Score |
| IoT Devices | 10M devices sending data/sec → avoid hot partitions? | PK randomization / sharding |
| Multi-Region App | App should be globally available with low latency. Solution? | DynamoDB Global Tables |
| Audit Logs | Store logs & auto-delete after 30 days. How? | TTL attribute |
| Banking | Need ACID transactions for balance update. Feature? | DynamoDB Transactions |
| High Read Traffic | 200K reads/sec. Improve performance? | DAX or caching |
| Real-time Analytics | Want to stream changes to S3 for analytics. How? | Kinesis via Streams |
| Multi-Tenant App | Prevent tenant data from mixing. DB design? | TenantID as PK namespace |

</details>

---
