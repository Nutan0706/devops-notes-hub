# Amazon S3 Interview Questions

# ☁️ AWS S3 – Interview Questions (Beginner → Advanced → Scenarios)

This document contains **40 S3 Interview Questions** categorized into 4 levels with **hints**.  
Each section is **collapsible** for easy reading on GitHub.

---

<details>
<summary><strong>🟢 1. Basic / Commonly Asked (10)</strong></summary>

1. **What is Amazon S3?**  
   _Hint: Object storage, durability, scalability._

2. **Explain Bucket & Object in S3.**  
   _Hint: Container vs stored data with metadata._

3. **What are S3 Storage Classes? Name at least 4.**  
   _Hint: Standard, IA, Intelligent-Tiering, Glacier..._

4. **What is Versioning in S3 and why is it used?**  
   _Hint: Protect against accidental delete/overwrite._

5. **How do you make an S3 bucket public?**  
   _Hint: Bucket policy + public access settings._

6. **Difference between S3 Bucket Policy and IAM Policy?**  
   _Hint: Resource based vs identity based._

7. **What is a Pre-Signed URL?**  
   _Hint: Temporary secure access to private object._

8. **What is the durability and availability of S3?**  
   _Hint: 11 9’s durability._

9. **Can you host a static website on S3? How?**  
   _Hint: Enable static website hosting page._

10. **What is S3 Intelligent-Tiering?**  
    _Hint: Automatically moves objects to cheaper tiers._

</details>

---

<details>
<summary><strong>🟡 2. Moderate Level Questions (10)</strong></summary>

1. **Explain S3 Consistency Model.**  
   _Hint: Strong read-after-write._

2. **Difference between S3 Standard-IA and One Zone-IA.**  
   _Hint: Multi-AZ vs single AZ._

3. **What is S3 Lifecycle Management?**  
   _Hint: Transition & Expiration rules._

4. **Explain S3 Encryption types.**  
   _Hint: SSE-S3, SSE-KMS, SSE-C, Client-side._

5. **What is Cross-Region Replication (CRR) and when is it used?**  
   _Hint: Compliance, DR._

6. **How can you restrict access to S3 objects at IP level?**  
   _Hint: Bucket policy with condition → IP Address._

7. **Difference between S3 Access Logs and CloudTrail logs.**  
   _Hint: Access vs API activity._

8. **How to prevent accidental deletion of objects?**  
   _Hint: Versioning + MFA Delete._

9. **Explain S3 Transfer Acceleration.**  
   _Hint: Uses CloudFront edge network._

10. **What is S3 Object Lock?**  
    _Hint: WORM – Write Once Read Many._

</details>

---

<details>
<summary><strong>🟠 3. Advanced Questions (10)</strong></summary>

1. **How does S3 handle data durability across AZs?**  
   _Hint: Replicates data internally across multiple AZs._

2. **Difference between S3 Replication (CRR/SRR) & Backup.**  
   _Hint: Asynchronous copying vs recovery snapshot._

3. **Can CRR replicate existing objects? How do you enable it?**  
   _Hint: Need replicate existing objects flag or Batch Operations._

4. **How does S3 Select improve performance & cost?**  
   _Hint: Query partial data using SQL._

5. **S3 vs EFS vs EBS – When to use what?**  
   _Hint: Object vs file vs block storage._

6. **How to enforce all uploads to S3 be encrypted?**  
   _Hint: Bucket Policy with deny if no `x-amz-server-side-encryption`._

7. **What are S3 Event Notifications limitations?**  
   _Hint: No ordering guarantee, may not deliver once, no cross-region event without EventBridge._

8. **What is Amazon Macie? How does it relate to S3?**  
   _Hint: Sensitive data discovery + security for S3._

9. **How do you protect S3 against public access?**  
   _Hint: Block Public Access, VPC endpoints, PrivateLink._

10. **Explain S3 Requester Pays.**  
    _Hint: Data access charges paid by requester, not bucket owner._

</details>

---

<details>
<summary><strong>🔴 4. Scenario-Based / Highly Advanced (10)</strong></summary>

1. **You need to host a static website for millions of users with low latency. How would you design it using S3?**  
   _Hint: S3 + CloudFront + OAC/OAI + Route53._

2. **Your S3 bucket is private. You want to share a file for download for only 2 hours. What will you use?**  
   _Hint: Pre-Signed URL._

3. **A company wants objects replicated across regions but only if they are tagged “Prod”. How to achieve this?**  
   _Hint: CRR + replication rules + tag filter._

4. **User uploaded data to S3 but cannot access it from EC2 private subnet. How to fix?**  
   _Hint: VPC Endpoint for S3._

5. **You want to ensure that no one (including root) can delete objects for 7 years.**  
   _Hint: Object Lock Compliance mode._

6. **S3 storage costs have increased heavily. How do you reduce cost without deleting data?**  
   _Hint: Lifecycle rules + Intelligent-Tiering + S3 Storage Lens._

7. **You must allow a 3rd-party vendor to upload files to your S3 but not read existing files.**  
   _Hint: Bucket policy with PutObject only + no ListObjects._

8. **Users from a particular country must be blocked from accessing S3 assets.**  
   _Hint: Bucket policy with geo-based deny (CloudFront recommended)._

9. **Your S3 events must trigger multiple actions (Lambda, SQS, SNS). How to design with limitations?**  
   _Hint: Use EventBridge instead of S3 native event notifications._

10. **Data lake on S3 has millions of objects. How do you copy/tag/modify metadata for all existing objects?**  
    _Hint: S3 Batch Operations._

</details>

---

