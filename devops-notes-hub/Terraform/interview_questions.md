# 🌍 Terraform Interview Questions & Notes

---

## 1. Benefits of Infrastructure as Code (IaC)
1. **Consistent Setup** – Same environment every time, no manual errors.  
2. **Faster Deployment** – Automates setup and saves time.  
3. **Easy Tracking** – Version control with Git for quick updates and rollbacks.

## 2. Terraform vs Other IaC Tools
1. **Multi-Cloud Support** – Works with AWS, Azure, GCP, and many more.  
2. **Declarative Language** – Uses simple HCL syntax to define desired state.  
3. **Large Community** – Huge ecosystem with many providers and modules.


## 3. Providers
1. purpose of the provider block in tf with AWS.?
2. can you use multiple AWS provider block in a single configuration.?
3. How you handles AWS credentials when using AWS provider in terraform.?
4. what happen if you don't specify the region in the AWS provider.?
5. can you use an IAM role instead of AWS access and secret key when configurating the AWS provider.?
6. How do you upgrade the AWS provider to a newer version in tf.?
7. can you override the AWS provider region for specific resource.?
8. how can you handle version constraints for the AWS provider in your terraform project.?
9. How can you test validity of AWS provider config without applying changes.?
10. How can you handle AWS provider authentication for a terraform module used by multiple team.?
11. How can you view the current version of the AWS provider used in terraform configuration.?
12. How does terraform handle AWS provider plugin updates.?
13. can you import existing AWS resources into terraform using the AWS provider.?

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

---

## 10. State Locking

---

## 11. State File Structure

---

## 12. Input Variable

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

## 15. Purpose of Workspaces

---

## 16. Managing Multiple Environments

---

## 17. Using Provisioners (e.g., local-exec, remote-exec)

---

## 18. Terraform Backends

---

## 19. Configuring Backends (e.g., S3, Azure Blob, etc.)

---

## 20. Structuring Terraform Projects

---

## 21. Managing Sensitive Data (e.g., Secrets)

---

## 22. Debugging Terraform Configurations

---

## 23. Common Errors and Solutions

---

## 24. Dynamic Blocks and Expressions

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

## 26. Custom Providers

---

## 27. Using Terraform with CI/CD Pipelines

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
## 30. Scenario Based Questions

---
