# 📘 AWS RDS – Complete Notes

**Amazon RDS (Relational Database Service)** is a **fully managed relational database service** that simplifies database setup, operation, and scaling — while automating **backups, patching, monitoring, and failover**.

---

## ✅ 1. What is RDS?

* AWS **managed relational database service**.
* Automates **backups, patching, monitoring, and scaling**.
* Provides **high availability** and **disaster recovery** using Multi-AZ deployments.
* Supports **OLTP workloads** and multiple popular **database engines**.
* Integrated with **IAM, VPC, CloudWatch, and KMS** for full security & observability.

💡 **Key Benefit:** Focus on your data and queries — AWS handles the operational heavy lifting.

---

## 🧠 2. Supported Database Engines

| Engine            | Description                                    | Key Benefit                                                                   |
| ----------------- | ---------------------------------------------- | ----------------------------------------------------------------------------- |
| **Amazon Aurora** | AWS-built MySQL & PostgreSQL-compatible engine | 5× faster than MySQL, 3× faster than PostgreSQL, auto-healing, fault-tolerant |
| **MySQL**         | Open-source relational database                | Popular, cost-effective, community-backed                                     |
| **PostgreSQL**    | Advanced open-source DB                        | Supports complex queries, JSON, and custom extensions                         |
| **MariaDB**       | MySQL fork                                     | Enhanced performance and features                                             |
| **Oracle**        | Enterprise-grade DB                            | Enterprise licensing, robust features, PL/SQL                                 |
| **SQL Server**    | Microsoft DB                                   | Integrated with Windows & .NET ecosystem                                      |

💡 **Aurora** is the best option for performance, scalability, and managed resilience.

---

## 🧩 3. RDS Core Concepts

| Concept               | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| **DB Instance**       | A single database environment (compute + storage).           |
| **DB Cluster**        | Group of DB instances (specific to Aurora).                  |
| **Endpoint**          | Hostname used to connect to the database.                    |
| **Multi-AZ**          | Standby replica in another AZ for high availability.         |
| **Read Replica**      | Asynchronous replica for read scaling and disaster recovery. |
| **Parameter Group**   | Controls DB runtime configuration settings.                  |
| **Option Group**      | Adds optional features (e.g., Oracle TDE, SQL Server Audit). |
| **Snapshot**          | Point-in-time backup of the database instance.               |
| **Automated Backups** | Continuous PITR backups (up to 35 days).                     |

💡 **Parameter Group** = Configuration at runtime
**Option Group** = Add-on database features

---

## 🛡️ 4. High Availability & Durability

### 🔁 Multi-AZ Deployment

* Provides **synchronous replication** to a standby instance in another AZ.
* Ensures **automatic failover** during outages.
* Used primarily for **high availability** and **disaster recovery**.

### 📖 Read Replicas

* Provides **asynchronous replication** from the primary DB.
* Used for **read scalability** or **reporting queries**.
* Can be **promoted** to a standalone database.

| Feature              | Multi-AZ               | Read Replica             |
| -------------------- | ---------------------- | ------------------------ |
| **Replication Type** | Synchronous            | Asynchronous             |
| **Purpose**          | High Availability / DR | Read Scaling             |
| **Failover**         | Automatic              | Manual (Promote Replica) |
| **Availability**     | Standby (same region)  | Cross-region supported   |

💡 Use **Multi-AZ** for HA and **Read Replicas** for read-heavy workloads.

---

## 🗂️ 5. Backups

| Type                  | Description                                 | Retention              |
| --------------------- | ------------------------------------------- | ---------------------- |
| **Automated Backups** | Daily snapshots + transaction logs for PITR | Up to **35 days**      |
| **Manual Snapshots**  | User-initiated snapshots                    | Retained until deleted |

🧩 **Point-In-Time Recovery (PITR):** Restore DB to any specific time within retention window.

---

## 🔐 6. Security

* **IAM Policies** → Manage RDS actions (not DB logins).
* **Encryption at Rest** → AWS KMS integration for automatic encryption.
* **Encryption in Transit** → Enforce SSL/TLS connections.
* **VPC Isolation** → Deploy RDS in private subnets.
* **Security Groups** → Control inbound/outbound access.
* **Master User Credentials** → Used for DB-level authentication.
* **IAM Authentication** → Optionally connect using temporary IAM tokens.

💡 **Best Practice:**
Disable public access for production databases and restrict access via **bastion hosts** or **private endpoints**.

---

## 📊 7. Monitoring & Performance

| Feature                  | Description                                                          |
| ------------------------ | -------------------------------------------------------------------- |
| **Amazon CloudWatch**    | Tracks CPU, memory, IOPS, and connections.                           |
| **Enhanced Monitoring**  | Provides real-time OS-level metrics (1–60 sec intervals).            |
| **Performance Insights** | Visual dashboard for query analysis and tuning.                      |
| **RDS Events**           | Sends notifications for instance changes, failovers, or maintenance. |

💡 Use **Performance Insights** to identify top SQL queries affecting performance.

---

## 🛠️ 8. Maintenance & Patching

* AWS applies **automatic minor version updates** during the **maintenance window**.
* You can **schedule or defer** maintenance.
* **Major upgrades** (e.g., MySQL 8 → 9) require manual intervention.
* Supports **zero-downtime patching** for Aurora.

✅ Always test upgrades in a **staging RDS instance** before applying to production.

---

## 📈 9. Scaling

| Scaling Type             | Description                                                    |
| ------------------------ | -------------------------------------------------------------- |
| **Vertical Scaling**     | Increase instance size (e.g., `db.t3.small` → `db.m6g.large`). |
| **Horizontal Scaling**   | Add **Read Replicas** to distribute read load.                 |
| **Storage Auto Scaling** | Automatically increases storage size when nearing capacity.    |
| **Aurora Serverless**    | Auto-scales compute capacity based on workload demand.         |

💡 Use **Aurora Serverless v2** for unpredictable workloads — scales seamlessly with near-zero downtime.

---

## 💾 10. Backup & Restore Process

### 🧱 Backup

* Automated snapshots happen daily.
* Transaction logs allow **Point-in-Time Recovery (PITR)**.
* Manual snapshots can be created anytime.

### 🔁 Restore

* Restore from automated or manual snapshots.
* Restored DB creates a **new instance**.
* Can restore across regions for **DR setup**.

💡 Always test your **restore procedures** to ensure recovery readiness.

---

## 💬 11. Common RDS Interview Questions

1. Explain **Multi-AZ vs Read Replica** differences.
2. How does **RDS automatic failover** work?
3. How do you **encrypt data** at rest and in transit?
4. What is **Point-in-Time Recovery (PITR)**?
5. What is **Amazon Aurora** and why is it faster?
6. How to **scale writes** in RDS?
7. How do you **secure RDS inside a VPC**?
8. Difference between **Parameter Group** and **Option Group**?
9. How to **backup and restore RDS**?
10. Difference between **RDS vs Aurora vs Aurora Serverless**?

---

## 🧩 12. Typical RDS Architecture

```
Client → Application Server (EC2) → RDS (Primary DB)
                         ↳ Read Replica (Read Queries)
                         ↳ Multi-AZ Standby (Failover)
```

**Example Setup:**

* RDS deployed in **private subnet** within VPC.
* Application (EC2 / Lambda) in **public subnet** or behind **ALB**.
* RDS connected via **Security Group rules** (port 3306 for MySQL).
* **CloudWatch Alarms** monitor CPU/memory thresholds.

---

## 🧠 Quick Memory Hooks

| Concept                  | One-Line Recall                         |
| ------------------------ | --------------------------------------- |
| **RDS**                  | Managed relational database on AWS      |
| **Multi-AZ**             | Synchronous standby for HA              |
| **Read Replica**         | Async copy for read scaling             |
| **PITR**                 | Restore DB to any second within 35 days |
| **Parameter Group**      | DB runtime config                       |
| **Option Group**         | Add-on features                         |
| **Aurora**               | Fastest AWS-managed RDS engine          |
| **Enhanced Monitoring**  | OS-level metrics                        |
| **Performance Insights** | Query performance analyzer              |

---

✅ **Final Tip:**
Use **RDS for production workloads** needing relational data, but switch to **Aurora or Aurora Serverless** for enterprise-grade performance, scalability, and cost optimization.
