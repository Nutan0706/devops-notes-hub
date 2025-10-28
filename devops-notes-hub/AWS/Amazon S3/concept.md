# Amazon S3 Concepts

# ☁️ AWS S3 (Simple Storage Service) – Complete Notes

## ✨ 1. What is S3?

> **Amazon S3 (Simple Storage Service)** is an object storage service used to store and retrieve any amount of data from anywhere.

- Object-based storage (not block/file storage)
- Infinitely scalable
- Highly available
- **11 9’s durability** → `99.999999999%` (designed for 99.99% availability)

---

## 📌 2. Core Concepts

| Concept | Description |
|--------|--------------|
| **Bucket** | Container for objects; bucket name must be globally unique |
| **Object** | Data + Metadata stored inside a bucket |
| **Key** | Unique identifier for an object |
| **Region** | Buckets are created per region |
| **Prefix** | Acts like folder path (pseudo-folder) |
| **Versioning** | Stores multiple versions of the same object |
| **Storage Classes** | Different cost vs access trade-off |

---

## 🧊 3. S3 Storage Classes

| Storage Class | Use Case | Key Points |
|---------------|-----------|-------------|
| **Standard** | Frequent access | Default, multi-AZ |
| **Intelligent-Tiering** | Unknown/variable usage | Auto-moves to cheaper tier |
| **Standard-IA** | Infrequent access | Minimum retention charges |
| **One Zone-IA** | Infrequent access but non-critical | Stored in 1 AZ (low cost) |
| **Glacier Instant Retrieval** | Archive with instant access | Millisecond retrieval |
| **Glacier Flexible Retrieval** | Archive with less frequent access | Minutes to hours |
| **Glacier Deep Archive** | Long-term backup | Up to 12-hour retrieval, cheapest |

---

## 🔄 4. Data Consistency Model

✅ **Strong Read-After-Write consistency** for:

- PUTs of new objects
- Overwrite PUTs & DELETEs

---

## 🔐 5. Security in S3

- **Bucket Policy** → JSON policy applied to entire bucket
- **IAM Policy** → User/role-based access
- **ACL (Access Control List)** → Legacy, object-level permissions (avoid)
- **Block Public Access** → Recommended to avoid accidental exposure
- **Encryption** Options:  

  - **SSE-S3** → AES-256 (managed by AWS)  
  - **SSE-KMS** → KMS managed keys + audit trail  
  - **SSE-C** → Customer-provided keys  
  - **Client-Side Encryption** → You encrypt before upload  

---

## 🛡️ 6. Data Protection

| Feature | Purpose |
|--------|----------|
| **Versioning** | Protect from accidental deletes/overwrites |
| **MFA Delete** | Adds multi-factor authentication for delete ops |
| **Replication (CRR / SRR)** | Copy objects to another bucket (cross or same region) |
| **Object Lock** | WORM (Write Once Read Many) compliance |

---

## 🌍 7. Public Access & Sharing

- Default: **Private**
- Can be made public using:
  - Bucket Policy
  - ACL (not recommended)
  - **Pre-Signed URLs** (temporary access without making it public)

---

## 🔁 8. Lifecycle Management

Automate:

- Move objects to cheaper classes
- Delete old versions
- Expire unused data

---

## 🌐 9. Static Website Hosting

- Host static HTML, CSS, JS
- Must enable **public read** or using CloudFront
- Can use Route53 for custom domain

---

## ⚡ 10. Performance Optimization

- Use **Multipart Upload** for >100 MB objects
- Use **S3 Transfer Acceleration** for faster global uploads
- Use multiple prefixes to improve throughput

---

## 🔔 11. S3 Event Notifications

Trigger events to:

| Service | Use Case |
|---------|------------|
| **Lambda** | Process files on upload |
| **SNS** | Send notifications |
| **SQS** | Queue for processing |

---

## 💰 12. Pricing Components

You are charged for:

- **Storage** per GB
- **Requests** (GET, PUT, DELETE)
- **Data Transfer Out**
- **Glacier retrieval**

> TIP: Inbound data is **FREE**.

---

## 🧑‍💻 13. Useful CLI Commands

```bash
# List all buckets
aws s3 ls

# List objects in a bucket
aws s3 ls s3://my-bucket/

# Upload file to bucket
aws s3 cp file.txt s3://my-bucket/

# Sync local folder to bucket
aws s3 sync . s3://my-bucket/

# Remove object
aws s3 rm s3://my-bucket/file.txt
