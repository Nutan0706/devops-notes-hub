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
