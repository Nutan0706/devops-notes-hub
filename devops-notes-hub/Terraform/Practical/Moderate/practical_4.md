## 🎯 Practical Task: **Use Terraform Modules**

**Key Focus / Concept:**  
Create **reusable Terraform modules** to manage resources like **VPC**, **EC2**, and **Security Groups** — enabling modular, scalable, and maintainable infrastructure code.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have valid AWS credentials
- You understand basic Terraform resources and variables

---

### **Step 2 — Create Working Directory Structure**

Create a folder structure to organize modules and the main configuration.

```bash
terraform-modules-demo/
├── main.tf
├── variables.tf
├── outputs.tf
└── modules/
    ├── vpc/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    ├── ec2/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    └── security-group/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

---

### **Step 3 — Create `modules/vpc/main.tf`**

This module creates a **custom VPC** and **subnets**.

```hcl
resource "aws_vpc" "custom_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = var.vpc_name
  }
}

resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.custom_vpc.id
  cidr_block              = var.public_subnet_cidr
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"

  tags = {
    Name = "Public-Subnet"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.custom_vpc.id

  tags = {
    Name = "IGW"
  }
}

output "vpc_id" {
  value = aws_vpc.custom_vpc.id
}

output "public_subnet_id" {
  value = aws_subnet.public_subnet.id
}
```

---

### **Step 4 — Create `modules/vpc/variables.tf`**

```hcl
variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC"
}

variable "vpc_name" {
  type        = string
  description = "Name of the VPC"
}

variable "public_subnet_cidr" {
  type        = string
  description = "CIDR for public subnet"
}
```

---

### **Step 5 — Create `modules/security-group/main.tf`**

This module creates a security group allowing SSH and HTTP.

```hcl
resource "aws_security_group" "app_sg" {
  name        = var.sg_name
  description = "Allow SSH and HTTP"
  vpc_id      = var.vpc_id

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
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

output "sg_id" {
  value = aws_security_group.app_sg.id
}
```

---

### **Step 6 — Create `modules/security-group/variables.tf`**

```hcl
variable "vpc_id" {
  type        = string
  description = "VPC ID where SG will be created"
}

variable "sg_name" {
  type        = string
  description = "Name of the Security Group"
}
```

---

### **Step 7 — Create `modules/ec2/main.tf`**

This module creates an EC2 instance.

```hcl
resource "aws_instance" "web_instance" {
  ami                    = "ami-0c55b159cbfafe1f0"
  instance_type          = var.instance_type
  subnet_id              = var.subnet_id
  vpc_security_group_ids = [var.sg_id]
  key_name               = var.key_name
  associate_public_ip_address = true

  tags = {
    Name = var.instance_name
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo yum install -y httpd
              systemctl start httpd
              echo "<h1>Deployed via Terraform Module</h1>" > /var/www/html/index.html
              EOF
}

output "instance_public_ip" {
  value = aws_instance.web_instance.public_ip
}
```

---

### **Step 8 — Create `modules/ec2/variables.tf`**

```hcl
variable "instance_type" {
  type        = string
  description = "EC2 instance type"
}

variable "subnet_id" {
  type        = string
  description = "Subnet where instance is launched"
}

variable "sg_id" {
  type        = string
  description = "Security Group ID"
}

variable "key_name" {
  type        = string
  description = "Key pair name"
}

variable "instance_name" {
  type        = string
  description = "EC2 instance name"
}
```

---

### **Step 9 — Create `main.tf` (Root Module)**

Now we use our custom modules to deploy the VPC, Security Group, and EC2 together.

```hcl
provider "aws" {
  region = "us-east-1"
}

# VPC Module
module "vpc" {
  source             = "./modules/vpc"
  vpc_cidr           = "10.10.0.0/16"
  vpc_name           = "Modular-VPC"
  public_subnet_cidr = "10.10.1.0/24"
}

# Security Group Module
module "security_group" {
  source  = "./modules/security-group"
  vpc_id  = module.vpc.vpc_id
  sg_name = "Modular-SG"
}

# EC2 Module
module "ec2" {
  source        = "./modules/ec2"
  instance_type = "t2.micro"
  subnet_id     = module.vpc.public_subnet_id
  sg_id         = module.security_group.sg_id
  key_name      = var.key_name
  instance_name = "Modular-EC2"
}
```

---

### **Step 10 — Create `variables.tf` (Root)**

```hcl
variable "key_name" {
  description = "Existing AWS Key Pair name"
  type        = string
  default     = "terraform-key"
}
```

---

### **Step 11 — Initialize Terraform**

Initialize Terraform and modules.

```bash
terraform init
```

✅ Output:

```
Terraform has been successfully initialized!
- Module "vpc" downloaded from ./modules/vpc
- Module "security_group" downloaded from ./modules/security-group
- Module "ec2" downloaded from ./modules/ec2
```

---

### **Step 12 — Validate and Apply**

```bash
terraform validate
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 5 added, 0 changed, 0 destroyed.

Outputs:
instance_public_ip = "54.175.12.87"
```

---

### **Step 13 — Verify in AWS Console**

Go to:

* **VPC Dashboard** → Check “Modular-VPC”
* **EC2 → Instances** → View instance “Modular-EC2”
* **Security Groups** → Confirm “Modular-SG”

Or verify via CLI:

```bash
aws ec2 describe-instances --query "Reservations[*].Instances[*].{ID:InstanceId,State:State.Name}" --output table
```

---

### **Step 14 — Clean Up**

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 5 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept             | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| **Module**          | A reusable container for Terraform configurations (like a function).  |
| **Root Module**     | The main configuration that calls submodules.                         |
| **Source Argument** | Specifies where the module is located (local path, registry, or Git). |
| **Output Sharing**  | Modules expose resource outputs for use in parent modules.            |
| **Encapsulation**   | Keeps infrastructure organized and reusable.                          |

---

## 🧾 Summary

| Step | Task                         | Command                                  |
| ---- | ---------------------------- | ---------------------------------------- |
| 1    | Create Folder Structure      | `mkdir modules/{vpc,ec2,security-group}` |
| 2    | Define VPC Module            | `modules/vpc/main.tf`                    |
| 3    | Define Security Group Module | `modules/security-group/main.tf`         |
| 4    | Define EC2 Module            | `modules/ec2/main.tf`                    |
| 5    | Initialize Terraform         | `terraform init`                         |
| 6    | Validate and Apply           | `terraform apply -auto-approve`          |
| 7    | Destroy Infrastructure       | `terraform destroy -auto-approve`        |


