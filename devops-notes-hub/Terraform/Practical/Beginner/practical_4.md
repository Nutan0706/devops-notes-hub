## 🎯 Practical Task: **Define Provider Block**

**Key Focus / Concept:**  
Configure the AWS provider with region and credentials to enable Terraform to interact with AWS services.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have valid AWS credentials (Access Key & Secret Key)

---

### **Step 2 — Create Working Directory**

Create a new folder for this practical:

```bash
mkdir terraform-provider-demo
cd terraform-provider-demo
```

---

### **Step 3 — Create `main.tf` File**

Define the AWS provider configuration block.

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region                  = "us-east-1"
  shared_credentials_file = "~/.aws/credentials"
  profile                 = "default"
}
```

---

### **Step 4 — Verify Your AWS CLI Configuration**

Run this command to check if your AWS CLI credentials are configured properly:

```bash
aws sts get-caller-identity
```

✅ Expected Output:

```
{
    "UserId": "AIDAEXAMPLE123456",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/your-username"
}
```
<img width="519" height="117" alt="image" src="https://github.com/user-attachments/assets/897c466c-c46f-4e0f-8b2b-6fe244752b4f" />

This ensures your credentials file (`~/.aws/credentials`) is set up correctly.

---

### **Step 5 — Initialize Terraform**

Run the following command to initialize Terraform and download the AWS provider plugin:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```

---

### **Step 6 — Validate the Configuration**

Validate your Terraform configuration file for correctness:

```bash
terraform validate
```

✅ Expected Output:

```
Success! The configuration is valid.
```

---

### **Step 7 — List Installed Providers**

Check which provider plugins have been installed:

```bash
terraform providers
```

✅ Example Output:

```
Providers required by configuration:
.
└── provider[registry.terraform.io/hashicorp/aws] ~> 5.0
```
<img width="510" height="118" alt="image" src="https://github.com/user-attachments/assets/ff1f3975-7869-444c-a586-4bd819bd5933" />

---

### **Step 8 — (Optional) Use Variables for Region & Profile**

To make your provider configuration flexible, replace static values with variables.

Update **`main.tf`**:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}
```

Create a **`variables.tf`** file:

```hcl
variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "aws_profile" {
  description = "AWS CLI profile to use"
  type        = string
  default     = "default"
}
```

---

### **Step 9 — Initialize Again (for Variables)**

Re-run initialization to ensure Terraform recognizes the variable changes:

```bash
terraform init
```

---

### **Step 10 — Validate Again**

```bash
terraform validate
```

✅ Expected Output:

```
Success! The configuration is valid.
```

---

## 🧾 Summary

| Step | Task                   | Command                       |
| ---- | ---------------------- | ----------------------------- |
| 1    | Define Provider Block  | `provider "aws" { ... }`      |
| 2    | Verify AWS Credentials | `aws sts get-caller-identity` |
| 3    | Initialize Terraform   | `terraform init`              |
| 4    | Validate Configuration | `terraform validate`          |
| 5    | List Providers         | `terraform providers`         |

---


