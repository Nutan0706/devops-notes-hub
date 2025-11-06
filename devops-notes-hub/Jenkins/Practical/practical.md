# 🚀 Jenkins Practical Learning Guide

## 🧩 Table of Contents

1. [Beginner-Level Practicals](#beginner-level-practicals)
2. [Intermediate-Level Practicals](#intermediate-level-practicals)
3. [Advanced-Level Practicals](#advanced-level-practicals)
4. [Bonus Tips](#bonus-tips)
5. [References](#references)

---

## 🟢 10 Beginner-Level Practicals — Core Jenkins Concepts

These exercises help you understand the **core functionality** of Jenkins, its UI, and how CI/CD basics work.

| No. | Practical                                    | Description                                                                                                  |
| --- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 1️⃣ | **Install Jenkins on Local Machine / EC2**   | Install Jenkins on Ubuntu or EC2 using `apt` and start the Jenkins service. Verify web access via port 8080. |
| 2️⃣ | **Explore Jenkins Dashboard**                | Get familiar with Jenkins dashboard — understand Jobs, Build History, Nodes, Plugins, and System Config.     |
| 3️⃣ | **Create Your First Freestyle Project**      | Create a basic freestyle job that prints “Hello Jenkins” and executes a shell command.                       |
| 4️⃣ | **Integrate Git with Jenkins**               | Connect Jenkins with GitHub or Bitbucket. Create a job that clones a repo and prints files.                  |
| 5️⃣ | **Trigger Builds Automatically (Poll SCM)**  | Configure Jenkins to trigger a build when code changes are pushed to GitHub using webhook or Poll SCM.       |
| 6️⃣ | **Archive Build Artifacts**                  | Store build outputs (e.g., .jar or .zip) as artifacts and download them from Jenkins UI.                     |
| 7️⃣ | **Install and Manage Plugins**               | Install popular plugins like Git, Pipeline, Blue Ocean, Docker, and Credentials Binding.                     |
| 8️⃣ | **Create Jenkins User and Roles**            | Set up Jenkins users and assign roles using “Role-Based Access Control” plugin.                              |
| 9️⃣ | **Email Notifications**                      | Configure SMTP and send build success/failure notifications automatically.                                   |
| 🔟  | **Backup and Restore Jenkins Configuration** | Backup Jenkins home directory and restore it to a new instance.                                              |

---

## 🟡 10 Intermediate-Level Practicals — Real-World Scenarios

These practicals will help you understand **pipelines, environment setup, agents**, and **automated deployments**.

| No. | Practical                                   | Description                                                                                       |
| --- | ------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 1️⃣ | **Create a Simple Pipeline (Jenkinsfile)**  | Write a Jenkinsfile with `pipeline { agent any; stages { stage('Build'){...} } }` and run it.     |
| 2️⃣ | **Parameterized Builds**                    | Create a job with parameters (string, choice) and use them inside your Jenkinsfile.               |
| 3️⃣ | **Use Environment Variables**               | Access and print environment variables (`env.BUILD_ID`, `env.JOB_NAME`) in pipeline logs.         |
| 4️⃣ | **Integrate Jenkins with Docker**           | Install Docker on the Jenkins host and build a Docker image from source code during pipeline run. |
| 5️⃣ | **Set Up Jenkins Agents (Slave Nodes)**     | Connect a Linux node as an agent and execute specific jobs on that node.                          |
| 6️⃣ | **Pipeline with Multiple Stages**           | Create a pipeline with Build, Test, and Deploy stages using declarative syntax.                   |
| 7️⃣ | **Integrate Jenkins with Maven**            | Build a Java application using Maven goals (`clean install`) in Jenkins pipeline.                 |
| 8️⃣ | **Post-Build Actions (Test Reports)**       | Generate JUnit or Allure test reports and publish them in Jenkins dashboard.                      |
| 9️⃣ | **Integrate Jenkins with GitHub Webhooks**  | Configure GitHub webhook for instant build triggers on code push.                                 |
| 🔟  | **Secure Jenkins with Credentials Binding** | Store GitHub token, DockerHub credentials, and AWS keys using Jenkins credentials plugin.         |

---

## 🔴 10 Advanced-Level Practicals — Production & DevOps Use Cases

These simulate **real production environments** — integrating Jenkins with Kubernetes, AWS, Terraform, and CI/CD automation.

| No. | Practical                                              | Description                                                                                      |
| --- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| 1️⃣ | **Jenkins Declarative CI/CD Pipeline for Node.js App** | Build, test, and deploy a Node.js app with a full declarative Jenkinsfile.                       |
| 2️⃣ | **Blue Ocean Visualization**                           | Use the Blue Ocean plugin to visualize pipelines and parallel stages.                            |
| 3️⃣ | **Pipeline as Code with Shared Libraries**             | Create a shared library and use it in multiple pipelines for reusable functions.                 |
| 4️⃣ | **Jenkins + Docker + Kubernetes Integration**          | Build a Docker image and deploy it to a Kubernetes cluster using `kubectl`.                      |
| 5️⃣ | **Automate Infrastructure with Terraform**             | Run Terraform commands (`init`, `apply`, `destroy`) from Jenkins pipeline using AWS credentials. |
| 6️⃣ | **Jenkins + AWS S3 Deployment**                        | Upload build artifacts or website files directly to S3 from Jenkins pipeline.                    |
| 7️⃣ | **Jenkins CI/CD for Flask App on EC2**                 | Automate build → test → deploy pipeline for a Python Flask app to EC2 using SSH.                 |
| 8️⃣ | **Implement Jenkins Pipeline for Microservices**       | Use parallel stages to build and deploy multiple microservices concurrently.                     |
| 9️⃣ | **Monitor Jenkins with Prometheus & Grafana**          | Integrate Jenkins metrics endpoint with Prometheus and visualize via Grafana dashboard.          |
| 🔟  | **High Availability Jenkins Setup (Master + Agents)**  | Configure master-agent architecture using distributed builds and Jenkins HA best practices.      |

---

## 🧠 Bonus Tips

* 🧩 **Use Jenkinsfile Everywhere:** Always define pipelines as code.
* 🧰 **Integrate SCM + Docker + Kubernetes** for full CI/CD.
* 🔒 **Secure Jenkins:** Use HTTPS, RBAC, and credentials binding.
* 🧼 **Clean Up Old Builds:** Use build discard policy for better performance.
* ⚙️ **Automate Everything:** From testing to deployment — minimize manual triggers.
* ☁️ **Leverage Cloud Agents:** Use ephemeral agents on EC2 or Kubernetes for scalability.

---

## 📚 References

* [Jenkins Official Docs](https://www.jenkins.io/doc/)
* [Jenkins Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)
* [Jenkins Shared Libraries](https://www.jenkins.io/doc/book/pipeline/shared-libraries/)
* [Blue Ocean Plugin](https://www.jenkins.io/doc/book/blueocean/)
* [Jenkins + Docker Integration Guide](https://www.jenkins.io/doc/book/installing/docker/)
