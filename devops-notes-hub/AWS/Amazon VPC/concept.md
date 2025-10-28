# Amazon VPC Concepts

# AWS VPC (Virtual Private Cloud) – Complete Notes

## 1. VPC (Virtual Private Cloud)
A logically isolated virtual network in AWS where you launch and manage resources securely.  
You control IP range, subnets, routing, security, and connectivity.

---

## 2. VPC Core Components

| Component | Description |
|----------|--------------|
| **CIDR Block** | IP range of VPC (e.g., `10.0.0.0/16`) |
| **Subnets** | Divide IP range (Public / Private) |
| **Route Tables** | Define routing rules for traffic |
| **Internet Gateway (IGW)** | Enables public internet access for public subnets |
| **NAT Gateway / NAT Instance** | Enables outbound internet for private subnets |
| **Elastic IP (EIP)** | Static public IP |
| **Security Group (SG)** | *Stateful* instance-level firewall |
| **Network ACL (NACL)** | *Stateless* subnet-level traffic rules |
| **VPC Peering** | Private connection between two VPCs |
| **VPN Gateway** | Connect on-prem to AWS via VPN |
| **Transit Gateway** | Connect multiple VPCs & VPNs using hub-and-spoke |
| **Endpoints** | Private access to AWS services without internet |
| **Flow Logs** | Capture IP traffic metadata |
| **Bastion Host** | Secure SSH/RDP access to private instances |

---

## 3. Public vs Private Subnet

| Subnet Type | Internet Access | How? |
|-------------|------------------|-------|
| **Public Subnet** | Yes | Route to IGW |
| **Private Subnet** | Outbound only | NAT Gateway / NAT Instance |

---

## 4. Route Table
- Controls where traffic is routed (e.g., `0.0.0.0/0 → IGW`)
- Subnets must be associated with a Route Table
- **Main Route Table** vs **Custom Route Table**

---

## 5. Internet Gateway (IGW)
- One IGW can be attached to one VPC
- Enables instances in public subnet to access Internet

---

## 6. NAT Gateway vs NAT Instance

| Feature | **NAT Gateway** | **NAT Instance** |
|---------|------------------|-------------------|
| Managed By | AWS | Self-managed EC2 |
| High Availability | Yes (per AZ) | No |
| Scaling | Automatic | Manual |
| Cost | Higher | Lower |
| Best For | Production | Learning/Testing |

---

## 7. Security Groups (SG)
- **Stateful** – return traffic automatically allowed
- Works at **instance ENI level**
- Only **allow** rules supported
- Example: Allow SSH (22), HTTP (80)

---

## 8. Network ACL (NACL)
- **Stateless** – return traffic must be explicitly allowed
- Works at **subnet level**
- Supports **allow + deny**
- Rules evaluated in order (Rule #)

---

## 9. VPC Peering
- Private communication between 2 VPCs
- Can be same/different region
- **No transitive peering**

---

## 10. VPC Endpoints
Private access to AWS services **without IGW, NAT, or VPN**

| Type | Used For | Description |
|------|-----------|--------------|
| **Interface Endpoint** | Most AWS services | ENI created in subnet |
| **Gateway Endpoint** | S3, DynamoDB | Route table entry created |

---

## 11. Transit Gateway
- Hub-and-spoke model to interconnect VPCs, VPN & on-prem
- Reduces complex VPC-peering mesh

---

## 12. VPC Flow Logs
- Captures traffic metadata to/from ENI
- Helps debug, monitor & audit network

---

## 13. Default VPC vs Custom VPC

| Feature | **Default VPC** | **Custom VPC** |
|----------|------------------|------------------|
| CIDR | `172.31.0.0/16` | User-defined |
| Subnets | 1 per AZ | As needed |
| IGW | Attached by default | Need to attach |
| SG | Default allows all within VPC | Custom rules |

---

## 14. Additional Concepts (Often Missed in Interviews)

| Topic | Why Important |
|--------|----------------|
| **PrivateLink** | Secure SaaS/private service access |
| **Egress-Only IGW** | IPv6 outbound internet only |
| **DHCP Options Set** | Custom DNS for VPC |
| **Direct Connect** | Dedicated on-prem to AWS link |
| **Prefix Lists** | Reusable IP lists in SG/RT |
| **Customer Gateway / Virtual Private Gateway** | Needed for site-to-site VPN |
| **VPC Sharing** | Share subnets across AWS accounts |

---

## 15. Common Interview Scenarios
- Design **Public vs Private** subnet architecture
- Connect 2 VPCs securely (Peering vs TGW)
- Private EC2 wants internet access (NAT)
- Difference: **SG vs NACL** (Stateful vs Stateless)
- On-prem ↔ AWS connectivity options (VPN / DX)
- Debug connectivity issues (SG, NACL, RT, IGW, Flow Logs)

---

## 16. AWS CLI Quick Commands

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

# Associate Subnet with Route Table
aws ec2 associate-route-table --route-table-id rtb-xxxx --subnet-id subnet-xxxx
