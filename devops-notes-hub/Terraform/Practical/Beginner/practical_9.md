
## 🎯 Practical Task: **Create EBS Volume & Attach to EC2**
---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have an existing key pair in AWS (or create one)
- Basic understanding of EC2 and EBS

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-ebs-demo
cd terraform-ebs-demo
```

---

### **Step 3 — Create `main.tf` File**

Create the main Terraform configuration file:

```hcl
provider "aws" {
  region = "us-east-1"
}

# Security Group for EC2
resource "aws_security_group" "ec2_sg" {
  name        = "ebs-demo-sg"
  description = "Allow SSH access"

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
    Name = "EBS-Demo-SG"
  }
}

# EC2 Instance
resource "aws_instance" "my_ec2" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2
  instance_type = "t2.micro"
  key_name      = var.key_name
  security_groups = [aws_security_group.ec2_sg.name]

  tags = {
    Name = "Terraform-EC2-EBS"
  }
}

# Create EBS Volume
resource "aws_ebs_volume" "my_volume" {
  availability_zone = aws_instance.my_ec2.availability_zone
  size              = 5   # 5 GB volume
  type              = "gp2"

  tags = {
    Name = "Terraform-EBS-Volume"
  }
}

# Attach EBS Volume to EC2
resource "aws_volume_attachment" "attach_ebs" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.my_volume.id
  instance_id = aws_instance.my_ec2.id
}
```

---

### **Step 4 — Create `variables.tf` File**

Define the key pair name as a variable:

```hcl
variable "key_name" {
  description = "Existing AWS Key Pair name for EC2 instance"
  type        = string
  default     = "terraform-key"
}
```

---

### **Step 5 — Initialize Terraform**

Initialize your working directory:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```

---

### **Step 6 — Validate Configuration**

Check the configuration syntax and structure:

```bash
terraform validate
```

✅ Expected Output:

```
Success! The configuration is valid.
```

---

### **Step 7 — Review Execution Plan**

Preview what resources Terraform will create:

```bash
terraform plan
```

✅ Example Output:

```
Plan: 3 to add, 0 to change, 0 to destroy.
```

---

### **Step 8 — Apply Configuration**

Create the EC2 instance, EBS volume, and attach it:

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

---

### **Step 9 — Verify in AWS Console**

1. Go to **AWS Console → EC2 → Instances**
2. Check that your EC2 instance is running
3. Navigate to the **Storage** tab and verify that your **EBS volume** is attached

Or verify via AWS CLI:

```bash
aws ec2 describe-volumes --filters Name=tag:Name,Values=Terraform-EBS-Volume --query "Volumes[*].{ID:VolumeId,State:State,AZ:AvailabilityZone}" --output table
```

✅ Example Output:

```
-------------------------------------------------
|               DescribeVolumes                 |
+----------+--------------+---------------------+
|   AZ     |    ID        |       State         |
+----------+--------------+---------------------+
| us-east-1a | vol-0abc12345def6789 | in-use |
+----------+--------------+---------------------+
```

---

### **Step 10 — Connect to EC2 & Verify Volume (Optional)**

SSH into your instance:

```bash
ssh -i ~/.ssh/id_rsa ec2-user@<public-ip>
```

List block devices inside EC2:

```bash
lsblk
```

✅ Example Output:

```
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
xvda    202:0    0    8G  0 disk /
xvdh    202:112  0    5G  0 disk
```

The extra device (`/dev/xvdh`) is your attached EBS volume.

---

### **Step 11 — Define Outputs**

Create an **`outputs.tf`** file:

```hcl
output "instance_id" {
  description = "EC2 Instance ID"
  value       = aws_instance.my_ec2.id
}

output "volume_id" {
  description = "EBS Volume ID"
  value       = aws_ebs_volume.my_volume.id
}

output "attachment_state" {
  description = "EBS Attachment State"
  value       = aws_volume_attachment.attach_ebs.device_name
}
```

After apply, view outputs:

```bash
terraform output
```

✅ Example Output:

```
instance_id = "i-0abc123def456"
volume_id = "vol-0abc12345def6789"
attachment_state = "/dev/sdh"
```

---

### **Step 12 — Clean Up**

Destroy all created resources:

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 3 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                   | Description                                     |
| ------------------------- | ----------------------------------------------- |
| **aws_ebs_volume**        | Creates a new Elastic Block Store (EBS) volume. |
| **aws_volume_attachment** | Attaches an EBS volume to an EC2 instance.      |
| **availability_zone**     | Ensures EBS is created in the same zone as EC2. |
| **lsblk**                 | Linux command to list attached block devices.   |

---

## 🧾 Summary

| Step | Task                   | Command                           |
| ---- | ---------------------- | --------------------------------- |
| 1    | Initialize Terraform   | `terraform init`                  |
| 2    | Validate Configuration | `terraform validate`              |
| 3    | Review Plan            | `terraform plan`                  |
| 4    | Apply Configuration    | `terraform apply -auto-approve`   |
| 5    | Verify Volume          | `aws ec2 describe-volumes`        |
| 6    | SSH & Check            | `lsblk`                           |
| 7    | Destroy Resources      | `terraform destroy -auto-approve` |
