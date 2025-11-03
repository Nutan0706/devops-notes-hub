## 🎯 Practical Task: **Destroy Resources Safely**

**Key Focus / Concept:**  
Understand how to safely destroy Terraform-managed resources using `terraform destroy`, and learn how Terraform handles **dependencies** during destruction.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have valid AWS credentials
- A Terraform configuration with multiple dependent resources (like EC2, Security Group, EBS)

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-destroy-demo
cd terraform-destroy-demo
```

---

### **Step 3 — Create `main.tf` File**

We’ll create an **EC2 instance**, **Security Group**, and an **EBS volume** — then later destroy them safely.

```hcl
provider "aws" {
  region = "us-east-1"
}

# Security Group
resource "aws_security_group" "demo_sg" {
  name        = "destroy-demo-sg"
  description = "Allow SSH and HTTP access"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
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
    Name = "Destroy-Demo-SG"
  }
}

# EC2 Instance
resource "aws_instance" "demo_ec2" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  security_groups = [aws_security_group.demo_sg.name]
  key_name      = var.key_name

  tags = {
    Name = "Destroy-Demo-EC2"
  }
}

# EBS Volume (depends on EC2 availability zone)
resource "aws_ebs_volume" "demo_volume" {
  availability_zone = aws_instance.demo_ec2.availability_zone
  size              = 5

  tags = {
    Name = "Destroy-Demo-Volume"
  }
}

# Attach EBS Volume to EC2
resource "aws_volume_attachment" "demo_attach" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.demo_volume.id
  instance_id = aws_instance.demo_ec2.id
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

✅ Expected Output:

```
Terraform has been successfully initialized!
```

---

### **Step 6 — Validate Configuration**

```bash
terraform validate
```

✅ Expected Output:

```
Success! The configuration is valid.
```

---

### **Step 7 — Apply Configuration**

Create all resources:

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
```

---

### **Step 8 — Verify in AWS Console**

Go to:

* **EC2 → Instances** → Confirm your instance is running
* **EC2 → Volumes** → Verify attached volume
* **EC2 → Security Groups** → Confirm SG exists

Or verify via CLI:

```bash
aws ec2 describe-instances --query "Reservations[*].Instances[*].{ID:InstanceId,State:State.Name}" --output table
```

✅ Example Output:

```
-------------------------------------------------
|              DescribeInstances                |
+------------------+-------------+
|        ID        |   State     |
+------------------+-------------+
| i-0a12b3c4d5e678 |  running    |
+------------------+-------------+
```

---

### **Step 9 — Understand Dependencies**

Terraform automatically handles dependencies using **resource references**:

* `aws_volume_attachment` depends on both `aws_instance` and `aws_ebs_volume`.
* `aws_ebs_volume` depends on `aws_instance` for its availability zone.
* Therefore, Terraform destroys them **in reverse order of creation**:

  ```
  Detach Volume → Delete Volume → Terminate Instance → Delete Security Group
  ```

This ensures safe and dependency-aware deletion.

---

### **Step 10 — Dry Run (Check Before Destroying)**

Use the `-destroy` flag with `terraform plan` to preview what will be destroyed:

```bash
terraform plan -destroy
```

✅ Example Output:

```
Plan: 0 to add, 0 to change, 4 to destroy.
```

This helps you confirm before actually deleting any resource.

---

### **Step 11 — Destroy All Resources Safely**

Run the destroy command:

```bash
terraform destroy -auto-approve
```

✅ Example Output:

```
aws_volume_attachment.demo_attach: Destroying... [id=vai-12345]
aws_ebs_volume.demo_volume: Destroying... [id=vol-12345]
aws_instance.demo_ec2: Destroying... [id=i-0abc12345]
aws_security_group.demo_sg: Destroying... [id=sg-12345]

Destroy complete! Resources: 4 destroyed.
```

---

### **Step 12 — Partial Destruction (Specific Resource)**

You can destroy a specific resource if needed:

```bash
terraform destroy -target=aws_instance.demo_ec2 -auto-approve
```

✅ Example Output:

```
Destroy complete! Resources: 1 destroyed.
```

---

### **Step 13 — Remove from State Without Destroying**

If you’ve deleted a resource manually in AWS, remove it from Terraform state to avoid errors:

```bash
terraform state rm aws_instance.demo_ec2
```

✅ Output:

```
Removed aws_instance.demo_ec2
Successfully removed 1 resource instance(s).
```

---

## 🧠 Key Concepts Learned

| Concept               | Description                                                                      |
| --------------------- | -------------------------------------------------------------------------------- |
| **terraform destroy** | Safely destroys all managed resources.                                           |
| **Dependency Graph**  | Terraform automatically determines destroy order based on dependencies.          |
| **-destroy flag**     | Previews resources that will be destroyed.                                       |
| **-target flag**      | Destroys specific resources only.                                                |
| **State Management**  | You can remove manually deleted resources from state using `terraform state rm`. |

---

## 🧾 Summary

| Step | Task                      | Command                                |
| ---- | ------------------------- | -------------------------------------- |
| 1    | Initialize Terraform      | `terraform init`                       |
| 2    | Apply Configuration       | `terraform apply -auto-approve`        |
| 3    | Preview Destruction       | `terraform plan -destroy`              |
| 4    | Destroy Resources         | `terraform destroy -auto-approve`      |
| 5    | Destroy Specific Resource | `terraform destroy -target=<resource>` |
| 6    | Remove from State         | `terraform state rm <resource>`        |

