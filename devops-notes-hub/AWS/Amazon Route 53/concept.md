# 🌐 AWS Route 53 — Complete Notes

**Amazon Route 53** is a **highly available, scalable, and global DNS service** provided by AWS.
It connects user requests to applications hosted on AWS or external infrastructure.

💡 The name **“53”** comes from **port 53**, the standard DNS port.

---

## ✅ Table of Contents

* [What is Route 53?](#-what-is-route-53)
* [Main Features](#-main-features)
* [Hosted Zones](#-hosted-zones)
* [Record Types](#-record-types)
* [Routing Policies](#-routing-policies)
* [Health Checks](#-health-checks)
* [Alias vs CNAME](#-alias-vs-cname)
* [Integration with AWS](#-integration-with-aws)
* [Security & Reliability](#-security--reliability)

---

## 🔍 What is Route 53?

**Amazon Route 53** is a **fully managed DNS (Domain Name System)** web service that provides:

* **Domain registration**
* **DNS routing**
* **Health checking**
* **Traffic management**

| Feature                | Description                                           |
| ---------------------- | ----------------------------------------------------- |
| 🌍 **Global DNS**      | Routes user traffic to AWS or external endpoints.     |
| ⚙️ **Fully Managed**   | AWS handles scaling, reliability, and updates.        |
| 🔒 **Highly Reliable** | Uses Anycast network with distributed edge locations. |

💡 Route 53 acts as your “Internet phonebook,” mapping domain names to IP addresses.

---

## 🚀 Main Features

### 1️⃣ Domain Registration

Buy, transfer, and manage **domain names** directly within AWS.

### 2️⃣ DNS Management

Create and manage **public** or **private DNS zones** and records.

### 3️⃣ Health Checks

Continuously monitor endpoint health and automatically remove unhealthy targets.

### 4️⃣ Traffic Management

Use **routing policies** to distribute traffic globally based on latency, location, or availability.

💡 **Example:** You can route users from Asia to a Singapore EC2 instance and users from the US to a Virginia instance using latency-based routing.

---

## 🗂 Hosted Zones

| Type                       | Description                                           |
| -------------------------- | ----------------------------------------------------- |
| 🌎 **Public Hosted Zone**  | Used for internet-facing domains (e.g., `myapp.com`). |
| 🏠 **Private Hosted Zone** | Used within a VPC for internal DNS resolution.        |

💡 **Hosted Zone** = Container for DNS records related to a domain.

---

## 📍 Record Types

| Record Type | Purpose                      | Example                                 |
| ----------- | ---------------------------- | --------------------------------------- |
| **A**       | Maps a domain → IPv4 address | `myapp.com → 192.0.2.1`                 |
| **AAAA**    | Maps a domain → IPv6 address | `myapp.com → 2001:db8::1`               |
| **CNAME**   | Maps domain → another domain | `www.myapp.com → myapp.com`             |
| **Alias**   | AWS-specific record mapping  | `myapp.com → CloudFront / ALB / S3`     |
| **MX**      | Mail Exchange records        | Used for email routing                  |
| **TXT**     | Text records                 | Used for verification (e.g., DKIM, SPF) |
| **NS**      | Nameserver records           | Delegates a domain to Route 53          |
| **SOA**     | Start of Authority           | Contains domain admin and refresh info  |

💡 **Alias records** are preferred in AWS — they support root domains and are **free of DNS query charges**.

---

## 🧠 Routing Policies

| Policy                    | Description                                              | Use Case                                  |
| ------------------------- | -------------------------------------------------------- | ----------------------------------------- |
| **Simple Routing**        | Single resource                                          | Basic record mapping                      |
| **Weighted Routing**      | Traffic split by percentage                              | A/B testing or blue-green deployments     |
| **Latency-Based Routing** | Routes users to the region with lowest latency           | Improves user performance                 |
| **Failover Routing**      | Primary-active, standby-passive setup                    | DR and HA                                 |
| **Geolocation Routing**   | Based on user’s country/continent                        | Regional content delivery                 |
| **Geoproximity Routing**  | Routes based on geographic proximity (with bias control) | Region-prioritized load balancing         |
| **Multi-Value Answer**    | Returns multiple healthy IPs                             | Simple load balancing and fault tolerance |

💡 You can **combine routing policies** with **health checks** for automatic failover.

---

## 💓 Health Checks

* Monitors **endpoints** (HTTP, HTTPS, TCP).
* Detects failures and removes unhealthy resources from DNS responses.
* Can trigger **CloudWatch alarms** and **SNS notifications**.
* Used with:

  * ✅ **Failover Routing**
  * ✅ **Multi-Value Answer Routing**

**Example:**
If an EC2 web server fails health checks, Route 53 automatically directs users to a backup instance.

---

## 🔗 Alias Records vs CNAME

| Feature                 | **Alias Record**                                      | **CNAME Record** |
| ----------------------- | ----------------------------------------------------- | ---------------- |
| **AWS-Only Feature**    | ✅ Yes                                                 | ❌ No             |
| **Root Domain Support** | ✅ Yes (`example.com`)                                 | ❌ No             |
| **Cost**                | Free                                                  | Paid DNS query   |
| **Target**              | AWS services (e.g., ALB, CloudFront, S3, API Gateway) | Any domain       |
| **DNS Query Type**      | Returns A/AAAA                                        | Returns CNAME    |

💡 **Best Practice:** Always use **Alias** for AWS service mappings (e.g., CloudFront or ALB).

---

## 🔧 Integration with AWS

Route 53 seamlessly integrates with other AWS services:

| AWS Service                         | Integration Example                         |
| ----------------------------------- | ------------------------------------------- |
| **CloudFront**                      | Connect CDN distributions via Alias records |
| **Elastic Load Balancer (ALB/NLB)** | Route traffic to load balancers             |
| **S3 (Static Hosting)**             | Map domain → S3 bucket website endpoint     |
| **API Gateway**                     | Custom domain mapping                       |
| **Global Accelerator**              | Optimize cross-region latency               |
| **Route 53 Resolver**               | Hybrid DNS resolution (AWS ↔ On-prem)       |

💡 You can create **private DNS** zones for internal microservices inside a VPC.

---

## 🛡️ Security & Reliability

* **Anycast global network** → Routes users to the nearest DNS server.
* **DNS Failover** → Automatic redirection to healthy resources.
* **Private DNS** → Restrict domain resolution to internal AWS networks.
* **IAM integration** → Granular control for DNS management operations.
* **DDoS protection** → Built-in via AWS Shield and Route 53 infrastructure.
* **Query logging** → Store DNS queries in CloudWatch Logs or S3 for auditing.

💡 Route 53 is one of the **most resilient and globally distributed** DNS systems in the world.

---

## 🧠 Quick Revision Hooks

| Concept                 | Quick Recall                          |
| ----------------------- | ------------------------------------- |
| **Route 53**            | AWS’s managed DNS service             |
| **Hosted Zone**         | Container for domain records          |
| **Alias Record**        | AWS mapping (works at root)           |
| **CNAME**               | Domain → Domain mapping               |
| **Health Check**        | Monitors endpoint health              |
| **Latency Routing**     | Directs user to nearest AWS region    |
| **Failover Routing**    | Auto DR between primary and secondary |
| **Geolocation Routing** | Serve region-specific content         |

---

✅ **Final Tip:**
Use **Route 53 + CloudFront + ALB** for **low-latency, fault-tolerant, global web architectures**.
For private workloads, pair **Private Hosted Zones + VPC Endpoints** to manage internal DNS securely.

