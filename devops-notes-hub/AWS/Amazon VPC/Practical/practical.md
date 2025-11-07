# 🌐 AWS VPC Practical Learning Guide

## 🟢 10 Beginner-Level Practicals — Core VPC Concepts

These practicals help you understand **fundamental AWS networking** concepts — subnets, routing, internet access, and security.

| No. | Practical                             | Description                                                                                                       |
| --- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 1️⃣ | **Create a Custom VPC**               | Create a new VPC with a specific CIDR block (e.g., 10.0.0.0/16) using AWS Console. Understand default components. |
| 2️⃣ | **Create Public and Private Subnets** | Add one public and one private subnet in different Availability Zones. Learn about subnet CIDR allocation.        |
| 3️⃣ | **Attach an Internet Gateway (IGW)**  | Attach an Internet Gateway to your VPC and associate it with the route table for the public subnet.               |
| 4️⃣ | **Configure Route Tables**            | Create and associate route tables to control traffic between subnets and the Internet.                            |
| 5️⃣ | **Launch EC2 Instances in Subnets**   | Launch EC2 in public and private subnets and test connectivity. Use key pair SSH to access public EC2 only.       |
| 6️⃣ | **Set Up Security Groups**            | Create Security Groups allowing SSH and HTTP traffic. Attach them to EC2 instances.                               |
| 7️⃣ | **Use Network ACLs (NACLs)**          | Configure a Network ACL to restrict traffic to/from specific IPs. Test by modifying rules.                        |
| 8️⃣ | **Elastic IP and NAT Overview**       | Allocate an Elastic IP and understand how NAT devices enable internet access for private subnets.                 |
| 9️⃣ | **DNS and DHCP Options**              | Explore DNS resolution inside VPC and customize DHCP options (domain name, DNS servers).                          |
| 🔟  | **VPC Peering Basics**                | Create VPC Peering between two VPCs and test ping between instances.                                              |

---

## 🟡 10 Intermediate-Level Practicals — Real-World Scenarios

These exercises cover **VPC connectivity, hybrid networking, and routing**, giving you an edge in real DevOps and Cloud Architect setups.

| No. | Practical                                        | Description                                                                                      |
| --- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| 1️⃣ | **VPC with NAT Gateway**                         | Create a NAT Gateway in the public subnet to allow private EC2s to access the internet.          |
| 2️⃣ | **VPC Flow Logs Setup**                          | Enable VPC Flow Logs and analyze network traffic logs in CloudWatch or S3.                       |
| 3️⃣ | **Multiple Public & Private Subnets (Multi-AZ)** | Build a high-availability VPC setup with 2 public and 2 private subnets across AZs.              |
| 4️⃣ | **Private Subnet Access via Bastion Host**       | Launch a Bastion Host in public subnet and use it to SSH into private EC2.                       |
| 5️⃣ | **VPC Peering Across Regions**                   | Connect VPCs across regions and verify inter-region connectivity.                                |
| 6️⃣ | **Route Table Troubleshooting**                  | Intentionally misconfigure a route and fix connectivity issues using Flow Logs and route tables. |
| 7️⃣ | **VPC Endpoints (S3 & DynamoDB)**                | Create VPC endpoints to connect privately to AWS services without using the internet.            |
| 8️⃣ | **Custom Network ACLs for Security Layers**      | Create restrictive NACLs to allow only specific ports and IPs, and analyze access results.       |
| 9️⃣ | **Elastic Load Balancer in VPC**                 | Deploy an Application Load Balancer (ALB) in public subnets pointing to private EC2 targets.     |
| 🔟  | **VPC Automation with AWS CLI**                  | Create a full VPC (VPC, subnets, route tables, IGW) using AWS CLI commands.                      |

---

## 🔴 10 Advanced-Level Practicals — Production & DevOps Use Cases

These simulate **real-world VPC architectures** — covering hybrid networks, security automation, and scalable production systems.

| No. | Practical                                                  | Description                                                                                     |
| --- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 1️⃣ | **VPC Creation with Terraform**                            | Write Terraform code to provision a complete VPC setup (subnets, NAT, routes, IGW, NACLs).      |
| 2️⃣ | **PrivateLink Setup for Service Access**                   | Create an AWS PrivateLink endpoint for secure access to services (e.g., S3 or custom app).      |
| 3️⃣ | **Transit Gateway Setup for Multi-VPC Architecture**       | Connect 3+ VPCs using AWS Transit Gateway and configure centralized routing.                    |
| 4️⃣ | **Hybrid Connectivity via VPN**                            | Create a Site-to-Site VPN connection between your AWS VPC and on-premises network (simulated).  |
| 5️⃣ | **Direct Connect Overview**                                | Understand and simulate AWS Direct Connect architecture for high-speed private connectivity.    |
| 6️⃣ | **VPC Security Automation (Lambda)**                       | Use Lambda to automatically modify NACLs or Security Groups based on CloudWatch triggers.       |
| 7️⃣ | **Multi-Account VPC Peering**                              | Set up VPC peering between two AWS accounts securely with proper routing.                       |
| 8️⃣ | **Centralized Logging with Flow Logs + S3 + Athena**       | Send all VPC Flow Logs to S3, then query using Athena for network analytics.                    |
| 9️⃣ | **VPC Cost Optimization & CIDR Planning**                  | Design CIDR allocation for multi-environment (Dev, Staging, Prod) VPCs efficiently.             |
| 🔟  | **Highly Available 3-Tier Architecture (VPC + ALB + RDS)** | Deploy a full production-grade setup: Web Tier (public), App Tier (private), DB Tier (private). |

---

## 🧠 Bonus Tips

* 🧩 **Always Use Separate Subnets:** Keep web, app, and DB layers isolated.
* 🧰 **Enable Flow Logs:** Essential for debugging network issues.
* 🔐 **Use IAM Roles & Security Groups:** Never open 0.0.0.0/0 unnecessarily.
* 🧭 **Document CIDR Plans:** Helps prevent overlapping ranges across environments.
* ⚙️ **Automate Everything:** Use Terraform or CloudFormation for repeatable VPC creation.
* ☁️ **Simulate Production:** Use multi-AZ setups even in learning environments.

---

## 📚 References

* [AWS VPC Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
* [AWS VPC Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-best-practices.html)
* [AWS Transit Gateway Docs](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
* [Terraform AWS VPC Module](https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/latest)
* [AWS CLI VPC Commands](https://docs.aws.amazon.com/cli/latest/reference/ec2/)
