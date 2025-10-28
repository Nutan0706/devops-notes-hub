# ☁️ AWS S3 (Simple Storage Service) – Complete Notes

<details>
<summary><strong>1️⃣ What is S3?</strong></summary>

- **Amazon S3 (Simple Storage Service)** is an object storage service used to store and retrieve any amount of data from anywhere.
- Object-based storage (not block/file storage)
- Infinitely scalable
- Highly available
- **11 9’s durability** → `99.999999999%` (designed for 99.99% availability)

</details>

---

<details>
<summary><strong>2️⃣ Core Concepts</strong></summary>

| Concept | Description |
|--------|--------------|
| **Bucket** | Container for objects; bucket name must be globally unique |
| **Object** | Data + Metadata stored inside a bucket |
| **Key** | Unique identifier for an object |
| **Region** | Buckets are created per region |
| **Prefix** | Acts like folder path (pseudo-folder) |
| **Versioning** | Stores multiple versions of the same object |
| **Storage Classes** | Different cost vs access trade-off |

</details>

---

<details>
<summary><strong>3️⃣ S3 Storage Classes</strong></summary>

| Storage Class | Use Case | Key Points |
|---------------|-----------|-------------|
| **Standard** | Frequent access | Default, multi-AZ |
| **Intelligent-Tiering** | Unknown/variable usage | Auto-moves to cheaper tier |
| **Standard-IA** | Infrequent access | Minimum retention charges |
| **One Zone-IA** | Infrequent access but non-critical | Stored in 1 AZ (low cost) |
| **Glacier Instant Retrieval** | Archive with instant access | Millisecond retrieval |
| **Glacier Flexible Retrieval** | Archive with less frequent access | Minutes to hours |
| **Glacier Deep Archive** | Long-term backup | Up to 12-hour retrieval, cheapest |

</details>

---

<details>
<summary><strong>4️⃣ Data Consistency Model</strong></summary>

✅ **Strong Read-After-Write consistency** for:
- PUTs of new objects
- Overwrite PUTs & DELETEs

</details>

---

<details>
<summary><strong>5️⃣ Security in S3</strong></summary>

- **Bucket Policy** → JSON policy applied to entire bucket  
- **IAM Policy** → User/role-based access  
- **ACL (Access Control List)** → Legacy, object-level permissions (avoid)  
- **Block Public Access** → Recommended to avoid accidental exposure  
- **Encryption** Options:  
  - **SSE-S3** → AES-256 (managed by AWS)  
  - **SSE-KMS** → KMS managed keys + audit trail  
  - **SSE-C** → Customer-provided keys  
  - **Client-Side Encryption** → You encrypt before upload  

</details>

---

<details>
<summary><strong>6️⃣ Data Protection</strong></summary>

| Feature | Purpose |
|--------|----------|
| **Versioning** | Protect from accidental deletes/overwrites |
| **MFA Delete** | Adds multi-factor authentication for delete ops |
| **Replication (CRR / SRR)** | Copy objects to another bucket (cross or same region) |
| **Object Lock** | WORM (Write Once Read Many) compliance |

</details>

---

<details>
<summary><strong>7️⃣ Public Access & Sharing</strong></summary>

- Default: **Private**
- Can be made public using:
  - Bucket Policy
  - ACL (not recommended)
  - **Pre-Signed URLs** (temporary access without making it public)

</details>

---

<details>
<summary><strong>8️⃣ Lifecycle Management</strong></summary>

Automate:
- Move objects to cheaper classes
- Delete old versions
- Expire unused data

</details>

---

<details>
<summary><strong>9️⃣ Static Website Hosting</strong></summary>

- Host static HTML, CSS, JS
- Must enable **public read** or via CloudFront
- Can use Route53 for custom domain

</details>

---

<details>
<summary><strong>🔟 Performance Optimization</strong></summary>

- Use **Multipart Upload** for >100 MB objects
- Use **S3 Transfer Acceleration** for faster global uploads
- Use multiple prefixes to improve throughput

</details>

---

<details>
<summary><strong>1️⃣1️⃣ S3 Event Notifications</strong></summary>

Trigger events to:

| Service | Use Case |
|---------|------------|
| **Lambda** | Process files on upload |
| **SNS** | Send notifications |
| **SQS** | Queue for processing |

</details>

---

<details>
<summary><strong>1️⃣2️⃣ Pricing Components</strong></summary>

You are charged for:

- **Storage** per GB
- **Requests** (GET, PUT, DELETE)
- **Data Transfer Out**
- **Glacier retrieval**

> 💡 **Inbound data is FREE**

</details>

---

<details>
<summary><strong>1️⃣3️⃣ Useful CLI Commands</strong></summary>

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
