## 🎯 Practical Task: **Use tfvars File for Different Environments**

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have valid AWS credentials
- Basic understanding of variables in Terraform

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-tfvars-demo
cd terraform-tfvars-demo
```

---

### **Step 3 — Create `main.tf` File**

We’ll create an S3 bucket where configuration (like bucket name, environment, and tags) changes based on the `.tfvars` file used.

```hcl
provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "env_bucket" {
  bucket = var.bucket_name
  acl    = var.bucket_acl

  tags = {
    Environment = var.environment
    Owner       = var.owner
  }
}

output "bucket_name" {
  value = aws_s3_bucket.env_bucket.bucket
}

output "environment" {
  value = var.environment
}
```

---

### **Step 4 — Create `variables.tf` File**

Define all variables that can differ per environment:

```hcl
variable "aws_region" {
  description = "AWS region to create resources"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}

variable "bucket_acl" {
  description = "Access level for the bucket"
  type        = string
  default     = "private"
}

variable "environment" {
  description = "Environment name (e.g., dev, prod)"
  type        = string
}

variable "owner" {
  description = "Owner tag for the resource"
  type        = string
  default     = "TerraformUser"
}
```

---

### **Step 5 — Create Environment-Specific tfvars Files**

Create two files — one for **development** and one for **production**.

#### 🧩 `dev.tfvars`

```hcl
bucket_name = "terraform-dev-bucket-12345"
bucket_acl  = "private"
environment = "dev"
owner       = "DevOpsTeam"
```

#### 🧩 `prod.tfvars`

```hcl
bucket_name = "terraform-prod-bucket-12345"
bucket_acl  = "private"
environment = "prod"
owner       = "ProductionTeam"
```

---

### **Step 6 — Initialize Terraform**

Run initialization to set up the workspace:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```

---

### **Step 7 — Apply for Development Environment**

Apply configuration using the `dev.tfvars` file:

```bash
terraform apply -var-file="dev.tfvars" -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:
bucket_name = "terraform-dev-bucket-12345"
environment = "dev"
```

<img width="511" height="121" alt="image" src="https://github.com/user-attachments/assets/03318c8f-3ed6-4678-9374-5bea2a169cb2" />


---

### **Step 8 — Apply for Production Environment**

Now, deploy using the `prod.tfvars` file:

```bash
terraform apply -var-file="prod.tfvars" -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:
bucket_name = "terraform-prod-bucket-12345"
environment = "prod"
```
<img width="483" height="137" alt="image" src="https://github.com/user-attachments/assets/b035ddc5-0efc-4acc-a3d0-04653152b526" />

---

### **Step 9 — Verify the Buckets**

Go to **AWS Console → S3** and confirm:

* A bucket named `terraform-dev-bucket-12345` for **dev**
* A bucket named `terraform-prod-bucket-12345` for **prod**

Or verify via AWS CLI:

```bash
aws s3 ls | grep terraform
```
<img width="435" height="63" alt="image" src="https://github.com/user-attachments/assets/4a974924-da3e-404e-b512-4a6619d65934" />


✅ Example Output:

```
2025-10-31 12:22:45 terraform-dev-bucket-12345
2025-10-31 12:25:17 terraform-prod-bucket-12345
```

---

### **Step 10 — Destroy Resources (Environment-Specific)**

You can destroy the infrastructure for a specific environment using the same `-var-file` flag.

For **development**:

```bash
terraform destroy -var-file="dev.tfvars" -auto-approve
```

For **production**:

```bash
terraform destroy -var-file="prod.tfvars" -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 1 destroyed.
```

---

## 🧠 Key Takeaways

| Concept               | Description                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------- |
| `terraform.tfvars`    | Default variable values file automatically loaded by Terraform.                              |
| `-var-file`           | Lets you specify custom `.tfvars` for environment-specific configurations.                   |
| Separate Environments | Enables distinct resource naming, tagging, and parameters per environment (e.g., dev, prod). |
| Output Values         | Help verify which environment is currently applied.                                          |

---

## 🧾 Summary

| Step | Task                     | Command                                                  |
| ---- | ------------------------ | -------------------------------------------------------- |
| 1    | Initialize Terraform     | `terraform init`                                         |
| 2    | Apply Dev Configuration  | `terraform apply -var-file="dev.tfvars" -auto-approve`   |
| 3    | Apply Prod Configuration | `terraform apply -var-file="prod.tfvars" -auto-approve`  |
| 4    | Verify Buckets           | `aws s3 ls`                                              |
| 5    | Destroy Environment      | `terraform destroy -var-file="dev.tfvars" -auto-approve` |



