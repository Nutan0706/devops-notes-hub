Perfect 🔥 — here’s your **complete single `.md` file** for **Terraform Practical #6 — Create Security Group**, written in the same clean GitHub-ready format.
You can directly copy-paste this as `06-create-security-group.md` in your repo.


## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- Valid AWS credentials are present

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-sg-demo
cd terraform-sg-demo
```

---

### **Step 3 — Create `main.tf` File**

Create a file named **`main.tf`** and add the following configuration:

```hcl
provider "aws" {
  region = "us-east-1"
}

# Create Security Group
resource "aws_security_group" "web_sg" {
  name        = "terraform-web-sg"
  description = "Allow SSH and HTTP inbound traffic"
  vpc_id      = null  # Uses default VPC if not specified

  # Ingress rules (Inbound)
  ingress {
    description = "Allow SSH from anywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Egress rules (Outbound)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Terraform-SG"
  }
}
```

---

### **Step 4 — Initialize Terraform**

Initialize the Terraform working directory to download the provider:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```

---

### **Step 5 — Validate Configuration**

Check syntax and structure of your configuration:

```bash
terraform validate
```

✅ Output:

```
Success! The configuration is valid.
```

---

### **Step 6 — Review the Execution Plan**

Generate a plan to preview changes:

```bash
terraform plan
```

✅ Expected Output:

```
Plan: 1 to add, 0 to change, 0 to destroy.
```

---

### **Step 7 — Apply Configuration**

Apply the configuration to create the security group:

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

---

### **Step 8 — Verify the Security Group**

Verify in the **AWS Console → EC2 → Security Groups**,
or use the AWS CLI command:

```bash
aws ec2 describe-security-groups --query "SecurityGroups[*].{Name:GroupName,ID:GroupId,Description:Description}" --output table
```

<img width="1688" height="70" alt="image" src="https://github.com/user-attachments/assets/97473c10-31c6-4a2f-9057-d19bacb023ad" />


✅ Example Output:

```
----------------------------------------------------------
|                DescribeSecurityGroups                  |
+----------------+-----------------+----------------------+
| Description    | ID              | Name                 |
+----------------+-----------------+----------------------+
| Allow SSH/HTTP | sg-0a12b3c4d5e6 | terraform-web-sg     |
+----------------+-----------------+----------------------+
```
<img width="979" height="166" alt="image" src="https://github.com/user-attachments/assets/1f5a4743-c0a0-4651-8d81-1d0d3273b4d5" />

---

### **Step 9 — Add Variables for Flexibility**

Let’s make the configuration reusable with variables.

Create **`variables.tf`** file:

```hcl
variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "sg_name" {
  description = "Name of the security group"
  type        = string
  default     = "terraform-web-sg"
}

variable "ssh_cidr" {
  description = "CIDR block allowed for SSH access"
  type        = string
  default     = "0.0.0.0/0"
}

variable "http_cidr" {
  description = "CIDR block allowed for HTTP access"
  type        = string
  default     = "0.0.0.0/0"
}
```

Update **`main.tf`** to use the variables:

```hcl
provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "web_sg" {
  name        = var.sg_name
  description = "Allow SSH and HTTP inbound traffic"

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.ssh_cidr]
  }

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = [var.http_cidr]
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
```

---

### **Step 10 — Define Outputs**

Create **`outputs.tf`** file:

```hcl
output "security_group_id" {
  description = "Security Group ID"
  value       = aws_security_group.web_sg.id
}

output "security_group_name" {
  description = "Security Group Name"
  value       = aws_security_group.web_sg.name
}
```

---

### **Step 11 — Apply with Variables**

Reinitialize and apply the configuration:

```bash
terraform init
terraform apply -auto-approve
```

✅ Output Example:

```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:
security_group_id = "sg-0a12b3c4d5e6"
security_group_name = "terraform-web-sg"
```
<img width="702" height="141" alt="image" src="https://github.com/user-attachments/assets/e0bde924-4304-464d-ac04-e2e5d2e7ba0e" />

---

### **Step 12 — Clean Up Resources**

To delete the created security group:

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 1 destroyed.
```

---

## 🧾 Summary

| Step | Task                  | Command                            |
| ---- | --------------------- | ---------------------------------- |
| 1    | Initialize Terraform  | `terraform init`                   |
| 2    | Validate Config       | `terraform validate`               |
| 3    | Review Plan           | `terraform plan`                   |
| 4    | Apply Configuration   | `terraform apply -auto-approve`    |
| 5    | Verify Security Group | `aws ec2 describe-security-groups` |
| 6    | Destroy Resources     | `terraform destroy -auto-approve`  |





