# 🧠 AWS EC2 – Interview Questions (Beginner → Advanced)

This document contains **40+ AWS EC2 interview questions**, grouped by difficulty level:
✅ **Commonly Asked** • 🟦 **Moderate** • 🟨 **Advanced** • 🔥 **Scenario-Based**

---

## 🟩 10 Commonly Asked EC2 Interview Questions

1. **What is EC2 in AWS?**
   → EC2 stands for *Elastic Compute Cloud*, a web service that provides scalable virtual servers (instances) in the AWS Cloud.

2. **What is an AMI (Amazon Machine Image)?**
   → An AMI is a template that contains the operating system, software, and configurations needed to launch an EC2 instance.

3. **What is the difference between EBS and Instance Store?**
   → EBS is persistent block storage, while Instance Store is temporary and data is lost when stopped or terminated.

4. **What is a Security Group in EC2?**
   → A Security Group acts as a virtual firewall that controls inbound and outbound traffic to EC2 instances.

5. **What are EC2 instance types? Give examples.**
   → Instance types define CPU, memory, and storage resources (e.g., `t3.micro`, `m5.large`, `c6g.xlarge`).

6. **How do you connect to an EC2 instance using SSH?**
   → Use: `ssh -i <keypair.pem> ec2-user@<public-ip>`.

7. **What is an Elastic IP and why is it used?**
   → A static public IPv4 address for maintaining a consistent IP even after instance restarts.

8. **Difference between Stop, Terminate, and Reboot in EC2?**
   → Stop = Shutdown instance, data persists on EBS.
   Terminate = Delete instance + EBS (if delete-on-termination true).
   Reboot = Just restarts instance.

9. **What is User Data in EC2?**
   → A bootstrap script that runs once when the instance is launched (used for setup/configuration).

10. **What is an On-Demand Instance?**
    → Pay-per-use EC2 instance with no commitment — best for unpredictable workloads.

---

## 🟦 10 Moderate-Level EC2 Interview Questions

1. **Explain the pricing models of EC2.**
   → On-Demand, Reserved, Spot, Dedicated Host, and Savings Plans.

2. **What are Spot Instances and when should you use them?**
   → Low-cost instances that can be interrupted anytime — ideal for fault-tolerant jobs.

3. **What is an Auto Scaling Group (ASG)?**
   → A group of EC2 instances that automatically scale up or down based on demand.

4. **Difference between Security Group and NACL?**
   → SG = Stateful, instance-level; NACL = Stateless, subnet-level.

5. **What is a Placement Group? Explain its types.**

   * **Cluster:** Low-latency, same AZ.
   * **Spread:** Across multiple AZs for fault tolerance.
   * **Partition:** For large distributed workloads.

6. **Can we attach multiple ENIs to an EC2 instance?**
   → Yes, depending on the instance type; useful for multi-homed networking.

7. **What is a Launch Template vs Launch Configuration?**
   → Launch Templates support versioning and newer EC2 features; Launch Configs are legacy.

8. **What is EC2 Hibernate and how is it different from Stop?**
   → Hibernate saves RAM data to EBS and resumes state; Stop reboots from scratch.

9. **Explain EC2 instance lifecycle states.**
   → `pending → running → stopping → stopped → terminated`.

10. **How to take a backup of an EC2 instance?**
    → Create an **AMI** for full instance backup or **EBS snapshot** for volume-level backup.

---

## 🟨 10 Advanced EC2 Interview Questions

1. **How do you design a Highly Available EC2 architecture across Multi-AZ?**
   → Use **ASG + ELB + Multi-AZ deployment** for redundancy.

2. **How do Spot Fleet and Spot Blocks work?**
   → Spot Fleet manages multiple spot instances; Spot Block prevents termination for a fixed duration.

3. **How does Elastic Load Balancer integrate with EC2 Auto Scaling?**
   → ELB automatically registers/deregisters EC2 instances as they scale.

4. **Explain differences between M, T, C, R, P, and G instance families.**

   * **T:** Burstable
   * **M:** General-purpose
   * **C:** Compute-optimized
   * **R:** Memory-optimized
   * **P/G:** GPU/ML/AI optimized

5. **How do you secure EC2 instances in production?**
   → Use IAM roles, SGs, key pairs, private subnets, VPC endpoints, and encrypted EBS volumes.

6. **Explain ENI, ENA, and EFA and when to use each.**

   * **ENI:** Virtual network interface
   * **ENA:** Enhanced networking for higher performance
   * **EFA:** HPC and ML workloads with low latency

7. **What’s the difference between Vertical and Horizontal Scaling in EC2?**
   → Vertical = Bigger instance size; Horizontal = More instances.

8. **How does EC2 Capacity Reservations work?**
   → Reserve capacity in a specific AZ for critical workloads.

9. **What is the Nitro System in EC2?**
   → Next-gen hypervisor and hardware stack providing better performance and isolation.

10. **How do you troubleshoot EC2 performance issues (CPU, Network, Disk)?**
    → Use **CloudWatch metrics**, check **status checks**, and analyze **system logs** or **top/iostat/sar**.

---

## 🔥 10 Scenario-Based EC2 Interview Questions

| #  | Scenario                      | Question                                                                                          |
| -- | ----------------------------- | ------------------------------------------------------------------------------------------------- |
| 1  | 🚧 Sudden Traffic Spike       | Your website traffic increases 10×. How will you scale EC2 to handle the load?                    |
| 2  | 💸 High Billing               | EC2 costs spiked unexpectedly. How will you identify and optimize cost?                           |
| 3  | 🔐 Security Breach            | You suspect an EC2 instance is compromised. What steps will you take?                             |
| 4  | 💀 Instance Crashed           | A production EC2 instance terminated unexpectedly. How to ensure auto-recovery next time?         |
| 5  | 🧵 Long-Running Jobs          | You run Big Data workloads — which instance types should you choose and why?                      |
| 6  | 🌍 Multi-Region HA            | You want multi-region EC2 for DR — how will you configure it?                                     |
| 7  | 🗄️ Persistent Shared Storage | App requires shared storage for 5 EC2s — what would you choose (EFS, FSx, or S3) and why?         |
| 8  | 📡 Public App + Private DB    | Deploy a web app + DB on EC2 — describe subnet, SG, and VPC design.                               |
| 9  | ⏳ Slow Deployment             | EC2 takes 25+ mins to deploy — how will you optimize using AMIs or User Data?                     |
| 10 | 🕵️ Startup Failure           | EC2 boots but app fails — how will you debug? (Check logs, systemd, CloudWatch, User Data output) |

---

## 🧠 Quick Revision Hooks

| Concept             | Quick Recall                            |
| ------------------- | --------------------------------------- |
| **EC2**             | Elastic virtual server on AWS           |
| **AMI**             | Template for instance OS + config       |
| **ASG**             | Auto scaling group for dynamic capacity |
| **SG vs NACL**      | Instance vs Subnet firewall             |
| **EBS**             | Persistent storage                      |
| **Spot Instance**   | Cheapest, interruptible                 |
| **Nitro**           | Next-gen EC2 hardware platform          |
| **User Data**       | Boot-time automation script             |
| **Placement Group** | Control instance placement              |
| **EFA**             | Low-latency HPC network adapter         |

---

✅ **Final Tip:**
When preparing for EC2 interviews — focus on:

* **Architecture design** (ASG + ELB + Multi-AZ)
* **Security and cost optimization**
* **Troubleshooting performance issues**
* **Automation using CLI, SDK, or Terraform**
