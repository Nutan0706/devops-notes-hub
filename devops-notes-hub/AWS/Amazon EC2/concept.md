# 🖥️ AWS EC2 – Complete Notes

Amazon **EC2 (Elastic Compute Cloud)** provides **resizable compute capacity** in the AWS cloud.
It allows you to **launch and manage virtual servers (instances)** using a **pay-as-you-go** model.

---

## 1️⃣ What is EC2?

* A **virtual server** in the cloud for running applications.
* Offers **scalable compute resources** (CPU, memory, network).
* **Pay only for what you use** — flexible billing.
* Enables quick provisioning, automation, and integration with other AWS services.

💡 **Analogy:** Think of EC2 as your remote computer (VM) hosted in AWS, accessible anytime, anywhere.

---

## 2️⃣ Core EC2 Concepts

| Concept                        | Description                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| **AMI (Amazon Machine Image)** | Blueprint of an instance (OS + software + configuration).    |
| **Instance Type**              | Defines compute resources (CPU, RAM, storage, networking).   |
| **EBS (Elastic Block Store)**  | Persistent block storage for EC2 instances.                  |
| **Instance Store**             | Temporary (ephemeral) storage tied to instance lifecycle.    |
| **Key Pair**                   | SSH key used to securely connect to instances.               |
| **Security Group (SG)**        | Virtual firewall controlling inbound/outbound traffic.       |
| **Elastic IP**                 | Static public IPv4 address associated with your instance.    |
| **User Data**                  | Script executed at first boot for automation (setup/config). |
| **Placement Group**            | Strategy for placing instances (Cluster, Spread, Partition). |
| **ASG (Auto Scaling Group)**   | Automatically adjusts the number of instances.               |
| **Launch Template**            | Modern way to configure and launch instances consistently.   |

💡 **Tip:** Use Launch Templates + ASGs for production environments for consistency and automation.

---

## 3️⃣ EC2 Pricing Models

| Pricing Model                    | Best For                                     | Savings             |
| -------------------------------- | -------------------------------------------- | ------------------- |
| **On-Demand**                    | Short-term, unpredictable workloads          | ❌ Least savings     |
| **Reserved Instances (1–3 yrs)** | Steady workloads                             | ✅ Up to 75% savings |
| **Spot Instances**               | Flexible, fault-tolerant jobs                | ✅ Up to 90% savings |
| **Dedicated Hosts**              | Compliance/licensing requirements            | 💲 High cost        |
| **Savings Plans**                | Consistent compute usage across AWS services | ✅ Flexible savings  |

💡 **Pro Tip:** Start with On-Demand → Move to Savings Plans for predictable workloads.

---

## 4️⃣ Storage Options

| Storage Type                  | Storage Level | Persistent? | Use Case                                  |
| ----------------------------- | ------------- | ----------- | ----------------------------------------- |
| **EBS (Elastic Block Store)** | Block         | ✅ Yes       | OS volumes, Databases                     |
| **Instance Store**            | Block         | ❌ No        | Temporary or cache data                   |
| **EFS (Elastic File System)** | File (POSIX)  | ✅ Yes       | Shared storage between multiple instances |
| **FSx**                       | File          | ✅ Yes       | Windows file systems, HPC workloads       |

💡 **Tip:**
Use **EBS** for boot volumes and **EFS** for shared app data.
Use **Instance Store** only for non-critical, temporary data.

---

## 5️⃣ EC2 Networking

| Concept                             | Description                                                 |
| ----------------------------------- | ----------------------------------------------------------- |
| **Public IP**                       | Automatically assigned; changes when instance stops/starts. |
| **Elastic IP (EIP)**                | Static public IP; persistent even after stop/start.         |
| **ENI (Elastic Network Interface)** | Virtual network adapter; can attach/detach dynamically.     |
| **Security Group (SG)**             | Instance-level firewall — **stateful**.                     |
| **Network ACL (NACL)**              | Subnet-level firewall — **stateless**.                      |

### 🧩 Security Group vs NACL

| Feature              | Security Group                       | NACL                         |
| -------------------- | ------------------------------------ | ---------------------------- |
| **Scope**            | Instance level                       | Subnet level                 |
| **Type**             | Stateful                             | Stateless                    |
| **Rules Applied**    | Allow only                           | Allow + Deny                 |
| **Default Behavior** | Deny all inbound, allow all outbound | Allow all inbound & outbound |

---

## 6️⃣ High Availability & Scaling

| Concept                         | Description                                                   |
| ------------------------------- | ------------------------------------------------------------- |
| **ASG (Auto Scaling Group)**    | Automatically increases/decreases instances based on metrics. |
| **Launch Template**             | Defines instance config for consistent deployments.           |
| **ELB (Elastic Load Balancer)** | Distributes traffic across multiple EC2 instances.            |
| **Multi-AZ Deployment**         | Launches instances in multiple Availability Zones.            |
| **Health Checks**               | Automatically replaces unhealthy instances.                   |

💡 **Best Practice:** Combine **ASG + ELB + Multi-AZ** for maximum uptime.

---

## 7️⃣ EC2 Spot Instances

* **Cheapest EC2 option** — up to **90% cost savings**.
* AWS can **terminate** them when capacity/pricing changes.
* Best suited for:

  * ✅ Batch processing
  * ✅ Big Data / Analytics
  * ✅ CI/CD runners
  * ✅ Fault-tolerant workloads

🔹 Use **Spot Fleet** or **Mixed ASG** to balance cost and reliability.

---

## 8️⃣ User Data

User Data scripts automate initial setup on instance launch.
Runs as **root user**, and executes only **once on first boot**.

### Example: Install Apache Web Server

```bash
#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from EC2 Instance</h1>" > /var/www/html/index.html
```

💡 **Tip:** Use User Data for bootstrapping — install apps, configure services, and run init scripts.

---

## 9️⃣ Monitoring & Logs

| Tool                  | Purpose                                                          |
| --------------------- | ---------------------------------------------------------------- |
| **Amazon CloudWatch** | Monitors performance metrics (CPU, Memory, Disk I/O, Network).   |
| **AWS CloudTrail**    | Logs all API-level activities for auditing.                      |
| **EC2 Status Checks** | Detects hardware/system-level issues (Instance & System checks). |

✅ **Recommended:**
Set **CloudWatch alarms** to trigger **Auto Scaling** actions automatically.

---

## 🔟 Common AWS CLI Commands for EC2

```bash
# List all instances
aws ec2 describe-instances

# Launch an instance
aws ec2 run-instances \
  --image-id ami-xxxxxx \
  --instance-type t2.micro \
  --key-name my-key \
  --security-group-ids sg-xxxxxx \
  --subnet-id subnet-xxxxxx

# Stop instance
aws ec2 stop-instances --instance-ids i-xxxxxx

# Start instance
aws ec2 start-instances --instance-ids i-xxxxxx

# Terminate instance
aws ec2 terminate-instances --instance-ids i-xxxxxx

# Create AMI from running instance
aws ec2 create-image --instance-id i-xxxxxx --name "my-custom-ami"
```

💡 **Tip:** Use `--query` and `--output table` for readable CLI outputs.

---

## 🧠 Quick Revision Hooks

| Concept            | Shortcut Memory Trick                |
| ------------------ | ------------------------------------ |
| **EC2**            | Virtual server on AWS                |
| **AMI**            | OS + configuration image             |
| **EBS**            | Persistent storage                   |
| **Instance Store** | Temporary fast storage               |
| **SG**             | Stateful firewall                    |
| **NACL**           | Stateless firewall                   |
| **ASG**            | Auto scales EC2 instances            |
| **ELB**            | Distributes traffic                  |
| **User Data**      | Automation script                    |
| **Spot Instance**  | Cheapest compute, can vanish anytime |

---

✅ **Final Tip:**
For **production-grade EC2 architecture**, always combine:
**VPC + Security Group + EBS + ASG + ELB + CloudWatch** — ensuring **performance, cost efficiency, and reliability**.
