## 🎯 Practical Task: **Use Terraform State Commands**

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have an existing Terraform setup (for example, EC2 or S3 bucket)

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-state-demo
cd terraform-state-demo
```

---

### **Step 3 — Create `main.tf` File**

We’ll use a simple S3 bucket example to demonstrate state commands.

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "demo_bucket" {
  bucket = "terraform-state-demo-bucket-12345"
  acl    = "private"

  tags = {
    Name = "Terraform State Demo Bucket"
  }
}
```

---

### **Step 4 — Initialize Terraform**

Run initialization to download the required provider plugins:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
```

---

### **Step 5 — Apply Configuration**

Apply your configuration to create the resource:

```bash
terraform apply -auto-approve
```

✅ Output:

```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

---

### **Step 6 — View the Terraform State File**

Terraform maintains a state file (`terraform.tfstate`) that tracks all managed resources.

Run this command to inspect the list of resources in the state:

```bash
terraform state list
```

✅ Example Output:

```
aws_s3_bucket.demo_bucket
```
<img width="380" height="56" alt="image" src="https://github.com/user-attachments/assets/009d3fb0-26f2-423b-9ba3-9c77d24ed30b" />

---

### **Step 7 — Inspect a Resource in the State**

To see detailed information about a specific resource, use:

```bash
terraform state show aws_s3_bucket.demo_bucket
```

✅ Example Output:

```
# aws_s3_bucket.demo_bucket:
resource "aws_s3_bucket" "demo_bucket" {
  acl    = "private"
  arn    = "arn:aws:s3:::terraform-state-demo-bucket-12345"
  bucket = "terraform-state-demo-bucket-12345"
  id     = "terraform-state-demo-bucket-12345"
  ...
}
```
<img width="665" height="661" alt="image" src="https://github.com/user-attachments/assets/512151b9-8915-465f-912d-ca69a62a29cb" />

---

### **Step 8 — Move or Rename a Resource in the State**

Suppose you renamed your resource block in code from `demo_bucket` to `main_bucket`.
You can update the state reference without recreating the resource using:

```bash
terraform state mv aws_s3_bucket.demo_bucket aws_s3_bucket.main_bucket
```

✅ Output:

```
Move "aws_s3_bucket.demo_bucket" to "aws_s3_bucket.main_bucket"
```
<img width="557" height="64" alt="image" src="https://github.com/user-attachments/assets/b3feb917-f2dd-4ed6-a06a-4dd7c99db16b" />

---

### **Step 9 — Remove a Resource from the State File**

This removes the resource from Terraform’s tracking (⚠️ it doesn’t delete it from AWS):

```bash
terraform state rm aws_s3_bucket.main_bucket
```

✅ Output:

```
Removed aws_s3_bucket.main_bucket
Successfully removed 1 resource instance(s).
```

<img width="443" height="70" alt="image" src="https://github.com/user-attachments/assets/38bd9700-e49b-4306-812e-1c938567f1b2" />


After removal, check the list again:

```bash
terraform state list
```

✅ Output:

```
(no resources found)
```
<img width="286" height="53" alt="image" src="https://github.com/user-attachments/assets/6fef61ce-38ca-43e2-951a-e465d8fa61e3" />
<img width="354" height="29" alt="image" src="https://github.com/user-attachments/assets/4fa963a2-28dc-4479-a037-1362c3da2eaf" />


---

### **Step 10 — Refresh the State File**

If someone modifies a resource outside Terraform, use the refresh command to sync state with the real infrastructure:

```bash
terraform refresh
```

✅ Output Example:

```
Refreshing Terraform state in-memory prior to plan...
```

---

### **Step 11 — Backup the State File**

Always back up your state file (`terraform.tfstate`) before major changes:

```bash
cp terraform.tfstate terraform.tfstate.backup
```

✅ Output:

```
No output (creates backup copy)
```

---

### **Step 12 — Destroy All Resources**

Once you’re done, clean up the resources:

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 1 destroyed.
```

---

## 🧠 Common Terraform State Commands Summary

| Command                           | Description                                             |
| --------------------------------- | ------------------------------------------------------- |
| `terraform state list`            | Lists all resources tracked in the current state.       |
| `terraform state show <resource>` | Displays detailed information for a specific resource.  |
| `terraform state mv <src> <dest>` | Moves or renames resources in the state file.           |
| `terraform state rm <resource>`   | Removes a resource from Terraform state tracking.       |
| `terraform refresh`               | Syncs Terraform state with actual cloud infrastructure. |

---

## 🧾 Summary

| Step | Task                  | Command                           |
| ---- | --------------------- | --------------------------------- |
| 1    | Initialize Terraform  | `terraform init`                  |
| 2    | Apply Configuration   | `terraform apply -auto-approve`   |
| 3    | List Resources        | `terraform state list`            |
| 4    | Show Resource Details | `terraform state show <resource>` |
| 5    | Move Resource         | `terraform state mv <src> <dest>` |
| 6    | Remove Resource       | `terraform state rm <resource>`   |
| 7    | Refresh State         | `terraform refresh`               |
| 8    | Destroy Resources     | `terraform destroy -auto-approve` |



