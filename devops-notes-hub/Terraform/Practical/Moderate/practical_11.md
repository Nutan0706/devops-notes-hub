## 🎯 Practical Task: **Use Count & for_each Meta-Arguments**

**Key Focus / Concept:**  
Learn how to **dynamically create multiple resources** (like EC2 instances, S3 buckets, or IAM users) using **`count`** and **`for_each`** meta-arguments in Terraform — improving scalability, flexibility, and code efficiency.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have an existing AWS key pair (`terraform-key`)
- Familiarity with Terraform variables and resource basics

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-count-foreach-demo
cd terraform-count-foreach-demo
```

---

## 🌱 Part 1 — Using `count` Meta-Argument

### **Step 3 — Create `main.tf` File**

In this example, we’ll create **multiple EC2 instances** dynamically using the `count` parameter.

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ Create Security Group
# --------------------------
resource "aws_security_group" "count_sg" {
  name        = "count-demo-sg"
  description = "Allow SSH"
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
    Name = "Count-Demo-SG"
  }
}

# --------------------------
# 2️⃣ Launch Multiple EC2 Instances using Count
# --------------------------
resource "aws_instance" "count_instances" {
  count                     = var.instance_count
  ami                       = "ami-0c55b159cbfafe1f0"
  instance_type             = "t2.micro"
  key_name                  = var.key_name
  vpc_security_group_ids    = [aws_security_group.count_sg.id]
  associate_public_ip_address = true

  tags = {
    Name = "Count-Demo-Instance-${count.index + 1}"
    Environment = var.environment
  }

  user_data = <<-EOF
              #!/bin/bash
              echo "Instance ${count.index + 1} launched successfully!" > /home/ec2-user/info.txt
              EOF
}

# --------------------------
# 3️⃣ Data Source for Default VPC
# --------------------------
data "aws_vpc" "default" {
  default = true
}

# --------------------------
# 4️⃣ Outputs
# --------------------------
output "instance_public_ips" {
  description = "Public IPs of created instances"
  value       = aws_instance.count_instances[*].public_ip
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

variable "instance_count" {
  description = "Number of EC2 instances to create"
  type        = number
  default     = 2
}

variable "environment" {
  description = "Environment name"
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

### **Step 6 — Apply Configuration**

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:
instance_public_ips = [
  "3.94.214.87",
  "54.164.22.105"
]
```

---

### **Step 7 — Verify in AWS Console**

Go to:

* **EC2 → Instances**
* You’ll see 2 instances:

  ```
  Count-Demo-Instance-1
  Count-Demo-Instance-2
  ```

✅ Both have public IPs and same security group.

---

## 🌿 Part 2 — Using `for_each` Meta-Argument

### **Step 8 — Create S3 Buckets using `for_each`**

Let’s create multiple **S3 buckets** from a map using the `for_each` meta-argument.

#### File: `s3.tf`

```hcl
resource "aws_s3_bucket" "bucket_demo" {
  for_each = var.s3_buckets

  bucket = each.value.bucket_name

  tags = {
    Name        = each.value.bucket_name
    Environment = each.value.env
  }
}
```

#### File: `variables.tf` (add these variables)

```hcl
variable "s3_buckets" {
  description = "Map of S3 buckets to create"
  type = map(object({
    bucket_name = string
    env         = string
  }))
  default = {
    bucket1 = {
      bucket_name = "terraform-demo-bucket-1-2025"
      env         = "dev"
    },
    bucket2 = {
      bucket_name = "terraform-demo-bucket-2-2025"
      env         = "staging"
    }
  }
}
```

---

### **Step 9 — Apply S3 Configuration**

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:
aws_s3_bucket.bucket_demo["bucket1"]: Creation complete
aws_s3_bucket.bucket_demo["bucket2"]: Creation complete
```

---

### **Step 10 — Verify in AWS Console**

Go to:

* **S3 → Buckets**
* Verify created buckets:

  ```
  terraform-demo-bucket-1-2025
  terraform-demo-bucket-2-2025
  ```

Each has environment-specific tags (`dev`, `staging`).

---

### **Step 11 — Clean Up Resources**

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 5 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                    | Description                                                               |
| -------------------------- | ------------------------------------------------------------------------- |
| **count**                  | Used to create multiple instances of a resource based on a numeric value. |
| **for_each**               | Used to create resources dynamically from maps or sets.                   |
| **count.index**            | Refers to the index (starting from 0) of each resource instance.          |
| **each.key / each.value**  | Access elements in a map when using `for_each`.                           |
| **Dynamic Infrastructure** | Avoids repetitive blocks and enables scalable, efficient provisioning.    |

---

## 🧾 Summary

| Step | Task                      | Command                           |
| ---- | ------------------------- | --------------------------------- |
| 1    | Initialize Terraform      | `terraform init`                  |
| 2    | Apply EC2 Count Example   | `terraform apply -auto-approve`   |
| 3    | Verify EC2 Instances      | AWS Console → EC2                 |
| 4    | Apply S3 for_each Example | `terraform apply -auto-approve`   |
| 5    | Verify Buckets            | AWS Console → S3                  |
| 6    | Destroy Resources         | `terraform destroy -auto-approve` |

