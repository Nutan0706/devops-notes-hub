## 🎯 Practical Task: **Use Locals & Conditionals**

**Key Focus / Concept:**  
Simplify complex Terraform configurations by using **local variables (`locals`)** and **conditional expressions (`? :`)** to reduce repetition and make infrastructure code cleaner and more maintainable.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have basic Terraform knowledge (variables, outputs, etc.)

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-locals-conditionals-demo
cd terraform-locals-conditionals-demo
```

---

### **Step 3 — Concept Overview**

#### 🧠 What are Locals?

Locals are used to define **temporary, reusable values** (like computed names or common tags) to simplify code.

#### 🧠 What are Conditionals?

Conditional expressions allow Terraform to make **decisions at runtime** based on variable values — similar to `if-else`.

---

### **Step 4 — Create `main.tf` File**

We’ll create:

* A **local block** for naming conventions and tags
* **Conditional logic** to choose EC2 instance type and environment configuration dynamically

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ Define Input Variables
# --------------------------
variable "environment" {
  description = "Deployment environment (dev/stage/prod)"
  type        = string
  default     = "dev"
}

variable "enable_public_ip" {
  description = "Enable public IP for EC2 instance"
  type        = bool
  default     = true
}

variable "key_name" {
  description = "AWS key pair name"
  type        = string
  default     = "terraform-key"
}

# --------------------------
# 2️⃣ Define Local Variables
# --------------------------
locals {
  # Dynamic naming pattern
  project_name = "LocalsDemo"

  # Environment-specific prefix
  prefix = "${local.project_name}-${var.environment}"

  # Conditional logic for instance size
  instance_type = var.environment == "prod" ? "t3.medium" : "t2.micro"

  # Standardized tags
  common_tags = {
    Project     = local.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

# --------------------------
# 3️⃣ Create Security Group
# --------------------------
resource "aws_security_group" "locals_sg" {
  name        = "${local.prefix}-sg"
  description = "Allow SSH"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(local.common_tags, { Name = "${local.prefix}-SG" })
}

# --------------------------
# 4️⃣ Create EC2 Instance (Conditional Logic)
# --------------------------
resource "aws_instance" "locals_ec2" {
  ami                    = "ami-0c55b159cbfafe1f0"
  instance_type          = local.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.locals_sg.id]
  associate_public_ip_address = var.enable_public_ip

  user_data = <<-EOF
              #!/bin/bash
              yum install -y httpd
              echo "<h1>Environment: ${var.environment}</h1>" > /var/www/html/index.html
              systemctl start httpd
              EOF

  tags = merge(local.common_tags, {
    Name = "${local.prefix}-EC2"
  })
}

# --------------------------
# 5️⃣ Data Source for Default VPC
# --------------------------
data "aws_vpc" "default" {
  default = true
}

# --------------------------
# 6️⃣ Outputs
# --------------------------
output "instance_type" {
  description = "Selected EC2 instance type based on environment"
  value       = local.instance_type
}

output "ec2_name" {
  description = "EC2 instance name"
  value       = aws_instance.locals_ec2.tags["Name"]
}

output "ec2_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.locals_ec2.public_ip
}
```

---

### **Step 5 — Initialize Terraform**

```bash
terraform init
```

✅ Example Output:

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

### **Step 7 — Review Execution Plan**

```bash
terraform plan
```

✅ Example Output:

```
Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + instance_type = "t2.micro"
  + ec2_name      = "LocalsDemo-dev-EC2"
```

---

### **Step 8 — Apply Configuration**

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:
instance_type = "t2.micro"
ec2_name      = "LocalsDemo-dev-EC2"
ec2_public_ip = "3.92.150.89"
```

---

### **Step 9 — Verify in AWS Console**

1. Go to **EC2 → Instances**

   * Confirm instance name: `LocalsDemo-dev-EC2`
   * Verify tags: `Project`, `Environment`, `ManagedBy`
2. Go to **Security Groups**

   * Check `LocalsDemo-dev-sg` is created

---

### **Step 10 — Test Conditional Logic**

Now change the environment in your variables:

```hcl
variable "environment" {
  default = "prod"
}
```

Run:

```bash
terraform apply -auto-approve
```

✅ Output:

```
instance_type = "t3.medium"
ec2_name      = "LocalsDemo-prod-EC2"
```

Terraform automatically switches to **t3.medium** instance type in production — no need to manually edit multiple files.

---

### **Step 11 — Clean Up Resources**

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 2 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                  | Description                                                          |
| ------------------------ | -------------------------------------------------------------------- |
| **locals**               | Defines computed values that can be reused across the configuration. |
| **Conditionals (`? :`)** | Used for logical decisions in Terraform (if-else equivalent).        |
| **merge()**              | Combines multiple maps (useful for dynamic tags).                    |
| **Computed Naming**      | Use locals to generate consistent resource names dynamically.        |
| **Environment Logic**    | Simplify environment-based configurations using locals.              |

---

## 🧾 Summary

| Step | Task                             | Command                           |
| ---- | -------------------------------- | --------------------------------- |
| 1    | Initialize Terraform             | `terraform init`                  |
| 2    | Validate Configuration           | `terraform validate`              |
| 3    | Review Plan                      | `terraform plan`                  |
| 4    | Apply Configuration              | `terraform apply -auto-approve`   |
| 5    | Test with Different Environments | Change `environment` variable     |
| 6    | Destroy Resources                | `terraform destroy -auto-approve` |
