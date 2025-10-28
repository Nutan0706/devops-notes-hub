# 📘 AWS RDS – Complete Notes 

Amazon RDS (Relational Database Service) is a **fully managed relational database service** that automates backups, patching, monitoring, and scaling.

---

<details>
<summary><h2>✅ 1. What is RDS?</h2></summary>

- **AWS Managed Relational Database Service**
- Automates: **Backups, patching, automatic failover, monitoring, scaling**
- Supports multiple database engines  
- Great for **OLTP workloads**

</details>

---

<details>
<summary><h2>🧠 2. Supported DB Engines</h2></summary>

| Engine | Description | Key Benefit |
|--------|--------------|----------------|
| **Aurora** | AWS-built, MySQL & PostgreSQL compatible | 5× faster than MySQL, 3× faster than PostgreSQL, auto-healing |
| **MySQL** | Open-source relational DB | Cost-effective, community support |
| **PostgreSQL** | Advanced, open-source | Best for complex queries & extensions |
| **MariaDB** | MySQL fork | Enhancements over MySQL |
| **Oracle** | Enterprise DB | Supports enterprise features, license dependent |
| **SQL Server** | Microsoft DB | Windows + enterprise ecosystem |

</details>

---

<details>
<summary><h2>🧩 3. RDS Core Concepts</h2></summary>

| Concept | Description |
|----------|----------------|
| **DB Instance** | Single DB compute + storage environment |
| **DB Cluster** | Group of DB instances (Aurora only) |
| **Endpoint** | Hostname to connect to DB |
| **Multi-AZ** | Synchronous standby DB for HA & failover |
| **Read Replica** | Asynchronous copy for read scaling |
| **Parameter Group** | Controls DB runtime configurations |
| **Option Group** | Adds DB engine optional features (e.g., Oracle TDE) |
| **Snapshots** | Backup of DB state |
| **Automated Backups** | PITR (Point-in-time) up to 35 days |

</details>

---

<details>
<summary><h2>🛡️ 4. High Availability & Durability</h2></summary>

### 🔁 Multi-AZ Deployment (for HA)
- Synchronous replication to standby in another AZ
- Automatic failover on primary failure

### 📖 Read Replicas (for Read Scaling)
- Asynchronous replication
- Offload read workload
- Replicas can be **promoted** to standalone DB

| Feature | Multi-AZ | Read Replica |
|---------|-----------|----------------|
| Replication | Sync | Async |
| Use Case | HA / DR | Read scaling |
| Failover | Automatic | Manual promote |

</details>

---

<details>
<summary><h2>🗂️ 5. Backups</h2></summary>

| Type | Description | Retention |
|-------|----------------|--------------|
| **Automated Backups** | Daily snapshot + transaction logs (PITR) | Up to 35 days |
| **Manual Snapshots** | User-initiated | Until deleted |

</details>

---

<details>
<summary><h2>🔐 6. Security</h2></summary>

- **IAM Policies** → Control who can manage RDS (not DB login)
- **Encryption at Rest** → KMS managed keys
- **Encryption in Transit** → SSL/TLS
- **VPC + Security Groups** → Network isolation & access control
- **Master User Credentials** → For DB authentication
- IAM roles for DB API calls

> **Tip:** Always disable public access unless required.

</details>

---

<details>
<summary><h2>📊 7. Monitoring</h2></summary>

| Feature | Purpose |
|----------|------------|
| **CloudWatch** | Monitor CPU, memory, IOPS, connections |
| **Enhanced Monitoring** | OS-level metrics every 1–60 sec |
| **Performance Insights** | Query analysis + bottleneck detection |
| **RDS Events** | Notifications for DB events/changes |

</details>

---

<details>
<summary><h2>🛠️ 8. Maintenance & Patching</h2></summary>

- AWS performs **automatic minor version updates**
- You can set **maintenance window**
- Major upgrades — **manual action** required

</details>

---

<details>
<summary><h2>💬 9. Common Interview Questions</h2></summary>

1. Explain **Multi-AZ vs Read Replica**.  
2. How does **RDS automatic failover** work?  
3. How do you **encrypt data at rest and in transit**?  
4. What is **Point-In-Time Recovery** (PITR)?  
5. What is **Aurora** and why is it faster than MySQL/PostgreSQL?  
6. How do you **scale write operations** in RDS?  
7. How do you **secure RDS** inside a VPC?  
8. Explain **Parameter Group vs Option Group**.  
9. How do you take **backup and restore RDS**?  
10. Difference between **RDS vs Aurora vs Aurora Serverless**?  

</details>

---

### 📍 Typical Architecture with RDS
