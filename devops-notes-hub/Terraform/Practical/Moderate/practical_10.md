## 🎯 Practical Task: **Manage Route53 DNS Records**

**Key Focus / Concept:**  
Automate **domain and subdomain setup** in AWS **Route53** using Terraform — including hosted zones, record sets, and ALB integration for real-time DNS management.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You own a **registered domain name** (e.g., from Route53, GoDaddy, or Namecheap)
- Domain is either:
  - Registered on Route53, **or**
  - Configured to use Route53 **as the DNS provider** (using NS records)

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-route53-demo
cd terraform-route53-demo
```

---

### **Step 3 — Create `main.tf` File**

We’ll:

1. Create a **hosted zone** for the domain
2. Add **DNS records** for root and subdomains
3. Integrate with **ALB** (optional)

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ Create Route53 Hosted Zone
# --------------------------
resource "aws_route53_zone" "primary_zone" {
  name = var.domain_name

  tags = {
    Name = "Terraform-Route53-Demo"
    Environment = var.environment
  }
}

# --------------------------
# 2️⃣ Create A Record for Root Domain
# --------------------------
resource "aws_route53_record" "root_a_record" {
  zone_id = aws_route53_zone.primary_zone.zone_id
  name    = var.domain_name
  type    = "A"
  ttl     = 300
  records = [var.ip_address]
}

# --------------------------
# 3️⃣ Create CNAME Record for Subdomain
# --------------------------
resource "aws_route53_record" "subdomain_cname" {
  zone_id = aws_route53_zone.primary_zone.zone_id
  name    = "app.${var.domain_name}"
  type    = "CNAME"
  ttl     = 300
  records = [var.subdomain_target]
}

# --------------------------
# 4️⃣ Optional — ALB DNS Record (if using ALB)
# --------------------------
resource "aws_route53_record" "alb_alias" {
  zone_id = aws_route53_zone.primary_zone.zone_id
  name    = "www.${var.domain_name}"
  type    = "A"

  alias {
    name                   = var.alb_dns_name
    zone_id                = var.alb_zone_id
    evaluate_target_health = true
  }
}

# --------------------------
# 5️⃣ Output Values
# --------------------------
output "route53_zone_id" {
  description = "ID of the created Route53 Hosted Zone"
  value       = aws_route53_zone.primary_zone.zone_id
}

output "root_record" {
  description = "Root domain A record"
  value       = aws_route53_record.root_a_record.fqdn
}

output "subdomain_record" {
  description = "Subdomain CNAME record"
  value       = aws_route53_record.subdomain_cname.fqdn
}
```

---

### **Step 4 — Create `variables.tf` File**

```hcl
variable "domain_name" {
  description = "The primary domain name"
  type        = string
  default     = "example.com"
}

variable "ip_address" {
  description = "Public IP address for root domain"
  type        = string
  default     = "18.220.10.15"
}

variable "subdomain_target" {
  description = "CNAME target for subdomain (e.g., ALB or EC2 public DNS)"
  type        = string
  default     = "ec2-3-91-54-100.compute-1.amazonaws.com"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "alb_dns_name" {
  description = "Optional: ALB DNS name for alias record"
  type        = string
  default     = "terraform-app-lb-123456789.us-east-1.elb.amazonaws.com"
}

variable "alb_zone_id" {
  description = "ALB Hosted Zone ID"
  type        = string
  default     = "Z35SXDOTRQ7X7K"
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

Outputs:
route53_zone_id = "Z05614232ABCDEFGH"
root_record     = "example.com"
subdomain_record = "app.example.com"
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
route53_zone_id  = "Z05614232ABCDEFGH"
root_record      = "example.com"
subdomain_record = "app.example.com"
```

---

### **Step 9 — Verify in AWS Console**

1. Go to **AWS Console → Route53 → Hosted Zones**
2. Verify that:

   * Hosted Zone `example.com` exists
   * `A` record → `example.com` → points to IP
   * `CNAME` → `app.example.com` → points to ALB/EC2 DNS

✅ Example:

| Record Name                               | Type      | Value / Target                                         | TTL |
| ----------------------------------------- | --------- | ------------------------------------------------------ | --- |
| example.com                               | A         | 18.220.10.15                                           | 300 |
| app.example.com                           | CNAME     | ec2-3-91-54-100.compute-1.amazonaws.com                | 300 |
| [www.example.com](http://www.example.com) | A (Alias) | terraform-app-lb-123456789.us-east-1.elb.amazonaws.com | —   |

---

### **Step 10 — Test DNS Resolution**

You can verify using `dig` or `nslookup`:

```bash
dig example.com +short
dig app.example.com +short
```

✅ Output:

```
18.220.10.15
ec2-3-91-54-100.compute-1.amazonaws.com
```

Or visit:

```
http://example.com
http://app.example.com
```

---

### **Step 11 — Optional: Import Existing Hosted Zone**

If your domain is already hosted in Route53, import it to Terraform:

```bash
terraform import aws_route53_zone.primary_zone Z05614232ABCDEFGH
```

Then run:

```bash
terraform plan
```

✅ This syncs existing infrastructure with Terraform state.

---

### **Step 12 — Clean Up Resources**

```bash
terraform destroy -auto-approve
```

✅ Example Output:

```
Destroy complete! Resources: 4 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                  | Description                                                                   |
| ------------------------ | ----------------------------------------------------------------------------- |
| **Route53 Hosted Zone**  | Container for all DNS records of a domain.                                    |
| **A Record**             | Maps domain/subdomain to an IP address.                                       |
| **CNAME Record**         | Points subdomain to another domain (e.g., ALB or EC2 DNS).                    |
| **Alias Record**         | AWS-specific record that points to AWS resources like ALB, CloudFront, or S3. |
| **Terraform Automation** | Helps manage and version DNS infrastructure as code.                          |

---

## 🧾 Summary

| Step | Task                    | Command                           |
| ---- | ----------------------- | --------------------------------- |
| 1    | Initialize Terraform    | `terraform init`                  |
| 2    | Validate Configuration  | `terraform validate`              |
| 3    | Review Plan             | `terraform plan`                  |
| 4    | Apply DNS Configuration | `terraform apply -auto-approve`   |
| 5    | Verify Hosted Zone      | AWS Console → Route53             |
| 6    | Test DNS Resolution     | `dig example.com +short`          |
| 7    | Destroy Resources       | `terraform destroy -auto-approve` |
