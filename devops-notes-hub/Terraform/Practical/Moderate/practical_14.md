## 🎯 Practical Task: **Manage Multiple Environments Using Workspaces**
**Key Focus / Concept:**  
Use **Terraform Workspaces** to manage multiple environments (**dev**, **stage**, and **prod**) efficiently with a **single configuration**, maintaining isolated state files for each environment.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have valid AWS credentials
- You understand Terraform basics (variables, backend, state)

---

### **Step 2 — Concept Overview**

Terraform **Workspaces** allow you to:
- Maintain **separate states** for different environments (like dev, staging, prod)
- Use the **same codebase**, but with different variable values
- Avoid copying directories for each environment

✅ Example structure:
```

terraform-workspace-demo/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars (default)
├── dev.tfvars
├── stage.tfvars
└── prod.tfvars

````

---

### **Step 3 — Create Working Directory**

```bash
mkdir terraform-workspace-demo
cd terraform-workspace-demo
```

---

### **Step 4 — Create `main.tf` File**

This example will create an **EC2 instance** that changes configuration based on the active workspace.

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ Local Variables
# --------------------------
locals {
  environment = terraform.workspace
}

# --------------------------
# 2️⃣ Create Security Group
# --------------------------
resource "aws_security_group" "ws_sg" {
  name        = "ws-sg-${local.environment}"
  description = "Allow SSH in ${local.environment} environment"
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
    Name        = "SG-${local.environment}"
    Environment = local.environment
  }
}

# --------------------------
# 3️⃣ EC2 Instance
# --------------------------
resource "aws_instance" "ws_ec2" {
  ami                    = "ami-0c55b159cbfafe1f0"
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.ws_sg.id]
  associate_public_ip_address = true

  tags = {
    Name        = "EC2-${local.environment}"
    Environment = local.environment
  }
}

# --------------------------
# 4️⃣ Data Source
# --------------------------
data "aws_vpc" "default" {
  default = true
}

# --------------------------
# 5️⃣ Outputs
# --------------------------
output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.ws_ec2.public_ip
}

output "environment" {
  description = "Current workspace environment"
  value       = local.environment
}
```

---

### **Step 5 — Create `variables.tf` File**

```hcl
variable "key_name" {
  description = "AWS key pair name"
  type        = string
  default     = "terraform-key"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
}
```

---

### **Step 6 — Create Environment Variable Files**

#### `dev.tfvars`

```hcl
instance_type = "t2.micro"
```

#### `stage.tfvars`

```hcl
instance_type = "t2.small"
```

#### `prod.tfvars`

```hcl
instance_type = "t3.medium"
```

---

### **Step 7 — Initialize Terraform**

```bash
terraform init
```

✅ Output:

```
Terraform has been successfully initialized!
```

---

### **Step 8 — Create & List Workspaces**

#### Create a new workspace:

```bash
terraform workspace new dev
```

#### List all workspaces:

```bash
terraform workspace list
```

✅ Example Output:

```
* dev
  default
```

#### Create other environments:

```bash
terraform workspace new stage
terraform workspace new prod
```

✅ Output:

```
Created and switched to workspace "stage"!
Created and switched to workspace "prod"!
```

---

### **Step 9 — Select a Workspace**

```bash
terraform workspace select dev
```

✅ Output:

```
Switched to workspace "dev".
```

---

### **Step 10 — Apply Configuration per Environment**

#### For Dev:

```bash
terraform apply -var-file="dev.tfvars" -auto-approve
```

✅ Output:

```
Apply complete! EC2 instance for dev created.
```

#### For Stage:

```bash
terraform workspace select stage
terraform apply -var-file="stage.tfvars" -auto-approve
```

✅ Output:

```
Apply complete! EC2 instance for stage created.
```

#### For Prod:

```bash
terraform workspace select prod
terraform apply -var-file="prod.tfvars" -auto-approve
```

✅ Output:

```
Apply complete! EC2 instance for prod created.
```

---

### **Step 11 — Verify in AWS Console**

Go to:

* **EC2 → Instances**
* You will see 3 instances:

  ```
  EC2-dev
  EC2-stage
  EC2-prod
  ```

Each has different instance types (`t2.micro`, `t2.small`, `t3.medium`) and tags indicating their environment.

---

### **Step 12 — View Current Workspace**

```bash
terraform workspace show
```

✅ Output:

```
dev
```

---

### **Step 13 — Destroy Specific Environment**

To destroy only the `dev` environment:

```bash
terraform workspace select dev
terraform destroy -var-file="dev.tfvars" -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 2 destroyed.
```

Repeat for other environments as needed.

---

## 🧠 Key Concepts Learned

| Concept                   | Description                                                                      |
| ------------------------- | -------------------------------------------------------------------------------- |
| **Workspace**             | Isolated state file environment for separate deployments using the same code.    |
| **terraform.workspace**   | Built-in variable that returns the current workspace name.                       |
| **Variable Files**        | Define environment-specific values like instance type, region, etc.              |
| **Environment Isolation** | Each workspace maintains its own `terraform.tfstate`.                            |
| **Best Practice**         | Use workspaces for environments (dev, stage, prod) and backend state separation. |

---

## 🧾 Summary

| Step | Task                  | Command                                                    |
| ---- | --------------------- | ---------------------------------------------------------- |
| 1    | Initialize Terraform  | `terraform init`                                           |
| 2    | Create Workspace      | `terraform workspace new dev`                              |
| 3    | List Workspaces       | `terraform workspace list`                                 |
| 4    | Select Workspace      | `terraform workspace select <env>`                         |
| 5    | Apply Environment     | `terraform apply -var-file="<env>.tfvars" -auto-approve`   |
| 6    | Show Active Workspace | `terraform workspace show`                                 |
| 7    | Destroy Specific Env  | `terraform destroy -var-file="<env>.tfvars" -auto-approve` |
