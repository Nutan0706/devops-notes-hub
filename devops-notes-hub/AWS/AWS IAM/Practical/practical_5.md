# 🧩 Practical 5 — Cross-Account IAM Role Access

## 🎯 Objective
Allow a user or service from **Account A** to access resources (like S3 or EC2) in **Account B** using **role assumption**.  
This enables secure access **without sharing credentials** between accounts.

---

## 🧠 Prerequisite Setup
- You have **two AWS accounts**:
  - **Account A (Source)** → where the IAM user exists.
  - **Account B (Target)** → where the resources and IAM role exist.

> Example IDs:  
> - Account A ID → `111111111111`  
> - Account B ID → `222222222222`

---

## 🪜 Step-by-Step Implementation

### **Step 1: Create IAM Role in Account B (Target Account)**
1. Log in to **Account B** (target account).
2. Open **IAM → Roles → Create role**.
3. Under **Trusted entity type**, select **Another AWS account**.
4. Enter **Account A’s AWS Account ID** (e.g., `111111111111`).
5. (Optional) Enable **Require external ID** for extra security (commonly used in CI/CD setups).

🖼️ _Add Screenshot: Trusted entity setup with Account A ID_

---

### **Step 2: Attach Permissions to the Role**
1. Choose the permissions this role will grant — for example:
   - `AmazonS3ReadOnlyAccess`
   - or any custom policy for specific resources.
2. Click **Next** → **Name the role** as `CrossAccountS3AccessRole`.
3. Click **Create role**.

🖼️ _Add Screenshot: Role creation with attached policy_

---

### **Step 3: Copy the Role ARN**
1. After creation, open the role you just made.  
2. Copy its **Role ARN**, e.g.: arn:aws:iam::222222222222:role/CrossAccountS3AccessRole
🖼️ _Add Screenshot: Role ARN from role summary page_

---

### **Step 4: Create IAM Policy in Account A (Source Account)**
1. Switch to **Account A**.
2. Go to **IAM → Policies → Create policy**.
3. Choose the **JSON** tab and paste the following:

```json
{
"Version": "2012-10-17",
"Statement": [
 {
   "Effect": "Allow",
   "Action": "sts:AssumeRole",
   "Resource": "arn:aws:iam::222222222222:role/CrossAccountS3AccessRole"
 }
]
}
```
4. Replace 222222222222 with your **target account ID**.
5. Name the policy → AllowCrossAccountRoleAssume.
6. Click **Create policy**.

🖼️ Add Screenshot: JSON for AssumeRole policy

---

### **Step 5: Attach Policy to IAM User in Account A**

1. Go to **IAM → Users**.  
2. Select your IAM user (e.g., **devops-user**).  
3. Click **Add permissions → Attach existing policies directly**.  
4. Select the policy **AllowCrossAccountRoleAssume**.  
5. Click **Save changes**.  

🖼️ _Add Screenshot: Policy attached to user_

---

### **Step 6: Assume Role via AWS CLI (from Account A)**

1. Log in as the **IAM user** from **Account A** using the AWS CLI.  
2. Run the following command to assume the cross-account role:

   ```bash
   aws sts assume-role \
     --role-arn arn:aws:iam::222222222222:role/CrossAccountS3AccessRole \
     --role-session-name CrossAccountSession
   ```
3. The output will include temporary credentials:
```json
{
  "Credentials": {
    "AccessKeyId": "ASIA...",
    "SecretAccessKey": "xxxx",
    "SessionToken": "xxxx",
    "Expiration": "2025-10-30T12:00:00Z"
  }
}
```
🖼️ Add Screenshot: CLI output for assume-role command

---
## 🧩 Step 7: Use Temporary Credentials

Export the temporary credentials to your environment variables:

```bash
export AWS_ACCESS_KEY_ID=ASIA...
export AWS_SECRET_ACCESS_KEY=xxxx
export AWS_SESSION_TOKEN=xxxx
```
Now, test access to the target resource (for example, an S3 bucket in Account B):
```bash
aws s3 ls
```
✅ If the configuration is correct, you’ll see the list of S3 buckets or objects accessible via the assumed role.

🖼️ Screenshot:
Add CLI output verifying successful cross-account access below:

```

## ✅ Verification Checklist

- [x] **IAM Role** created in the target account with the correct **trust policy**.  
- [x] **IAM User** in the source account can **assume the role** successfully.  
- [x] **Temporary credentials** generated and exported correctly.  
- [x] Verified **access to target account resources** (e.g., S3 bucket listing works).







