## 🎯 Practical Task: **Version Locking for Providers**

**Key Focus / Concept:**  
Use `required_providers` and `required_version` blocks to **lock Terraform and provider versions**, ensuring consistency and preventing breaking changes across environments.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have an AWS account with credentials configured
- Basic knowledge of Terraform provider setup

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-version-locking-demo
cd terraform-version-locking-demo
```

---

### **Step 3 — Create `main.tf` File**

Here, we’ll explicitly specify **Terraform version** and **AWS provider version** to ensure consistent behavior.

```hcl
terraform {
  required_version = ">= 1.5.0, < 2.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "version_lock_demo" {
  bucket = "terraform-version-locking-demo-bucket-12345"
  acl    = "private"

  tags = {
    Name        = "VersionLockingDemo"
    Environment = "Dev"
  }
}
```

---

### **Step 4 — Explanation of Key Blocks**

#### 🔹 `required_version`

Locks the **Terraform CLI version** range compatible with your configuration.

```hcl
required_version = ">= 1.5.0, < 2.0.0"
```

✅ Meaning:

* Minimum Terraform version: 1.5.0
* Maximum allowed version: below 2.0.0

This ensures new Terraform versions won’t break your configuration.

---

#### 🔹 `required_providers`

Locks provider source and version:

```hcl
required_providers {
  aws = {
    source  = "hashicorp/aws"
    version = "~> 5.0"
  }
}
```

✅ Meaning:

* Provider must be from **HashiCorp’s AWS registry**
* Version constraint `~> 5.0` allows updates like `5.1, 5.2, 5.9` but blocks major updates like `6.x`

---

### **Step 5 — Initialize Terraform**

Run initialization to download the exact provider version specified:

```bash
terraform init
```

✅ Expected Output:

```
Terraform has been successfully initialized!
- Installing hashicorp/aws v5.51.0...
```

---

### **Step 6 — Check Installed Provider Version**

Verify which provider version was installed:

```bash
terraform providers
```

✅ Example Output:

```
Providers required by configuration:
.
└── provider[registry.terraform.io/hashicorp/aws] ~> 5.0
```

---

### **Step 7 — Validate Configuration**

Check for syntax or version errors:

```bash
terraform validate
```

✅ Output:

```
Success! The configuration is valid.
```

If your Terraform version is below `1.5.0` or above `2.0.0`, you’ll see an error like:

```
Error: Unsupported Terraform Core version
This configuration does not support Terraform version 0.14.0.
```

---

### **Step 8 — Apply Configuration**

Apply the configuration to create resources:

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

---

### **Step 9 — View Lock File (`.terraform.lock.hcl`)**

After initialization, Terraform automatically generates a lock file to ensure version consistency across systems.

File: `.terraform.lock.hcl`

Example Content:

```hcl
provider "registry.terraform.io/hashicorp/aws" {
  version     = "5.51.0"
  constraints = "~> 5.0"
  hashes = [
    "h1:JKoQ9yA1A4bP3z...",
    "h1:WbuzXrj0RwcvG...",
  ]
}
```

✅ **Purpose of `.terraform.lock.hcl`:**

* Locks exact provider version and integrity hashes
* Ensures all team members and CI/CD environments use the same provider build

---

### **Step 10 — Upgrade Providers (When Needed)**

To check for newer provider versions:

```bash
terraform init -upgrade
```

✅ Output:

```
- Upgrading hashicorp/aws v5.51.0 → v5.52.0...
```

This respects version constraints defined in `main.tf`.

---

### **Step 11 — Clean Up Resources**

Once verified, destroy all resources:

```bash
terraform destroy -auto-approve
```

✅ Output:

```
Destroy complete! Resources: 1 destroyed.
```

---

## 🧠 Key Concepts Learned

| Concept                       | Description                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------- |
| **required_version**          | Ensures Terraform CLI compatibility.                                                  |
| **required_providers**        | Specifies the provider source and version constraint.                                 |
| **~> (pessimistic operator)** | Allows patch/minor updates but blocks major version upgrades.                         |
| **.terraform.lock.hcl**       | Automatically created lock file that freezes provider versions for consistent builds. |
| **terraform init -upgrade**   | Updates provider versions while respecting constraints.                               |

---

## 🧾 Summary

| Step | Task                       | Command                           |
| ---- | -------------------------- | --------------------------------- |
| 1    | Define Version Constraints | In `terraform` block              |
| 2    | Initialize Terraform       | `terraform init`                  |
| 3    | Check Installed Providers  | `terraform providers`             |
| 4    | Validate Configuration     | `terraform validate`              |
| 5    | Apply Configuration        | `terraform apply -auto-approve`   |
| 6    | Upgrade Provider           | `terraform init -upgrade`         |
| 7    | Destroy Resources          | `terraform destroy -auto-approve` |
