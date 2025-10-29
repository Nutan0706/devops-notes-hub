# 🧩 Practical 3 — Create IAM Role for EC2 to Access S3

## 🎯 Objective
Create an **IAM Role** that grants **EC2 instances** permission to access **Amazon S3** — a common real-world scenario where an application running on EC2 needs to read/write data from an S3 bucket.

---

## 🪜 Step-by-Step Implementation

### **Step 1: Open IAM Dashboard**
1. Sign in to **AWS Management Console**.
2. Go to **IAM** service.
3. From the left panel, click on **Roles**.
4. Click on **“Create role”** button.

<img width="1881" height="776" alt="image" src="https://github.com/user-attachments/assets/3873ed90-8dc6-4a09-81cf-ad07f66e48ac" />

---

### **Step 2: Select Trusted Entity Type**
1. Under **Trusted entity type**, choose **AWS service**.
2. In the **Use case** section, select **EC2**.
3. Click **Next**.
<img width="1903" height="860" alt="image" src="https://github.com/user-attachments/assets/4c017c85-944c-4cd6-88d3-84c860efd85f" />
---

### **Step 3: Attach Permissions Policies**
1. Search for the policy named `AmazonS3FullAccess` or `AmazonS3ReadOnlyAccess`.  
   - For production-like environments, prefer **ReadOnly** for security.
2. Select the checkbox next to the desired policy.
3. Click **Next**.
<img width="1676" height="379" alt="image" src="https://github.com/user-attachments/assets/f26f308d-ebf1-4981-be9c-958e360549d8" />


---

### **Step 4: Add Tags (Optional)**
1. (Optional) Add tags like:
   - `Key: Project`, `Value: DevOps-Lab`
   - `Key: Environment`, `Value: Demo`
2. Click **Next**.

---

### **Step 5: Name and Create the Role**
1. Enter **Role name** → `EC2-S3-Access-Role`.
2. (Optional) Add a short description:  
   > “Allows EC2 instances to access S3 buckets.”
3. Review the permissions and click **Create role**.
<img width="1408" height="368" alt="image" src="https://github.com/user-attachments/assets/3680785a-fd1a-46a3-8443-4ad3b980a7ec" />
---

### **Step 6: Attach Role to an EC2 Instance**
1. Go to **EC2 → Instances**.
2. Select an existing instance (or launch a new one).
3. Click **Actions → Security → Modify IAM role**.
4. Choose the newly created role `EC2-S3-Access-Role`.
5. Click **Update IAM role**.
<img width="1402" height="311" alt="image" src="https://github.com/user-attachments/assets/16661b8b-6313-486b-9159-4a1fd2113f96" />

---

### **Step 7: Test Access from EC2**
1. Connect to your EC2 instance via **SSH**.
2. Run the following commands to test S3 access:
   ```bash
   aws s3 ls
   aws s3 ls s3://<your-bucket-name>
   ```
