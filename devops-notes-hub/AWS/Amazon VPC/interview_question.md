# 🧠 AWS VPC – Interview Questions (Beginner → Advanced + Scenarios)

A structured, interview-ready list of **VPC questions** commonly asked in **AWS / Cloud / DevOps interviews**, from fundamentals to real-world scenarios.

---

## 🔥 10 Commonly Asked VPC Questions

1. What is a VPC in AWS?
2. What is the difference between Public and Private Subnet?
3. What is an Internet Gateway (IGW)? Why is it used?
4. How can an EC2 instance in a private subnet access the Internet?
5. What is the difference between Security Groups and NACLs?
6. What is a Route Table and why do we need it?
7. What is VPC Peering?
8. What are VPC Endpoints and why do we use them?
9. What is CIDR in VPC?
10. What is a NAT Gateway and how is it different from a NAT Instance?

---

## ⚙️ 10 Moderate-Level VPC Questions

1. Can a Security Group span across multiple VPCs?
2. Can a Subnet span multiple Availability Zones? Explain why.
3. Explain **Stateful vs Stateless** with examples in VPC.
4. Why is **VPC Peering not transitive**?
5. Difference between **Interface Endpoint** and **Gateway Endpoint**.
6. When would you choose **Transit Gateway** instead of **VPC Peering**?
7. What is an **Egress-Only Internet Gateway** and when is it used?
8. How do **Flow Logs** help in troubleshooting connectivity issues?
9. What is **AWS PrivateLink**? How is it different from VPC Peering?
10. How can you **restrict public access to S3 while accessing it from VPC**?
    💡 *Hint: Use VPC Endpoint + Bucket Policy.*

---

## 🚀 10 Advanced VPC Questions

1. How does **Transit Gateway** enable multi-VPC and hybrid connectivity?
2. What is the difference between **Transit Gateway**, **VPC Peering**, and **PrivateLink**?
3. Explain how **DNS resolution** works inside a VPC (Route 53 Resolver, DHCP Options Set).
4. How do you design a **multi-account VPC architecture** following AWS best practices?
5. Explain the role of **Prefix Lists** in managing network access.
6. What is **VPC Sharing**, and when should you use it?
7. How would you **secure workloads inside a VPC** using SGs, NACLs, WAF, and Firewall Manager?
8. How does **AWS Direct Connect** differ from **VPN**? When do we use both together?
9. How do you implement **centralized egress** for multiple VPCs?
10. Explain the **packet flow from a private EC2 instance to S3** using a VPC Endpoint.

---

## 🧩 10 Scenario-Based VPC Questions (Real-World)

These are asked for **4+ years Cloud / DevOps Engineer roles**.

---

### Scenario 1 – Private Instance No Internet Access

Your EC2 instance in a private subnet cannot reach the internet. How will you troubleshoot?
✅ *Hint:* Route Table → NAT → SG → NACL → IGW (in public subnet)

---

### Scenario 2 – One-Way Peering Issue

Two VPCs (A & B) are peered. A can reach B, but B cannot reach A. Why?
✅ *Hint:* Routing + SG + NACL misconfiguration

---

### Scenario 3 – Secure Access to One Customer

You need to securely expose a service in your VPC to only one customer’s VPC in another AWS account.
✅ *Hint:* Use **AWS PrivateLink**

---

### Scenario 4 – Multi-VPC + On-Prem Connectivity

Your organization has 10 VPCs and needs to connect them along with an on-prem data center.
✅ *Hint:* Use **Transit Gateway** for centralized hub-and-spoke connectivity.

---

### Scenario 5 – Private EC2 Pulling Docker Images

A private EC2 instance needs to pull Docker images from **ECR** without internet access.
✅ *Hint:* Use **VPC Endpoints for ECR + S3**

---

### Scenario 6 – Inter-Region Latency

Traffic between two VPCs in different regions is slow. How do you optimize it?
✅ *Hint:* Use **Inter-region VPC Peering** (uses AWS backbone network)

---

### Scenario 7 – Restricted Database Access

Your database in a private subnet should only accept traffic from one specific application subnet.
✅ *Hint:* Use **Security Group rules**, not wide NACLs.

---

### Scenario 8 – On-Prem Connectivity Options

How do you allow on-prem systems to securely connect to your VPC? Provide 3 architectures.
✅ *Hint:* VPN, Direct Connect (DX), or VPN + DX with **Transit Gateway**

---

### Scenario 9 – Restricted Developer Access

You need to give developers restricted access to only one subnet in the VPC.
✅ *Hint:* Combine **IAM**, **SCP**, **NACL**, **SG**, and **SSM Session Manager**.

---

### Scenario 10 – Reducing NAT Gateway Cost

Your NAT Gateway bill is too high. How do you reduce cost?
✅ *Solutions:*

* Use **1 NAT per AZ** only if needed
* Use **S3 & DynamoDB VPC Endpoints**
* Deploy **Proxy / Split routing** for certain workloads

---

## 🧠 Quick Revision Table

| Concept                 | Description                                |
| ----------------------- | ------------------------------------------ |
| **VPC**                 | Logical isolated network in AWS            |
| **Subnet**              | Logical division (Public / Private)        |
| **IGW**                 | Internet connectivity for public subnets   |
| **NAT Gateway**         | Outbound-only internet for private subnets |
| **SG (Security Group)** | Stateful instance firewall                 |
| **NACL**                | Stateless subnet firewall                  |
| **Transit Gateway**     | Connects multiple VPCs & on-prem           |
| **PrivateLink**         | Private service-to-service communication   |
| **Flow Logs**           | Capture VPC network traffic metadata       |
| **Prefix List**         | Manage IPs in route tables easily          |

---

✅ **Final Tip:**
In interviews, focus on **VPC design thinking**:

* Explain **data flow** from instance → subnet → route table → gateway.
* Understand **troubleshooting flow**: SG → NACL → RT → NAT/IGW → Flow Logs.
* Know when to use **Transit Gateway, Peering, or PrivateLink**.
* Be ready to **sketch** a VPC architecture if asked.
