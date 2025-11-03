## 🎯 Practical Task: **Use Terraform Import Command**

**Key Focus / Concept:**  
Learn how to **import existing AWS resources** (created manually or via console) into Terraform management, without recreating or destroying them — ensuring full infrastructure-as-code visibility.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You already have existing AWS resources (e.g., EC2 instance, S3 bucket)
- You understand Terraform state management basics

---

### **Step 2 — Scenario Overview**

Assume you already have:
- An existing **S3 bucket**: `my-existing-bucket-demo`
- An existing **EC2 instance**: `i-0abcd1234efgh5678`

Your goal:  
✅ Bring these existing AWS resources **under Terraform management**  
✅ Without deleting or recreating them.

---

### **Step 3 — Create Working Directory**

```bash
mkdir terraform-import-demo
cd terraform-import-demo
```

---

### **Step 4 — Create `main.tf` File**

We’ll define **empty resource blocks** for resources that already exist in AWS.
Terraform will later “link” these blocks with the actual AWS resources.

```hcl
provider "aws" {
  region = "us-east-1"
}

# --------------------------
# 1️⃣ Existing S3 Bucket
# --------------------------
resource "aws_s3_bucket" "imported_bucket" {
  # Bucket already exists; Terraform will import its state.
}

# --------------------------
# 2️⃣ Existing EC2 Instance
# --------------------------
resource "aws_instance" "imported_ec2" {
  # EC2 instance already exists; Terraform will import its state.
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

### **Step 6 — Verify Existing Resources**

Before importing, confirm the AWS resources exist:

#### For S3 bucket:

```bash
aws s3 ls | grep my-existing-bucket-demo
```

#### For EC2 instance:

```bash
aws ec2 describe-instances \
  --query "Reservations[*].Instances[*].{ID:InstanceId,State:State.Name,Name:Tags[?Key=='Name']|[0].Value}" \
  --output table
```

✅ Example Output:

```
----------------------------------------------------
|                    DescribeInstances              |
+-------------+-----------+------------------------+
|     ID      |  State    |         Name           |
+-------------+-----------+------------------------+
| i-0abcd1234efgh5678 | running | my-demo-instance |
+-------------+-----------+------------------------+
```

---

### **Step 7 — Import S3 Bucket**

Terraform import syntax:

```bash
terraform import <resource_type>.<resource_name> <resource_identifier>
```

For S3 bucket:

```bash
terraform import aws_s3_bucket.imported_bucket my-existing-bucket-demo
```

✅ Output:

```
aws_s3_bucket.imported_bucket: Importing from ID "my-existing-bucket-demo"...
aws_s3_bucket.imported_bucket: Import prepared!
Import successful!
```

---

### **Step 8 — Import EC2 Instance**

For EC2 instance:

```bash
terraform import aws_instance.imported_ec2 i-0abcd1234efgh5678
```

✅ Output:

```
aws_instance.imported_ec2: Importing from ID "i-0abcd1234efgh5678"...
aws_instance.imported_ec2: Import complete!
```

---

### **Step 9 — Verify Imported Resources**

After import, check the state file to confirm both resources are tracked:

```bash
terraform state list
```

✅ Output:

```
aws_instance.imported_ec2
aws_s3_bucket.imported_bucket
```

You can also inspect the full resource details:

```bash
terraform state show aws_s3_bucket.imported_bucket
terraform state show aws_instance.imported_ec2
```

---

### **Step 10 — Generate Configuration (Optional)**

If you imported a resource but didn’t have full configuration in your `.tf` file, use the **Terraform Show command** to extract its state and convert to code:

```bash
terraform show -no-color > imported_state.txt
```

Then manually copy attributes into your `main.tf` for future management.

📝 Example snippet after importing EC2:

```hcl
resource "aws_instance" "imported_ec2" {
  ami                    = "ami-0c55b159cbfafe1f0"
  instance_type          = "t2.micro"
  subnet_id              = "subnet-0b12345678"
  vpc_security_group_ids = ["sg-0123456789"]
  key_name               = "terraform-key"

  tags = {
    Name = "my-demo-instance"
  }
}
```

---

### **Step 11 — Plan & Verify Drift**

Now that resources are imported, run:

```bash
terraform plan
```

✅ Example Output:

```
No changes. Infrastructure is up-to-date.
```

If Terraform detects differences between actual resource configuration and `.tf` files, it will show what would change.
You can fix this by updating your `.tf` to match current state.

---

### **Step 12 — Clean Up (Optional)**

If you no longer need the imported resources **managed by Terraform**, simply remove them from state:

```bash
terraform state rm aws_s3_bucket.imported_bucket
terraform state rm aws_instance.imported_ec2
```

✅ Output:

```
Removed aws_s3_bucket.imported_bucket
Removed aws_instance.imported_ec2
```

This **removes** them from Terraform management **without deleting them from AWS**.

---

## 🧠 Key Concepts Learned

| Concept                  | Description                                                                |
| ------------------------ | -------------------------------------------------------------------------- |
| **terraform import**     | Brings existing AWS resources under Terraform state management.            |
| **State Linking**        | Connects existing AWS resource with Terraform resource block.              |
| **terraform state show** | Displays full configuration of imported resource.                          |
| **Manual Code Sync**     | After import, you must define matching configuration in `.tf` files.       |
| **State Safety**         | Import does not modify or recreate the actual resource — it just links it. |

---

## 🧾 Summary

| Step | Task                         | Command                                                        |
| ---- | ---------------------------- | -------------------------------------------------------------- |
| 1    | Initialize Terraform         | `terraform init`                                               |
| 2    | Import S3 Bucket             | `terraform import aws_s3_bucket.imported_bucket <bucket-name>` |
| 3    | Import EC2 Instance          | `terraform import aws_instance.imported_ec2 <instance-id>`     |
| 4    | Verify Imported State        | `terraform state list`                                         |
| 5    | Show Resource Details        | `terraform state show <resource>`                              |
| 6    | Sync Configuration           | `terraform show -no-color > imported_state.txt`                |
| 7    | Remove from State (optional) | `terraform state rm <resource>`                                |
