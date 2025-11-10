# 🛡️ AWS VPC (Virtual Private Cloud) – Complete Notes

**Amazon VPC (Virtual Private Cloud)** is a **logically isolated virtual network** within AWS that lets you securely launch and manage your resources such as EC2, RDS, and Load Balancers.

---

## 📌 Table of Contents

1. [What is a VPC?](#1-what-is-a-vpc)
2. [VPC Core Components](#2-vpc-core-components)
3. [Public vs Private Subnets](#3-public-vs-private-subnets)
4. [Route Table](#4-route-table)
5. [Internet Gateway (IGW)](#5-internet-gateway-igw)
6. [NAT Gateway vs NAT Instance](#6-nat-gateway-vs-nat-instance)
7. [Security Groups (SG)](#7-security-groups-sg)
8. [Network ACL (NACL)](#8-network-acl-nacl)
9. [VPC Peering](#9-vpc-peering)
10. [VPC Endpoints](#10-vpc-endpoints)
11. [Transit Gateway](#11-transit-gateway)
12. [VPC Flow Logs](#12-vpc-flow-logs)
13. [Default vs Custom VPC](#13-default-vs-custom-vpc)
14. [Additional Important Concepts](#14-additional-important-concepts)
15. [Common Interview Scenarios](#15-common-interview-scenarios)
16. [AWS CLI Quick Commands](#16-aws-cli-quick-commands)

---

## 1️⃣ What is a VPC?

A **Virtual Private Cloud (VPC)** is a **customizable private network** within AWS where you can launch AWS resources in a logically isolated section of the cloud.

You control:

* IP address range (CIDR)
* Subnets (public/private)
* Routing
* Internet connectivity
* Security (SGs, NACLs)

💡 **Think of it as your private data center inside AWS.**

---

## 2️⃣ VPC Core Components

| Component                  | Description                                                    |
| -------------------------- | -------------------------------------------------------------- |
| **CIDR Block**             | Defines IP range of the VPC (e.g., `10.0.0.0/16`).             |
| **Subnets**                | Logical divisions within the VPC (Public/Private).             |
| **Route Tables**           | Define how traffic is directed within and outside the VPC.     |
| **Internet Gateway (IGW)** | Enables resources in the VPC to connect to the internet.       |
| **NAT Gateway / Instance** | Allows private subnets to access the internet securely.        |
| **Elastic IP (EIP)**       | Static, public IPv4 address for resources.                     |
| **Security Group (SG)**    | Stateful firewall for instances (inbound/outbound).            |
| **Network ACL (NACL)**     | Stateless firewall for subnets.                                |
| **VPC Peering**            | Enables private communication between two VPCs.                |
| **VPN Gateway**            | Connects on-premises network to VPC.                           |
| **Transit Gateway**        | Central hub to connect multiple VPCs and on-premises networks. |
| **Endpoints**              | Private connection to AWS services.                            |
| **Flow Logs**              | Capture metadata about traffic flow in your VPC.               |
| **Bastion Host**           | Jump server for accessing private EC2 instances securely.      |

---

## 3️⃣ Public vs Private Subnets

| Subnet Type        | Internet Access  | How It Works                                     |
| ------------------ | ---------------- | ------------------------------------------------ |
| **Public Subnet**  | ✅ Yes            | Route to Internet Gateway (IGW).                 |
| **Private Subnet** | ♻️ Outbound only | Uses NAT Gateway/Instance for outbound internet. |

💡 **Tip:** Place frontend servers (ALB, web apps) in **public subnets**, and backend servers (DB, internal apps) in **private subnets**.

---

## 4️⃣ Route Table

* Defines **how traffic is routed** within the VPC.
* Each subnet must be associated with a route table.
* Contains rules mapping destination IPs to targets (e.g., IGW, NAT, VGW).

### Example Routes:

| Destination   | Target    | Description                              |
| ------------- | --------- | ---------------------------------------- |
| `10.0.0.0/16` | local     | VPC internal routing                     |
| `0.0.0.0/0`   | igw-12345 | Public internet access                   |
| `0.0.0.0/0`   | nat-12345 | Outbound-only access for private subnets |

💡 **Main Route Table** = Default for all subnets unless custom ones are attached.

---

## 5️⃣ Internet Gateway (IGW)

* Enables **bi-directional communication** between VPC and the internet.
* Each VPC can have **only one** IGW.
* Must be **attached** to the VPC and referenced in the **route table**.

💡 Without an IGW, instances cannot have public internet connectivity.

---

## 6️⃣ NAT Gateway vs NAT Instance

| Feature               | **NAT Gateway**      | **NAT Instance**         |
| --------------------- | -------------------- | ------------------------ |
| **Management**        | Fully managed by AWS | You manage it            |
| **High Availability** | ✅ Yes (per AZ)       | ❌ Manual setup           |
| **Scaling**           | Auto                 | Manual                   |
| **Performance**       | Scales up to 45 Gbps | Depends on instance type |
| **Cost**              | 💰 Higher            | 💰 Lower                 |
| **Best Use**          | Production           | Dev/Test Environments    |

💡 Use **NAT Gateway** for production-grade applications.

---

## 7️⃣ Security Groups (SG)

* **Stateful firewall** that controls inbound and outbound traffic for instances.
* Automatically allows **return traffic** for allowed inbound rules.
* Attached to **ENIs** (Elastic Network Interfaces).
* Only **Allow** rules — no Deny rules.

💡 Example:

| Type  | Protocol | Port | Source    |
| ----- | -------- | ---- | --------- |
| SSH   | TCP      | 22   | My IP     |
| HTTP  | TCP      | 80   | 0.0.0.0/0 |
| HTTPS | TCP      | 443  | 0.0.0.0/0 |

---

## 8️⃣ Network ACL (NACL)

* **Stateless firewall** applied at the **subnet level**.
* Evaluates rules in numerical order.
* Supports both **Allow** and **Deny** rules.
* Return traffic must be explicitly allowed.

💡 **Use SGs for instance-level control**, and **NACLs for subnet-level filtering.**

---

## 9️⃣ VPC Peering

* Enables **private connectivity between two VPCs** using private IPs.
* Can be in the same or different AWS regions.
* **Transitive peering not supported** (A ↔ B ↔ C won’t work).
* Communication restricted by routing + SG + NACL settings.

💡 Use **Transit Gateway** for large-scale multi-VPC connectivity.

---

## 🔟 VPC Endpoints

Used for **private access to AWS services** without using an Internet Gateway, NAT, or VPN.

| Type                   | Used For          | Description                     |
| ---------------------- | ----------------- | ------------------------------- |
| **Interface Endpoint** | Most AWS services | Creates ENI in your subnet      |
| **Gateway Endpoint**   | S3, DynamoDB      | Adds route entry in route table |

💡 Example: Private S3 access from private subnet using a **Gateway Endpoint**.

---

## 1️⃣1️⃣ Transit Gateway

* **Hub-and-spoke architecture** that simplifies connecting multiple VPCs, VPNs, and Direct Connect links.
* Acts as a **central router**.
* Supports **inter-region peering** and scalable throughput.

💡 Replaces the need for complex VPC Peering mesh setups.

---

## 1️⃣2️⃣ VPC Flow Logs

* Capture metadata about network traffic (accepted/rejected).
* Helps with **troubleshooting, security auditing, and performance monitoring**.
* Logs can be sent to **CloudWatch Logs** or **S3**.

Example use cases:

* Identify **blocked traffic**
* Analyze **malicious access**
* Debug **network latency**

---

## 1️⃣3️⃣ Default VPC vs Custom VPC

| Feature        | **Default VPC**          | **Custom VPC**        |
| -------------- | ------------------------ | --------------------- |
| CIDR           | `172.31.0.0/16`          | User-defined          |
| Subnets        | One per AZ               | User-created          |
| IGW            | Attached automatically   | Manual setup          |
| Security Group | Default allow within VPC | Custom rules required |
| Route Table    | Preconfigured            | Must define manually  |

💡 Always **build a custom VPC** in production for better control and security.

---

## 1️⃣4️⃣ Additional Important Concepts

| Concept                           | Description                                               |
| --------------------------------- | --------------------------------------------------------- |
| **PrivateLink**                   | Connect to SaaS or third-party services privately.        |
| **Egress-Only IGW**               | Enables IPv6 outbound-only internet access.               |
| **DHCP Options Set**              | Customize DNS and domain names for instances.             |
| **Direct Connect (DX)**           | Dedicated, high-speed connection from on-premises to AWS. |
| **Prefix Lists**                  | Shared lists of IP ranges used in SGs or route tables.    |
| **Customer Gateway (CGW)**        | On-prem VPN endpoint.                                     |
| **Virtual Private Gateway (VGW)** | AWS side of VPN.                                          |
| **VPC Sharing**                   | Allows multiple AWS accounts to share subnets.            |

---

## 1️⃣5️⃣ Common Interview Scenarios

* Design public and private subnets.
* Connect 2 VPCs securely (Peering vs Transit Gateway).
* Private instance needs internet → Use NAT Gateway.
* Explain SG vs NACL (Stateful vs Stateless).
* Set up hybrid connection (VPN / Direct Connect).
* Debug connectivity issue → Check **SG → NACL → Route Table → IGW → Flow Logs**.

💡 Be ready to **diagram and explain data flow** through these components.

---

## 1️⃣6️⃣ AWS CLI Quick Commands

```bash
# Create VPC
aws ec2 create-vpc --cidr-block 10.0.0.0/16

# Create Subnet
aws ec2 create-subnet --vpc-id vpc-xxxx --cidr-block 10.0.1.0/24

# Create Internet Gateway
aws ec2 create-internet-gateway

# Attach IGW to VPC
aws ec2 attach-internet-gateway --internet-gateway-id igw-xxxx --vpc-id vpc-xxxx

# Create Route Table
aws ec2 create-route-table --vpc-id vpc-xxxx

# Associate Route Table with Subnet
aws ec2 associate-route-table --route-table-id rtb-xxxx --subnet-id subnet-xxxx
```

---

## 🧠 Quick Memory Hooks

| Concept             | Quick Recall                               |
| ------------------- | ------------------------------------------ |
| **VPC**             | Private virtual network inside AWS         |
| **Subnet**          | Logical partition of VPC                   |
| **IGW**             | Enables public internet access             |
| **NAT Gateway**     | Outbound-only internet for private subnets |
| **SG**              | Stateful, instance-level                   |
| **NACL**            | Stateless, subnet-level                    |
| **Peering**         | Private VPC-to-VPC link                    |
| **Endpoint**        | Private AWS service access                 |
| **Flow Logs**       | Track VPC network activity                 |
| **Transit Gateway** | Central router for multi-VPC setups        |

---

✅ **Final Tip:**
When designing a VPC, **start from inside → out**:

1. Define CIDR and subnets
2. Attach IGW or NAT as needed
3. Configure route tables
4. Secure using SG + NACL
5. Add Flow Logs for visibility
