# 🧠 AWS S3 Practical Learning — For 5-Year Experienced DevOps Engineer

---

Amazon S3 (Simple Storage Service) is one of the most essential AWS services for storing and managing data at scale.  
This guide covers hands-on practical tasks from **beginner** to **advanced** — designed specifically for experienced DevOps professionals.

---

## 🟢 Beginner Level (Fundamentals)

| # | Practical Task | Description |
|---|----------------|-------------|
| 1 | **Create an S3 Bucket** | Create a basic S3 bucket using AWS Console and AWS CLI.<br>```bash<br>aws s3 mb s3://my-first-devops-bucket --region ap-south-1<br>``` |
| 2 | **Upload and Download Files** | Upload and download files using both Console and AWS CLI.<br>```bash<br>aws s3 cp sample.txt s3://my-first-devops-bucket/<br>aws s3 cp s3://my-first-devops-bucket/sample.txt ./<br>``` |
| 3 | **Set Bucket Permissions** | Configure public/private access for objects and experiment with Access Control Lists (ACLs). |
| 4 | **Enable Versioning** | Enable versioning on a bucket to keep multiple versions of the same object for recovery.<br>```bash<br>aws s3api put-bucket-versioning --bucket my-first-devops-bucket --versioning-configuration Status=Enabled<br>``` |
| 5 | **Enable Static Website Hosting** | Host a simple HTML website on S3 and access it via the bucket endpoint. |

> ✅ **Tip:** Use `aws s3 ls` to list buckets and verify if your configurations are applied correctly.

---

### ✅ Outcome
By the end of this section, you’ll confidently:
- Create and manage S3 buckets  
- Upload/download data  
- Control permissions  
- Enable versioning and website hosting  
- Understand the basic S3 storage concepts  

---

## 🟡 Moderate Level (Real-World Use Cases)

| # | Practical Task | Description |
|---|----------------|-------------|
| 1 | **Setup S3 Lifecycle Policy** | Configure lifecycle rules to move objects from Standard → Glacier or delete after a set time. |
| 2 | **Enable Logging & Monitoring** | Enable Server Access Logging and integrate S3 with CloudWatch for monitoring. |
| 3 | **Use S3 with AWS CLI Sync** | Sync a local folder with S3 bucket for efficient backup.<br>```bash<br>aws s3 sync ./backup-folder s3://my-devops-backups --delete<br>``` |
| 4 | **Implement Cross-Region Replication (CRR)** | Replicate data automatically between two buckets in different regions for disaster recovery. |
| 5 | **Encrypt S3 Data (SSE-S3 & SSE-KMS)** | Apply encryption at rest using either S3-managed keys or KMS-managed keys.<br>```bash<br>aws s3 cp file.txt s3://secure-devops-bucket/ --sse aws:kms<br>``` |

> ⚙️ **Tip:** Always enable encryption by default using **Bucket Default Encryption** for compliance and data protection.

---

### ✅ Outcome
After completing this level, you’ll:
- Automate S3 data lifecycle  
- Monitor and log S3 activity  
- Maintain regional redundancy  
- Secure data with encryption  
- Perform efficient backups using CLI sync  

---

## 🔴 Advanced Level (Automation, Integration, and Security)

| # | Practical Task | Description |
|---|----------------|-------------|
| 1 | **Automate S3 Bucket Creation using Terraform** | Write a Terraform script to create S3 buckets with versioning and encryption enabled.<br>```bash<br>resource "aws_s3_bucket" "devops_bucket" {<br>  bucket = "terraform-devops-s3"<br>  versioning { enabled = true }<br>  server_side_encryption_configuration {<br>    rule { apply_server_side_encryption_by_default { sse_algorithm = "AES256" } }<br>  }<br>}<br>``` |
| 2 | **Integrate S3 with Lambda** | Configure an event trigger on `s3:ObjectCreated:*` to automatically invoke a Lambda function for processing uploads. |
| 3 | **Implement S3 Access via IAM Roles & Policies** | Create least-privilege IAM roles for EC2/Lambda access to S3.<br>```json<br>{ "Effect": "Allow", "Action": ["s3:GetObject"], "Resource": "arn:aws:s3:::my-secure-bucket/*" }<br>``` |
| 4 | **Secure Access with Bucket Policy & VPC Endpoint** | Restrict S3 access to only specific VPC endpoints for private network communication. |
| 5 | **Setup S3 Event Notifications to SNS/SQS** | Create S3 event notifications to send object creation events to SNS or SQS for further processing. |

> 🔐 **Tip:** Always validate your bucket policies using **IAM Policy Simulator** to avoid accidental public exposure.

---

### ✅ Outcome
After completing this level, you’ll:
- Automate infrastructure creation with Terraform  
- Integrate S3 with serverless components like Lambda  
- Enforce least-privilege access control  
- Build secure, event-driven systems  
- Master end-to-end S3 automation for DevOps pipelines  

---

## 🧰 Bonus Tools & Commands

| Purpose | Command |
|----------|----------|
| List all buckets | `aws s3 ls` |
| Delete bucket | `aws s3 rb s3://bucket-name --force` |
| Get bucket policy | `aws s3api get-bucket-policy --bucket bucket-name` |
| Upload recursively | `aws s3 cp . s3://bucket-name --recursive` |
| Set default encryption | `aws s3api put-bucket-encryption --bucket bucket-name --server-side-encryption-configuration file://encrypt.json` |

> 💡 **Pro Tip:** Always combine S3 with **CloudTrail**, **CloudWatch**, and **IAM Access Analyzer** to monitor access and enforce compliance.

---

### 🎯 Final Outcome

By mastering all 3 levels, you’ll be able to:
- Design, deploy, and secure large-scale S3 architectures  
- Automate configurations via Terraform and AWS CLI  
- Integrate S3 with Lambda, SNS, and SQS  
- Implement enterprise-grade backup, logging, and replication strategies  

---

> 🏁 **Next Steps:**  
> - Integrate S3 with **CloudFront** for global content delivery  
> - Combine with **AWS Backup** for centralized data protection  
> - Explore **S3 Object Lock** and **Intelligent-Tiering** for advanced use cases  

---
