## 🎯 Practical Task: **Use Data Sources**


## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have an active AWS account
- You understand basics of providers and resources in Terraform

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-data-source-demo
cd terraform-data-source-demo
```

---

### **Step 3 — Create `main.tf` File**

We’ll use Terraform data sources to **fetch the latest Amazon Linux 2 AMI**, **use the default VPC**, and **get its subnets**.

```hcl
provider "aws" {
  region = "us-east-1"
}

# ✅ Fetch the latest Amazon Linux 2 AMI dynamically
data "aws_ami" "amazon_linux" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["amazon"]
}

# ✅ Fetch the default VPC
data "aws_vpc" "default" {
  default = true
}

# ✅ Fetch all subnets in the default VPC
data "aws_subnets" "default_subnets" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

# ✅ Create EC2 instance using fetched data
resource "aws_instance" "web_server" {
  ami                    = data.aws_ami.amazon_linux.id
  instance_type          = "t2.micro"
  subnet_id              = data.aws_subnets.default_subnets.ids[0]
  associate_public_ip_address = true

  tags = {
    Name        = "Terraform-DataSource-EC2"
    Environment = "Dev"
  }
}

# ✅ Outputs
output "ami_id" {
  description = "Fetched Amazon Linux 2 AMI ID"
  value       = data.aws_ami.amazon_linux.id
}

output "vpc_id" {
  description = "Default VPC ID"
  value       = data.aws_vpc.default.id
}

output "subnet_ids" {
  description = "All subnet IDs from the default VPC"
  value       = data.aws_subnets.default_subnets.ids
}

output "instance_public_ip" {
  description = "Public IP of the created EC2 instance"
  value       = aws_instance.web_server.public_ip
}
```

---

### **Step 4 — Initialize Terraform**

Initialize the working directory and download the AWS provider plugin:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```

---

### **Step 5 — Validate Configuration**

Check syntax and configuration validity:

```bash
terraform validate
```

✅ Expected Output:

```
Success! The configuration is valid.
```

---

### **Step 6 — Review Execution Plan**

Preview what Terraform will fetch and create:

```bash
terraform plan
```

✅ Example Output:

```
data.aws_ami.amazon_linux: Reading...
data.aws_vpc.default: Reading...
data.aws_subnets.default_subnets: Reading...
Plan: 1 to add, 0 to change, 0 to destroy.
```

---

### **Step 7 — Apply Configuration**

Create the EC2 instance using dynamically fetched data:

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:
ami_id = "ami-0c55b159cbfafe1f0"
vpc_id = "vpc-0a1b2c3d4e5f67890"
subnet_ids = [
  "subnet-0a12b3c4d5e6f7890",
  "subnet-0b23c4d5e6f7a8901",
]
instance_public_ip = "54.210.88.45"
```

---

### **Step 8 — Verify in AWS Console**

1. Go to **AWS Console → EC2 → Instances**
2. Confirm your EC2 instance is running
3. Check that the **AMI ID**, **VPC**, and **subnet** match your outputs

Or verify via AWS CLI:

```bash
aws ec2 describe-instances --query "Reservations[*].Instances[*].{ID:InstanceId,AMI:ImageId,Subnet:SubnetId,VPC:VpcId,State:State.Name}" --output table
```

✅ Example Output:

```
---------------------------------------------------------
|                DescribeInstances                      |
+-----------------+------------------+------------------+
|   ID            |   AMI            |   Subnet         |
+-----------------+------------------+------------------+
| i-0a12b3c4d5e6  | ami-0c55b159cbf  | subnet-0a12b3c4d |
+-----------------+------------------+------------------+
```

---

### **Step 9 — Clean Up**

Destroy all resources to avoid unnecessary charges:

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 1 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                   | Description                                                    |
| ------------------------- | -------------------------------------------------------------- |
| **Data Source**           | Used to fetch existing infrastructure information dynamically. |
| **aws_ami**               | Retrieves AMI details (e.g., latest Amazon Linux 2).           |
| **aws_vpc**               | Fetches existing VPC details.                                  |
| **aws_subnets**           | Retrieves all subnets from a given VPC.                        |
| **Dynamic Configuration** | Makes Terraform reusable without hardcoded IDs or names.       |

---

## 🧾 Summary

| Step | Task                 | Command                           |
| ---- | -------------------- | --------------------------------- |
| 1    | Initialize Terraform | `terraform init`                  |
| 2    | Validate Config      | `terraform validate`              |
| 3    | Preview Plan         | `terraform plan`                  |
| 4    | Apply to Create EC2  | `terraform apply -auto-approve`   |
| 5    | Verify Outputs       | `terraform output`                |
| 6    | Destroy Resources    | `terraform destroy -auto-approve` |
