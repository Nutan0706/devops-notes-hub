## 🎯 Practical Task: **Resource Tagging**

**Key Focus / Concept:**  
Add and manage **tags** in Terraform resources for environment identification, cost tracking, and better resource organization in AWS.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have valid AWS credentials
- Basic knowledge of AWS resources (EC2, S3, etc.)

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-tagging-demo
cd terraform-tagging-demo
```

---

### **Step 3 — Create `main.tf` File**

We’ll create an **EC2 instance** and an **S3 bucket**, both with multiple tags like **Environment**, **Owner**, and **CostCenter**.

```hcl
provider "aws" {
  region = "us-east-1"
}

# Create S3 Bucket with tags
resource "aws_s3_bucket" "tagged_bucket" {
  bucket = "terraform-tagging-demo-bucket-12345"
  acl    = "private"

  tags = {
    Name         = "Terraform-Tagged-Bucket"
    Environment  = var.environment
    Owner        = var.owner
    CostCenter   = var.cost_center
    ManagedBy    = "Terraform"
  }
}

# Create EC2 instance with tags
resource "aws_instance" "tagged_ec2" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2
  instance_type = "t2.micro"
  key_name      = var.key_name

  tags = {
    Name         = "Terraform-Tagged-EC2"
    Environment  = var.environment
    Owner        = var.owner
    CostCenter   = var.cost_center
    ManagedBy    = "Terraform"
  }
}
```

---

### **Step 4 — Create `variables.tf` File**

Define variables for reusable tagging information:

```hcl
variable "key_name" {
  description = "Existing AWS key pair name"
  type        = string
  default     = "terraform-key"
}

variable "environment" {
  description = "Environment type (dev, test, prod)"
  type        = string
  default     = "dev"
}

variable "owner" {
  description = "Owner of the resource"
  type        = string
  default     = "DevOpsTeam"
}

variable "cost_center" {
  description = "Department or cost center for tracking"
  type        = string
  default     = "IT-1001"
}
```

---

### **Step 5 — Initialize Terraform**

Initialize your working directory:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```

---

### **Step 6 — Validate Configuration**

```bash
terraform validate
```

✅ Output:

```
Success! The configuration is valid.
```

---

### **Step 7 — Review the Execution Plan**

Preview what resources Terraform will create:

```bash
terraform plan
```

✅ Example Output:

```
Plan: 2 to add, 0 to change, 0 to destroy.
```

---

### **Step 8 — Apply Configuration**

Apply the configuration to create resources with tags:

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

---

### **Step 9 — Verify Tags in AWS Console**

Go to:

* **EC2 → Instances → Tags tab**
* **S3 → Your bucket → Properties → Tags**

You should see tags like:

| Key         | Value                |
| ----------- | -------------------- |
| Name        | Terraform-Tagged-EC2 |
| Environment | dev                  |
| Owner       | DevOpsTeam           |
| CostCenter  | IT-1001              |
| ManagedBy   | Terraform            |

---

### **Step 10 — Modify Tag Values**

You can easily switch environments (e.g., from `dev` to `prod`) using variables.
Update the value in `variables.tf`:

```hcl
default = "prod"
```

Then reapply:

```bash
terraform apply -auto-approve
```

✅ Output:

```
Apply complete! Resources: 0 added, 2 changed, 0 destroyed.
```

---

### **Step 11 — Output Resource Tags (Optional)**

You can display tag information using Terraform outputs.

Create an **`outputs.tf`** file:

```hcl
output "ec2_tags" {
  description = "All tags applied to EC2 instance"
  value       = aws_instance.tagged_ec2.tags
}

output "s3_tags" {
  description = "All tags applied to S3 bucket"
  value       = aws_s3_bucket.tagged_bucket.tags
}
```

After applying, run:

```bash
terraform output
```

✅ Example Output:

```
ec2_tags = {
  "CostCenter"  = "IT-1001"
  "Environment" = "prod"
  "ManagedBy"   = "Terraform"
  "Name"        = "Terraform-Tagged-EC2"
  "Owner"       = "DevOpsTeam"
}

s3_tags = {
  "CostCenter"  = "IT-1001"
  "Environment" = "prod"
  "ManagedBy"   = "Terraform"
  "Name"        = "Terraform-Tagged-Bucket"
  "Owner"       = "DevOpsTeam"
}
```

---

### **Step 12 — Destroy Resources**

Once verified, clean up:

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 2 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept             | Description                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| **Tags**            | Key-value metadata assigned to AWS resources for organization and tracking. |
| **Environment Tag** | Identifies which environment (dev/test/prod) the resource belongs to.       |
| **Cost Center Tag** | Used for billing and cost tracking within an organization.                  |
| **ManagedBy Tag**   | Indicates automation ownership (e.g., Terraform, Jenkins).                  |
| **Dynamic Tagging** | Use variables for environment-specific tagging flexibility.                 |

---

## 🧾 Summary

| Step | Task                     | Command                           |
| ---- | ------------------------ | --------------------------------- |
| 1    | Initialize Terraform     | `terraform init`                  |
| 2    | Validate Configuration   | `terraform validate`              |
| 3    | Review Plan              | `terraform plan`                  |
| 4    | Apply Configuration      | `terraform apply -auto-approve`   |
| 5    | View Tags in AWS Console | —                                 |
| 6    | Destroy Resources        | `terraform destroy -auto-approve` |

