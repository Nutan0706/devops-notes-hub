# ☁️ AWS S3 (Simple Storage Service) – Complete Notes

**Amazon S3 (Simple Storage Service)** is a **fully managed object storage** service that allows you to store and retrieve **any amount of data** from anywhere in the world.

It’s **highly available**, **secure**, and **infinitely scalable**, offering **11 9’s durability** (`99.999999999%`) and **99.99% availability**.

---

## 1️⃣ What is S3?

* **Object-based storage** (stores files as objects with metadata).
* Ideal for **backups, static websites, big data, and analytics**.
* Infinitely scalable and accessible via REST API, CLI, SDK, or AWS Console.
* Designed for **11 9’s durability** and **multi-AZ redundancy**.

💡 **Note:** Unlike EBS or EFS, S3 is not a file or block storage service — it’s **object storage**.

---

## 2️⃣ Core Concepts

| Concept             | Description                                                       |
| ------------------- | ----------------------------------------------------------------- |
| **Bucket**          | A container for storing objects (must have globally unique name). |
| **Object**          | The actual data + metadata.                                       |
| **Key**             | A unique identifier for each object in a bucket.                  |
| **Region**          | Buckets exist within a single AWS region.                         |
| **Prefix**          | Acts like a folder path (used for performance optimization).      |
| **Versioning**      | Maintains multiple versions of the same object.                   |
| **Storage Classes** | Tiered storage based on cost and access frequency.                |

💡 **Tip:** Avoid using overly nested “folders” — S3 is a flat structure under the hood.

---

## 3️⃣ S3 Storage Classes

| Storage Class                       | Use Case                                 | Key Points                                   |
| ----------------------------------- | ---------------------------------------- | -------------------------------------------- |
| **Standard**                        | Frequently accessed data                 | Default class, multi-AZ storage              |
| **Intelligent-Tiering**             | Unknown or changing access patterns      | Automatically moves objects to cheaper tiers |
| **Standard-IA (Infrequent Access)** | Infrequently accessed but critical data  | Low cost, retrieval fee                      |
| **One Zone-IA**                     | Non-critical, infrequently accessed data | Stored in a single AZ                        |
| **Glacier Instant Retrieval**       | Archival with immediate access           | Retrieval in milliseconds                    |
| **Glacier Flexible Retrieval**      | Archival with low-cost access            | Retrieval in minutes to hours                |
| **Glacier Deep Archive**            | Long-term cold storage                   | Cheapest, retrieval can take up to 12 hours  |

💡 Use **Lifecycle Rules** to automatically transition data between these classes.

---

## 4️⃣ Data Consistency Model

S3 provides **strong read-after-write consistency** for all operations:

* New object PUTs
* Overwrites and DELETEs

This ensures data reads immediately reflect the latest write operation.

---

## 5️⃣ Security in S3

| Security Layer                | Description                                                   |
| ----------------------------- | ------------------------------------------------------------- |
| **Bucket Policy**             | JSON-based policy for controlling access at the bucket level. |
| **IAM Policy**                | Grants users, roles, or services access to S3 resources.      |
| **ACL (Access Control List)** | Legacy access mechanism (avoid using).                        |
| **Block Public Access**       | Global setting to block public access (recommended).          |
| **Encryption Options**        | Protect data at rest and in transit.                          |

### 🔐 Encryption Types

| Type            | Managed By | Description                         |
| --------------- | ---------- | ----------------------------------- |
| **SSE-S3**      | AWS        | AES-256 encryption (default option) |
| **SSE-KMS**     | AWS KMS    | KMS-managed keys + audit trail      |
| **SSE-C**       | Customer   | Customer-provided keys              |
| **Client-Side** | You        | Encrypt before upload               |

💡 Always enable **SSE-KMS** for enterprise-grade data protection and compliance.

---

## 6️⃣ Data Protection

| Feature                     | Purpose                                                       |
| --------------------------- | ------------------------------------------------------------- |
| **Versioning**              | Preserve, retrieve, and restore previous versions of objects. |
| **MFA Delete**              | Adds multi-factor authentication for delete operations.       |
| **Replication (CRR / SRR)** | Copy objects across or within regions for redundancy.         |
| **Object Lock**             | Enforce WORM (Write Once, Read Many) for compliance.          |

💡 **CRR** (Cross-Region Replication) improves durability and supports disaster recovery setups.

---

## 7️⃣ Public Access & Sharing

* Buckets are **private by default**.
* Public access can be granted via:

  * **Bucket Policy**
  * **Object ACLs** (not recommended)
  * **Pre-Signed URLs** (temporary access)

### Example: Generate Pre-Signed URL

```bash
aws s3 presign s3://my-bucket/photo.png --expires-in 3600
```

➡️ Grants temporary (1-hour) read access.

---

## 8️⃣ Lifecycle Management

Automate **data transitions and deletions** using lifecycle policies:

* Move data to **IA** or **Glacier** after X days.
* Delete old versions automatically.
* Expire temporary or unused data.

💡 Common use case:
`Standard → IA after 30 days → Glacier after 90 days → Delete after 365 days`

---

## 9️⃣ Static Website Hosting

* You can **host static websites** (HTML, CSS, JS) directly from S3.
* Enable **Static Website Hosting** in bucket properties.
* Set permissions to allow **public read** (or use CloudFront).
* Optional: Use **Route 53** for custom domain mapping.

💡 Example Website Endpoint:
`http://mybucket.s3-website-us-east-1.amazonaws.com`

---

## 🔟 Performance Optimization

| Optimization              | Description                                                 |
| ------------------------- | ----------------------------------------------------------- |
| **Multipart Upload**      | Speeds up upload of large files (>100 MB).                  |
| **Transfer Acceleration** | Uploads via AWS edge locations for faster global transfers. |
| **Parallelization**       | Use multiple prefixes to improve throughput.                |

💡 Use **S3 Transfer Acceleration** for distributed teams or global applications.

---

## 1️⃣1️⃣ S3 Event Notifications

| Integration    | Description                                     |
| -------------- | ----------------------------------------------- |
| **AWS Lambda** | Trigger serverless functions on object uploads. |
| **Amazon SNS** | Send notifications to subscribers.              |
| **Amazon SQS** | Queue file processing workflows.                |

💡 Example:
When a file is uploaded → Trigger Lambda → Process → Store result → Notify via SNS.

---

## 1️⃣2️⃣ Pricing Components

You are charged for:

* **Storage Used (per GB/month)**
* **Requests** (PUT, GET, DELETE)
* **Data Transfer Out**
* **Glacier Retrievals**

💡 **Inbound data transfers are free.**

### Example:

| Component          | Example Cost            |
| ------------------ | ----------------------- |
| Storage (Standard) | $0.023 / GB / month     |
| PUT/GET Requests   | $0.005 / 1,000 requests |
| Data Transfer Out  | $0.09 / GB              |

---

## 1️⃣3️⃣ Useful AWS CLI Commands

```bash
# List all buckets
aws s3 ls

# List objects in a bucket
aws s3 ls s3://my-bucket/

# Upload file to bucket
aws s3 cp file.txt s3://my-bucket/

# Sync local folder to bucket
aws s3 sync . s3://my-bucket/

# Delete object
aws s3 rm s3://my-bucket/file.txt

# Enable versioning
aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled
```

---

## 🧠 Quick Memory Hooks

| Concept              | One-Line Recall                          |
| -------------------- | ---------------------------------------- |
| **Bucket**           | Container for objects                    |
| **Object**           | File + metadata                          |
| **Key**              | Unique object identifier                 |
| **Storage Classes**  | Different tiers for cost optimization    |
| **SSE-KMS**          | AWS-managed encryption with audit trail  |
| **CRR**              | Replication across regions               |
| **Lifecycle Policy** | Automate transitions & deletions         |
| **Pre-Signed URL**   | Temporary access without making public   |
| **Multipart Upload** | Boosts performance for large files       |
| **Durability**       | 11 9’s reliability = near zero data loss |

---

✅ **Final Tip:**
Use **S3 + CloudFront + Route 53** to host **secure, globally distributed static websites**,
and pair with **S3 Versioning + Lifecycle Rules + Replication** for data protection and compliance.
