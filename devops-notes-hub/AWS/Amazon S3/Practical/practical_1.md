# 🪣 Create an S3 Bucket — Step-by-step Guide (Console + AWS CLI)

> **Goal:** Provide a clear, GitHub-ready, stepwise `.md` document to create an Amazon S3 bucket using both the **AWS Management Console** and the **AWS CLI**.  
> After each step you'll add a snapshot — placeholders are included (`<!-- Add snapshot here -->`).

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Naming & Region Best Practices](#naming--region-best-practices)
3. [Console: Step-by-step](#console-step-by-step)
4. [CLI: Step-by-step](#cli-step-by-step)
5. [Verify the Bucket](#verify-the-bucket)
6. [Post-creation Recommendations](#post-creation-recommendations)
7. [Cleanup (Optional)](#cleanup-optional)
8. [Troubleshooting & Tips](#troubleshooting--tips)

---

## Prerequisites
- An AWS account with permissions to create S3 buckets (`s3:CreateBucket`, `s3:PutBucket*` as needed).  
- If using AWS CLI: AWS CLI installed and configured (`aws configure`) with an IAM user or role that has S3 permissions.  
> 💡 **Tip:** Use an IAM user with least privilege required for this task (do not use root credentials).

---

## Naming & Region Best Practices
- Bucket names must be globally unique across **all** AWS accounts.  
- Use only lowercase letters, numbers, hyphens (`-`) and periods (`.`) (avoid underscores).  
- Avoid personally identifiable information in bucket names.  
- Choose a region close to your users/compute to reduce latency and egress costs (e.g., `ap-south-1` for Mumbai).  
> ✅ **Note:** When using periods in bucket names, TLS certificate validation can be impacted for virtual-hosted–style access. Prefer hyphens if you plan to use SSL and virtual-hosted style.

---

## Console: Step-by-step

### Step 1 — Open the S3 Console
1. Sign in to the [AWS Management Console].  
2. In the Services search, type **S3** and click **S3** to open the S3 console.
<!-- Add snapshot here -->

---

### Step 2 — Click **Create bucket**
1. In the S3 dashboard, click **Create bucket** (blue button).
<!-- Add snapshot here -->

---

### Step 3 — Configure basic bucket details
1. **Bucket name**: Enter a globally unique name (e.g., `my-company-devops-bucket-2025`).  
2. **Region**: Choose desired region (e.g., **Asia Pacific (Mumbai) ap-south-1**).  
<!-- Add snapshot here -->

> 💡 **Tip:** Keep a naming convention that includes environment and purpose, e.g., `acme-prod-logs-ap-south-1`.
---

### Step 4 — Configure options (Versioning, Tags, Default Encryption)
1. **Versioning** — Enable if you want to keep multiple versions of objects (useful for accidental deletes).  
2. **Tags** — Add key/value tags for cost allocation (e.g., `Environment:dev`, `Owner:team-x`).  
3. **Default encryption** — Enable and choose AWS-SSE-KMS or SSE-S3. KMS gives more control (key rotation, IAM policies).  
<!-- Add snapshot here -->

> 🔐 **Tip:** For production buckets, set **Default encryption** to `aws:kms` and choose an appropriate KMS key.

---

### Step 5 — Block Public Access settings
1. By default, **Block all public access** is enabled — keep this enabled unless you *explicitly* need public objects (e.g., static website).  
2. If you need public access for specific objects, prefer object ACLs or bucket policy with careful scoping instead of disabling block in full.
<!-- Add snapshot here -->

> ⚠️ **Note:** Disabling Block Public Access without strict policies may expose data publicly. Double-check before proceeding.

---

### Step 6 — Review and Create
1. Review all settings.  
2. Click **Create bucket**.
<!-- Add snapshot here -->

> ✅ **Note:** After creation you will see your bucket listed in the S3 console.

---

## CLI: Step-by-step

> **Assumption:** AWS CLI is installed and `aws configure` is set up with an IAM user/role.

### Step 1 — Choose a unique bucket name & region
> Example:
- Bucket name: `my-first-devops-bucket-2025`
- Region: `ap-south-1`

---

### Step 2 — Create the bucket
```bash
# Create a bucket (for most regions use --region)
aws s3 mb s3://my-first-devops-bucket-2025 --region ap-south-1
```

<!-- Add snapshot here -->
✅ Note: For us-east-1 the --region argument behaves differently; prefer specifying --create-bucket-configuration LocationConstraint=us-east-1 for CreateBucket calls when needed.

---

### Step 3 — Enable versioning (optional but recommended for many use-cases)
```bash
aws s3api put-bucket-versioning \
  --bucket my-first-devops-bucket-2025 \
  --versioning-configuration Status=Enabled
```
<!-- Add snapshot here -->
---

### Step 4 — Enable default encryption with AWS KMS (example)
 Create or use an existing KMS key (or use the AWS-managed key aws/s3).
Apply default encryption:
```bash 
aws s3api put-bucket-encryption \
  --bucket my-first-devops-bucket-2025 \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "aws:kms",
        "KMSMasterKeyID": "arn:aws:kms:ap-south-1:123456789012:key/abcd-1234-efgh-5678"
      }
    }]
  }'
```
<!-- Add snapshot here -->

🔐 Tip: If you don’t want to manage KMS keys, use SSE-S3 by setting "SSEAlgorithm": "AES256".

---

### Step 5 — Apply a basic bucket policy to deny non-HTTPS (optional hardening)
```bash
cat > deny-non-https.json <<'POLICY'
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Sid":"DenyNonSSLRequests",
      "Effect":"Deny",
      "Principal":"*",
      "Action":"s3:*",
      "Resource":[
        "arn:aws:s3:::my-first-devops-bucket-2025",
        "arn:aws:s3:::my-first-devops-bucket-2025/*"
      ],
      "Condition":{
        "Bool":{
          "aws:SecureTransport":"false"
        }
      }
    }
  ]
}
POLICY

aws s3api put-bucket-policy --bucket my-first-devops-bucket-2025 --policy file://deny-non-https.json

```

<!-- Add snapshot here -->

✅ Note: Replace my-first-devops-bucket-2025 with your bucket name. Test policies in a non-production environment first.

---

### Verify the Bucket
Verify via Console
  Refresh the S3 console and locate your bucket. Check Properties for Versioning and Encryption settings.

<!-- Add snapshot here -->
Verify via CLI
# List buckets
```bash 
aws s3 ls

# Check versioning
aws s3api get-bucket-versioning --bucket my-first-devops-bucket-2025

# Check encryption
aws s3api get-bucket-encryption --bucket my-first-devops-bucket-2025
```

<!-- Add snapshot here -->
---

### Post-creation Recommendations
1. Enable Server Access Logging or CloudTrail for auditing bucket access.
2. Consider Lifecycle rules to transition older objects to cheaper storage (Intelligent-Tiering/Glacier).
3. Add Tags for cost allocation and owner identification.
4. Configure Replication (CRR or SRR) if cross-region or cross-account redundancy is required.
💡 Tip: Use bucket policies + IAM roles to implement least-privilege access for applications and users.

---

### Cleanup (Optional)
If this bucket was created for testing and you want to remove it:
⚠️ Warning: Deleting a bucket will permanently delete all objects (including versions) unless retained elsewhere.

# Remove all objects (non-versioned)
aws s3 rm s3://my-first-devops-bucket-2025 --recursive

# If versioned, remove versions (careful!)
# Use the aws s3api delete-object with VersionId in a loop or use lifecycle to expire versions.

# Remove the bucket
aws s3 rb s3://my-first-devops-bucket-2025 --force

<!-- Add snapshot here -->

---
### Troubleshooting & Common Errors
# Bucket name already exists
Error: BucketAlreadyOwnedByYou or BucketAlreadyExists
Fix: Choose a globally unique name (append timestamp or org id).

# AccessDenied when creating bucket
Cause: IAM policy denies s3:CreateBucket.
Fix: Ask your admin for the required permissions or adjust IAM policy.

# Region mismatch errors with CLI
Cause: Using wrong --region or not specifying LocationConstraint for certain regions.
Fix: Add --region or --create-bucket-configuration LocationConstraint=<region>.

# Public exposure when unintended
Cause: Bucket policy, ACL, or disabled Block Public Access.
Fix: Re-enable Block Public Access, remove public ACLs/policies, and validate using AWS Trusted Advisor or S3 console warnings.

✅ Tip: Use the AWS CLI aws s3api get-bucket-policy and the S3 console "Permissions" tab to review effective access.
