# 🚀 AWS EC2 Practical Learning Guide

## 🟢 10 Beginner-Level Practicals — Core EC2 Concepts

These exercises cover the **foundational concepts** of EC2 — perfect for beginners or those revising basics.

| No. | Practical                                | Description                                                                                                       |
| --- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 1️⃣ | **Launch Your First EC2 Instance**       | Launch an EC2 instance using AWS Console (Amazon Linux 2). Configure key pair, security group, and instance type. |
| 2️⃣ | **Connect via SSH**                      | Use SSH to connect to your EC2 instance from your local machine (Windows → PuTTY or Linux/Mac → terminal).        |
| 3️⃣ | **Explore EC2 Dashboard**                | Understand EC2 dashboard components: Instances, AMIs, Volumes, Security Groups, Elastic IPs, and Key Pairs.       |
| 4️⃣ | **Create and Attach EBS Volume**         | Create a new Elastic Block Store (EBS) volume and attach it to your running EC2 instance. Format and mount it.    |
| 5️⃣ | **Understand Security Groups**           | Create a custom Security Group allowing SSH (22), HTTP (80), and HTTPS (443). Test connectivity rules.            |
| 6️⃣ | **Elastic IP Allocation**                | Allocate and associate an Elastic IP to your EC2 instance. Verify access via browser/terminal.                    |
| 7️⃣ | **AMI Creation**                         | Create a custom Amazon Machine Image (AMI) from your running instance and launch another instance using that AMI. |
| 8️⃣ | **Start, Stop, and Terminate Instances** | Practice state changes and understand pricing implications of each state.                                         |
| 9️⃣ | **EC2 Metadata & User Data**             | Retrieve EC2 instance metadata and add simple User Data script to install Apache at launch.                       |
| 🔟  | **Tagging and Naming Resources**         | Add tags (Key=Environment, Value=Dev) to your instance and understand tagging best practices.                     |

---

## 🟡 10 Intermediate-Level Practicals — Real-World Scenarios

These exercises help you explore **automation, scaling, and networking** concepts commonly used in real-world DevOps environments.

| No. | Practical                                    | Description                                                                                                             |
| --- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 1️⃣ | **Launch EC2 using AWS CLI**                 | Use the AWS CLI to launch, describe, and terminate EC2 instances programmatically.                                      |
| 2️⃣ | **EC2 with Load Balancer (ALB)**             | Launch two EC2 instances, install Nginx, and configure an **Application Load Balancer (ALB)** for traffic distribution. |
| 3️⃣ | **EC2 Auto Scaling Group (ASG)**             | Create an ASG that scales out/in based on CPU utilization using CloudWatch metrics.                                     |
| 4️⃣ | **Launch Template and Launch Configuration** | Create Launch Templates to standardize instance configurations.                                                         |
| 5️⃣ | **User Data for App Deployment**             | Automate web app deployment using User Data (e.g., deploy a Flask app on startup).                                      |
| 6️⃣ | **Elastic Network Interface (ENI)**          | Create and attach multiple network interfaces to an instance and test network routing.                                  |
| 7️⃣ | **IAM Role for EC2**                         | Attach an IAM role that allows EC2 to access S3. Test with AWS CLI (e.g., `aws s3 ls`).                                 |
| 8️⃣ | **EC2 Monitoring with CloudWatch**           | Enable detailed monitoring and create custom CPU utilization alarms.                                                    |
| 9️⃣ | **EC2 Snapshots & Restore**                  | Create an EBS snapshot, delete volume, and restore it from the snapshot.                                                |
| 🔟  | **EC2 Instance Connect & Session Manager**   | Access your EC2 instance securely without SSH using Systems Manager Session Manager.                                    |

---

## 🔴 10 Advanced-Level Practicals — Production & DevOps Use Cases

These tasks simulate **real production-grade scenarios** — involving automation, infrastructure as code (IaC), and performance optimization.

| No. | Practical                                    | Description                                                                                 |
| --- | -------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 1️⃣ | **Launch EC2 using Terraform**               | Write a Terraform configuration to provision EC2, Security Groups, and EBS volumes.         |
| 2️⃣ | **EC2 with Ansible Provisioning**            | Use Ansible to install software and configure EC2 instances post-launch.                    |
| 3️⃣ | **EC2 with Jenkins Deployment**              | Automate app deployment to EC2 using Jenkins CI/CD pipeline.                                |
| 4️⃣ | **EC2 in a Private Subnet**                  | Launch an instance inside a private subnet and connect via a Bastion Host.                  |
| 5️⃣ | **Custom AMI Pipeline**                      | Automate custom AMI creation using Packer and deploy through Terraform.                     |
| 6️⃣ | **Spot vs On-Demand Cost Optimization**      | Compare performance and cost savings of Spot vs On-Demand EC2 instances.                    |
| 7️⃣ | **EC2 Backup Automation**                    | Write a Python or Bash script using AWS CLI to schedule EBS snapshots and cleanup old ones. |
| 8️⃣ | **High Availability Setup**                  | Deploy multi-AZ web servers behind a load balancer with health checks.                      |
| 9️⃣ | **EC2 CloudWatch Logs & Alarms Integration** | Forward EC2 logs to CloudWatch Logs and trigger alarms based on error thresholds.           |
| 🔟  | **EC2 + S3 + RDS Integration**               | Build a 3-tier architecture where EC2 (app) interacts with S3 (storage) and RDS (database). |

---

## 🧠 Bonus Tips

* 🏷️ **Tag Everything:** Helps with cost tracking and environment separation.
* 🧰 **Always Use IAM Roles** instead of hardcoding credentials.
* 🧼 **Clean Up Resources:** Stop/terminate unused instances to avoid charges.
* 🔐 **Use Security Groups wisely:** Allow only required ports and restrict IP ranges.
* ☁️ **Practice Automation:** Use CLI, Terraform, or Ansible instead of the AWS console for repetition.

---

## 📚 References

* [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
* [AWS CLI Commands for EC2](https://docs.aws.amazon.com/cli/latest/reference/ec2/)
* [Terraform AWS Provider Docs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
* [AWS Pricing Calculator](https://calculator.aws/)

