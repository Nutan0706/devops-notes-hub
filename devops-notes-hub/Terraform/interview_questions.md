# 🌍 Terraform Interview Questions & Notes

---

### 🧩 1. Benefits of Infrastructure as Code (IaC)

| Benefit | Description |
|----------|-------------|
| **Consistent Setup** | Same environment every time, avoiding manual configuration errors. |
| **Faster Deployment** | Automates infrastructure setup, saving time and effort. |
| **Easy Tracking** | Version control with Git enables quick updates and rollbacks. |

## 2. Terraform vs Other IaC Tools
1. **Multi-Cloud Support** – Works with AWS, Azure, GCP, and many more.  
2. **Declarative Language** – Uses simple HCL syntax to define desired state.  
3. **Large Community** – Huge ecosystem with many providers and modules.


### 🧩 3. Providers

| No. | Question |
|-----|-----------|
| 1 | What is the **purpose of the provider block** in Terraform with AWS? |
| 2 | Can you use **multiple AWS provider blocks** in a single configuration? |
| 3 | How do you **handle AWS credentials** when using the AWS provider in Terraform? |
| 4 | What happens if you **don’t specify the region** in the AWS provider? |
| 5 | Can you use an **IAM role instead of access/secret keys** when configuring the AWS provider? |
| 6 | How do you **upgrade the AWS provider** to a newer version in Terraform? |
| 7 | Can you **override the AWS provider region** for a specific resource? |
| 8 | How can you **handle version constraints** for the AWS provider in your Terraform project? |
| 9 | How can you **test the validity of AWS provider configuration** without applying changes? |
| 10 | How can you **handle AWS provider authentication** for a Terraform module used by multiple teams? |
| 11 | How can you **view the current version** of the AWS provider used in Terraform configuration? |
| 12 | How does Terraform **handle AWS provider plugin updates**? |
| 13 | Can you **import existing AWS resources** into Terraform using the AWS provider? |

---

## 4. Variables
1. primitive type :- string, number, bool
2. complex type :- list, map, object
3. important best practices
  
1. Explain how variable validation work in terraform.?
2. what is the purpose of locals in terraform and how can they be used with variables.?
3. Difference between variables and local variables.?
4. How do you handle situttion where a variable must not be left unset.?
5. what are variable groups in terraform cloud or terraform enterprise.?

---

## 5. State management 
1. Default storage
2. remote storage
3. state locking
4. sensitive data
5. sate manipulation
6. what command can be used to veiw the current state of your terraform configuration.?
7. how can you modify terraform state for a particular resource manually.?
8. Explain the concept of Tainted resources in terraform state.?
9. Difference between terraform refresh and terraform apply.?


---

## 6. Terraform Commands (init, plan, apply, destroy, fmt, validate, refresh)
## 🧠 Terraform Commands

### 🏗️ Basic Commands
- `terraform init`
- `terraform fmt`
- `terraform validate`
- `terraform plan`
- `terraform apply`
- `terraform destroy`
- `terraform show`
- `terraform state list`
- `terraform taint`
- `terraform import <resource_id>`
- `terraform providers`
- `terraform fmt -recursive`
- `terraform output`
- `terraform refresh`
- `terraform console`

---

### 📂 State Management Commands
- `terraform state list`
- `terraform state show`
- `terraform state mv`
- `terraform state rm`
- `terraform state pull`
- `terraform state push`

---

### ⚙️ Providers, Modules, and Plugins
- `terraform providers`
- `terraform provider lock`
- `terraform get`
- `terraform login`
- `terraform logout`
- `terraform provider mirror`

---

### 🧩 Debug, Documentation, and Misc Commands
- `terraform version`
- `terraform help`
- `terraform graph`
- `terraform force-unlock`
- `terraform provider schema`
- `terraform workspace new`
- `terraform workspace select`
- `terraform workspace show`
- `terraform workspace delete`

---

### 🔐 Special Commands
- `terraform plan -out=tfplan`
- `terraform apply tfplan`
- `terraform destroy -target=<resource_name>`
- `terraform taint`
- `terraform untaint`

---

## 7. Terraform Resources
1. Explain the purpose of the name attribute within an AWS resource block.?
2. How can you reference attributes from one aws resource within another resource configuration.?
3. How do you handle the creation of dependent resources such as ec2 instance that required a security group and subnet.?
4. How do you use the provisioner block within a resource block for AWS resources.?
5. How do you handle potential changes in aws resources config over time without cauing disruption.?
6. Explain how terraform handles rolling updates or replacement of AWS resources with minimal downtime.?

---

## 8. Terraform Modules
1. what is difference between calling a module with and without explict versioning.?
2. Explain how terraform manages state files when using modules.?
3. can you use community contributed modules in your terraform project and what precautions should you take.?

---
## 9. Local vs Remote State

- **Local State**  
  - Stored in a file named `terraform.tfstate` on your local machine.  
  - Best for small projects or testing environments.  
  - Risky for teams — state can get out of sync or lost if not backed up.  

- **Remote State**  
  - Stored in a shared backend like **S3**, **Azure Blob**, or **Terraform Cloud**.  
  - Enables **team collaboration** and **state locking** to prevent conflicts.  
  - Provides **better security, backup, and versioning** for production use.  

✅ **Best Practice:** Always use **remote state** for team or production projects.

---
## 10. State Locking

- **Purpose:** Prevents multiple users from modifying the same Terraform state at the same time.  
- **How it works:** When one operation (like `apply` or `plan`) is running, Terraform locks the state file.  
- **Supported by:** Remote backends such as **AWS S3 with DynamoDB**, **Terraform Cloud**, and **Consul**.  
- **Benefit:** Avoids race conditions and ensures consistent infrastructure updates.  

✅ **Best Practice:** Always enable state locking when using remote backends.

---
## 11. State File Structure

- **Purpose:** The `terraform.tfstate` file stores the current state of your infrastructure.  
- **Contains:**  
  - Resource metadata (IDs, dependencies, attributes).  
  - Module and provider details.  
  - Output values from your configurations.  
- **Format:** JSON structure managed automatically by Terraform.  
- **Location:** Stored locally or remotely (depending on backend).  

⚠️ **Note:** Never edit the state file manually — use Terraform commands to manage changes safely.

---
## 12. Input Variables

- **Purpose:** Allow you to customize Terraform configurations without changing code.  
- **Defined in:** `variables.tf` file using the `variable` block.  
- **Used for:** Passing dynamic values like region, instance type, or environment.  
- **Can be set via:**  
  - `.tfvars` files  
  - Command-line flags (`-var`)  
  - Environment variables  

✅ **Example:**
```hcl
variable "region" {
  description = "AWS region"
  default     = "ap-south-1"
}

provider "aws" {
  region = var.region
}
```
---

## 13. Output
1. How can you reference an output value in another terraform configuration.?
2. how can you access nested output values.?
3. how can you test the corretness of an output value in tf.?

---

## 14. Variable Files (.tfvars)

- `.tfvars` files are used to define variable values separately from the main configuration.  
- They help manage different environments (like dev, test, prod) easily.  
- You can pass them while running commands using:  
  ```bash
  terraform apply -var-file="dev.tfvars"

---

## 15.🧭 Purpose of Workspaces

- Workspaces let you manage **multiple environments** (like dev, test, prod) in the same configuration.  
- Each workspace has its **own state file**, keeping resources isolated.  
- Useful for testing changes safely before deploying to production.  
- Common commands:  
  ```bash
  terraform workspace new dev
  terraform workspace select dev
  terraform workspace list
  terraform workspace show

---
## 16. Managing Multiple Environments

- **Purpose:** Helps manage separate environments like `dev`, `staging`, and `prod` with isolated configurations and state.
- **Benefit:** Avoids accidental changes to production and keeps environment-specific configs clean and organized.
- **Common Approaches:**  
  1. **Separate Workspaces** – One codebase, multiple states.  
  2. **Folder Structure per Environment** – Separate directories for dev, staging, and prod.  
  3. **Modules** – Reuse the same code across different environments with different variable values.

### Recommended Folder Structure
├── main.tf
├── variables.tf
├── outputs.tf
├── provider.tf
├── terraform.tfvars
├── modules/
│ └── vpc/
│ ├── main.tf
│ ├── variables.tf
│ └── outputs.tf
└── envs/
├── dev/
├── staging/
└── prod/

✅ **Best Practices:**
- Keep environment-specific values in separate `.tfvars` files.
- Use modules to avoid code duplication.
- Use remote state and workspaces for safe state isolation.
- Never hardcode environment values; use variables.

---
## 17. Using Provisioners (e.g., local-exec, remote-exec)

- **Purpose:** Provisioners are used to run scripts or commands on local or remote machines after a resource is created or destroyed.
- **Types of Provisioners:**  
  - **local-exec:** Runs commands on the machine where Terraform is executed.  
  - **remote-exec:** Runs commands on the remote resource (e.g., SSH into EC2 and run setup scripts).  

⚠️ **Note:** Provisioners should be used only when required (e.g., bootstrapping), as Terraform prefers immutable infrastructure.

**Example: local-exec**
```hcl
resource "aws_s3_bucket" "example" {
  bucket = "my-bucket"

  provisioner "local-exec" {
    command = "echo Bucket created: ${self.bucket}"
  }
}

```
**Example: remote-exec**
```hcl
resource "aws_instance" "web" {
  ami           = "ami-1234567890"
  instance_type = "t2.micro"

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install -y nginx"
    ]
  }
}
```
---
## 18. Terraform Backends

- **Purpose:** Backends define where and how Terraform stores its state file.
- **Types of Backends:**  
  - **Local Backend:** Stores state on your local machine (`terraform.tfstate`).  
  - **Remote Backend:** Stores state in a shared location for team access (e.g., S3, Azure Blob, GCS, Terraform Cloud).  

✅ **Why Use Remote Backends?**  
- Enables team collaboration  
- Provides state locking  
- Better security, backups & versioning  

**Example Backend Configuration:**
```hcl
terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}
```
---
## 19. Configuring Backends (e.g., S3, Azure Blob, etc.)

- **Purpose:** Backends store and manage Terraform state remotely to enable collaboration, security, and state locking.  
- **Common Backends:**  
  - **AWS S3 + DynamoDB** (state storage + locking)  
  - **Azure Blob Storage**  
  - **Google Cloud Storage (GCS)**  
  - **Terraform Cloud**  

✅ **Benefits of Remote Backends:**  
- Centralized & secure state storage  
- Team collaboration with state locking  
- Automatic versioning and backups  

**Example: AWS S3 Backend**
```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}
```

---
## 20.🧱 Structuring Terraform Projects

- Organize Terraform code for **clarity, reusability, and scalability**.  
- Keep separate folders for **environments** like `dev`, `staging`, and `prod`.  
- Use **modules** to group related resources and avoid code duplication.  
- Store **variables**, **outputs**, and **backend configs** in separate files.  

### 📂 Example Project Structure
├── main.tf
├── variables.tf
├── outputs.tf
├── provider.tf
├── terraform.tfvars
├── modules/
│ └── vpc/
│ ├── main.tf
│ ├── variables.tf
│ └── outputs.tf
└── envs/
├── dev/
├── staging/
└── prod/

---
## 21. Managing Sensitive Data (e.g., Secrets)

- **Never hardcode secrets** (API keys, passwords, tokens) in `.tf` or `.tfvars` files.
- Use **environment variables**, **secret managers**, or CI/CD encrypted variables to pass sensitive values.
- Mark variables as **sensitive** to hide them from logs and output.

✅ **Best Practices:**
- Use secret stores like **AWS Secrets Manager**, **Azure Key Vault**, **Vault**, or **SSM Parameter Store**.
- Add `.tfvars` files containing secrets to `.gitignore`.
- Use `sensitive = true` to avoid exposing secret values in CLI output.

**Example:**
```hcl
variable "db_password" {
  type        = string
  sensitive   = true
  description = "Database password"
}
```

---
## 22. Debugging Terraform Configurations

Debugging in Terraform helps identify and resolve issues that occur during configuration, planning, or applying infrastructure changes. Terraform provides multiple ways to debug configurations, logs, and provider behavior.

---

### 🔍 Common Debugging Techniques

1. **Validate Configuration**
   - Run:
     ```bash
     terraform validate
     ```
   - Checks for syntax errors and invalid arguments in `.tf` files.

2. **Dry Run with Plan**
   - Run:
     ```bash
     terraform plan
     ```
   - Allows you to preview what changes Terraform will make before applying them.

3. **Enable Debug Logs**
   - Set the log level to capture detailed internal logs:
     ```bash
     export TF_LOG=TRACE
     ```
   - Other log levels:
     - `TRACE` → Most detailed (shows all internal steps)
     - `DEBUG` → Provider interactions and evaluations
     - `INFO` → High-level information
     - `WARN` → Warnings
     - `ERROR` → Errors only

   - You can also save logs to a file:
     ```bash
     export TF_LOG_PATH=terraform.log
     terraform apply
     ```

4. **Use Terraform Console**
   - A great tool to inspect variables and expressions:
     ```bash
     terraform console
     ```
   - Example:
     ```hcl
     > var.instance_type
     "t2.micro"
     > length(var.subnet_ids)
     3
     ```

5. **Format and Validate Files**
   - Helps catch small formatting or syntax issues:
     ```bash
     terraform fmt -check
     terraform validate
     ```

6. **Check State Files**
   - Sometimes issues occur due to stale or corrupt state.
   - Use:
     ```bash
     terraform state list
     terraform state show <resource_name>
     ```

7. **Use Targeted Apply**
   - To isolate issues with a specific resource:
     ```bash
     terraform apply -target=aws_instance.example
     ```

8. **Provider Debugging**
   - For provider-specific debugging:
     ```bash
     TF_LOG=DEBUG TF_LOG_PATH=provider.log terraform plan
     ```

9. **Dependency Graph**
   - Visualize dependencies:
     ```bash
     terraform graph | dot -Tpng > graph.png
     ```
   - This helps identify circular dependencies or incorrect references.

10. **Common Mistakes**
    - Misspelled variable names
    - Incorrect provider version
    - Uninitialized backend
    - Outdated state files

---

### 🧩 Example Debug Workflow

```bash
terraform validate                # Check syntax and structure
terraform plan                    # Preview changes
export TF_LOG=DEBUG               # Enable debug logs
export TF_LOG_PATH=tf-debug.log   # Save logs
terraform apply                   # Apply configuration
cat tf-debug.log | grep "Error"   # Check errors
```

---
## 23. ⚠️ Common Errors and Solutions

### 🧩 Initialization & Configuration
- **Backend initialization required** – Run `terraform init` first.  
- **Required provider not found** – Run `terraform init -upgrade` to download providers.  
- **Unsupported Terraform version** – Update Terraform to match `required_version`.

---

### 📦 Variable & Input Issues
- **No value for required variable** – Define in `.tfvars` or pass with `-var`.  
- **Invalid variable type** – Match correct type (string, number, list, etc.).  
- **Missing variable file** – Use `terraform apply -var-file="dev.tfvars"`.

---

### 🔗 State & Locking
- **State file locked** – Use `terraform force-unlock <LOCK_ID>` to unlock.  
- **State file missing or corrupted** – Restore from `.tfstate.backup` or backend.  
- **Resource already managed** – Use `terraform import <resource_id>`.

---

### 🏗️ Resource & Dependency Issues
- **Resource already exists** – Import it instead of recreating.  
- **Dependency cycle detected** – Remove circular dependencies between resources.  
- **Invalid index or key** – Check your list/map index or key values.  
- **Provider version mismatch** – Run `terraform init -upgrade`.

---

### 🧠 Logical & Syntax Errors
- **Unsupported argument** – Remove or rename invalid arguments.  
- **Invalid block definition** – Ensure blocks are properly nested and closed.  
- **Unknown resource referenced** – Verify resource names and dependencies.  
- **Invalid function call** – Check syntax and argument types.

---

### 🧹 Miscellaneous
- **Timeout while applying changes** – Check network or increase timeout in config.  
- **Insufficient permissions** – Verify cloud credentials or IAM roles.  
- **Plan differs after apply** – Run `terraform refresh` to sync state.  
- **Provider plugin not found** – Delete `.terraform` folder and reinit with `terraform init`.

---

✅ **Tip:** Always run `terraform fmt` and `terraform validate` before `plan` or `apply` to catch issues early.

---
## 24.⚙️ Dynamic Blocks and Expressions

- **Dynamic blocks** are used to **generate repeated nested blocks** inside a resource dynamically.  
- Useful when the number of nested items (like `ingress` rules or `tags`) changes frequently.  
- **Expressions** allow you to use variables, functions, and conditions within Terraform code.  
- Common expressions include `for`, `if`, and interpolation `${}`.

### 🧱 Example:
```hcl
resource "aws_security_group" "example" {
  name = "dynamic-sg"

  dynamic "ingress" {
    for_each = var.rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr
    }
  }
}
```
---

## 25. Data Sources
1. Fix existing infra
2. dynamic config
3. avoid hardcoding
4. enables dependencies
5. how do you handle data source errors such as when the requested resource is not found.?
6. how do you prevent unnessessary data source fetch to optimize peformance
7. how can you handle situation where data sources require complex fileing or quaries.?
8. it is possible to use dynamic data source config fetched from external files.?

---
## 26. 🧩 Custom Providers

- Custom providers let you **extend Terraform** to manage any external system or API.  
- You can create your own provider when an official one doesn’t exist.  
- Written in **Go language** using the Terraform Plugin SDK.  
- Must implement **CRUD operations** (Create, Read, Update, Delete) for each resource.  
- Once built, it can be added to your Terraform setup using:  
  ```bash
  terraform init

---
## 27. Using Terraform with CI/CD Pipelines

- **Purpose:** Automates Terraform workflows (init, validate, plan, apply) through CI/CD tools.
- **Benefits:** Ensures consistency, faster deployments, automatic checks, and safer infrastructure updates.
- **Common Tools:** GitHub Actions, GitLab CI, Jenkins, Azure DevOps, CircleCI, Bitbucket Pipelines.
- **Typical Pipeline Steps:**  
  1. **Checkout Code** – Pull Terraform code from the repo.  
  2. **Install Terraform** – Set up Terraform environment.  
  3. **Initialize Backend** – `terraform init`  
  4. **Validate Config** – `terraform validate`  
  5. **Plan** – Show changes via `terraform plan` (manual approval recommended).  
  6. **Apply** – Execute `terraform apply` (run only on protected branches like `main` or `prod`).  

✅ **Recommendations:**  
- Use **remote backend & state locking** to avoid conflicts.  
- Require **manual approval** before apply in production.  
- Store secrets (cloud credentials) in **secure CI/CD secret managers** (not in code).
---
## 28.🏷️ Tags in Terraform

- **Tags** are key-value pairs used to organize and identify resources.  
- Help in **cost tracking**, **management**, and **automation**.  
- Can be added inside resource blocks like this:  
  ```hcl
  resource "aws_instance" "example" {
    ami           = "ami-123456"
    instance_type = "t2.micro"

    tags = {
      Name    = "MyServer"
      Project = "DemoApp"
      Env     = "Dev"
    }
  }

---
## 29. Terraform File Types

- **.tf** – Main config files with resources, variables, and outputs.  
- **.tf.json** – Same as `.tf` but written in JSON format.  
- **.tfvars** – Stores variable values separately for different environments.  
- **.tftest.hcl / .tftest.json** – Used for writing Terraform tests.  
- **.terraform.lock.hcl** – Locks provider versions for consistent setups.  
- **.tfstate** – Tracks the current state of your infrastructure.  
- **.tfstate.backup** – Backup of the state file before changes.


---
## 30. Scenario-Based Questions

1. **You need to deploy the same infrastructure in Dev, Staging, and Prod. How will you design it in Terraform?**  
   *Hint:* Use modules, separate `.tfvars`, and remote state with workspaces or folder-based environments.

2. **Two team members ran `terraform apply` at the same time and the state got corrupted. How will you prevent this?**  
   *Hint:* Use a remote backend with state locking (e.g., S3 + DynamoDB, Terraform Cloud).

3. **Your Terraform apply failed halfway, leaving partial resources created. What will you do?**  
   *Hint:* Use `terraform plan`, `terraform refresh`, and re-run apply; check state file for drift.

4. **How do you handle a situation where a resource was created manually outside Terraform?**  
   *Hint:* Bring it under Terraform management using `terraform import`.

5. **You need to change a resource without destroying it (e.g., update an EC2 tag). How will you ensure no recreation happens?**  
   *Hint:* Understand “force replacement” fields, use `lifecycle` block to prevent destroy (e.g., `prevent_destroy`, `ignore_changes`).

6. **Your module is used by many teams; how will you ensure no breaking changes affect them?**  
   *Hint:* Use versioning for modules, maintain backward compatibility, apply semantic versioning.

7. **Your secrets (passwords, keys) are visible in logs. How will you fix it?**  
   *Hint:* Mark variables as `sensitive = true`, move secrets to secret stores, avoid pushing secrets in `.tfvars`.

8. **You need to roll back to a previous infrastructure version. How will you do it with Terraform?**  
   *Hint:* Re-apply previous code version + use state snapshots; avoid manual state edits.

9. **A resource was removed from code. What happens, and how to handle if you don’t want to delete it from cloud?**  
   *Hint:* Terraform will destroy it; use `lifecycle { prevent_destroy = true }` or remove from state if needed (`state rm`).

10. **Terraform is taking too long because of unnecessary plan on unchanged resources. How to optimize?**  
   *Hint:* Use `targets`, organize modules, use `-refresh=false`, avoid overly deep dependencies.

## 31. Scenario-Based Advanced 

1. **You need to deploy identical infrastructure for Dev, Staging, and Prod. How will you structure your Terraform code?**
2. **Two engineers ran `terraform apply` at the same time and the state got corrupted. How will you prevent this in future?**
3. **Your `terraform apply` failed midway and created partial resources. What steps will you take to fix it?**
4. **A resource was created manually outside Terraform. How will you bring it under Terraform management?**
5. **Terraform wants to destroy and recreate a resource, but you only want to update it. How will you prevent recreation?**
6. **Your module is consumed by multiple teams. How will you avoid breaking changes when updating it?**
7. **Sensitive values like passwords are showing in logs. How will you hide them?**
8. **You want to roll back infrastructure to a previous version. How will you do it using Terraform?**
9. **Terraform shows a resource will be destroyed after code changes, but you want to keep it. What will you do?**
10. **State refresh takes too long for large infra. How will you speed up the plan process?**
11. **You need to run some custom script after resource creation. How will you do it?**
12. **Two resources need to be created in a specific order. How will you enforce dependency?**
13. **You want to provision resources across multiple regions but share common code. How will you do that?**
14. **Your team is using Terraform open-source and wants cost estimation before deploying. How can this be achieved?**
15. **Your `.tfstate` file is large and difficult to manage. How will you optimize it?**
16. **You want to reuse the same module but with slight behavior differences per environment. How will you handle this?**
17. **The S3 bucket storing Terraform remote state was accidentally deleted. How do you recover state?**
18. **Your Terraform workspace setup became messy. How do you decide between Workspaces vs separate folders?**
19. **You need to migrate Terraform state from local to remote backend. What steps will you follow?**
20. **A resource was removed from code but must stay in cloud. How will you stop Terraform from deleting it?**
21. **You need to move resources between modules without destroying them. How will you achieve state move?**
22. **A colleague updated infra manually in cloud console, causing drift. How will you reconcile state?**
23. **You need to run Terraform `plan` automatically on every PR and `apply` only after approval. How will you build this CI/CD flow?**
24. **You want to dynamically create multiple similar resources (e.g., subnets). Which Terraform feature will you use?**
25. **During deployment, external API rate limits cause provision failure. How will you handle retry logic?**
26. **You need to share Terraform modules privately within the organization. What’s the best approach?**
27. **How will you handle zero-downtime update for an application load-balanced EC2 setup using Terraform?**
28. **Terraform is failing due to provider version mismatch across team members. How will you fix the provider version consistency?**
29. **You want to track who made changes to infra using Terraform. How do you enable audit history?**
30. **You need to create resources in multiple AWS accounts securely. What is the best strategy to authenticate and manage access?**


## 32. Advanced Terraform project github link.
---
