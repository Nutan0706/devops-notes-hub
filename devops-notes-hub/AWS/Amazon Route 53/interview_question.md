# 🌐 AWS Route 53 — Interview Questions

This document contains **30 Route 53 Interview Questions** categorized into **Basic**, **Moderate**, **Advanced**, and **Scenario-Based** — formatted for GitHub with collapsible sections and tables.

---

## 📑 Table of Contents
- [Basic Interview Questions (10)](#-basic-interview-questions-10)
- [Moderate-Level Questions (10)](#-moderate-level-questions-10)
- [Advanced Questions (10)](#-advanced-questions-10)
- [Scenario-Based Questions](#-scenario-based-questions)

---

<details>
<summary><h2>🟢 Basic Interview Questions (10)</h2></summary>

| # | Question |
|---|-----------|
| 1 | What is Route 53 and why is it called "53"? |
| 2 | What is a Hosted Zone in Route 53? |
| 3 | Difference between Public Hosted Zone and Private Hosted Zone. |
| 4 | What are Alias Records in Route 53? |
| 5 | What is the use of a CNAME record? |
| 6 | Can a CNAME record be used at the root domain? Why/Why not? |
| 7 | What are routing policies in Route 53? Name a few. |
| 8 | What is a Health Check in Route 53? |
| 9 | What DNS record type maps a domain name to an IPv4 address? |
| 10 | What AWS services commonly integrate with Route 53? |

</details>

---

<details>
<summary><h2>🟡 Moderate-Level Questions (10)</h2></summary>

| # | Question |
|---|-----------|
| 11 | When should you use Weighted Routing over Latency-Based Routing? |
| 12 | Explain the difference between Alias and CNAME records with an example. |
| 13 | How does Failover Routing work in Route 53? |
| 14 | What is Multi-Value Answer Routing and how is it different from a Load Balancer? |
| 15 | Which routing policy helps in A/B testing and how? |
| 16 | Can Route 53 be used for on-premise environments? If yes, how? |
| 17 | What is the TTL value in DNS and how does it affect Route 53 responses? |
| 18 | Explain Geolocation vs Geoproximity Routing. |
| 19 | What mechanisms ensure high availability in Route 53? |
| 20 | How do Health Checks integrate with CloudWatch? |

</details>

---

<details>
<summary><h2>🔴 Advanced Questions (10)</h2></summary>

| # | Question |
|---|-----------|
| 21 | How does Route 53 achieve global fault tolerance and low latency routing? |
| 22 | How would DNS-based load balancing differ from Application Load Balancer routing? |
| 23 | Can Route 53 route traffic based on user device type (mobile/web)? If yes/no, explain. |
| 24 | What is Route 53 Resolver and when do you use it? |
| 25 | How do you implement **private DNS** resolution across multiple VPCs? |
| 26 | How does Route 53 support hybrid cloud DNS setups? |
| 27 | How does caching impact DNS failover timing? |
| 28 | What happens if all endpoints fail health checks in Multi-Value Routing? |
| 29 | How do Alias queries remain free while CNAME queries are billed? |
| 30 | Difference between Route 53 and Google DNS/Azure DNS from architecture perspective. |

</details>

---

<details>
<summary><h2>🧠 Scenario-Based Questions</h2></summary>

| Scenario # | Question |
|------------|------------|
| S1 | Your website is hosted in us-east-1, and users in India face latency. Which routing policy will you use and why? |
| S2 | You want Blue/Green deployment for a new release with 90% traffic to old and 10% to new. Which routing policy suits this? |
| S3 | Your primary website is down; traffic must go to DR site automatically. How do you configure it in Route 53? |
| S4 | You need to route EU traffic to EU servers and Asia traffic to Singapore region. Which routing policy helps? |
| S5 | You want to shift 20% of US traffic to the EU region temporarily. Which routing policy will you use? |
| S6 | You need DNS resolution for internal services across 3 VPCs. How will you configure this? |
| S7 | Your app uses on-prem DNS + AWS DNS. How do you integrate them for seamless resolution? |
| S8 | You're using Multi-Value Routing with 6 IPs, 3 become unhealthy. What will Route 53 return? |
| S9 | You must route based on latency but also remove unhealthy endpoints. What two features must you combine? |
| S10 | A client wants a single domain to serve different websites in US, India, and Japan using their nearest servers. Design this. |

</details>

---
