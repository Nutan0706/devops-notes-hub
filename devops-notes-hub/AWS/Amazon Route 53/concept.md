# 🌐 AWS Route 53 — Complete Notes

> **Route 53** → AWS’s Highly Available & Scalable Cloud DNS Service  
> 💡 Name “53” comes from **DNS port 53**.

---

## ✅ Table of Contents
- [What is Route 53?](#-what-is-route-53)
- [Main Features](#-main-features)
- [Hosted Zones](#-hosted-zones)
- [Record Types](#-record-types)
- [Routing Policies](#-routing-policies)
- [Health Checks](#-health-checks)
- [Alias vs CNAME](#-alias-vs-cname)
- [Integration with AWS](#-integration-with-aws)
- [Security & Reliability](#-security--reliability)

---

<details>
<summary><h2>🔍 What is Route 53?</h2></summary>

Route 53 is AWS’s fully managed, highly scalable **Domain Name System (DNS)** web service.

| Feature | Description |
|--------|--------------|
| 🌍 Global DNS | Routes traffic across regions |
| 🔒 Highly Reliable | Global network + Anycast |
| ⚙️ Managed | Register domains, host zones, routing |

</details>

---

<details>
<summary><h2>🚀 Main Features</h2></summary>

### 1️⃣ Domain Registration  
Buy and manage domain names directly in Route 53.

### 2️⃣ DNS Service  
- Host DNS zones and records  
- Low latency, global availability  

### 3️⃣ Health Checks  
- Monitor endpoint health  
- Remove unhealthy endpoints from routing  

### 4️⃣ Traffic Management  
Supports advanced routing policies for global traffic distribution.

</details>

---

<details>
<summary><h2>🗂 Hosted Zones</h2></summary>

| Type | Usage |
|-------|--------|
| 🌎 **Public Hosted Zone** | Internet-facing domains |
| 🏠 **Private Hosted Zone** | Internal records within a VPC |

</details>

---

<details>
<summary><h2>📍 Record Types</h2></summary>

| Record | Maps To | Notes |
|--------|---------|--------|
| **A** | IPv4 | Most common |
| **AAAA** | IPv6 | — |
| **CNAME** | Domain → Domain | Cannot be used at root |
| **Alias** | Domain → AWS Service | Works at root, free queries |
| **MX, TXT, PTR, SRV, NS, SOA** | Standard DNS Records | Email, verification, etc |

> ✅ **Alias Record** supports root domain (e.g., `example.com`), while **CNAME does NOT**.

</details>

---

<details>
<summary><h2>🧠 Routing Policies</h2></summary>

| Policy | Use Case |
|--------|------------|
| **Simple Routing** | Single resource |
| **Weighted** | % traffic split (A/B testing) |
| **Latency-Based** | Best user performance |
| **Failover** | Active-Passive setup |
| **Geolocation** | Route based on user's country/region |
| **Geoproximity** | Based on proximity + adjustable bias |
| **Multi-Value Answer** | Returns multiple healthy IPs (basic LB) |

</details>

---

<details>
<summary><h2>💓 Health Checks</h2></summary>

- Monitor endpoints (HTTP, HTTPS, TCP)  
- Remove unhealthy endpoints from DNS responses  
- Integrates with CloudWatch Alarms  

Used mostly with:  
✅ Failover Routing  
✅ Multi-Value Answer Routing  

</details>

---

<details>
<summary><h2>🔗 Alias Records vs CNAME</h2></summary>

| Feature | Alias Record | CNAME |
|--------|---------------|--------|
| AWS-Only | ✅ Yes | ❌ No |
| Works at Root (Apex) | ✅ Yes (`example.com`) | ❌ No |
| Cost | Free | Paid DNS queries |
| Points To | AWS Services (ALB, S3, CF) | Any domain |

> 📌 Prefer **Alias** for AWS mapped records.

</details>

---

<details>
<summary><h2>🔧 Integration with AWS</h2></summary>

Used commonly with:

- **CloudFront** CDN  
- **ALB/NLB** load balancers  
- **S3 Static Website**  
- **API Gateway**  
- **Global Accelerator**  
- Hybrid DNS with **Route 53 Resolver**

</details>

---

<details>
<summary><h2>🛡️ Security & Reliability</h2></summary>

- **Globally distributed Anycast network**  
- Highly available DNS failover  
- Hybrid DNS resolution (On-Prem ↔ AWS)  

</details>

---
