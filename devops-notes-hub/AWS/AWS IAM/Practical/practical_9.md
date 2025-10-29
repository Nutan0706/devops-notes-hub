## 🧠 **Practical 9 — Integrate IAM with AWS CLI**

**🎯 Goal:** Configure multiple AWS CLI profiles, assume IAM roles, and test API access directly from the terminal.

### 🔹 **Step-by-Step Guide**

### **Step 1: Install and Configure AWS CLI**

1. **Verify installation:**
   ```bash
   aws --version
   ```
2. If not installed, download it from the AWS CLI Installation Guide
3. Configure your first profile:
   ```bash
      aws configure --profile dev-profile
   ```
4. Enter the following details when prompted:
   ```pgsql
   AWS Access Key ID: <user_access_key>
   AWS Secret Access Key: <user_secret_key>
   Default region name: ap-south-1
   Default output format: json
   ```
 📁 This command creates configuration files at:
  ~/.aws/credentials and ~/.aws/config

  <img width="742" height="198" alt="image" src="https://github.com/user-attachments/assets/10267b34-4673-4c1b-8c42-a64b3bf279d6" />

 ---

 ### **Step 2: Verify Configuration**

1. Run the following command:
   ```bash
   aws sts get-caller-identity --profile dev-profile
   ```
2. ✅ The output should display the User ARN, Account ID, and User ID, confirming a valid configuration.
   <img width="789" height="166" alt="image" src="https://github.com/user-attachments/assets/97880267-76c4-4d8e-89f7-29542d1e8390" />

   
---

### **Step 3: Create IAM Role for Cross-Account or Role Assumption**
1. Go to **AWS Console → IAM → Roles → Create Role**.  
2. Select **Another AWS Account** or **Service (e.g., EC2)** depending on your use case.  
3. Attach a simple policy, e.g., **AmazonS3ReadOnlyAccess**.  
4. Note down the **Role ARN**, for example: arn:aws:iam::123456789012:role/S3ReadRole
<img width="1608" height="601" alt="image" src="https://github.com/user-attachments/assets/65258597-9eb4-4875-b470-ec9a0aaf2a52" />

---

### **Step 4: Add Role Assumption Configuration in CLI**
1. Open the configuration file for editing: ~/.aws/config
2. Add the following section:
```ini
[profile assumed-role]
role_arn = arn:aws:iam::123456789012:role/S3ReadRole
source_profile = dev-profile
region = ap-south-1
```
3. This configuration means the assumed-role profile will assume the specified IAM role using credentials from dev-profile.

---

### **Step 5: Test Role Assumption**

1. Run the following command:
   ```bash
   aws sts get-caller-identity --profile assumed-role
   ```
2. ✅ You should now see the Role ARN in the response, confirming that the role assumption worked successfully.

---
### **Step 6: Test API Access**

1. For example, list S3 buckets using the assumed role:
   ```bash
   aws s3 ls --profile assumed-role
   ```
2. If permissions are correct, you’ll see the list of accessible S3 buckets.

---

## ✅ Outcome

You’ve successfully configured **AWS CLI** with multiple profiles, assumed an **IAM Role**, and accessed **AWS services securely** through terminal-based authentication.


   

