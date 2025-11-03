## 🎯 Practical Task: **Integrate Terraform with Jenkins**

**Key Focus / Concept:**  
Automate **Terraform Plan** and **Apply** operations using a **Jenkins CI/CD pipeline** — enabling infrastructure provisioning through version-controlled, repeatable, and auditable workflows.

---

## 🪜 Step-by-Step Implementation

### **Step 1 — Prerequisites**

Before starting:
- Jenkins server is installed and running  
- Terraform is installed on the Jenkins node  
- AWS CLI and credentials are configured on Jenkins  
- Git repository contains your Terraform code (e.g., `main.tf`, `variables.tf`, etc.)

---

### **Step 2 — Install Required Plugins in Jenkins**

Navigate to **Manage Jenkins → Plugins → Available Plugins** and install:

✅ **Plugins to Install:**
- **Terraform Plugin**
- **Pipeline Plugin**
- **Git Plugin**
- **Credentials Binding Plugin**

Once installed, restart Jenkins.

---

### **Step 3 — Configure AWS Credentials in Jenkins**

1. Go to **Manage Jenkins → Credentials → Global → Add Credentials**  
2. Select **Kind: AWS Credentials**  
3. Enter your:
   - **Access Key ID**
   - **Secret Access Key**
4. Add an ID like:  
```

aws-terraform-creds

```

---

### **Step 4 — Prepare Terraform Code in GitHub**

Your Git repository structure should look like:

```

terraform-jenkins-demo/
├── main.tf
├── variables.tf
├── outputs.tf
└── Jenkinsfile

````

Example `main.tf`:

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "jenkins_demo_bucket" {
  bucket = "terraform-jenkins-demo-bucket-12345"
  acl    = "private"

  tags = {
    Name        = "Terraform-Jenkins-Demo"
    Environment = "CI-CD"
  }
}
````

---

### **Step 5 — Create a Jenkinsfile**

Create a **`Jenkinsfile`** in your repo root to define the Terraform pipeline.

```groovy
pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
        TF_WORKSPACE = 'default'
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo '📦 Checking out code from Git...'
                git branch: 'main', url: 'https://github.com/your-username/terraform-jenkins-demo.git'
            }
        }

        stage('Setup Terraform') {
            steps {
                echo '⚙️ Initializing Terraform...'
                sh 'terraform init'
            }
        }

        stage('Validate Terraform') {
            steps {
                echo '✅ Validating Terraform configuration...'
                sh 'terraform validate'
            }
        }

        stage('Plan Infrastructure') {
            steps {
                echo '🧠 Generating Terraform plan...'
                sh 'terraform plan -out=tfplan'
            }
        }

        stage('Approval for Apply') {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    input message: 'Approve Terraform Apply?', ok: 'Apply Now'
                }
            }
        }

        stage('Apply Infrastructure') {
            steps {
                echo '🚀 Applying Terraform changes...'
                sh 'terraform apply -auto-approve tfplan'
            }
        }

        stage('Post Apply') {
            steps {
                echo '🧾 Terraform Apply Completed Successfully!'
                sh 'terraform output'
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning workspace...'
            deleteDir()
        }
    }
}
```

---

### **Step 6 — Create a New Jenkins Pipeline Job**

1. Go to **Jenkins Dashboard → New Item → Pipeline**
2. Enter name: `Terraform-CI-CD`
3. Choose **Pipeline**
4. Under **Pipeline → Definition**, select:

   * **Pipeline script from SCM**
   * **SCM: Git**
   * Enter your **repository URL**
   * Branch: `main`
5. Save the configuration.

---

### **Step 7 — Trigger the Pipeline**

Now click **“Build Now”** on your Jenkins job.
Jenkins will automatically:

1. Clone your repo
2. Initialize Terraform
3. Validate configuration
4. Generate a plan
5. Wait for manual approval
6. Apply changes on approval

✅ Example Console Output:

```
[Checkout Code] Checking out code from Git...
[Setup Terraform] Initializing the backend...
Terraform has been successfully initialized!
[Validate Terraform] Success! The configuration is valid.
[Plan Infrastructure] Plan: 1 to add, 0 to change, 0 to destroy.
[Approval for Apply] Waiting for manual confirmation...
[Apply Infrastructure] Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

---

### **Step 8 — Verify in AWS Console**

Go to:

* **S3 → Buckets**
  Check for the newly created bucket:

  ```
  terraform-jenkins-demo-bucket-12345
  ```

Or verify via CLI:

```bash
aws s3 ls | grep terraform-jenkins-demo-bucket
```

✅ Output:

```
2025-10-31 12:34:56 terraform-jenkins-demo-bucket-12345
```

---

### **Step 9 — Optional Enhancements**

#### ✅ Add Backend Configuration

You can configure **remote backend** (S3 + DynamoDB) for shared state management.

#### ✅ Add Terraform Workspace Support

```groovy
sh 'terraform workspace select dev || terraform workspace new dev'
```

#### ✅ Add Notifications (Slack/Email)

Integrate Jenkins post-build steps for alerts after successful Terraform apply.

---

### **Step 10 — Destroy Infrastructure (CI/CD Controlled)**

Add a manual cleanup stage in Jenkins for environment destruction.

```groovy
stage('Destroy Infrastructure') {
    steps {
        input message: 'Confirm Destroy?', ok: 'Destroy Now'
        sh 'terraform destroy -auto-approve'
    }
}
```

---

## 🧠 Key Concepts Learned

| Concept                                   | Description                                                                         |
| ----------------------------------------- | ----------------------------------------------------------------------------------- |
| **Terraform Automation**                  | Running `terraform plan` and `apply` automatically through Jenkins.                 |
| **Infrastructure as Code (IaC) Pipeline** | Ensures infrastructure is tested and deployed through version-controlled pipelines. |
| **Manual Approval**                       | Prevents accidental deployment with Jenkins `input` step.                           |
| **Terraform Plugin in Jenkins**           | Simplifies Terraform integration with Jenkins jobs.                                 |
| **Environment Variables**                 | Manage AWS region, workspace, and credentials dynamically.                          |

---

## 🧾 Summary

| Step | Task                      | Command / Action                    |
| ---- | ------------------------- | ----------------------------------- |
| 1    | Install Plugins           | Terraform, Git, Pipeline            |
| 2    | Configure AWS Credentials | `aws-terraform-creds`               |
| 3    | Create Jenkinsfile        | Define CI/CD stages                 |
| 4    | Create Jenkins Job        | Type: Pipeline (SCM)                |
| 5    | Run Pipeline              | Auto Terraform Init → Plan → Apply  |
| 6    | Verify AWS Resource       | Check S3 bucket                     |
| 7    | Destroy Infrastructure    | Manual stage or `terraform destroy` |


Would you like me to continue with **Advanced Practical #9 — Implement Terraform Workspaces (Dev, Stage, Prod Environments)** next in the same `.md` format?
```
