## 🎯 Practical Task: **Remote State Storage in S3 with DynamoDB Locking**

**Key Focus / Concept:**  
Enable collaboration and prevent Terraform state corruption by storing state files in an **S3 bucket** with **DynamoDB-based state locking** for concurrency protection.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Terraform is installed (`terraform -version`)
- AWS CLI is configured (`aws configure`)
- You have an S3 bucket and DynamoDB table permissions
- You understand Terraform state management concepts

---

### **Step 2 — Create Working Directory**

```bash
mkdir terraform-remote-state-demo
cd terraform-remote-state-demo
```

---

### **Step 3 — Create an S3 Bucket for Remote State**

You can create it manually in the AWS Console or via Terraform CLI.

#### Using AWS CLI:

```bash
aws s3api create-bucket \
  --bucket terraform-remote-state-demo-12345 \
  --region us-east-1
```

✅ Example Output:

```
{
    "Location": "/terraform-remote-state-demo-12345"
}
```

---

### **Step 4 — Create DynamoDB Table for State Locking**

This table prevents multiple users from updating the same Terraform state simultaneously.

```bash
aws dynamodb create-table \
  --table-name terraform-lock-table \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

✅ Output:

```
TableDescription:
    TableName: terraform-lock-table
    TableStatus: ACTIVE
```

---

### **Step 5 — Create `backend.tf` File**

Configure Terraform to use S3 as the backend for state storage and DynamoDB for state locking.

```hcl
terraform {
  backend "s3" {
    bucket         = "terraform-remote-state-demo-12345"
    key            = "network/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock-table"
    encrypt        = true
  }
}
```

✅ Explanation:

* `bucket`: S3 bucket where state files are stored
* `key`: Path to store the `.tfstate` file (logical folder structure)
* `dynamodb_table`: Used for state locking
* `encrypt`: Enables AES-256 server-side encryption in S3

---

### **Step 6 — Create `main.tf` File**

We’ll create a simple VPC resource to demonstrate remote state functionality.

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "remote_state_vpc" {
  cidr_block           = "10.20.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "Remote-State-VPC"
    ManagedBy = "Terraform"
  }
}
```

---

### **Step 7 — Initialize Terraform**

During initialization, Terraform will configure the backend and create the remote state connection.

```bash
terraform init
```

✅ Example Output:

```
Initializing the backend...
Successfully configured the backend "s3"!
Terraform has been successfully initialized!
```

You will now see a message like:

```
Terraform has detected that the backend has changed.
Do you want to copy existing state to the new backend? [yes/no]
```

Type **`yes`** to migrate local state to the S3 bucket.

---

### **Step 8 — Apply Configuration**

```bash
terraform apply -auto-approve
```

✅ Example Output:

```
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

---

### **Step 9 — Verify Remote State Storage**

#### ✅ Check in AWS Console:

1. Go to **S3 → terraform-remote-state-demo-12345**
2. Open the path `network/terraform.tfstate`
3. Verify state file is present

#### ✅ Check DynamoDB Lock Table:

* Navigate to **DynamoDB → terraform-lock-table**
* Observe a temporary lock entry when another `terraform apply` is in progress

---

### **Step 10 — Simulate State Locking (Optional)**

Open **two terminals** and run:

```bash
terraform apply
```

in both simultaneously.

One will proceed, and the other will display:

```
Error: Error acquiring the state lock
Lock Info:
  ID:        <unique-lock-id>
  Path:      network/terraform.tfstate
  Operation: OperationTypeApply
  Who:       <your-username>
```

✅ This confirms DynamoDB-based **state locking** works correctly.

---

### **Step 11 — Validate Remote Backend**

You can confirm the backend is remote using:

```bash
terraform state list
```

✅ Example Output:

```
aws_vpc.remote_state_vpc
```

Now this state is being read directly from **S3**, not your local `.terraform` folder.

---

### **Step 12 — Destroy the Resource**

```bash
terraform destroy -auto-approve
```

✅ Example Output:

```
Destroy complete! Resources: 1 destroyed.
```

Check the S3 bucket again — the state file remains stored, now updated to reflect the destruction.

---

## 🧠 Key Concepts Learned

| Concept              | Description                                                          |
| -------------------- | -------------------------------------------------------------------- |
| **Remote State**     | Stores Terraform state files centrally (e.g., S3) for shared access. |
| **DynamoDB Locking** | Prevents concurrent Terraform runs that could corrupt state.         |
| **terraform init**   | Configures and initializes the remote backend connection.            |
| **encrypt=true**     | Ensures S3 state files are AES-256 encrypted for security.           |
| **key**              | Logical path for organizing multiple environment state files.        |

---

## 🧾 Summary

| Step | Task                       | Command                           |
| ---- | -------------------------- | --------------------------------- |
| 1    | Create S3 Bucket           | `aws s3api create-bucket`         |
| 2    | Create DynamoDB Lock Table | `aws dynamodb create-table`       |
| 3    | Configure Backend          | Add `backend "s3"` block          |
| 4    | Initialize Terraform       | `terraform init`                  |
| 5    | Apply Resources            | `terraform apply -auto-approve`   |
| 6    | Verify State in S3         | AWS Console or CLI                |
| 7    | Destroy Resources          | `terraform destroy -auto-approve` |

