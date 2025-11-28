# **🌟 Hybrid Brinson Attribution**

Hybrid Brinson Attribution is basically a **portfolio performance attribution model**
where we break down how much return came from:

1. **Asset allocation**
2. **Security selection**
3. **Interaction effects**

---

## **1. Portfolio-Level Setup**

* Every **Portfolio Manager (PM)** has a unique **Account Number**.
* For each account, we maintain a **list of securities (Ticker)** that must be processed as part of the Hybrid Brinson attribution calculation.

---

## **2. Per-Security Docker Image Creation**

### **👉 2.1 We create a Docker image per security**

Each Docker image includes:

* Security-level attribution calculation logic
* Hybrid Brinson formula implementation
* Python/R scripts
* Market & benchmark mapping logic

### **👉 2.2 Docker images are generated for multiple horizons**

For every security, we generate four separate processing jobs:

* **Daily**
* **WTD (Week-to-Date)**
* **QTD (Quarter-to-Date)**
* **YTD (Year-to-Date)**

---

## **🔹 3. Execution Using EKS (Kubernetes)**

Once Docker images are ready, the workload is executed on an **EKS cluster (Kubernetes on AWS)**.

---

# **✔️ Terraform Infrastructure Layer (Added After Point 3)**

Before running any jobs, we **provision our entire cloud infrastructure using Terraform**.
Terraform automates the setup of:

* **EKS Cluster**

  * Control plane
  * Managed node groups (parent + child worker nodes)
* **VPC + Subnets + Route Tables + NAT + Internet Gateway**
* **Security Groups & IAM Roles**
* **ECR repository** (for storing Docker images)
* **S3 buckets** (for output data)
* **CloudWatch log groups** (for logs and metrics)

Terraform ensures:

* Infrastructure is **fully automated and reproducible**
* Scaling policies and node groups are **consistent across environments**
* Zero manual setup — everything is code-driven (IaC)

---

## **👉 3.1 Jobs are dispatched to the EKS cluster**

* **Parent Node** → Manages orchestration
* **Child Nodes** → Run each security-level computation in parallel

## **👉 3.2 Kubernetes parallelizes the complete workflow**

* Each security runs independently in its own pod
* Auto-scaling based on load
* Fault tolerance with auto-retry

## **👉 3.3 After processing completes**

Each container produces:

* Security-level attribution CSV
* Horizon-specific output files
* Summary logs / error logs

All processed data is **stored in S3**.

---

## **🔹 4. S3 Used as Output Storage**

A dedicated S3 bucket acts as the storage layer for all processed outputs.

Typical folder structure:

* `/daily/`
* `/wtd/`
* `/qtd/`
* `/ytd/`
* `/logs/`

Each security's processed CSV lands in the appropriate directory.

*This creates a clean, scalable, pay-as-you-go storage layer.*

---

## **🔹 5. Jenkins Pipeline for Post-Processing**

When EKS completes and files appear in S3, Jenkins takes over.

### **👉 Jenkins Pipeline Steps**

#### **1. Extraction Stage**

* Jenkins extracts only the required CSVs from S3
* Performs cleaning, merging, and standardization

#### **2. Validation Stage**

* Checks data consistency
* Ensures no missing fields
* Validates completeness for each PM account

#### **3. Load Stage**

* Final transformed dataset is **loaded into Snowflake**
* Used for:

  * Reporting
  * Dashboards
  * Analytics & downstream processes

*Jenkins acts as a controlled ETL pipeline orchestrator.*

---

