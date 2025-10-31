## 🎯 Practical Task: **Use Variables & Outputs**
---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have completed the EC2 creation practical (or similar setup)

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-variables-demo
cd terraform-variables-demo
```

---

### **Step 3 — Create `main.tf` File**

This file defines the actual resources that will use variables.

```hcl
provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "ec2_sg" {
  name        = "terraform-sg"
  description = "Allow SSH access"

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

  tags = {
    Name = var.sg_name
  }
}

resource "aws_instance" "ec2_instance" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name
  security_groups = [aws_security_group.ec2_sg.name]

  tags = {
    Name = var.instance_name
  }
}

# Output values
output "instance_id" {
  description = "EC2 Instance ID"
  value       = aws_instance.ec2_instance.id
}

output "instance_public_ip" {
  description = "EC2 Public IP Address"
  value       = aws_instance.ec2_instance.public_ip
}
```

---

### **Step 4 — Create `variables.tf` File**

Define all input variables here for flexibility and better manageability.

```hcl
variable "aws_region" {
  description = "AWS region where resources will be created"
  type        = string
  default     = "us-east-1"
}

variable "ami_id" {
  description = "Amazon Machine Image ID for EC2"
  type        = string
  default     = "ami-0c55b159cbfafe1f0"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "Name of existing AWS key pair"
  type        = string
  default     = "terraform-key"
}

variable "sg_name" {
  description = "Security group name"
  type        = string
  default     = "terraform-demo-sg"
}

variable "instance_name" {
  description = "Name tag for EC2 instance"
  type        = string
  default     = "Terraform-Variable-EC2"
}
```

---

### **Step 5 — (Optional) Create `terraform.tfvars` File**

You can override variable values here.
Create a file named **`terraform.tfvars`**:

```hcl
aws_region      = "us-east-1"
ami_id          = "ami-0c55b159cbfafe1f0"
instance_type   = "t2.micro"
key_name        = "terraform-key"
sg_name         = "demo-sg"
instance_name   = "MyEC2-From-Vars"
```

---

### **Step 6 — Initialize Terraform**

Run the initialization command:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```

---

### **Step 7 — Validate Configuration**

```bash
terraform validate
```

✅ Output:

```
Success! The configuration is valid.
```

---

### **Step 8 — Review the Execution Plan**

Preview all resources before creation:

```bash
terraform plan
```

✅ Output Example:

```
Plan: 2 to add, 0 to change, 0 to destroy.
```

---

### **Step 9 — Apply Configuration**

Create the resources:

```bash
terraform apply -auto-approve
```

✅ Output Example:

```
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:
instance_id = "i-0abcd1234ef56789"
instance_public_ip = "54.210.45.123"
```

---

### **Step 10 — Verify Outputs**

Check Terraform output values anytime:

```bash
terraform output
```

✅ Expected Output:

```
instance_id = "i-0abcd1234ef56789"
instance_public_ip = "54.210.45.123"
```

---

### **Step 11 — Clean Up**

Destroy all resources:

```bash
terraform destroy -auto-approve
```

✅ Expected Output:

```
Destroy complete! Resources: 2 destroyed.
```

---

## 🧾 Summary

| Step | Task                   | Command                           |
| ---- | ---------------------- | --------------------------------- |
| 1    | Initialize Terraform   | `terraform init`                  |
| 2    | Validate Configuration | `terraform validate`              |
| 3    | View Plan              | `terraform plan`                  |
| 4    | Apply Configuration    | `terraform apply -auto-approve`   |
| 5    | Show Outputs           | `terraform output`                |
| 6    | Destroy Resources      | `terraform destroy -auto-approve` |

---


