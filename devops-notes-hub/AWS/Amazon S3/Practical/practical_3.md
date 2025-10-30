# 🧠 AWS S3 — Set Bucket Permissions

---

## 🎯 Objective
Configure public/private access for S3 bucket objects and experiment with **Access Control Lists (ACLs)** using both the **AWS Console** and **AWS CLI**.

---

## 🧩 Part 1: Configure Public/Private Access (via Console)

### Step 1: Open the S3 Management Console
1. Go to **AWS Management Console → S3**.  
2. Select your bucket (e.g., `my-first-devops-bucket`).

> 💡 **Tip:** Always double-check the bucket name — modifying wrong bucket permissions can cause data leaks.

---

### Step 2: Go to Permissions Tab
1. Navigate to the **Permissions** tab.  
2. Scroll down to **Block Public Access (Bucket Settings)**.  
3. Click **Edit**.

<img width="1627" height="708" alt="image" src="https://github.com/user-attachments/assets/a15dbc13-3ed7-47c5-b452-895427d2d514" />


---

### Step 3: Configure Public or Private Access
- To **make the bucket private**, ensure all checkboxes are **enabled** (block all public access).  
- To **make it public**, uncheck the boxes for “Block all public access” and confirm the warning.

> ✅ **Note:** Public buckets expose your data on the internet. Use only for testing or static website hosting.

---

### Step 4: Save Changes
Click **Save Changes** and confirm your choice.  
You’ll see the **Public access status** updated on the bucket overview page.

---

## 🧩 Part 2: Manage Bucket and Object ACLs (via AWS CLI)

### Step 1: Check Current ACL
Use this command to view your bucket’s current ACL:

```bash
aws s3api get-bucket-acl --bucket my-first-devops-bucket
```
💡 Tip: ACLs define who can access your bucket and what actions they can perform.

---

### Step 2: Make Bucket Public (ACL-Based)
To make your bucket public using ACLs:
```bash 
aws s3api put-bucket-acl \
  --bucket my-first-devops-bucket \
  --acl public-read
```
<!-- Add snapshot here -->
✅ Note: ACLs are considered legacy by AWS. Prefer using Bucket Policies for fine-grained control.

---

### Step 3: Make Object Private or Public
To make a specific object private:
``` bash 
aws s3api put-object-acl \
  --bucket my-first-devops-bucket \
  --key sample.txt \
  --acl private
```
To make the object public:
```bash
aws s3api put-object-acl \
  --bucket my-first-devops-bucket \
  --key sample.txt \
  --acl public-read
```
<!-- Add snapshot here -->

---

### Step 4: Verify Object Access
To confirm access, check the object’s ACL again:
```bash 
aws s3api get-object-acl \
  --bucket my-first-devops-bucket \
  --key sample.txt
```
<!-- Add snapshot here -->
💡 Tip: You can test public access by opening the object URL in a browser — if public, it will display or download directly.

---
### 🧩 Part 3: Revert to Secure Settings
Once testing is complete, revert your bucket to private mode:
```bash 
aws s3api put-bucket-acl \
  --bucket my-first-devops-bucket \
  --acl private
```
And re-enable “Block all public access” in the Console.
<!-- Add snapshot here -->

✅ Best Practice: Always keep production buckets private. Use IAM roles and bucket policies for controlled access.


