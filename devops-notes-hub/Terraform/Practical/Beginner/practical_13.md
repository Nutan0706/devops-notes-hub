## 🎯 Practical Task: **Terraform Format & Validate**

**Key Focus / Concept:**  
Use `terraform fmt` and `terraform validate` to ensure **syntax correctness**, **style consistency**, and **error-free configurations** before applying changes.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have a basic Terraform configuration ready

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-fmt-validate-demo
cd terraform-fmt-validate-demo
```

---

### **Step 3 — Create an Intentionally Misformatted `main.tf` File**

This file contains valid Terraform code but is **poorly formatted** for demonstration.

```hcl
provider "aws"{
region="us-east-1"
}

resource "aws_s3_bucket" "demo_bucket"{
bucket="terraform-fmt-demo-bucket-12345"
acl="private"
tags={
Name="DemoBucket"
Environment="Test"
}
}
```

---

### **Step 4 — Run `terraform fmt` (Format Code)**

The `terraform fmt` command automatically formats your Terraform files to follow **standard style guidelines**.

```bash
terraform fmt
```

✅ Example Output:

```
main.tf
```

This means Terraform detected formatting issues and fixed them automatically.

---

### **Step 5 — View the Formatted Code**

After running `terraform fmt`, your `main.tf` will now look clean and properly indented:

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "demo_bucket" {
  bucket = "terraform-fmt-demo-bucket-12345"
  acl    = "private"

  tags = {
    Name        = "DemoBucket"
    Environment = "Test"
  }
}
```

✅ **Tip:**
To check only (without changing files), run:

```bash
terraform fmt -check
```

If files are not formatted, Terraform will return a non-zero exit code.

---

### **Step 6 — Validate Configuration Syntax**

Next, use `terraform validate` to check the configuration structure and syntax before applying:

```bash
terraform validate
```

✅ Expected Output:

```
Success! The configuration is valid.
```

If there’s an error (for example, missing braces or quotes), Terraform shows descriptive messages like:

```
Error: Missing required argument
```

---

### **Step 7 — Combine Commands for CI/CD**

You can chain both commands to ensure code quality automatically (useful in pipelines):

```bash
terraform fmt -check && terraform validate
```

✅ Example Output:

```
Success! The configuration is valid.
```

If formatting fails, `terraform fmt -check` exits with a non-zero code — stopping the pipeline before invalid code runs.

---

### **Step 8 — Validate Module or Directory**

To validate a specific folder (like a module), run:

```bash
terraform validate ./modules/network
```

✅ Output:

```
Success! The configuration is valid.
```

---

### **Step 9 — Optional: Validate JSON Configuration**

Terraform can also validate `.tf.json` files using the same `validate` command:

```bash
terraform validate -json
```

✅ Example Output:

```json
{
  "valid": true,
  "error_count": 0,
  "warning_count": 0
}
```

---

### **Step 10 — Apply (Optional)**

Once your configuration is properly formatted and validated, you can safely apply it:

```bash
terraform apply -auto-approve
```

✅ Output:

```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

---

## 🧠 Key Concepts Learned

| Command                  | Description                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------- |
| **terraform fmt**        | Automatically formats Terraform files to a standard layout.                         |
| **terraform fmt -check** | Checks if files are formatted without making changes.                               |
| **terraform validate**   | Validates Terraform configuration files for syntax and structure.                   |
| **CI/CD Use**            | Common practice to run `fmt` and `validate` before `plan` or `apply` in automation. |

---

## 🧾 Summary

| Step | Task                  | Command                                      |
| ---- | --------------------- | -------------------------------------------- |
| 1    | Format Terraform Code | `terraform fmt`                              |
| 2    | Check Format Only     | `terraform fmt -check`                       |
| 3    | Validate Syntax       | `terraform validate`                         |
| 4    | Combine Commands      | `terraform fmt -check && terraform validate` |
| 5    | Apply Valid Code      | `terraform apply -auto-approve`              |
