## 🎯 Practical Task: **Create EC2 Instance**

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting, ensure:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have an active AWS account

---

### **Step 2 — Create a Working Directory**

Create a new folder for this project:
```bash
mkdir terraform-ec2-demo
cd terraform-ec2-demo
```

---

### **Step 3 — Create `main.tf` File**

Create a file named **`main.tf`** and add the following configuration:

```hcl
provider "aws" {
  region = "us-east-1"
}

# Create a security group
resource "aws_security_group" "ec2_sg" {
  name        = "terraform-ec2-sg"
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
    Name = "terraform-sg"
  }
}

# Create a key pair
resource "aws_key_pair" "ec2_key" {
  key_name   = "terraform-key"
  public_key = file("~/.ssh/id_rsa.pub")
}

# Create EC2 Instance
resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 (update region-wise)
  instance_type = "t2.micro"
  key_name      = aws_key_pair.ec2_key.key_name
  security_groups = [aws_security_group.ec2_sg.name]

  tags = {
    Name = "Terraform-EC2"
  }
}
```

---

### **Step 4 — Initialize Terraform**

Initialize the working directory to download required provider plugins:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```
<img width="719" height="348" alt="image" src="https://github.com/user-attachments/assets/f584c85b-0ecf-4bb4-93c8-d4655b02b42f" />

---

### **Step 5 — Validate the Configuration**

Validate syntax and configuration:

```bash
terraform validate
```
You may issue like 
```
Invalid value for "path" parameter: no file exists at this function works only with files │ that are distributed as part of the configuration source code, so if this file will be created by a resource in this configuration you must instead obtain this result │ from an attribute of that resource.
```
if yes just run this command in your terminal
```bash
ssh-keygen -t rsa -b 4096 -f id_rsa
```

✅ Expected Output:

```
Success! The configuration is valid.
```
<img width="364" height="51" alt="image" src="https://github.com/user-attachments/assets/f626eb90-2b9d-4e2f-b382-d5ec1867fdce" />

---

### **Step 6 — Review the Execution Plan**

Generate a plan to preview the resources Terraform will create:

```bash
terraform plan
```

✅ Output Example:

```
Plan: 3 to add, 0 to change, 0 to destroy.
```
<img width="461" height="395" alt="image" src="https://github.com/user-attachments/assets/4548c099-0271-4c05-83b9-01793ef9dbb8" />

---

### **Step 7 — Apply the Configuration**

Apply the configuration to create resources on AWS:

```bash
terraform apply -auto-approve
```

✅ Expected Output:

```
Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```
<img width="566" height="454" alt="image" src="https://github.com/user-attachments/assets/4f131602-1e98-476a-9be7-cd0f2b99fbd8" />

You’ll see your EC2 instance ID and public IP in the output.

---

### **Step 8 — Verify the Instance**

1. Go to **AWS Console → EC2 → Instances**
2. Check that a new instance named **Terraform-EC2** is running
3. Copy its **Public IP**
<img width="1528" height="754" alt="image" src="https://github.com/user-attachments/assets/86cdd1ee-9153-4742-bb4a-cf2d831c99d2" />

---

### **Step 9 — Connect to EC2 Instance**

Use SSH to connect:

```bash
ssh -i ~/.ssh/id_rsa ec2-user@<public-ip>
```

Example:

```bash
ssh -i ~/.ssh/id_rsa ec2-user@54.210.99.123
```
<img width="735" height="503" alt="image" src="https://github.com/user-attachments/assets/0d5e6817-6dbf-4413-84c1-0768df33480f" />

---

### **Step 10 — Clean Up Resources**

To destroy everything created by Terraform:

```bash
terraform destroy -auto-approve
```

✅ Expected Output:

```
Destroy complete! Resources: 3 destroyed.
```
<img width="608" height="444" alt="image" src="https://github.com/user-attachments/assets/d25bae5b-dc3e-43b2-a44e-73221cf0e4d5" />

---

## 🧾 Summary

| Step | Task                 | Command                           |
| ---- | -------------------- | --------------------------------- |
| 1    | Initialize Terraform | `terraform init`                  |
| 2    | Validate Config      | `terraform validate`              |
| 3    | Plan Deployment      | `terraform plan`                  |
| 4    | Apply to Create EC2  | `terraform apply -auto-approve`   |
| 5    | Destroy Resources    | `terraform destroy -auto-approve` |


---

✅ **Practical Completed Successfully!**
You’ve successfully created, verified, and destroyed an EC2 instance using Terraform — including key pairs and security groups.

