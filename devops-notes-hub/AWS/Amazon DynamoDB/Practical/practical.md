# 🧠 AWS DynamoDB Practical Learning — For 5 Years Experienced DevOps Engineer

---

## 🟢 Beginner Level (Fundamentals)

| # | Practical Task | Description |
|---|----------------|-------------|
| 1 | **Create Your First DynamoDB Table** | Create a table with partition key and sort key using AWS Console. |
| 2 | **Add, Update, and Delete Items** | Perform basic CRUD operations manually via the DynamoDB Console. |
| 3 | **Query and Scan Operations** | Learn the difference between Query (indexed) and Scan (full table). |
| 4 | **Understand Data Types & Keys** | Explore supported data types (String, Number, Boolean, Map, List) and primary key design. |
| 5 | **Enable Point-in-Time Recovery (PITR)** | Protect your data by enabling continuous backups and recovery. |

---

## 🟡 Intermediate Level (Real-World Scenarios)

| # | Practical Task | Description |
|---|----------------|-------------|
| 6 | **Access DynamoDB via AWS CLI** | Use CLI commands to create tables, insert items, and query data. |
| 7 | **Integrate DynamoDB with Lambda** | Trigger Lambda on table updates or stream new records for processing. |
| 8 | **Use DynamoDB Streams** | Capture and process real-time data changes with Streams and Lambda. |
| 9 | **Enable Auto Scaling** | Configure read/write capacity auto scaling for cost optimization. |
| 10 | **Implement Global Secondary Index (GSI)** | Create a GSI to enable queries on non-key attributes. |

---

## 🔴 Advanced Level (Enterprise & Automation)

| # | Practical Task | Description |
|---|----------------|-------------|
| 11 | **Deploy DynamoDB Using Terraform / CloudFormation** | Automate table creation, indexes, and capacity settings with IaC. |
| 12 | **Implement On-Demand vs Provisioned Capacity** | Understand and switch between capacity modes based on workload. |
| 13 | **Use Global Tables for Multi-Region Replication** | Set up global tables for high availability and low-latency access. |
| 14 | **Monitor Performance with CloudWatch Metrics** | Track throttled requests, latency, and consumed capacity. |
| 15 | **Implement DynamoDB TTL & Streams for Cleanup** | Automatically expire old records and trigger cleanup workflows. |

---

## ✅ Bonus Practical Tasks for DevOps Engineers

- Integrate **DynamoDB with CI/CD (Jenkins / GitHub Actions)** for table deployment automation.  
- Use **AWS SDK (Python Boto3)** scripts to automate CRUD operations.  
- Enable **Encryption at Rest (KMS)** and **Encryption in Transit (TLS)** for data security.  
- Build a **Serverless Application (API Gateway + Lambda + DynamoDB)** end-to-end.  
- Set **CloudWatch Alarms** to detect throttling, latency spikes, or capacity issues.  

---

> 💡 **Pro Tip:**  
> Design DynamoDB tables based on **access patterns**, not relations. Use **auto-scaling**, **Streams**, and **Global Tables** for enterprise workloads. Always monitor metrics and manage infrastructure using **Terraform** or **CloudFormation**.
