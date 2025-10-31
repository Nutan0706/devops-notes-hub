## 🎯 Practical Task: **Create S3 Bucket**

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- AWS credentials are valid and working

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-s3-demo
cd terraform-s3-demo
```

---

### **Step 3 — Create `main.tf` File**

Create a file named **`main.tf`** and add the following configuration:

```hcl
provider "aws" {
  region = "us-east-1"
}

# Create S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "terraform-demo-bucket-12345"  # Bucket name must be globally unique
  tags = {
    Name        = "Terraform Demo Bucket"
    Environment = "Dev"
  }
}
```

---

### **Step 4 — Initialize Terraform**

Run initialization to download required provider plugins:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```

---

### **Step 5 — Validate Configuration**

Check syntax correctness:

```bash
terraform validate
```

✅ Output:

```
Success! The configuration is valid.
```

---

### **Step 6 — Review Execution Plan**

View the plan before applying:

```bash
terraform plan
```

✅ Example Output:

```
Plan: 1 to add, 0 to change, 0 to destroy.
```

---

### **Step 7 — Apply Configuration**

Apply the configuration to create your S3 bucket:

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

---

### **Step 8 — Verify the S3 Bucket**

Verify from AWS Console:

1. Go to **AWS Console → S3**
2. Check if the bucket named **terraform-demo-bucket-12345** is created.
<img width="1466" height="280" alt="image" src="https://github.com/user-attachments/assets/6d3bb320-cb4f-49c6-bf15-c8b741d3dbad" />

Or verify using the AWS CLI:

```bash
aws s3 ls | grep terraform-demo-bucket
```

✅ Expected Output:

```
2025-10-31 15:23:45 terraform-demo-bucket-12345
```
<img width="467" height="44" alt="image" src="https://github.com/user-attachments/assets/407cdaa5-88d7-4d87-a3b3-6097500ba5de" />

---

### **Step 9 — Add Variables for Flexibility**

Let’s make it reusable using **variables**.

Create a **`variables.tf`** file:

```hcl
variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
  default     = "terraform-variable-bucket-12345"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "Dev"
}
```

Update **`main.tf`** to use the variables:

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = var.bucket_name
  acl    = "private"

  tags = {
    Name        = var.bucket_name
    Environment = var.environment
  }
}
```

Re-run initialization and apply:

```bash
terraform init
terraform apply -auto-approve
```

✅ Output:

```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

---

### **Step 10 — Define Outputs**

Create **`outputs.tf`** to display bucket details after creation:

```hcl
output "bucket_name" {
  description = "Name of the S3 bucket"
  value       = aws_s3_bucket.demo_bucket.bucket
}

output "bucket_arn" {
  description = "ARN of the S3 bucket"
  value       = aws_s3_bucket.demo_bucket.arn
}
```

After applying, run:

```bash
terraform validate
terraform plan
terraform apply -auto-approve
terraform output
```
<img width="556" height="62" alt="image" src="https://github.com/user-attachments/assets/374da207-05f4-4d8f-b8f4-f0722d52aa1b" />


✅ Expected Output:

```
bucket_name = "terraform-variable-bucket-12345"
bucket_arn  = "arn:aws:s3:::terraform-variable-bucket-12345"
```

---

### **Step 11 — Clean Up Resources**

Destroy all resources created by Terraform:

```bash
terraform destroy -auto-approve
```

✅ Expected Output:

```
Destroy complete! Resources: 1 destroyed.
```

---

## 🧾 Summary

| Step | Task                 | Command                           |
| ---- | -------------------- | --------------------------------- |
| 1    | Initialize Terraform | `terraform init`                  |
| 2    | Validate Config      | `terraform validate`              |
| 3    | Review Plan          | `terraform plan`                  |
| 4    | Apply to Create S3   | `terraform apply -auto-approve`   |
| 5    | View Outputs         | `terraform output`                |
| 6    | Destroy Bucket       | `terraform destroy -auto-approve` |


