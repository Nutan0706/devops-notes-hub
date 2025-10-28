# 📘 AWS Route 53 — Interview Questions

This file contains categorized Route 53 interview questions to help prepare for beginner to expert-level interviews.

---

## 📑 Table of Contents
- [Basic / Frequently Asked (10)](#-basic--frequently-asked-10)
- [Moderate Level (10)](#-moderate-level-10)
- [Advanced + Deep Technical (10)](#-advanced--deep-technical-10)
- [Scenario-Based Questions (10)](#-scenario-based-questions-10)

---

<details>
<summary><h2>🟢 Basic / Frequently Asked (10)</h2></summary>

1. What is Amazon Route 53 and why is it called “53”?
2. What are the main functions of Route 53?
3. Difference between **Public** and **Private Hosted Zones**?
4. What is a **Hosted Zone**?
5. What is the purpose of a **Health Check** in Route 53?
6. What is the difference between **A**, **AAAA**, and **CNAME** record types?
7. What is an **Alias Record** and how is it different from CNAME?
8. What are the most commonly used **Routing Policies** in Route 53?
9. Can you use a **CNAME** at the root domain (apex)? Why or why not?
10. What services can Route 53 integrate with?

</details>

---

<details>
<summary><h2>🟡 Moderate Level (10)</h2></summary>

1. How does Route 53 achieve high availability and low-latency DNS resolution?
2. Explain **Weighted Routing Policy** with a real-world example.
3. When would you use **Latency-Based Routing** vs **Geolocation Routing**?
4. What is **Multi-Value Answer Routing**? How is it different from a load balancer?
5. How do Health Checks work internally and how do they remove bad endpoints?
6. What is **Route 53 Failover Routing** and how does it work?
7. What is **Route 53 Resolver** and when would you use it?
8. What is the difference between **Geolocation** and **Geoproximity** routing?
9. Can Route 53 be used for **hybrid DNS** (on-prem + AWS)? How?
10. How does Route 53 help in **Disaster Recovery** architectures?

</details>

---

<details>
<summary><h2>🔴 Advanced & Deep Technical (10)</h2></summary>

1. How does Route 53 use **Anycast** for DNS routing, and why is it beneficial?
2. Explain the internal mechanism of DNS caching & TTL in Route 53.
3. How would you design a global multi-region application using Route 53 with **Active-Active** architecture?
4. How can Route 53 be used with **Global Accelerator** vs **CloudFront**? Compare.
5. How does Route 53 manage **Split-Horizon DNS**?
6. Can Route 53 be used to route traffic across **on-prem + multiple AWS accounts + multiple VPCs**?
7. How do you implement **zero-downtime DNS migration** using Route 53?
8. What are the security considerations when using Route 53 for internal DNS?
9. Why are **Alias** queries free in Route 53 but normal DNS queries are charged?
10. How does Route 53 handle DNS Failover for **Stateful Applications**?

</details>

---

<details>
<summary><h2>🧠 Scenario-Based Questions (10)</h2></summary>

> These are real interview-style scenario questions.

| # | Scenario |
|---|-----------|
| 1 | Your application is deployed in **2 regions** (us-east-1 & ap-south-1); you want users to go to the **closest region** automatically. Which routing policy would you choose and why? |
| 2 | You want to shift **20% of traffic** to a new version of your app for testing. Which routing policy should you use? |
| 3 | Your primary region goes down. Route 53 should failover to **DR region**—how would you configure it? |
| 4 | You want users in **India** to be routed to the Mumbai region, and European users to Frankfurt. What routing policy fits here? |
| 5 | SaaS company needs **different login pages for different continents**—which routing policy works best? |
| 6 | You want to provide **6 healthy IPs** of backend servers to users instead of using a load balancer—how to achieve? |
| 7 | You host a **private internal domain** for multiple VPCs across AWS accounts. How do you resolve DNS privately across them? |
| 8 | You need to route traffic based on **latency but slightly more traffic should always go to us-west-1**. Which routing policy? |
| 9 | Client wants to migrate DNS from GoDaddy to Route 53 **without downtime**—explain steps. |
| 10 | You need Route 53 to monitor **API health** and switch traffic to another region **only if HTTP response contains specific text**. How would you configure? |

</details>

---

### ⭐ Tip for GitHub Readers  
Use the dropdowns above to **practice level-wise**. Start with Basic → Moderate → Advanced → Scenarios.

---
