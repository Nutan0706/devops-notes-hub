## 🎯 Practical Task: **Manage IAM Roles & Policies**

**Key Focus / Concept:**  
Create and attach **IAM roles and policies** to EC2 instances using Terraform — allowing controlled access to AWS services like **S3, CloudWatch**, etc.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have IAM permissions to create roles, policies, and EC2 instances

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-iam-role-demo
cd terraform-iam-role-demo
```

---

### **Step 3 — Create `main.tf` File**

We’ll create:

* **IAM Role** → Grants EC2 permissions
* **IAM Policy** → Defines actions (S3 access)
* **IAM Role Attachment** → Links policy to role
* **Instance Profile** → Attaches role to EC2 instance
* **EC2 Instance** → Launches with IAM role

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ IAM Role for EC2
# --------------------------
resource "aws_iam_role" "ec2_role" {
  name = "Terraform-EC2-Role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })

  tags = {
    Name = "EC2-Role"
  }
}

# --------------------------
# 2️⃣ IAM Policy to Allow S3 Read-Only Access
# --------------------------
resource "aws_iam_policy" "s3_read_policy" {
  name        = "S3ReadOnlyPolicy"
  description = "Allow EC2 to read objects from S3 bucket"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["s3:ListBucket", "s3:GetObject"]
        Effect   = "Allow"
        Resource = ["arn:aws:s3:::*", "arn:aws:s3:::*/*"]
      }
    ]
  })
}

# --------------------------
# 3️⃣ Attach IAM Policy to IAM Role
# --------------------------
resource "aws_iam_role_policy_attachment" "attach_policy" {
  role       = aws_iam_role.ec2_role.name
  policy_arn = aws_iam_policy.s3_read_policy.arn
}

# --------------------------
# 4️⃣ Create Instance Profile
# --------------------------
resource "aws_iam_instance_profile" "ec2_instance_profile" {
  name = "Terraform-EC2-Instance-Profile"
  role = aws_iam_role.ec2_role.name
}

# --------------------------
# 5️⃣ Create Security Group for EC2
# --------------------------
resource "aws_security_group" "ec2_sg" {
  name        = "ec2-iam-sg"
  description = "Allow SSH access"
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

  tags = {
    Name = "IAM-Demo-SG"
  }
}

# --------------------------
# 6️⃣ Create EC2 Instance with IAM Role
# --------------------------
resource "aws_instance" "ec2_with_role" {
  ami                         = "ami-0c55b159cbfafe1f0"
  instance_type               = "t2.micro"
  key_name                    = var.key_name
  vpc_security_group_ids      = [aws_security_group.ec2_sg.id]
  iam_instance_profile        = aws_iam_instance_profile.ec2_instance_profile.name
  associate_public_ip_address = true

  user_data = <<-EOF
              #!/bin/bash
              yum install -y awscli
              echo "Listing S3 Buckets..."
              aws s3 ls > /home/ec2-user/s3-buckets.txt
              EOF

  tags = {
    Name = "EC2-With-IAM-Role"
  }
}

# --------------------------
# 7️⃣ Data Source for Default VPC
# --------------------------
data "aws_vpc" "default" {
  default = true
}

output "instance_public_ip" {
  description = "Public IP of EC2 instance"
  value       = aws_instance.ec2_with_role.public_ip
}
```

---

### **Step 4 — Create `variables.tf` File**

```hcl
variable "key_name" {
  description = "Existing AWS key pair name"
  type        = string
  default     = "terraform-key"
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

### **Step 7 — Apply Configuration**

Apply and create all IAM + EC2 resources:

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 6 added, 0 changed, 0 destroyed.

Outputs:
instance_public_ip = "3.85.210.145"
```

---

### **Step 8 — Verify in AWS Console**

1. Go to **IAM → Roles → Terraform-EC2-Role**

   * Confirm attached policy **S3ReadOnlyPolicy**
2. Go to **IAM → Instance Profiles**

   * Check **Terraform-EC2-Instance-Profile**
3. Go to **EC2 → Instances**

   * Verify the instance has the role attached under **IAM Role**

---

### **Step 9 — Test IAM Role Access**

SSH into your EC2 instance:

```bash
ssh -i ~/.ssh/terraform-key.pem ec2-user@<instance_public_ip>
```

Run the AWS CLI command inside EC2:

```bash
aws s3 ls
cat /home/ec2-user/s3-buckets.txt
```

✅ Expected Output:
List of S3 buckets (proves IAM Role works).

---

### **Step 10 — Destroy Resources**

After verification:

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 6 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                            | Description                                              |
| ---------------------------------- | -------------------------------------------------------- |
| **IAM Role**                       | Grants AWS service (EC2) permission to assume a role.    |
| **IAM Policy**                     | Defines allowed or denied actions on AWS resources.      |
| **Instance Profile**               | Container that allows attaching IAM roles to EC2.        |
| **aws_iam_role_policy_attachment** | Connects IAM roles to policies.                          |
| **Principle of Least Privilege**   | Assign minimal permissions required for a specific task. |

---

## 🧾 Summary

| Step | Task                   | Command                             |
| ---- | ---------------------- | ----------------------------------- |
| 1    | Initialize Terraform   | `terraform init`                    |
| 2    | Validate Configuration | `terraform validate`                |
| 3    | Apply Configuration    | `terraform apply -auto-approve`     |
| 4    | SSH into EC2           | `ssh -i <key> ec2-user@<public-ip>` |
| 5    | Test IAM Access        | `aws s3 ls`                         |
| 6    | Destroy Resources      | `terraform destroy -auto-approve`   |
