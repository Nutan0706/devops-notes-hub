## 🎯 Practical Task: **Install & Configure Terraform**

## 🪜 Step-by-Step Implementation

### **Step 1 — Install Terraform CLI**

#### 🧩 For Windows:
1. Go to the official Terraform download page:  
   👉 [https://developer.hashicorp.com/terraform/downloads](https://developer.hashicorp.com/terraform/downloads)
2. Download the appropriate ZIP file for Windows.
3. Extract the ZIP file to a directory (e.g., `C:\terraform`).
4. Add Terraform to the system PATH:
   - Open **System Properties → Advanced → Environment Variables**.
   - Under “System variables,” find `Path`, and click **Edit**.
   - Add the Terraform directory path (`C:\terraform`).
5. Open a new terminal and verify:
   ```bash
   terraform -version
   ```
   <img width="453" height="60" alt="image" src="https://github.com/user-attachments/assets/ad7cd0cd-a92c-4f04-9e31-53ecf4f1f6ea" />

#### 🧩 For macOS:

```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
terraform -version
```

#### 🧩 For Linux (Ubuntu/Debian):

```bash
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install terraform
terraform -version
```

---

### **Step 2 — Verify Installation**

Run:

```bash
terraform -help
```

✅ If you see a list of commands like `init`, `plan`, `apply`, etc., Terraform is successfully installed.

---

### **Step 3 — Configure AWS CLI (as Provider Example)**

Terraform needs provider credentials to interact with cloud services.

1. Install AWS CLI:

   ```bash
   sudo apt install awscli -y
   ```
   <img width="679" height="359" alt="image" src="https://github.com/user-attachments/assets/e8d63e68-2278-4b80-86fe-e6370bfa8724" />

2. Configure it:

   ```bash
   aws configure
   ```

   Provide:

   * AWS Access Key ID
   * AWS Secret Access Key
   * Default region name (e.g., `us-east-1`)
   * Output format (e.g., `json`)

---

### **Step 4 — Create Terraform Working Directory**

```bash
mkdir terraform-demo
cd terraform-demo
```

Create a new file named **`main.tf`** and add:

```hcl
provider "aws" {
  region = "us-east-1"
}
```

---

### **Step 5 — Initialize Terraform**

Run initialization to download provider plugins:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```
<img width="612" height="219" alt="image" src="https://github.com/user-attachments/assets/69f59beb-4d4d-41c1-b737-e1e5d3d95d4b" />

---

### **Step 6 — Validate Configuration**

Check syntax correctness:

```bash
terraform validate
```

✅ Expected Output:

```
Success! The configuration is valid.
```
<img width="378" height="51" alt="image" src="https://github.com/user-attachments/assets/856edd60-1cd1-4b14-952f-d48fada906e8" />

---

### **Step 7 — Verify Provider Installation**

List installed providers:

```bash
terraform providers
```

Expected Output:

```
Providers required by configuration:
.
└── provider[registry.terraform.io/hashicorp/aws]
```
<img width="497" height="104" alt="image" src="https://github.com/user-attachments/assets/f38d3bda-124f-49f7-ace6-91db7f41bb22" />

---

### **Step 8 — Cleanup (Optional)**

If you want to remove all local files and plugins:

```bash
rm -rf .terraform .terraform.lock.hcl
```

---

## 🧾 Summary

| Step | Task                   | Command               |
| ---- | ---------------------- | --------------------- |
| 1    | Install Terraform      | `terraform -version`  |
| 2    | Configure AWS Provider | `aws configure`       |
| 3    | Initialize Terraform   | `terraform init`      |
| 4    | Validate Configuration | `terraform validate`  |
| 5    | List Providers         | `terraform providers` |

---

📸 **Add Snapshot Placeholders**

<!-- Add snapshot: Terraform version check -->

<!-- Add snapshot: terraform init output -->

<!-- Add snapshot: terraform validate success -->

---

✅ **Practical Completed Successfully!**
You’ve now installed, configured, and verified Terraform setup for AWS provider integration.




