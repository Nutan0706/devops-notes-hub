## 🎯 Practical Task: **Integrate Terraform with Jenkins**

**Key Focus / Concept:**  
Automate **Terraform plan and apply** operations using a **Jenkins CI/CD pipeline**, enabling continuous infrastructure deployment and reducing manual intervention.

---

## 🪜 Step-by-Step Implementation

### **Goal**

✅ Configure Jenkins to:
1. Clone Terraform code from GitHub  
2. Initialize Terraform  
3. Run `terraform plan` and `terraform apply`  
4. Manage credentials securely using Jenkins credentials store  
5. Automate infrastructure provisioning with every commit

---

## 🌍 Part 1 — Terraform Configuration

### **Step 1 — Create Working Directory**

```bash
mkdir terraform-jenkins-integration
cd terraform-jenkins-integration
```

---

### **Step 2 — Create Terraform Code**

#### File: `main.tf`

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "jenkins_demo_ec2" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = var.key_name

  tags = {
    Name = "Terraform-Jenkins-Demo"
    Environment = var.environment
  }
}
```

#### File: `variables.tf`

```hcl
variable "key_name" {
  description = "AWS key pair name"
  type        = string
  default     = "terraform-key"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}
```

#### File: `outputs.tf`

```hcl
output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.jenkins_demo_ec2.public_ip
}
```

✅ Push this Terraform code to your GitHub repository.
Example:

```
https://github.com/<your-username>/terraform-jenkins-demo.git
```

---

## 🤖 Part 2 — Jenkins Configuration

### **Step 3 — Install Jenkins (if not installed)**

#### On Ubuntu EC2 (recommended)

```bash
sudo apt update -y
sudo apt install openjdk-17-jdk -y
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update -y
sudo apt install jenkins -y
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

Access Jenkins at:

```
http://<jenkins-server-ip>:8080
```

---

### **Step 4 — Install Required Plugins**

Go to:
**Manage Jenkins → Plugins → Available Plugins**

Install the following:

* 🧩 **Git Plugin**
* ⚙️ **Pipeline Plugin**
* ☁️ **Terraform Plugin** (optional, but recommended)
* 🔐 **Credentials Binding Plugin**

---

### **Step 5 — Configure AWS Credentials in Jenkins**

1. Go to **Manage Jenkins → Credentials → System → Global Credentials (unrestricted)**
2. Click **Add Credentials**
3. Choose **Kind: AWS Credentials**
4. Enter:

   * **Access Key ID** → `<your-aws-access-key>`
   * **Secret Access Key** → `<your-aws-secret-key>`
   * **ID** → `aws_creds`
   * **Description** → `AWS credentials for Terraform`

✅ Jenkins now securely stores your AWS credentials for pipeline use.

---

### **Step 6 — Create Jenkins Pipeline Job**

1. Go to **Jenkins Dashboard → New Item**
2. Enter job name → `terraform-jenkins-pipeline`
3. Select **Pipeline** → Click **OK**

---

## 🚀 Part 3 — Jenkins Pipeline Setup

### **Step 7 — Write Jenkinsfile**

#### File: `Jenkinsfile`

```groovy
pipeline {
    agent any

    environment {
        AWS_CREDS = credentials('aws_creds')
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning Terraform project from GitHub..."
                git branch: 'main', url: 'https://github.com/<your-username>/terraform-jenkins-demo.git'
            }
        }

        stage('Init') {
            steps {
                echo "Initializing Terraform..."
                sh '''
                terraform init
                '''
            }
        }

        stage('Validate') {
            steps {
                echo "Validating Terraform configuration..."
                sh 'terraform validate'
            }
        }

        stage('Plan') {
            steps {
                echo "Running Terraform Plan..."
                sh '''
                export AWS_ACCESS_KEY_ID=${AWS_CREDS_USR}
                export AWS_SECRET_ACCESS_KEY=${AWS_CREDS_PSW}
                terraform plan -out=tfplan
                '''
            }
        }

        stage('Apply') {
            when {
                expression { return params.APPLY_INFRA }
            }
            steps {
                echo "Applying Terraform configuration..."
                sh '''
                export AWS_ACCESS_KEY_ID=${AWS_CREDS_USR}
                export AWS_SECRET_ACCESS_KEY=${AWS_CREDS_PSW}
                terraform apply -auto-approve tfplan
                '''
            }
        }

        stage('Output') {
            steps {
                echo "Fetching Outputs..."
                sh 'terraform output'
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed."
        }
    }
}
```

---

### **Step 8 — Add Pipeline Parameters (Optional)**

To control deployments manually:

In Jenkins UI:

1. Open Job → Click **Configure**
2. Under **Pipeline → This project is parameterized**
3. Add **Boolean Parameter**

   * Name: `APPLY_INFRA`
   * Default: `false`
   * Description: "Check this to apply Terraform infrastructure"

✅ Now, you can run **only plan** or **plan + apply** as needed.

---

### **Step 9 — Configure Jenkins Environment**

In Jenkins UI:

1. Go to **Manage Jenkins → Global Tool Configuration**
2. Under **Terraform**, click **Add Terraform**

   * Name: `terraform`
   * Install automatically: ✅ Checked

Alternatively, install manually on Jenkins server:

```bash
sudo apt-get install unzip -y
wget https://releases.hashicorp.com/terraform/1.7.0/terraform_1.7.0_linux_amd64.zip
sudo unzip terraform_1.7.0_linux_amd64.zip -d /usr/local/bin/
terraform -version
```

---

## 🧩 Part 4 — Pipeline Execution

### **Step 10 — Run the Pipeline**

1. Go to Jenkins Dashboard → Select job → Click **Build with Parameters**
2. Keep `APPLY_INFRA` unchecked to just test `plan`
3. Check `APPLY_INFRA` for full deployment

✅ Example Pipeline Flow:

```
[Checkout] → [Init] → [Validate] → [Plan] → [Apply] → [Output]
```

---

### **Step 11 — Verify in AWS Console**

Go to:

* **EC2 → Instances**
* Check for instance: `Terraform-Jenkins-Demo`

✅ Tags:

```
Name = Terraform-Jenkins-Demo
Environment = dev
```

Or verify via CLI:

```bash
aws ec2 describe-instances --filters "Name=tag:Name,Values=Terraform-Jenkins-Demo" \
--query "Reservations[*].Instances[*].PublicIpAddress"
```

---

### **Step 12 — Clean Up Resources**

In Jenkins, create a destroy stage or run manually:

```bash
terraform destroy -auto-approve
```

To automate in pipeline, add a **"Destroy"** stage at the end:

```groovy
stage('Destroy') {
    when {
        expression { return params.DESTROY_INFRA }
    }
    steps {
        echo "Destroying Terraform resources..."
        sh '''
        export AWS_ACCESS_KEY_ID=${AWS_CREDS_USR}
        export AWS_SECRET_ACCESS_KEY=${AWS_CREDS_PSW}
        terraform destroy -auto-approve
        '''
    }
}
```

Then add another boolean parameter:
`DESTROY_INFRA` → default `false`

---

## 🧠 Key Concepts Learned

| Concept                            | Description                                                                |
| ---------------------------------- | -------------------------------------------------------------------------- |
| **Terraform Automation**           | Using Jenkins to automatically run Terraform commands (init, plan, apply). |
| **Pipeline as Code (Jenkinsfile)** | Defines CI/CD flow in code format for version control.                     |
| **AWS Credentials Binding**        | Securely inject AWS keys using Jenkins credentials plugin.                 |
| **Terraform Plan/Apply Stages**    | Separate planning from applying for safer deployments.                     |
| **Conditional Parameters**         | Allows manual control of infrastructure changes in Jenkins.                |

---

## 🧾 Summary

| Step | Task                      | Command / Action                                |
| ---- | ------------------------- | ----------------------------------------------- |
| 1    | Setup Jenkins & Terraform | Install both on server                          |
| 2    | Add AWS Credentials       | Jenkins → Credentials → Add AWS                 |
| 3    | Clone GitHub Repo         | `git branch: 'main'` in Jenkinsfile             |
| 4    | Create Jenkinsfile        | Define stages (init, plan, apply)               |
| 5    | Run Pipeline              | Jenkins → Build with Parameters                 |
| 6    | Verify EC2                | AWS Console or CLI                              |
| 7    | Destroy Resources         | Add Destroy stage or manual `terraform destroy` |

---
