## 🎯 Practical Task: **Deploy RDS Instance Securely**

**Key Focus / Concept:**  
Create a **secure and scalable RDS database setup** in AWS using Terraform — including **DB subnet groups**, **parameter groups**, and **AWS Secrets Manager** for storing credentials safely.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have access to a VPC (or you can create one)
- Basic knowledge of VPC, subnets, and databases

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-rds-secure-demo
cd terraform-rds-secure-demo
```

---

### **Step 3 — Create `main.tf` File**

This configuration will:

* Create a **VPC**, **Subnets**, and **Security Group**
* Create **DB Subnet Group**
* Create **Parameter Group**
* Store credentials in **AWS Secrets Manager**
* Deploy a **MySQL RDS instance** securely in private subnets

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ Create VPC and Subnets
# --------------------------
resource "aws_vpc" "rds_vpc" {
  cidr_block           = "10.20.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "RDS-VPC"
  }
}

resource "aws_subnet" "private_subnet_1" {
  vpc_id                  = aws_vpc.rds_vpc.id
  cidr_block              = "10.20.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = false

  tags = {
    Name = "Private-Subnet-1"
  }
}

resource "aws_subnet" "private_subnet_2" {
  vpc_id                  = aws_vpc.rds_vpc.id
  cidr_block              = "10.20.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = false

  tags = {
    Name = "Private-Subnet-2"
  }
}

# --------------------------
# 2️⃣ Create Security Group
# --------------------------
resource "aws_security_group" "rds_sg" {
  name        = "rds-secure-sg"
  description = "Allow MySQL access from specific sources"
  vpc_id      = aws_vpc.rds_vpc.id

  ingress {
    description = "Allow MySQL from specific IP or app"
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = [var.allowed_ip]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "RDS-SecurityGroup"
  }
}

# --------------------------
# 3️⃣ Create DB Subnet Group
# --------------------------
resource "aws_db_subnet_group" "rds_subnet_group" {
  name       = "rds-private-subnet-group"
  subnet_ids = [aws_subnet.private_subnet_1.id, aws_subnet.private_subnet_2.id]

  tags = {
    Name = "RDS-Subnet-Group"
  }
}

# --------------------------
# 4️⃣ Create DB Parameter Group
# --------------------------
resource "aws_db_parameter_group" "rds_param_group" {
  name        = "custom-mysql-params"
  family      = "mysql8.0"
  description = "Custom MySQL parameter group"

  parameters = [
    {
      name  = "character_set_server"
      value = "utf8mb4"
    },
    {
      name  = "slow_query_log"
      value = "1"
    }
  ]
}

# --------------------------
# 5️⃣ Store Credentials Securely in Secrets Manager
# --------------------------
resource "random_password" "db_password" {
  length  = 16
  special = true
}

resource "aws_secretsmanager_secret" "rds_secret" {
  name = "rds-db-credentials"
}

resource "aws_secretsmanager_secret_version" "rds_secret_version" {
  secret_id     = aws_secretsmanager_secret.rds_secret.id
  secret_string = jsonencode({
    username = var.db_username
    password = random_password.db_password.result
  })
}

# --------------------------
# 6️⃣ Create RDS Instance
# --------------------------
resource "aws_db_instance" "rds_instance" {
  identifier              = "terraform-secure-rds"
  engine                  = "mysql"
  engine_version          = "8.0"
  instance_class          = "db.t3.micro"
  allocated_storage       = 20
  storage_type            = "gp2"
  username                = var.db_username
  password                = random_password.db_password.result
  db_subnet_group_name    = aws_db_subnet_group.rds_subnet_group.name
  vpc_security_group_ids  = [aws_security_group.rds_sg.id]
  parameter_group_name    = aws_db_parameter_group.rds_param_group.name
  publicly_accessible     = false
  skip_final_snapshot     = true
  deletion_protection     = false
  multi_az                = true

  tags = {
    Name = "Secure-RDS-Instance"
    Environment = var.environment
  }
}

# --------------------------
# 7️⃣ Outputs
# --------------------------
output "rds_endpoint" {
  description = "RDS endpoint"
  value       = aws_db_instance.rds_instance.address
}

output "rds_secret_arn" {
  description = "ARN of the Secrets Manager secret"
  value       = aws_secretsmanager_secret.rds_secret.arn
}
```

---

### **Step 4 — Create `variables.tf` File**

```hcl
variable "db_username" {
  description = "Master username for RDS"
  type        = string
  default     = "admin"
}

variable "allowed_ip" {
  description = "IP allowed to access RDS (e.g., app server or VPN IP)"
  type        = string
  default     = "0.0.0.0/0"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
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
Plan: 10 to add, 0 to change, 0 to destroy.
```

---

### **Step 8 — Apply Configuration**

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 10 added, 0 changed, 0 destroyed.

Outputs:
rds_endpoint = "terraform-secure-rds.xxxxxxxx.us-east-1.rds.amazonaws.com"
rds_secret_arn = "arn:aws:secretsmanager:us-east-1:123456789012:secret:rds-db-credentials"
```

---

### **Step 9 — Verify in AWS Console**

Go to:

1. **VPC → Subnets:**

   * Two private subnets created
2. **RDS → Databases:**

   * RDS instance: `terraform-secure-rds`
   * Network: private subnets only
3. **Secrets Manager → Secrets:**

   * Secret name: `rds-db-credentials`
   * Contains `username` and `password` (encrypted)
4. **Parameter Groups:**

   * Custom parameter group: `custom-mysql-params`

---

### **Step 10 — Connect to RDS (Optional)**

To test connectivity, use an EC2 instance in the same VPC:

```bash
mysql -h terraform-secure-rds.xxxxxxxx.us-east-1.rds.amazonaws.com -u admin -p
```

Enter the password stored in Secrets Manager.

✅ If successful:

```
Welcome to the MySQL monitor.
mysql>
```

---

### **Step 11 — Clean Up Resources**

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 10 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                      | Description                                                             |
| ---------------------------- | ----------------------------------------------------------------------- |
| **DB Subnet Group**          | Ensures RDS runs in private subnets across multiple AZs.                |
| **Parameter Group**          | Allows fine-tuning of database configurations (e.g., charset, logging). |
| **Secrets Manager**          | Securely stores and retrieves credentials using encryption.             |
| **Multi-AZ Deployment**      | Provides high availability by replicating RDS in another AZ.            |
| **Security Group Isolation** | Restricts RDS access to trusted IPs or internal networks.               |

---

## 🧾 Summary

| Step | Task                   | Command                            |
| ---- | ---------------------- | ---------------------------------- |
| 1    | Initialize Terraform   | `terraform init`                   |
| 2    | Validate Configuration | `terraform validate`               |
| 3    | Review Plan            | `terraform plan`                   |
| 4    | Apply Configuration    | `terraform apply -auto-approve`    |
| 5    | Verify RDS & Secrets   | AWS Console → RDS, Secrets Manager |
| 6    | Destroy Resources      | `terraform destroy -auto-approve`  |

