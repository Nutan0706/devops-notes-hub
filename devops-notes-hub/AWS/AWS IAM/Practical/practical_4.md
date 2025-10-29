# 🧩 Practical 4 — Create Custom IAM Policy (JSON)

## 🎯 Objective
Create a **custom IAM policy** in JSON format that grants **restricted access** (e.g., read-only) to a **specific S3 bucket** instead of allowing access to all buckets.

---

## 🪜 Step-by-Step Implementation

### **Step 1: Open IAM Dashboard**
1. Sign in to the **AWS Management Console**.
2. Navigate to **IAM** service.
3. In the left panel, click on **Policies**.
4. Click **“Create policy”**.
<img width="1898" height="416" alt="image" src="https://github.com/user-attachments/assets/352e38b3-793f-4321-900e-fcc54ff0e106" />

---

### **Step 2: Switch to JSON Editor**
1. In the **Create policy** wizard, select the **JSON** tab.  
2. Remove any default JSON content.
<img width="1825" height="605" alt="image" src="https://github.com/user-attachments/assets/66de0bd6-b839-405f-8d61-3000b36e2491" />

---

### **Step 3: Write Custom Policy JSON**
Paste the following JSON into the editor:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-devops-bucket"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::my-devops-bucket/*"
      ]
    }
  ]
}
```
🔹 Replace my-devops-bucket with your actual S3 bucket name.

---

### *** Step 4: Review and Create Policy ***
1.Click on **Next**.
2.Add a **Policy name** — e.g., S3ReadOnlySpecificBucket.
3.(Optional) Add a **description** like:
   “Allows read-only access to a specific S3 bucket.”
5.Click **Create policy**.

🖼️ Add Screenshot: Review and create policy screen

---

### **Step 5: Attach Policy to User, Group, or Role**

1. Go to **IAM → Users** (or **Groups / Roles**, depending on your case).  
2. Select the target entity (e.g., **devops-user**).  
3. Navigate to **Permissions → Add permissions → Attach existing policies directly**.  
4. Search for your custom policy **S3ReadOnlySpecificBucket** and attach it.

🖼️ _Add Screenshot: Attach custom policy to user_

---

### **Step 6: Test the Custom Policy**

1. Log in as that **IAM user** or use their **AWS CLI credentials**.  
2. Run the following commands:

   ```bash
   aws s3 ls s3://my-devops-bucket
   aws s3 cp s3://my-devops-bucket/test.txt .
   aws s3 rm s3://my-devops-bucket/test.txt
   ```
3. Verify the behavior:
   ✅ **List** and **Get** operations succeed.
   ❌ **Delete** operation fails (since it’s not allowed).

---

### ✅ **Verification Checklist**

- ✅ Custom IAM policy created successfully.  
- ✅ Policy grants access to only one specific S3 bucket.  
- ✅ Correctly attached to user, group, or role.  
- ✅ Permissions tested successfully via AWS CLI.

