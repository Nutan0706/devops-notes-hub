## 🎯 Practical Task: **Deploy Auto Scaling Group & Load Balancer**

**Key Focus / Concept:**  
Automate the creation of a **highly available architecture** using **AWS Auto Scaling Group (ASG)** and **Application Load Balancer (ALB)** with Terraform — enabling elastic scaling, health checks, and automatic traffic distribution.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- Valid AWS key pair is available (`terraform-key`)
- Basic knowledge of EC2, Load Balancers, and scaling concepts

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-asg-alb-demo
cd terraform-asg-alb-demo
```

---

### **Step 3 — Create `main.tf` File**

This configuration will:

* Create a **VPC**, **Subnets**, and **Security Groups**
* Create an **ALB**
* Create a **Launch Template**
* Configure an **Auto Scaling Group** behind the ALB

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ VPC and Networking
# --------------------------
resource "aws_vpc" "asg_vpc" {
  cidr_block           = "10.100.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "ASG-VPC"
  }
}

resource "aws_subnet" "public_subnet_1" {
  vpc_id                  = aws_vpc.asg_vpc.id
  cidr_block              = "10.100.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "Public-Subnet-1"
  }
}

resource "aws_subnet" "public_subnet_2" {
  vpc_id                  = aws_vpc.asg_vpc.id
  cidr_block              = "10.100.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true

  tags = {
    Name = "Public-Subnet-2"
  }
}

resource "aws_internet_gateway" "asg_igw" {
  vpc_id = aws_vpc.asg_vpc.id

  tags = {
    Name = "ASG-IGW"
  }
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.asg_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.asg_igw.id
  }

  tags = {
    Name = "ASG-Public-RT"
  }
}

resource "aws_route_table_association" "subnet1_assoc" {
  subnet_id      = aws_subnet.public_subnet_1.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "subnet2_assoc" {
  subnet_id      = aws_subnet.public_subnet_2.id
  route_table_id = aws_route_table.public_rt.id
}

# --------------------------
# 2️⃣ Security Groups
# --------------------------
resource "aws_security_group" "alb_sg" {
  name        = "ALB-SG"
  description = "Allow HTTP from public"
  vpc_id      = aws_vpc.asg_vpc.id

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
    Name = "ALB-SG"
  }
}

resource "aws_security_group" "ec2_sg" {
  name        = "EC2-SG"
  description = "Allow HTTP from ALB and SSH from local"
  vpc_id      = aws_vpc.asg_vpc.id

  ingress {
    from_port       = 80
    to_port         = 80
    protocol        = "tcp"
    security_groups = [aws_security_group.alb_sg.id]
  }

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
    Name = "EC2-SG"
  }
}

# --------------------------
# 3️⃣ Create Application Load Balancer (ALB)
# --------------------------
resource "aws_lb" "app_lb" {
  name               = "terraform-app-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_sg.id]
  subnets            = [aws_subnet.public_subnet_1.id, aws_subnet.public_subnet_2.id]

  tags = {
    Name = "Terraform-ALB"
  }
}

resource "aws_lb_target_group" "app_tg" {
  name     = "app-target-group"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.asg_vpc.id

  health_check {
    path                = "/"
    interval            = 30
    timeout             = 5
    healthy_threshold   = 3
    unhealthy_threshold = 2
  }

  tags = {
    Name = "App-Target-Group"
  }
}

resource "aws_lb_listener" "app_listener" {
  load_balancer_arn = aws_lb.app_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.app_tg.arn
  }
}

# --------------------------
# 4️⃣ Launch Template
# --------------------------
resource "aws_launch_template" "app_lt" {
  name_prefix   = "asg-launch-template-"
  image_id      = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = var.key_name
  vpc_security_group_ids = [aws_security_group.ec2_sg.id]

  user_data = base64encode(<<-EOF
              #!/bin/bash
              yum install -y httpd
              systemctl start httpd
              echo "<h1>Welcome from Terraform Auto Scaling Instance $(hostname -f)</h1>" > /var/www/html/index.html
              EOF
  )

  tag_specifications {
    resource_type = "instance"
    tags = {
      Name = "ASG-Instance"
    }
  }
}

# --------------------------
# 5️⃣ Auto Scaling Group (ASG)
# --------------------------
resource "aws_autoscaling_group" "app_asg" {
  name                      = "terraform-app-asg"
  desired_capacity           = 2
  max_size                   = 3
  min_size                   = 1
  health_check_grace_period  = 30
  health_check_type          = "EC2"
  vpc_zone_identifier        = [aws_subnet.public_subnet_1.id, aws_subnet.public_subnet_2.id]
  target_group_arns          = [aws_lb_target_group.app_tg.arn]

  launch_template {
    id      = aws_launch_template.app_lt.id
    version = "$Latest"
  }

  tag {
    key                 = "Name"
    value               = "ASG-Instance"
    propagate_at_launch = true
  }

  lifecycle {
    create_before_destroy = true
  }
}

# --------------------------
# 6️⃣ Output Values
# --------------------------
output "load_balancer_dns_name" {
  description = "DNS name of the Application Load Balancer"
  value       = aws_lb.app_lb.dns_name
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

✅ Output:

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
Plan: 14 to add, 0 to change, 0 to destroy.
```

---

### **Step 8 — Apply Configuration**

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 14 added, 0 changed, 0 destroyed.

Outputs:
load_balancer_dns_name = "terraform-app-lb-1737463895.us-east-1.elb.amazonaws.com"
```

---

### **Step 9 — Verify Resources in AWS Console**

1. **VPC** → “ASG-VPC” created
2. **EC2 → Auto Scaling Groups** → “terraform-app-asg” active
3. **Load Balancer** → “terraform-app-lb” active with healthy targets
4. Visit the ALB URL:

   ```
   http://<load_balancer_dns_name>
   ```

   ✅ Expected Output:

   ```
   <h1>Welcome from Terraform Auto Scaling Instance ip-10-100-x-x</h1>
   ```

---

### **Step 10 — Scale and Test**

Manually change ASG size:

```bash
terraform apply -var="desired_capacity=3" -auto-approve
```

Or test **Auto Healing**:

* Stop one EC2 instance → ASG automatically launches a new one.

---

### **Step 11 — Clean Up Resources**

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 14 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                             | Description                                                              |
| ----------------------------------- | ------------------------------------------------------------------------ |
| **Auto Scaling Group (ASG)**        | Automatically adjusts EC2 instance count based on demand or health.      |
| **Application Load Balancer (ALB)** | Distributes incoming traffic across healthy EC2 instances.               |
| **Target Group**                    | Logical grouping of instances used by ALB for health checks and routing. |
| **Launch Template**                 | Defines instance configuration for ASG (AMI, type, user data).           |
| **High Availability**               | Achieved using multiple subnets across Availability Zones.               |

---

## 🧾 Summary

| Step | Task                   | Command                           |
| ---- | ---------------------- | --------------------------------- |
| 1    | Initialize Terraform   | `terraform init`                  |
| 2    | Validate Configuration | `terraform validate`              |
| 3    | Review Plan            | `terraform plan`                  |
| 4    | Apply Configuration    | `terraform apply -auto-approve`   |
| 5    | Verify ALB & ASG       | Check DNS in AWS Console          |
| 6    | Destroy Infrastructure | `terraform destroy -auto-approve` |
