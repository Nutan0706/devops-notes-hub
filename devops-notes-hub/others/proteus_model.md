
# **🌟 Proteus Model — Detailed Explanation (End-to-End Flow)**

The **Proteus** model is designed to calculate **Tracking Error, Volatility**, and other portfolio risk/analytics metrics by comparing an **Account (Portfolio)** against its corresponding **Benchmark/Bogie**.

---

# **1️⃣ Account & Bogie Setup**

### **🔹 Account Setup**

* We create **one account group** that contains all securities of similar characteristics.
     - Equity portfolio.
     - fixed-income portfolio.
     - sector-based portfolio.
* For each account, we package the required calculation logic, metadata, and security list into a **Docker image**.

### **🔹 Bogie (Benchmark) Setup**

* For every account, we build a *matching benchmark bogie*.
* Bogie includes:

  * Benchmark returns
  * Weight distributions
  * Risk factors
  * Comparison logic
* Bogie is also packaged into its own **Docker image**.

> So now we have two separate containerized entities:
> **Account Data Container** + **Benchmark/Bogie Container**

---

# **2️⃣ Terraform-Provisioned EKS Cluster & Caching Warmup Jobs**

Once both Docker images are prepared, we deploy them onto an **EKS cluster** that is provisioned using **Terraform**.

Terraform sets up:

### **✨ EKS Components**

* Control plane
* Parent + child worker node groups
* Auto-scaling rules

### **✨ Networking**

* VPC
* Public + private subnets
* Route tables
* NAT + Internet Gateway

### **✨ Access & Storage**

* IAM roles
* ECR repository (stores all Proteus docker images)
* S3 buckets (data lake storage)
* CloudWatch for logs & metrics

---

## **🔸 Warmup Jobs**

Before running the main Proteus model, EKS runs **warmup jobs**:

### **Warmup Job 1 — Account Cache Build**

* Loads account-level historical data
* Cleans and prepares factor exposures
* Stores results in in-memory cache (Redis/Valkey/K8s cache)

### **Warmup Job 2 — Bogie Cache Build**

* Loads benchmark returns
* Loads weight distributions
* Prepares bogie factor/sector mappings
* Caches them to speed up final calculations

⚡ **Purpose:**
Warmup ensures that the main Proteus job doesn’t repeatedly fetch & process heavy datasets — improving performance dramatically.

---

# **3️⃣ Combined Account–Bogie Mapping Model**

Once caches are ready, we build a **combined model Docker image**:

This combined image contains:

* Account ↔ Bogie mapping logic
* Tracking Error calculation
* Volatility calculation
* Covariance mathematically optimized scripts
* Risk decomposition modules
* Return reconciliation logic

---

# **4️⃣ Run Proteus Model on EKS Cluster**

The combined Docker container is executed on EKS:

### **Execution Workflow**

* Pull account data from cache
* Pull benchmark/bogie data from cache
* Run attribution + risk calculations
* Generate CSV outputs
* Write all results to S3 buckets

  * `/tracking_error/`
  * `/volatility/`
  * `/risk_components/`
  * `/logs/`

> **Using cache makes this step extremely fast** compared to traditional sequential file reads.

---

# **5️⃣ Post-Processing Jenkins Pipeline → Oracle**

After EKS finishes and files land in S3, Jenkins triggers a post-processing pipeline:

### **Jenkins Steps**

1. **Extract CSVs** from S3
2. **Clean, enrich, and validate** datasets
3. **Perform final transformations** expected by reporting teams
4. **Load the processed data into an Oracle database**

Oracle serves as the **intermediate enterprise datastore** for downstream workflows.

---

# **6️⃣ Oracle → Snowflake Synchronization Pipeline**

Once Oracle contains the fresh processed data, we run another scheduled pipeline:

### **Scheduled ETL Pipeline**

* Connects to Oracle
* Extracts updated Proteus datasets
* Loads them into **Snowflake**
* Snowflake tables then feed dashboards, reporting, and risk analytics applications

This ensures **all reporting tools** (Power BI, Tableau, internal dashboards) access the latest Proteus risk metrics.

---

# **✨ Final Summary (Interview-Friendly)**

Here is a crisp 5–6 line spoken-style version:

**“Basically our Proteus model generates tracking error, volatility, and other risk metrics by comparing each account with its corresponding bogie. First, we containerize account and benchmark data using Docker. Terraform sets up the full EKS infra, and we run warmup jobs to cache account and bogie data so that the main model runs extremely fast. Then we run a combined account-bogie Docker job on EKS, which outputs CSV files into S3. Jenkins picks up those files, loads them into Oracle, and later another scheduled job syncs the processed data from Oracle to Snowflake for reporting.”**
<img width="295" height="392" alt="image" src="https://github.com/user-attachments/assets/1818fa65-c178-4d53-812f-b30785567511" />



Here is your statement rewritten into **clear, crisp bullet points** — perfect for interviews or documentation:

---

### **Proteus Model — Key Workflow Pointers**

* Our **Proteus model** calculates **Tracking Error, Volatility, and other portfolio risk metrics** by comparing each **account** with its corresponding **bogie (benchmark)**.

* We **containerize** both account data and benchmark/bogie data using **Docker**, making each component modular and portable.

* **Terraform** provisions the entire infrastructure:

  * EKS cluster
  * Node groups
  * Networking, IAM, S3, ECR, etc.

* We run **warmup jobs** on EKS to:

  * Cache account data
  * Cache bogie data
    This significantly **accelerates the main model execution**.

* A **combined account–bogie Docker model** is executed on the EKS cluster, pulling most of its inputs from cache for high performance.

* The model generates **CSV outputs** (TE, Vol, Risk decomposition) and stores them in **S3**.

* **Jenkins** post-processes these outputs:

  * Extracts CSV files from S3
  * Cleans, validates, and transforms the data
  * Loads processed results into **Oracle**

* A **scheduled ETL pipeline** then moves data from **Oracle to Snowflake**, where it becomes available for analytics, reporting, and dashboards.

---

