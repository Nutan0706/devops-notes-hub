## 🎯 Practical Task: **Output Resource Information**

**Key Focus / Concept:**  
Display specific resource information such as **EC2 public IP**, **instance ID**, or **S3 bucket name** using Terraform `output` blocks after resource creation.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have valid AWS credentials
- Familiarity with EC2 or S3 resource creation in Terraform

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-outputs-demo
cd terraform-outputs-demo
```

---

### **Step 3 — Create `main.tf` File**

We’ll create a simple EC2 instance and then display its **Public IP**, **Instance ID**, and **Availability Zone** using outputs.

```hcl
provider "aws" {
  region = "us-east-1"
}

# Create a security group for SSH access
resource "aws_security_group" "ec2_sg" {
  name        = "output-demo-sg"
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
    Name = "Terraform-Output-SG"
  }
}

# Create EC2 instance
resource "aws_instance" "my_instance" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2
  instance_type = "t2.micro"
  key_name      = var.key_name
  security_groups = [aws_security_group.ec2_sg.name]

  tags = {
    Name = "Terraform-Output-Instance"
  }
}
```

---

### **Step 4 — Create `variables.tf` File**

Define variables for reusability:

```hcl
variable "key_name" {
  description = "Existing AWS key pair name"
  type        = string
  default     = "terraform-key"
}
```

---

### **Step 5 — Create `outputs.tf` File**

Define output values for the created EC2 instance:

```hcl
# Display instance public IP
output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.my_instance.public_ip
}

# Display instance ID
output "instance_id" {
  description = "ID of the created EC2 instance"
  value       = aws_instance.my_instance.id
}

# Display availability zone
output "availability_zone" {
  description = "Availability Zone of the EC2 instance"
  value       = aws_instance.my_instance.availability_zone
}
```

---

### **Step 6 — Initialize Terraform**

Initialize your Terraform project:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```

---

### **Step 7 — Validate Configuration**

Check the syntax and configuration validity:

```bash
terraform validate
```

✅ Output:

```
Success! The configuration is valid.
```

---

### **Step 8 — Apply Configuration**

Deploy the infrastructure and display the outputs:

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:
availability_zone = "us-east-1a"
instance_id       = "i-0abc1234d5ef6789"
instance_public_ip = "54.210.99.45"
```

---

### **Step 9 — View Outputs Separately**

You can view outputs anytime without re-applying:

```bash
terraform output
```

✅ Example Output:

```
availability_zone = "us-east-1a"
instance_id       = "i-0abc1234d5ef6789"
instance_public_ip = "54.210.99.45"
```

Or, view a single output value:

```bash
terraform output instance_public_ip
```

✅ Example Output:

```
54.210.99.45
```

---

### **Step 10 — Use Outputs for Automation**

Outputs can also be used by other Terraform modules or shell scripts.
For example, export the public IP to an environment variable:

```bash
export EC2_IP=$(terraform output -raw instance_public_ip)
echo "My EC2 instance IP is $EC2_IP"
```

✅ Example Output:

```
My EC2 instance IP is 54.210.99.45
```

---

### **Step 11 — Destroy Resources**

Clean up to avoid charges:

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 2 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                          | Description                                                          |
| -------------------------------- | -------------------------------------------------------------------- |
| **Output Values**                | Allow Terraform to print or share resource details after deployment. |
| **terraform output**             | Displays all defined output values.                                  |
| **terraform output -raw <name>** | Prints raw output for easy scripting and automation.                 |
| **Reusability**                  | Outputs can be passed between modules or pipelines.                  |

---

## 🧾 Summary

| Step | Task                   | Command                           |
| ---- | ---------------------- | --------------------------------- |
| 1    | Initialize Terraform   | `terraform init`                  |
| 2    | Validate Configuration | `terraform validate`              |
| 3    | Apply Configuration    | `terraform apply -auto-approve`   |
| 4    | View Outputs           | `terraform output`                |
| 5    | Get Single Output      | `terraform output -raw <name>`    |
| 6    | Destroy Resources      | `terraform destroy -auto-approve` |
