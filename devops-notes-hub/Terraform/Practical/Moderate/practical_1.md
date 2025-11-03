## 🎯 Practical Task: **Build a Custom VPC with Subnets**

**Key Focus / Concept:**  
Create a **custom VPC** in AWS with **public and private subnets**, **route tables**, an **Internet Gateway (IGW)**, and **NAT Gateway** for secure network segregation and internet access.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have a valid AWS account
- Understanding of basic VPC networking concepts (CIDR, subnets, routing)

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-vpc-demo
cd terraform-vpc-demo
```

---

### **Step 3 — Create `main.tf` File**

This configuration defines:

* VPC
* Public and Private Subnets
* Internet Gateway
* Route Tables and Associations
* NAT Gateway for Private Subnet Internet Access

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ Create Custom VPC
# --------------------------
resource "aws_vpc" "custom_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "Terraform-Custom-VPC"
    Environment = var.environment
  }
}

# --------------------------
# 2️⃣ Create Public Subnet
# --------------------------
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.custom_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"

  tags = {
    Name = "Public-Subnet"
    Tier = "Public"
  }
}

# --------------------------
# 3️⃣ Create Private Subnet
# --------------------------
resource "aws_subnet" "private_subnet" {
  vpc_id            = aws_vpc.custom_vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "Private-Subnet"
    Tier = "Private"
  }
}

# --------------------------
# 4️⃣ Create Internet Gateway
# --------------------------
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.custom_vpc.id

  tags = {
    Name = "Terraform-IGW"
  }
}

# --------------------------
# 5️⃣ Create Elastic IP for NAT Gateway
# --------------------------
resource "aws_eip" "nat_eip" {
  domain = "vpc"
}

# --------------------------
# 6️⃣ Create NAT Gateway for Private Subnet Internet Access
# --------------------------
resource "aws_nat_gateway" "nat_gw" {
  allocation_id = aws_eip.nat_eip.id
  subnet_id     = aws_subnet.public_subnet.id

  tags = {
    Name = "Terraform-NAT-Gateway"
  }

  depends_on = [aws_internet_gateway.igw]
}

# --------------------------
# 7️⃣ Create Public Route Table
# --------------------------
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.custom_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "Public-Route-Table"
  }
}

# Associate Public Subnet with Public Route Table
resource "aws_route_table_association" "public_assoc" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}

# --------------------------
# 8️⃣ Create Private Route Table
# --------------------------
resource "aws_route_table" "private_rt" {
  vpc_id = aws_vpc.custom_vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gw.id
  }

  tags = {
    Name = "Private-Route-Table"
  }
}

# Associate Private Subnet with Private Route Table
resource "aws_route_table_association" "private_assoc" {
  subnet_id      = aws_subnet.private_subnet.id
  route_table_id = aws_route_table.private_rt.id
}
```

---

### **Step 4 — Create `variables.tf` File**

Define variables for flexibility.

```hcl
variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}
```

---

### **Step 5 — Initialize Terraform**

Initialize your working directory and download AWS provider plugins.

```bash
terraform init
```

✅ Output:

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

Preview the resources Terraform will create.

```bash
terraform plan
```

✅ Example Output:

```
Plan: 9 to add, 0 to change, 0 to destroy.
```

---

### **Step 8 — Apply Configuration**

Apply the configuration to create the VPC, subnets, and networking components.

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 9 added, 0 changed, 0 destroyed.
```

---

### **Step 9 — Verify in AWS Console**

Go to:

* **VPC → Your VPCs** → Confirm `Terraform-Custom-VPC`
* **Subnets →** Check `Public-Subnet` and `Private-Subnet`
* **Route Tables →** Verify routes to IGW and NAT Gateway
* **Internet Gateways →** Confirm attached to your VPC

Or verify using AWS CLI:

```bash
aws ec2 describe-vpcs --query "Vpcs[*].VpcId"
```

✅ Example Output:

```
[
  "vpc-0a1b2c3d4e5f67890"
]
```

---

### **Step 10 — Destroy All Resources**

When testing is complete, safely destroy everything:

```bash
terraform destroy -auto-approve
```

✅ Example Output:

```
Destroy complete! Resources: 9 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                         | Description                                                   |
| ------------------------------- | ------------------------------------------------------------- |
| **VPC (Virtual Private Cloud)** | Isolated network environment in AWS.                          |
| **Public Subnet**               | Allows internet access via IGW.                               |
| **Private Subnet**              | Accesses internet via NAT Gateway.                            |
| **Route Tables**                | Define traffic direction for each subnet.                     |
| **Internet Gateway (IGW)**      | Provides internet access for public subnet.                   |
| **NAT Gateway**                 | Allows outbound internet access for private subnets securely. |

---

## 🧾 Summary

| Step | Task                   | Command                           |
| ---- | ---------------------- | --------------------------------- |
| 1    | Initialize Terraform   | `terraform init`                  |
| 2    | Validate Configuration | `terraform validate`              |
| 3    | Preview Plan           | `terraform plan`                  |
| 4    | Apply to Build VPC     | `terraform apply -auto-approve`   |
| 5    | Verify in AWS Console  | —                                 |
| 6    | Destroy Resources      | `terraform destroy -auto-approve` |
