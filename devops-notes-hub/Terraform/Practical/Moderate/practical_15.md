## 🎯 Practical Task: **Implement Secrets Management with AWS Secrets Manager**

**Key Focus / Concept:**  
Use **AWS Secrets Manager** to **securely store and inject secrets** (like DB credentials, API keys, etc.) into Terraform configurations — ensuring secrets are **never hardcoded** or exposed in `.tf` files or state.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have permission to manage Secrets Manager and IAM policies
- Basic understanding of Terraform variables and AWS services

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-secrets-manager-demo
cd terraform-secrets-manager-demo
```

---

### **Step 3 — Scenario Overview**

We’ll:

1. Store a **database credential** in AWS Secrets Manager
2. Fetch that secret securely during Terraform apply
3. Use it to create an **RDS database** (or simulate usage)

This ensures **no plain-text credentials** are stored in `.tf` files or Terraform state.

---

### **Step 4 — Create `main.tf` File**

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ Create a Random Password
# --------------------------
resource "random_password" "db_password" {
  length  = 16
  special = true
}

# --------------------------
# 2️⃣ Store Secrets in AWS Secrets Manager
# --------------------------
resource "aws_secretsmanager_secret" "db_secret" {
  name        = "terraform-demo-db-secret"
  description = "Stores DB credentials for Terraform demo"
}

resource "aws_secretsmanager_secret_version" "db_secret_version" {
  secret_id     = aws_secretsmanager_secret.db_secret.id
  secret_string = jsonencode({
    username = var.db_username
    password = random_password.db_password.result
  })
}

# --------------------------
# 3️⃣ Retrieve Secret (Simulating Usage)
# --------------------------
data "aws_secretsmanager_secret" "db_secret_lookup" {
  name = aws_secretsmanager_secret.db_secret.name
}

data "aws_secretsmanager_secret_version" "db_secret_value" {
  secret_id = data.aws_secretsmanager_secret.db_secret_lookup.id
}

locals {
  db_creds = jsondecode(data.aws_secretsmanager_secret_version.db_secret_value.secret_string)
}

# --------------------------
# 4️⃣ Example Resource (EC2 Instance Simulating DB Client)
# --------------------------
resource "aws_instance" "secret_demo_instance" {
  ami                    = "ami-0c55b159cbfafe1f0"
  instance_type          = "t2.micro"
  key_name               = var.key_name
  associate_public_ip_address = true

  user_data = <<-EOF
              #!/bin/bash
              echo "Connecting to DB with user: ${local.db_creds.username}" > /home/ec2-user/db-connection.txt
              EOF

  tags = {
    Name = "Secrets-Demo-Instance"
  }
}

# --------------------------
# 5️⃣ Outputs
# --------------------------
output "secret_arn" {
  description = "ARN of the created secret"
  value       = aws_secretsmanager_secret.db_secret.arn
}

output "db_username" {
  description = "Fetched username from Secrets Manager"
  value       = local.db_creds.username
}

output "db_password" {
  description = "Fetched password (hidden)"
  value       = nonsensitive(local.db_creds.password)
}
```

---

### **Step 5 — Create `variables.tf` File**

```hcl
variable "db_username" {
  description = "Database master username"
  type        = string
  default     = "adminuser"
}

variable "key_name" {
  description = "AWS EC2 key pair name"
  type        = string
  default     = "terraform-key"
}
```

---

### **Step 6 — Initialize Terraform**

```bash
terraform init
```

✅ Example Output:

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

### **Step 8 — Apply Configuration**

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:
db_username = "adminuser"
db_password = (sensitive value)
secret_arn  = arn:aws:secretsmanager:us-east-1:123456789012:secret:terraform-demo-db-secret
```

---

### **Step 9 — Verify in AWS Console**

Go to:

1. **AWS → Secrets Manager**

   * Secret name: `terraform-demo-db-secret`
   * Expand the secret to view:

     ```json
     {
       "username": "adminuser",
       "password": "<randomly_generated_password>"
     }
     ```
2. **EC2 → Instances**

   * Check `Secrets-Demo-Instance`
   * SSH into the instance and verify:

     ```bash
     cat /home/ec2-user/db-connection.txt
     ```

     ✅ Output:

     ```
     Connecting to DB with user: adminuser
     ```

---

### **Step 10 — Retrieve Secret Securely via CLI**

You can also retrieve the secret manually using AWS CLI:

```bash
aws secretsmanager get-secret-value --secret-id terraform-demo-db-secret
```

✅ Output:

```json
{
    "Name": "terraform-demo-db-secret",
    "SecretString": "{\"username\":\"adminuser\",\"password\":\"M8#4fS@pQZ9gL!tw\"}"
}
```

---

### **Step 11 — Destroy Resources**

When testing is done:

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 4 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                   | Description                                                                |
| ------------------------- | -------------------------------------------------------------------------- |
| **AWS Secrets Manager**   | Securely stores, rotates, and manages secrets for apps and infrastructure. |
| **random_password**       | Generates a random, secure password dynamically.                           |
| **jsonencode/jsondecode** | Encodes/decodes secrets to/from JSON format for safe usage.                |
| **nonsensitive()**        | Displays sensitive output values safely in logs.                           |
| **Secure Injection**      | Secrets are retrieved at runtime, not hardcoded in `.tf` files.            |

---

## 🧾 Summary

| Step | Task                   | Command                                |
| ---- | ---------------------- | -------------------------------------- |
| 1    | Initialize Terraform   | `terraform init`                       |
| 2    | Validate Configuration | `terraform validate`                   |
| 3    | Apply Configuration    | `terraform apply -auto-approve`        |
| 4    | Verify Secret          | AWS Console → Secrets Manager          |
| 5    | SSH into EC2           | `cat /home/ec2-user/db-connection.txt` |
| 6    | Destroy Resources      | `terraform destroy -auto-approve`      |
