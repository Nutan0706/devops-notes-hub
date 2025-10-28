# 🖥️ AWS EC2 – Complete Notes

Amazon **EC2 (Elastic Compute Cloud)** is a core AWS service that provides resizable compute capacity in the cloud. It allows you to launch virtual servers (instances) with pay-as-you-go pricing.

---

<details>
<summary><strong>1️⃣ What is EC2?</strong></summary>

- A **virtual server in the cloud** for running applications  
- Provides **resizable compute capacity**  
- **Pay-as-you-go** model — pay only for what you use  

</details>

---

<details>
<summary><strong>2️⃣ Core EC2 Concepts</strong></summary>

| Concept | Description |
|--------|--------------|
| **AMI (Amazon Machine Image)** | Blueprint for instance (OS + software + config) |
| **Instance Type** | Defines CPU, RAM, network, and storage power |
| **EBS (Elastic Block Store)** | Persistent block storage volumes |
| **Instance Store** | Temporary storage; data lost if stopped/terminated |
| **Key Pair** | Used for SSH authentication |
| **Security Group (SG)** | Virtual firewall controlling inbound & outbound traffic |
| **Elastic IP** | Static public IPv4 address |
| **User Data** | Script that runs on 1st boot for automation |
| **Placement Group** | Controls instance placement: Cluster, Spread, Partition |
| **ASG (Auto Scaling Group)** | Auto-scale instances based on demand |
| **Launch Template / Configuration** | Template for ASG launches |

</details>

---

<details>
<summary><strong>3️⃣ EC2 Pricing Models</strong></summary>

| Pricing Model | Best For | Savings |
|--------------|-----------|----------|
| **On-Demand** | Short-term, unpredictable workloads | ❌ Cheapest |
| **Reserved Instances (1–3 yrs)** | Predictable long-term usage | ✅ Up to **75%** cheaper |
| **Spot Instances** | Fault-tolerant, flexible jobs | ✅ Up to **90%** cheaper |
| **Dedicated Host** | Compliance, licensing needs | 💲 Expensive |
| **Savings Plans** | Consistent usage across compute services | ✅ Smart & Flexible |

</details>

---

<details>
<summary><strong>4️⃣ Storage Options</strong></summary>

| Storage | Type | Persistent? | Use Case |
|--------|--------|-------------|-----------|
| **EBS** | Block | ✅ Yes | OS, databases |
| **Instance Store** | Block | ❌ No | High-speed temporary storage |
| **EFS** | File (POSIX) | ✅ Yes | Multi-instance shared storage |
| **FSx** | File | ✅ Yes | Windows or HPC workloads |

</details>

---

<details>
<summary><strong>5️⃣ EC2 Networking</strong></summary>

- **Public IP** — auto-assigned, changes when stopped/started  
- **Elastic IP** — static public IPv4 that doesn’t change  
- **ENI (Elastic Network Interface)** — virtual network card  
- **Security Group vs NACL**  
  - SG = Instance-level firewall (Stateful)  
  - NACL = Subnet-level firewall (Stateless)  

</details>

---

<details>
<summary><strong>6️⃣ High Availability & Scaling</strong></summary>

- **ASG (Auto Scaling Group)** → Automatically adjusts instance count  
- **Launch Templates** → Recommended for launching instances  
- **ELB (Elastic Load Balancer)** → Distributes traffic across instances  
- **Multi-AZ Deployment** → High availability & fault tolerance  
- **Health Checks** → Auto-replace unhealthy instances  

</details>

---

<details>
<summary><strong>7️⃣ EC2 Spot Instances</strong></summary>

- Lowest-cost EC2 option (**up to 90% cheaper**)  
- Can be terminated anytime by AWS  
- Best for:  
  ✅ Batch jobs  
  ✅ Big Data & Analytics  
  ✅ CI/CD runners  
  ✅ Fault-tolerant workloads  
- Use **Spot Fleet** or **ASG with mixed instances** for reliability  

</details>

---

<details>
<summary><strong>8️⃣ User Data</strong></summary>

- Script that runs only **on first boot**  
- Ideal for installation, configuration & automation  
- Runs as **root user**  

**Example:**

```bash
#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
```

---

</details>
<details> <summary><strong>9️⃣ Monitoring & Logs</strong></summary>
Tool	Purpose
CloudWatch	Performance metrics (CPU, RAM, Disk, Network)
CloudTrail	API activity logs
EC2 Status Checks	System & Instance-level health
</details>

---

<details> 
<summary><strong>🔟 Common AWS CLI Commands for EC2</strong></summary>
# List Instances
aws ec2 describe-instances

# Launch an Instance
aws ec2 run-instances --image-id ami-xxx --instance-type t2.micro --key-name my-key --security-group-ids sg-xxx --subnet-id subnet-xxx

# Stop Instance
aws ec2 stop-instances --instance-ids i-xxxx

# Terminate Instance
aws ec2 terminate-instances --instance-ids i-xxxx

# Create AMI from Instance
aws ec2 create-image --instance-id i-xxxx --name "my-ami"
</details>
---
