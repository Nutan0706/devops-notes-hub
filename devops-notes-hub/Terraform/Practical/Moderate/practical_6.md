## 🎯 Practical Task: **Attach Elastic IP to EC2**

**Key Focus / Concept:**  
Allocate and attach an **Elastic IP (EIP)** to an **EC2 instance** programmatically using Terraform — ensuring static IP allocation for consistent public connectivity.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have a valid key pair for SSH access
- You understand EC2 networking basics (public IP, EIP, VPC)

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-eip-demo
cd terraform-eip-demo
```

---

### **Step 3 — Create `main.tf` File**

We’ll:

1. Create a Security Group
2. Launch an EC2 instance
3. Allocate an Elastic IP
4. Associate the EIP with the EC2 instance

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ Create Security Group
# --------------------------
resource "aws_security_group" "eip_sg" {
  name        = "eip-demo-sg"
  description = "Allow SSH access"
  vpc_id      = data.aws_vpc.default.id

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
    Name = "EIP-Demo-SG"
  }
}

# --------------------------
# 2️⃣ Launch EC2 Instance
# --------------------------
resource "aws_instance" "eip_instance" {
  ami                    = "ami-0c55b159cbfafe1f0" # Amazon Linux 2
  instance_type          = "t2.micro"
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.eip_sg.id]
  associate_public_ip_address = false  # Disable auto public IP

  tags = {
    Name = "EIP-Demo-EC2"
  }

  user_data = <<-EOF
              #!/bin/bash
              yum install -y httpd
              systemctl start httpd
              echo "<h1>Elastic IP Demo Instance</h1>" > /var/www/html/index.html
              EOF
}

# --------------------------
# 3️⃣ Allocate Elastic IP
# --------------------------
resource "aws_eip" "static_ip" {
  domain = "vpc"

  tags = {
    Name = "EIP-Demo"
  }
}

# --------------------------
# 4️⃣ Associate Elastic IP with EC2 Instance
# --------------------------
resource "aws_eip_association" "eip_assoc" {
  instance_id   = aws_instance.eip_instance.id
  allocation_id = aws_eip.static_ip.id
}

# --------------------------
# 5️⃣ Data Source for Default VPC
# --------------------------
data "aws_vpc" "default" {
  default = true
}

# --------------------------
# 6️⃣ Output Values
# --------------------------
output "elastic_ip" {
  description = "Elastic IP Address"
  value       = aws_eip.static_ip.public_ip
}

output "instance_id" {
  description = "EC2 Instance ID"
  value       = aws_instance.eip_instance.id
}
```

---

### **Step 4 — Create `variables.tf` File**

```hcl
variable "key_name" {
  description = "Existing AWS Key Pair name"
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

### **Step 7 — Review Execution Plan**

```bash
terraform plan
```

✅ Example Output:

```
Plan: 4 to add, 0 to change, 0 to destroy.
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
elastic_ip = "18.212.144.55"
instance_id = "i-0d12345abcd67890"
```

---

### **Step 9 — Verify in AWS Console**

1. Go to **EC2 → Instances**

   * Confirm instance “EIP-Demo-EC2” is running
   * Check that **Elastic IP** is attached under **Networking → Elastic IPs**

2. Go to **EC2 → Elastic IPs**

   * Verify the static IP is allocated and associated with your instance

Or verify using AWS CLI:

```bash
aws ec2 describe-addresses --query "Addresses[*].{IP:PublicIp,Instance:InstanceId}" --output table
```

✅ Example Output:

```
-------------------------------------
|           DescribeAddresses        |
+------------------+-----------------+
|       IP         |    Instance     |
+------------------+-----------------+
|  18.212.144.55   | i-0d12345abcd   |
+------------------+-----------------+
```

---

### **Step 10 — Access Web Page**

Open your browser and visit:

```
http://<elastic_ip>
```

✅ You should see:

```
<h1>Elastic IP Demo Instance</h1>
```

---

### **Step 11 — Clean Up Resources**

When testing is done, release all resources:

```bash
terraform destroy -auto-approve
```

✅ Example Output:

```
Destroy complete! Resources: 4 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                         | Description                                                              |
| ------------------------------- | ------------------------------------------------------------------------ |
| **Elastic IP (EIP)**            | A static, public IPv4 address for persistent access to instances.        |
| **aws_eip**                     | Allocates a new Elastic IP in your AWS account.                          |
| **aws_eip_association**         | Attaches an Elastic IP to an existing EC2 instance or network interface. |
| **associate_public_ip_address** | Set to `false` when manually assigning EIP.                              |
| **Static IP Benefit**           | Keeps a consistent IP even after instance stop/start.                    |

---

## 🧾 Summary

| Step | Task                   | Command                           |
| ---- | ---------------------- | --------------------------------- |
| 1    | Initialize Terraform   | `terraform init`                  |
| 2    | Validate Configuration | `terraform validate`              |
| 3    | Review Execution Plan  | `terraform plan`                  |
| 4    | Apply Configuration    | `terraform apply -auto-approve`   |
| 5    | Verify Elastic IP      | `aws ec2 describe-addresses`      |
| 6    | Destroy Resources      | `terraform destroy -auto-approve` |
