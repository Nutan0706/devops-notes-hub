# **🌍 Terraform Concepts – Category-wise Table (Badges in First Column + One-liner Definitions)**

---

# **1️⃣ Terraform Basics** ![](https://img.shields.io/badge/Category-Basics-blue)

| Badge                                                 | Concept         | Definition                                             |
| ----------------------------------------------------- | --------------- | ------------------------------------------------------ |
| ![](https://img.shields.io/badge/Terraform-CLI-blue)  | Terraform CLI   | Command-line tool used to run Terraform commands.      |
| ![](https://img.shields.io/badge/Provider-green)      | Provider        | Plugin to manage resources (AWS, Azure, GitHub, etc.). |
| ![](https://img.shields.io/badge/Resource-yellow)     | Resource        | Infrastructure component you want Terraform to create. |
| ![](https://img.shields.io/badge/Data--Source-orange) | Data Source     | Read-only external data used in configuration.         |
| ![](https://img.shields.io/badge/State-grey)          | Terraform State | Stores current infra state mapping to real cloud.      |
| ![](https://img.shields.io/badge/Backend-purple)      | Backend         | Where Terraform state is stored (local or remote).     |

---

# **2️⃣ Terraform Files & Structure** ![](https://img.shields.io/badge/Category-FileStructure-teal)

| Badge                                                        | Concept          | Definition                            |
| ------------------------------------------------------------ | ---------------- | ------------------------------------- |
| ![](https://img.shields.io/badge/main.tf-blue)               | main.tf          | Core resource configuration file.     |
| ![](https://img.shields.io/badge/variables.tf-green)         | variables.tf     | Contains all input variables.         |
| ![](https://img.shields.io/badge/outputs.tf-yellow)          | outputs.tf       | Stores output values after apply.     |
| ![](https://img.shields.io/badge/provider.tf-orange)         | provider.tf      | Defines cloud provider configuration. |
| ![](https://img.shields.io/badge/terraform.tfvars-lightgrey) | terraform.tfvars | Actual variable values.               |
| ![](https://img.shields.io/badge/modules%2F-purple)          | modules/         | Reusable folder for module code.      |

---

# **3️⃣ Terraform Commands** ![](https://img.shields.io/badge/Category-Commands-brightgreen)

| Badge                                             | Concept            | Definition                                  |
| ------------------------------------------------- | ------------------ | ------------------------------------------- |
| ![](https://img.shields.io/badge/init-blue)       | terraform init     | Initializes Terraform, downloads providers. |
| ![](https://img.shields.io/badge/plan-lightblue)  | terraform plan     | Shows changes before applying.              |
| ![](https://img.shields.io/badge/apply-green)     | terraform apply    | Creates/updates infrastructure.             |
| ![](https://img.shields.io/badge/destroy-red)     | terraform destroy  | Deletes all managed resources.              |
| ![](https://img.shields.io/badge/fmt-yellow)      | terraform fmt      | Auto-formats Terraform code.                |
| ![](https://img.shields.io/badge/validate-purple) | terraform validate | Validates syntax and configuration.         |

---

# **4️⃣ Variables & Expressions** ![](https://img.shields.io/badge/Category-Variables-orange)

| Badge                                                   | Concept            | Definition                                       |
| ------------------------------------------------------- | ------------------ | ------------------------------------------------ |
| ![](https://img.shields.io/badge/Input--Variable-green) | Input Variables    | Dynamic values provided by user.                 |
| ![](https://img.shields.io/badge/Local--Values-blue)    | Locals             | Intermediate values for readability.             |
| ![](https://img.shields.io/badge/Output-yellow)         | Output             | Values displayed after deployment.               |
| ![](https://img.shields.io/badge/Ternary-orange)        | Ternary Expression | Conditional operator `condition ? true : false`. |
| ![](https://img.shields.io/badge/Count-purple)          | count              | Creates multiple resources using index.          |
| ![](https://img.shields.io/badge/For--Each-red)         | for_each           | Creates resources from a map or set.             |

---

# **5️⃣ Terraform Modules** ![](https://img.shields.io/badge/Category-Modules-blueviolet)

| Badge                                                  | Concept                   | Definition                                 |
| ------------------------------------------------------ | ------------------------- | ------------------------------------------ |
| ![](https://img.shields.io/badge/Module-blue)          | Module                    | Reusable block of Terraform configuration. |
| ![](https://img.shields.io/badge/Public--Module-green) | Terraform Registry Module | Community modules from registry.           |
| ![](https://img.shields.io/badge/Child--Module-orange) | Child Module              | Module referenced within root module.      |
| ![](https://img.shields.io/badge/Root--Module-red)     | Root Module               | Main folder where Terraform runs.          |

---

# **6️⃣ Terraform State** ![](https://img.shields.io/badge/Category-State-grey)

| Badge                                                   | Concept              | Definition                                     |
| ------------------------------------------------------- | -------------------- | ---------------------------------------------- |
| ![](https://img.shields.io/badge/state--file-grey)      | terraform.tfstate    | Local state file storing infra details.        |
| ![](https://img.shields.io/badge/Remote--State-blue)    | Remote State         | Store state in S3, GCS, Azure Blob, etc.       |
| ![](https://img.shields.io/badge/State--Locking-orange) | State Locking        | Prevents parallel changes using DynamoDB, etc. |
| ![](https://img.shields.io/badge/Refresh--State-green)  | terraform refresh    | Syncs state with real cloud resources.         |
| ![](https://img.shields.io/badge/State--Show-yellow)    | terraform state show | Displays attributes of a resource.             |

---

# **7️⃣ Terraform Backends** ![](https://img.shields.io/badge/Category-Backends-blue)

| Badge                                                      | Concept            | Definition                              |
| ---------------------------------------------------------- | ------------------ | --------------------------------------- |
| ![](https://img.shields.io/badge/Local--Backend-lightgrey) | Local Backend      | Stores state on local machine.          |
| ![](https://img.shields.io/badge/S3--Backend-orange)       | S3 Backend         | Stores state in AWS S3 bucket.          |
| ![](https://img.shields.io/badge/GCS--Backend-yellow)      | GCS Backend        | Stores state in Google Cloud Storage.   |
| ![](https://img.shields.io/badge/Azure--Blob-blue)         | Azure Blob Backend | Stores state in Azure Blob Storage.     |
| ![](https://img.shields.io/badge/Consul-green)             | Consul Backend     | Stores state in Consul key-value store. |

---

# **8️⃣ Provisioners** ![](https://img.shields.io/badge/Category-Provisioners-red)

| Badge                                                   | Concept          | Definition                                           |
| ------------------------------------------------------- | ---------------- | ---------------------------------------------------- |
| ![](https://img.shields.io/badge/Local--Exec-blue)      | local-exec       | Runs local machine commands after resource creation. |
| ![](https://img.shields.io/badge/Remote--Exec-green)    | remote-exec      | Executes commands on remote machines.                |
| ![](https://img.shields.io/badge/File-yellow)           | file Provisioner | Copies files to remote hosts.                        |
| ![](https://img.shields.io/badge/Null--Resource-orange) | null_resource    | Resource used for triggers or provisioners.          |

---

# **9️⃣ Terraform Functions** ![](https://img.shields.io/badge/Category-Functions-purple)

| Badge                                                | Concept    | Definition                              |
| ---------------------------------------------------- | ---------- | --------------------------------------- |
| ![](https://img.shields.io/badge/lookup-blue)        | lookup()   | Get value from map with default.        |
| ![](https://img.shields.io/badge/join-green)         | join()     | Join list of strings using separator.   |
| ![](https://img.shields.io/badge/split-yellow)       | split()    | Split a string into list.               |
| ![](https://img.shields.io/badge/length-orange)      | length()   | Returns number of items in list/string. |
| ![](https://img.shields.io/badge/format-red)         | format()   | Format strings dynamically.             |
| ![](https://img.shields.io/badge/coalesce-lightgrey) | coalesce() | Returns first non-null argument.        |

---

# 🔟 **Terraform Cloud & Enterprise** ![](https://img.shields.io/badge/Category-Cloud-lightblue)

| Badge                                                      | Concept              | Definition                                              |
| ---------------------------------------------------------- | -------------------- | ------------------------------------------------------- |
| ![](https://img.shields.io/badge/Terraform-Cloud-green)    | Terraform Cloud      | HashiCorp hosted service for remote state & automation. |
| ![](https://img.shields.io/badge/Terraform-Enterprise-red) | Terraform Enterprise | Self-hosted enterprise version with governance.         |
| ![](https://img.shields.io/badge/Workspaces-blue)          | Workspace            | Multiple states for same configuration.                 |
| ![](https://img.shields.io/badge/Run--Tasks-orange)        | Run Tasks            | Integrates with security/scanning tools.                |


