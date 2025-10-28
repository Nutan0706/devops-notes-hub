# ⚡ AWS DynamoDB — Concepts & Quick Notes

DynamoDB is a **fully managed NoSQL database** by AWS offering **single-digit millisecond latency**, **serverless scaling**, and **built-in HA across AZs**.

---

## 📑 Table of Contents
- [What is DynamoDB?](#-what-is-dynamodb)
- [Core Concepts](#-core-concepts)
- [Capacity Modes](#-capacity-modes)
- [Consistency Models](#-consistency-models)
- [Indexes](#-indexes)
- [Security](#-security)
- [Backup & Restore](#-backup--restore)
- [Performance & Scaling](#-performance--scaling)
- [Monitoring](#-monitoring)
- [Use Cases](#-use-cases)
- [CLI Commands](#-cli-commands)

---

<details>
<summary><h2>📍 What is DynamoDB?</h2></summary>

- Fully managed **NoSQL key-value & document database**.
- Automatically scales to **millions of requests per second**.
- Data is **replicated across multiple AZs** for high availability.
- Supports **Key-Value** and **Document** data models.

</details>

---

<details>
<summary><h2>🧠 Core Concepts</h2></summary>

| Concept | Description |
|---------|--------------|
| **Table** | Collection of items (like a DB table). |
| **Item** | A record in a table (like a row). |
| **Attribute** | A field inside an item (column). |
| **Partition Key (PK)** | Mandatory key for partitioning data. |
| **Sort Key (SK)** | Optional; helps sort items within the same PK. |
| **Primary Key Types** | - **Simple PK:** Partition Key only <br> - **Composite PK:** Partition Key + Sort Key |

> ✅ **Tip:** Choose PK & SK wisely — it defines performance & scalability.

Example Primary Keys Table:

| Key Type | Example |
|----------|----------|
| PK Only | `UserID` |
| PK + SK | `UserID` + `OrderDate` |

</details>

---

<details>
<summary><h2>⚙️ Capacity Modes</h2></summary>

| Mode | Use Case | Notes |
|------|-----------|--------|
| **On-Demand** | Unpredictable traffic | Auto-scales; pay per request |
| **Provisioned** | Predictable workload | Set RCU/WCU manually |
| + **Auto Scaling** | For provisioned mode | Adjust capacity automatically |

- **RCU (Read Capacity Unit)** → 1 strongly consistent read / 2 eventually consistent reads per second for 4 KB item.  
- **WCU (Write Capacity Unit)** → 1 write/sec for 1 KB item.

</details>

---

<details>
<summary><h2>📏 Consistency Models</h2></summary>

| Model | Description | Latency |
|--------|----------------|-----------|
| **Eventually Consistent** | Data may take time to sync | Faster |
| **Strongly Consistent** | Always returns latest data | Slightly slower |

</details>

---

<details>
<summary><h2>🔍 Indexes</h2></summary>

| Index Type | Full Form | Purpose |
|-------------|-------------|------------|
| **LSI** | Local Secondary Index | Query on alternate SK (same PK) |
| **GSI** | Global Secondary Index | Query on different PK & SK |

> 📌 **LSI Limit:** Can only be created at table creation time and max **5 per table**.  
> 📌 **GSI:** Can be added anytime; consumes RCU/WCU separately.

</details>

---

<details>
<summary><h2>🔐 Security</h2></summary>

- IAM policies for access control.
- **Encryption at Rest** using KMS.
- **VPC Endpoints** for private connectivity.
- Fine-grained access control per item/attribute.

</details>

---

<details>
<summary><h2>📦 Backup & Restore</h2></summary>

| Feature | Description |
|----------|----------------|
| **Automated Backups** | Continuous backup & restore (PITR). |
| **Manual Snapshots** | On-demand snapshot backups. |
| **Global Tables** | Multi-region replication for DR/geo latency. |

</details>

---

<details>
<summary><h2>🚀 Performance & Scaling</h2></summary>

- Horizontal scaling via **partitions**.
- Hot partitions affect performance — avoid skewed PKs.
- Use **DAX (DynamoDB Accelerator)** for in-memory caching (microsecond latency).
- **Adaptive Capacity** auto balances partitions.

</details>

---

<details>
<summary><h2>📊 Monitoring</h2></summary>

- CloudWatch metrics (RCU/WCU usage, throttling, latency).
- CloudTrail for API auditing.
- Contributor Insights for identifying traffic hotspots.

</details>

---

<details>
<summary><h2>🧰 Common Use Cases</h2></summary>

- Real-time applications (gaming, bidding, auctions)
- Microservices session stores
- Shopping carts, IoT, AdTech
- Leaderboards & chat apps
- Serverless apps (Lambda + DynamoDB)

</details>

---

<details>
<summary><h2>💻 CLI Commands</h2></summary>

```bash
# List tables
aws dynamodb list-tables

# Create table
aws dynamodb create-table \
  --table-name Users \
  --attribute-definitions AttributeName=UserID,AttributeType=S \
  --key-schema AttributeName=UserID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST

# Put item
aws dynamodb put-item --table-name Users --item '{"UserID": {"S": "101"}, "Name": {"S": "Alex"}}'

# Query
aws dynamodb query \
  --table-name Users \
  --key-condition-expression "UserID = :id" \
  --expression-attribute-values '{":id":{"S":"101"}}'

</details>
