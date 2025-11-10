# ⚡ AWS DynamoDB — Concepts & Quick Notes

**Amazon DynamoDB** is a **fully managed NoSQL database** that delivers **single-digit millisecond latency**, **serverless scalability**, and **high availability** across multiple AZs.

---

## 📑 Table of Contents

* [What is DynamoDB?](#-what-is-dynamodb)
* [Core Concepts](#-core-concepts)
* [Capacity Modes](#-capacity-modes)
* [Consistency Models](#-consistency-models)
* [Indexes](#-indexes)
* [Security](#-security)
* [Backup & Restore](#-backup--restore)
* [Performance & Scaling](#-performance--scaling)
* [Monitoring](#-monitoring)
* [Common Use Cases](#-common-use-cases)
* [CLI Commands](#-cli-commands)

---

## 📍 What is DynamoDB?

* **Fully managed**, **serverless**, **NoSQL key-value** and **document database**.
* Automatically scales to **millions of requests per second**.
* **Replicated across multiple AZs** for fault tolerance.
* Ideal for workloads requiring **low latency** and **high throughput**.

💡 **Key Highlight:** DynamoDB abstracts all server management — no patching, provisioning, or replication setup needed.

---

## 🧠 Core Concepts

| Concept                | Description                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------- |
| **Table**              | Collection of items (like a relational table).                                         |
| **Item**               | A record in a table (like a row).                                                      |
| **Attribute**          | A field inside an item (like a column).                                                |
| **Partition Key (PK)** | Primary key used to partition data.                                                    |
| **Sort Key (SK)**      | Optional; helps sort and group items within the same PK.                               |
| **Primary Key Types**  | - **Simple PK:** Partition Key only  <br> - **Composite PK:** Partition Key + Sort Key |

📘 **Example:**

| Key Type    | Example                |
| ----------- | ---------------------- |
| **PK Only** | `UserID`               |
| **PK + SK** | `UserID` + `OrderDate` |

✅ **Tip:** Choosing the right **PK and SK** is critical for avoiding **hot partitions** and ensuring balanced performance.

---

## ⚙️ Capacity Modes

| Mode                           | When to Use             | Description                              |
| ------------------------------ | ----------------------- | ---------------------------------------- |
| **On-Demand**                  | Unpredictable workloads | Auto-scales instantly; pay per request.  |
| **Provisioned**                | Predictable workloads   | You define **RCU** and **WCU** manually. |
| **Auto Scaling (Provisioned)** | Dynamic workloads       | Adjusts RCU/WCU based on utilization.    |

### ⚡ Key Metrics

| Unit                          | Meaning                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------ |
| **RCU (Read Capacity Unit)**  | 1 strongly consistent read/sec for a 4KB item (2 eventually consistent reads). |
| **WCU (Write Capacity Unit)** | 1 write/sec for a 1KB item.                                                    |

💡 **Tip:** Always monitor **Consumed vs Provisioned Capacity** to avoid throttling.

---

## 📏 Consistency Models

| Model                     | Description                       | Performance                |
| ------------------------- | --------------------------------- | -------------------------- |
| **Eventually Consistent** | Data might take time to propagate | ✅ Fastest                  |
| **Strongly Consistent**   | Always reads the most recent data | ⚠️ Slightly higher latency |

Use **strong consistency** when reading immediately after writing critical data.

---

## 🔍 Indexes

| Index Type                       | Full Form                                | Purpose                                      |
| -------------------------------- | ---------------------------------------- | -------------------------------------------- |
| **LSI (Local Secondary Index)**  | Alternate sort key (same partition key). | Used for range queries on same partition.    |
| **GSI (Global Secondary Index)** | Alternate PK + SK combination.           | Enables flexible query patterns across data. |

📌 **Notes:**

* LSI: Must be created at table creation (max **5 per table**).
* GSI: Can be added later and scales independently (has separate RCU/WCU).

💡 Use GSIs for **query flexibility**, and LSIs for **sorted views** on existing PKs.

---

## 🔐 Security

* IAM roles & policies for access management.
* **Encryption at rest** using AWS KMS (enabled by default).
* **VPC Endpoints** for private DynamoDB access (no public internet).
* **Fine-grained access control (FGAC)** using IAM condition keys for per-item security.
* **Encryption in transit** via HTTPS (TLS).

✅ Combine IAM + KMS + VPC for full enterprise-grade protection.

---

## 📦 Backup & Restore

| Feature                           | Description                                                            |
| --------------------------------- | ---------------------------------------------------------------------- |
| **PITR (Point-in-Time Recovery)** | Continuous automatic backup up to 35 days.                             |
| **Manual Backups**                | Create on-demand snapshots for long-term retention.                    |
| **Global Tables**                 | Multi-region replication for disaster recovery and low-latency access. |

💡 **Tip:** Use **Global Tables** to sync data automatically across multiple AWS regions.

---

## 🚀 Performance & Scaling

* **Horizontal Scaling** via partitions (each partition stores a subset of data).
* Avoid **hot partitions** by choosing a **high-cardinality partition key**.
* Use **DAX (DynamoDB Accelerator)** for **microsecond latency** with in-memory caching.
* **Adaptive Capacity** automatically redistributes throughput to handle uneven access patterns.
* **Batch operations** (BatchGetItem / BatchWriteItem) improve bulk performance.

✅ **Best Practice:** Use **pagination** for large result sets to avoid exceeding size limits (1 MB per query).

---

## 📊 Monitoring

| Tool                     | Purpose                                                |
| ------------------------ | ------------------------------------------------------ |
| **CloudWatch Metrics**   | Monitor RCU/WCU usage, throttles, latency, and errors. |
| **CloudTrail**           | Logs all DynamoDB API calls for auditing.              |
| **Contributor Insights** | Identify hot keys or traffic-heavy items.              |

💡 Set CloudWatch **alarms** for throttling or high latency to auto-scale before issues occur.

---

## 🧰 Common Use Cases

| Use Case                     | Description                                     |
| ---------------------------- | ----------------------------------------------- |
| 🎮 **Gaming / Leaderboards** | Store scores and session data with low latency. |
| 🛒 **Shopping Carts**        | Real-time, user-specific cart data.             |
| 🧩 **IoT / Sensor Data**     | High-volume device event ingestion.             |
| 💬 **Chat / Messaging Apps** | Fast reads & writes with composite keys.        |
| ⚙️ **Serverless Apps**       | Works seamlessly with **Lambda + API Gateway**. |

✅ **Real-World Example:**
A **serverless microservice** using **Lambda + API Gateway + DynamoDB** for scalable data storage without managing servers.

---

## 💻 CLI Commands

```bash
# List all tables
aws dynamodb list-tables

# Create a new table
aws dynamodb create-table \
  --table-name Users \
  --attribute-definitions AttributeName=UserID,AttributeType=S \
  --key-schema AttributeName=UserID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST

# Insert an item
aws dynamodb put-item \
  --table-name Users \
  --item '{"UserID": {"S": "101"}, "Name": {"S": "Alex"}}'

# Query an item
aws dynamodb query \
  --table-name Users \
  --key-condition-expression "UserID = :id" \
  --expression-attribute-values '{":id":{"S":"101"}}'

# Delete an item
aws dynamodb delete-item \
  --table-name Users \
  --key '{"UserID": {"S": "101"}}'
```

💡 **Tip:** Always use `--billing-mode PAY_PER_REQUEST` during early dev/testing to avoid capacity throttling.

---

## 🧠 Quick Memory Hooks

| Concept           | Quick Recall                              |
| ----------------- | ----------------------------------------- |
| **PK / SK**       | Defines partitioning & sorting            |
| **RCU/WCU**       | Read & Write throughput units             |
| **LSI**           | Alternate SK on same PK                   |
| **GSI**           | New PK + SK combination                   |
| **PITR**          | Continuous backup (35 days)               |
| **DAX**           | In-memory cache for reads                 |
| **Global Tables** | Multi-region replication                  |
| **Hot Partition** | Too many requests on one key = throttling |

---

✅ **Final Tip:**
DynamoDB shines when you **design your data model around access patterns**.
Unlike relational databases — **think queries first, then design keys.**

