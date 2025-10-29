# 🧠 Practical 7 — Use IAM Policy Variables

## Goal: 
Add ${aws:username} in a policy to dynamically restrict access per user — for example, so each user can only access their own S3 folder.

---

## 🔹 Step-by-Step Guide

### 🧩 Step 1: Open IAM Console
1. Sign in to the **AWS Management Console**.  
2. Navigate to **IAM → Policies → Create policy**.  
3. Switch to the **JSON** tab to define your custom policy.

---

### 🧩 Step 2: Write Custom Policy using IAM Policy Variable

Paste the following JSON policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowUserSpecificFolderAccess",
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": "arn:aws:s3:::mycompany-data"
    },
    {
      "Sid": "AllowAccessToOwnFolder",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::mycompany-data/home/${aws:username}/*"
    }
  ]
}
```

📘 Explanation:
   1. ${aws:username} dynamically substitutes the IAM user’s username.
   2. Each user will only access their own S3 folder (e.g., mycompany-data/home/rahul/).
---

### 🧩 Step 3: Review and Create Policy

1. Click **Next** to move to the review page.  
2. Enter a policy name — for example: **UserSpecificS3AccessPolicy**.  
3. Optionally, add a **description** (e.g., “Allows each IAM user to access only their own S3 folder”).  
4. Review all details and click **Create policy**.

---
🖼️ **Screenshot:**  

### 🧩 Step 4: Attach Policy to Users or Group

1. Navigate to **IAM → Users**.  
2. Select the user(s) you want to grant access to.  
3. Go to the **Permissions** tab → click **Add permissions → Attach policies directly**.  
4. Search for **UserSpecificS3AccessPolicy**.  
5. Select it and click **Add permissions** to attach the policy.

---

🖼️ **Screenshot:**  

### 🧩 Step 5: Test the Policy

1. Log in as the IAM user to whom the policy was attached.  
2. Open the **S3 Console** and try the following actions:
   - ✅ **Allowed:** Upload to `s3://mycompany-data/home/<username>/` 
   - ❌ **Access Denied:** Try uploading to `s3://mycompany-data/home/otheruser/`

✅ Outcome
Each IAM user can only access their own S3 folder, automatically enforced by ${aws:username} — no need for separate policies per user. 

---

