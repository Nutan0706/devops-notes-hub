# 🛡️ AWS VPC (Virtual Private Cloud) – Complete Notes

> A complete, interview-ready, visually enriched guide to AWS VPC with collapsible sections for easy learning & revision.

---

## 📌 Table of Contents  
- [What is VPC?](#1-vpc-virtual-private-cloud)  
- [VPC Core Components](#2-vpc-core-components)  
- [Public vs Private Subnets](#3-public-vs-private-subnet)  
- [Route Table](#4-route-table)  
- [Internet Gateway](#5-internet-gateway-igw)  
- [NAT Gateway vs NAT Instance](#6-nat-gateway-vs-nat-instance)  
- [Security Groups](#7-security-groups-sg)  
- [Network ACL](#8-network-acl-nacl)  
- [VPC Peering](#9-vpc-peering)  
- [VPC Endpoints](#10-vpc-endpoints)  
- [Transit Gateway](#11-transit-gateway)  
- [VPC Flow Logs](#12-vpc-flow-logs)  
- [Default vs Custom VPC](#13-default-vpc-vs-custom-vpc)  
- [Additional Important Concepts](#14-additional-concepts-often-missed-in-interviews)  
- [Common Interview Scenarios](#15-common-interview-scenarios)  
- [CLI Quick Commands](#16-aws-cli-quick-commands)

---

## 1. VPC (Virtual Private Cloud)

> A **logically isolated virtual network** inside AWS where you launch and manage your resources securely.

✅ You control:  
- IP range  
- Subnets  
- Route tables  
- Security  
- Network connectivity  

---

<details>
<summary><h2>2. 🧩 VPC Core Components</h2></summary>

| Component | Description |
|----------|--------------|
| **CIDR Block** | IP range of VPC (e.g., `10.0.0.0/16`) |
| **Subnets** | Divide IP range (Public / Private) |
| **Route Tables** | Define routing rules for traffic |
| **Internet Gateway (IGW)** | Enables public internet access |
| **NAT Gateway / NAT Instance** | Outbound internet for private subnets |
| **Elastic IP (EIP)** | Static public IP |
| **Security Group (SG)** | *Stateful* instance firewall |
| **Network ACL (NACL)** | *Stateless* subnet firewall |
| **VPC Peering** | Private VPC-to-VPC connectivity |
| **VPN Gateway** | On-prem ↔ AWS VPN |
| **Transit Gateway** | Connect multiple VPCs & on-prem |
| **Endpoints** | Private AWS service access |
| **Flow Logs** | Capture traffic metadata |
| **Bastion Host** | SSH/RDP access to private instances |

</details>

---

<details>
<summary><h2>3. 🌐 Public vs Private Subnet</h2></summary>

| Subnet Type | Internet Access | How? |
|-------------|------------------|-------|
| **Public** | ✅ Yes | Route to IGW |
| **Private** | ♻️ Outbound only | NAT Gateway / NAT Instance |

</details>

---

<details>
<summary><h2>4. 🛣️ Route Table</h2></summary>

- Controls where traffic flows  
- Subnet must be associated to a route table  
- **Main** vs **Custom** Route Table  
- Example:

</details>

---

<details>
<summary><h2>5. 🌍 Internet Gateway (IGW)</h2></summary>

- One IGW per VPC  
- Required for **public internet access**  

</details>

---

<details>
<summary><h2>6. 🔁 NAT Gateway vs NAT Instance</h2></summary>

| Feature | **NAT Gateway** | **NAT Instance** |
|---------|------------------|-------------------|
| Managed | AWS | Self-managed |
| HA | ✅ Yes (per AZ) | ❌ No |
| Scaling | Auto | Manual |
| Cost | 💰 Higher | Low |
| Best For | Production | Learning/Testing |

</details>

---

<details>
<summary><h2>7. 🔐 Security Groups (SG)</h2></summary>

- **Stateful** – return traffic auto-allowed  
- Works at **instance ENI level**  
- Only **Allow** rules  
- Example: Allow SSH (22), HTTP (80)  

</details>

---

<details>
<summary><h2>8. 🚧 Network ACL (NACL)</h2></summary>

- **Stateless** – return traffic must be allowed explicitly  
- Works at **subnet level**  
- **Allow + Deny** supported  
- Rules evaluated in ascending order  

</details>

---

<details>
<summary><h2>9. 🔗 VPC Peering</h2></summary>

- Private connection between 2 VPCs  
- Same or different region  
❗ **No transitive peering**  

</details>

---

<details>
<summary><h2>10. 🔌 VPC Endpoints</h2></summary>

Private access to AWS services **without IGW, NAT, VPN**  

| Type | Use For | Description |
|------|-----------|--------------|
| **Interface Endpoint** | Most services | ENI in your subnet |
| **Gateway Endpoint** | S3, DynamoDB | Route table entry |

</details>

---

<details>
<summary><h2>11. 🛟 Transit Gateway</h2></summary>

- Hub-and-spoke architecture  
- Connects **VPC ↔ VPC**, **VPC ↔ On-Prem**, **DX**  

</details>

---

<details>
<summary><h2>12. 🧾 VPC Flow Logs</h2></summary>

- Captures traffic metadata  
- Helps debugging, monitoring & auditing  

</details>

---

<details>
<summary><h2>13. 🏗️ Default VPC vs Custom VPC</h2></summary>

| Feature | **Default VPC** | **Custom VPC** |
|----------|------------------|------------------|
| CIDR | `172.31.0.0/16` | User-defined |
| Subnets | 1 per AZ | As needed |
| IGW | Attached by default | Manually attach |
| SG | Default allow internal | Custom rules |

</details>

---

<details>
<summary><h2>14. 🧠 Additional Concepts (Often Missed)</h2></summary>

| Topic | Why Important |
|--------|----------------|
| **PrivateLink** | SaaS/private service access |
| **Egress-Only IGW** | IPv6 outbound |
| **DHCP Options Set** | Custom DNS |
| **Direct Connect** | Dedicated on-prem link |
| **Prefix Lists** | Reusable IP list |
| **Customer GW / VGW** | For VPN setup |
| **VPC Sharing** | Shared subnets multi-account |

</details>

---

<details>
<summary><h2>15. 🎯 Common Interview Scenarios</h2></summary>

✅ Design public & private subnets  
🔗 Connect 2 VPCs securely (Peering vs TGW)  
🌍 Private instance needs internet → NAT  
🧱 SG vs NACL (Stateful vs Stateless)  
🏢 On-prem ↔ AWS (VPN / DX)  
🔍 Debug traffic issues (SG → NACL → RT → IGW → Flow Logs)  

</details>

---

## 16. 🧑‍💻 AWS CLI Quick Commands

```bash
# Create VPC
aws ec2 create-vpc --cidr-block 10.0.0.0/16

# Create Subnet
aws ec2 create-subnet --vpc-id vpc-xxxx --cidr-block 10.0.1.0/24

# Create Internet Gateway
aws ec2 create-internet-gateway

# Attach IGW
aws ec2 attach-internet-gateway --internet-gateway-id igw-xxxx --vpc-id vpc-xxxx

# Create Route Table
aws ec2 create-route-table --vpc-id vpc-xxxx

# Associate Route Table
aws ec2 associate-route-table --route-table-id rtb-xxxx --subnet-id subnet-xxxx
