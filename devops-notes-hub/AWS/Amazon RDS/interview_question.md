# 🧠 AWS RDS – Interview Questions (Beginner → Advanced + Scenarios)

This document provides **40 well-structured RDS interview questions** with hints, categorized for all experience levels.

---

<details>
<summary><h2>📍 1. Commonly Asked RDS Interview Questions (Beginner Level)</h2></summary>

1. **What is Amazon RDS?**  
   _Hint: Managed relational database service..._

2. **Which database engines are supported by RDS?**  
   _Hint: At least 6 major engines…_

3. **What is the difference between RDS and Aurora?**  
   _Hint: Aurora is AWS-built, faster…_

4. **What is Multi-AZ in RDS?**  
   _Hint: High Availability, synchronous replication…_

5. **What are Read Replicas and why are they used?**  
   _Hint: Scaling read traffic…_

6. **What is an RDS Parameter Group?**  
   _Hint: DB runtime configuration settings…_

7. **What is the default backup retention period of RDS?**  
   _Hint: Between 0 to 35 days… default = ?_

8. **Does RDS provide automatic failover? If yes, when?**  
   _Hint: Multi-AZ only…_

9. **How can you connect to an RDS instance securely?**  
   _Hint: SG + SSL connectivity…_

10. **What are RDS Snapshots?**  
    _Hint: Manual vs automated backups…_
</details>

---

<details>
<summary><h2>⚙️ 2. Moderate-Level RDS Interview Questions</h2></summary>

1. **Explain Multi-AZ vs Read Replicas.**  
   _Hint: HA vs Scaling…_

2. **How does automatic failover work in RDS Multi-AZ?**  
   _Hint: Standby promoted… DNS switch…_

3. **How does RDS encryption at rest work?**  
   _Hint: KMS… once enabled, can't disable…_

4. **What is a DB Subnet Group? Why is it required?**  
   _Hint: At least 2 AZs… private subnets…_

5. **How to enable IAM Authentication for RDS MySQL/PostgreSQL?**  
   _Hint: Token-based, temporary credentials…_

6. **Difference between Parameter Group and Option Group.**  
   _Hint: Config vs Add-on features…_

7. **How to scale RDS vertically vs horizontally?**  
   _Hint: Instance class vs replicas…_

8. **Can we take snapshots of encrypted DB and restore to unencrypted DB?**  
   _Hint: Yes/No? Think encryption rules…_

9. **What is the use of Performance Insights?**  
   _Hint: Slow queries, DB bottleneck analysis…_

10. **How can you restrict RDS access from public internet?**  
    _Hint: VPC, SG, no public access…_
</details>

---

<details>
<summary><h2>🚀 3. Advanced RDS Interview Questions</h2></summary>

1. **How does Aurora achieve higher performance than RDS MySQL/PostgreSQL?**  
   _Hint: Shared storage + 6 copies across 3 AZs…_

2. **Describe the RDS storage types and when to use each.**  
   _Hint: GP3, IO-Optimized, Magnetic…_

3. **How does Point-In-Time Recovery (PITR) work internally?**  
   _Hint: Transaction log + snapshots…_

4. **Can we encrypt an existing unencrypted RDS instance? If yes, how?**  
   _Hint: Snapshot → copy with encryption → restore…_

5. **Explain RDS Proxy and its use case.**  
   _Hint: Connection pooling for Lambda/Serverless…_

6. **How Read Replicas work across regions?**  
   _Hint: Cross-Region Replication… Disaster recovery…_

7. **Can Multi-AZ and Read Replica be enabled together?**  
   _Hint: Yes… Multi-AZ replica as source?…_

8. **What happens during RDS maintenance window?**  
   _Hint: Patching, OS updates, downtime possibility…_

9. **Explain Aurora Global Database architecture.**  
   _Hint: Multi-region <1 sec replication…_

10. **How does RDS handle failover in Aurora?**  
    _Hint: Reader → Writer promotion in seconds…_
</details>

---

<details>
<summary><h2>📌 4. Scenario-Based RDS Interview Questions (Advanced + Real-World)</h2></summary>

1. **Your application is read-heavy and facing performance issues. How would you scale RDS?**  
   _Hint: Read Replicas, caching…_

2. **Your RDS MySQL instance in ap-south-1 must be available if the entire region fails. What will you do?**  
   _Hint: Cross-region read replica / Aurora Global…_

3. **Your DB CPU is 90%+ for 30 minutes. What actions will you take?**  
   _Hint: Analyze Performance Insights + scale…_

4. **Team needs to access RDS only via a bastion host. How do you configure networking?**  
   _Hint: Private subnets + SG rules…_

5. **RDS storage is increasing rapidly every day. How will you find root cause and reduce cost?**  
   _Hint: CloudWatch metrics, logs, lifecycle cleanup…_

6. **A developer accidentally deleted some data. Can RDS recover it? How?**  
   _Hint: PITR or snapshot restore…_

7. **An app using RDS + Lambda is failing due to too many connections. Solution?**  
   _Hint: RDS Proxy…_

8. **Need to migrate on-prem Oracle to AWS with minimal downtime — what service?**  
   _Hint: DMS + RDS Oracle/Aurora…_

9. **Application requires 0-second failover & sub-second replication — choice?**  
   _Hint: Aurora…_

10. **RDS is performing slow during peak hours. Give steps to troubleshoot.**  
    _Hint: Performance Insights → Enhanced Monitoring → Indexing…_
</details>

---

<details>
<summary><h2>⭐ 5. Bonus: 10 Most Frequently Asked in Interviews</h2></summary>

> ✅ **If you have time for only 10 — learn these!**

1. RDS vs Aurora  
2. Multi-AZ vs Read Replica  
3. RDS backup & restore strategy  
4. How encryption works  
5. Performance Insights  
6. RDS Proxy use cases  
7. How failover happens  
8. RDS scaling methods  
9. Parameter vs Option Groups  
10. Cross-Region DR strategy  
</details>

---
