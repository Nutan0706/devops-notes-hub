## 🎯 Practical Task: **Deploy Multi-Tier Architecture**

**Key Focus / Concept:**  
Automate deployment of a **3-tier application architecture** (VPC + EC2 + RDS) using Terraform — creating a scalable, isolated, and production-ready environment.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have valid AWS credentials
- You understand basic networking, EC2, and RDS concepts

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-multitier-demo
cd terraform-multitier-demo
```

---

### **Step 3 — Architecture Overview**

**Layers in the 3-Tier Setup:**

1. **VPC & Networking Layer** → Creates custom VPC, public/private subnets, route tables, and NAT gateway
2. **Compute Layer (Web Tier)** → Launches EC2 instances in the public subnet
3. **Database Layer (Data Tier)** → Deploys RDS MySQL in the private subnet

---

### **Step 4 — Create `main.tf` File**

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ VPC & Subnets
# --------------------------
resource "aws_vpc" "multi_vpc" {
  cidr_block           = "10.1.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "MultiTier-VPC"
    Environment = var.environment
  }
}

# Public Subnet
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.multi_vpc.id
  cidr_block              = "10.1.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"

  tags = {
    Name = "Public-Subnet"
    Tier = "Web"
  }
}

# Private Subnet
resource "aws_subnet" "private_subnet" {
  vpc_id            = aws_vpc.multi_vpc.id
  cidr_block        = "10.1.2.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "Private-Subnet"
    Tier = "Database"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.multi_vpc.id

  tags = {
    Name = "MultiTier-IGW"
  }
}

# Elastic IP for NAT Gateway
resource "aws_eip" "nat_eip" {
  domain = "vpc"
}

# NAT Gateway
resource "aws_nat_gateway" "nat_gw" {
  allocation_id = aws_eip.nat_eip.id
  subnet_id     = aws_subnet.public_subnet.id

  tags = {
    Name = "MultiTier-NAT-GW"
  }

  depends_on = [aws_internet_gateway.igw]
}

# Public Route Table
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.multi_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "Public-RT"
  }
}

resource "aws_route_table_association" "public_assoc" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}

# Private Route Table
resource "aws_route_table" "private_rt" {
  vpc_id = aws_vpc.multi_vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gw.id
  }

  tags = {
    Name = "Private-RT"
  }
}

resource "aws_route_table_association" "private_assoc" {
  subnet_id      = aws_subnet.private_subnet.id
  route_table_id = aws_route_table.private_rt.id
}

# --------------------------
# 2️⃣ Security Groups
# --------------------------
# Web Tier Security Group
resource "aws_security_group" "web_sg" {
  name        = "WebSG"
  description = "Allow HTTP and SSH"
  vpc_id      = aws_vpc.multi_vpc.id

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow SSH"
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
    Name = "Web-SG"
  }
}

# Database Security Group
resource "aws_security_group" "db_sg" {
  name        = "DatabaseSG"
  description = "Allow MySQL access from WebSG"
  vpc_id      = aws_vpc.multi_vpc.id

  ingress {
    description      = "Allow MySQL from WebSG"
    from_port        = 3306
    to_port          = 3306
    protocol         = "tcp"
    security_groups  = [aws_security_group.web_sg.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "DB-SG"
  }
}

# --------------------------
# 3️⃣ EC2 (Web Tier)
# --------------------------
resource "aws_instance" "web_server" {
  ami                    = "ami-0c55b159cbfafe1f0" # Amazon Linux 2
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.public_subnet.id
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  associate_public_ip_address = true

  tags = {
    Name = "Web-Tier-EC2"
    Tier = "Web"
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo yum install -y httpd
              sudo systemctl start httpd
              sudo systemctl enable httpd
              echo "<h1>Welcome to Multi-Tier Terraform Demo</h1>" > /var/www/html/index.html
              EOF
}

# --------------------------
# 4️⃣ RDS (Database Tier)
# --------------------------
resource "aws_db_subnet_group" "rds_subnet_group" {
  name       = "rds-subnet-group"
  subnet_ids = [aws_subnet.private_subnet.id]

  tags = {
    Name = "RDS-Subnet-Group"
  }
}

resource "aws_db_instance" "rds_instance" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  db_name              = "appdb"
  username             = "admin"
  password             = "Terraform123!"
  parameter_group_name = "default.mysql8.0"
  db_subnet_group_name = aws_db_subnet_group.rds_subnet_group.name
  vpc_security_group_ids = [aws_security_group.db_sg.id]
  skip_final_snapshot   = true

  tags = {
    Name = "RDS-MySQL"
    Tier = "Database"
  }
}
```

---

### **Step 5 — Create `variables.tf` File**

```hcl
variable "key_name" {
  description = "Existing AWS key pair name"
  type        = string
  default     = "terraform-key"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}
```

---

### **Step 6 — Initialize Terraform**

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

### **Step 8 — Review Execution Plan**

```bash
terraform plan
```

✅ Example Output:

```
Plan: 14 to add, 0 to change, 0 to destroy.
```

---

### **Step 9 — Apply Configuration**

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 14 added, 0 changed, 0 destroyed.
```

---

### **Step 10 — Verify Resources in AWS Console**

Go to:

* **VPC Dashboard** → Verify custom VPC, subnets, IGW, and NAT
* **EC2 → Instances** → Confirm web server running in the public subnet
* **RDS → Databases** → Check for `RDS-MySQL` instance in private subnet

Or check via CLI:

```bash
aws ec2 describe-instances --query "Reservations[*].Instances[*].{ID:InstanceId,State:State.Name,Subnet:SubnetId}" --output table
```

---

### **Step 11 — Clean Up Resources**

When testing is complete:

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 14 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                 | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| **3-Tier Architecture** | Separates web, app, and database layers for security and scalability. |
| **Public Subnet**       | Hosts EC2 instances with internet access via IGW.                     |
| **Private Subnet**      | Hosts RDS instances, accessible only from web tier via NAT.           |
| **Security Groups**     | Control inbound/outbound traffic between tiers.                       |
| **User Data**           | Automates web server setup (Apache installation).                     |

---

## 🧾 Summary

| Step | Task                   | Command                           |
| ---- | ---------------------- | --------------------------------- |
| 1    | Initialize Terraform   | `terraform init`                  |
| 2    | Validate Configuration | `terraform validate`              |
| 3    | Review Plan            | `terraform plan`                  |
| 4    | Apply Configuration    | `terraform apply -auto-approve`   |
| 5    | Verify Resources       | `aws ec2 describe-instances`      |
| 6    | Destroy Infrastructure | `terraform destroy -auto-approve` |
