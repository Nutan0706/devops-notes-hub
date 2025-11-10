# 🌐 AWS Route 53 — Interview Questions

This document contains **40+ AWS Route 53 interview questions**, categorized into **Basic**, **Moderate**, **Advanced**, and **Scenario-Based** sections — formatted for GitHub readability.

---

## 📑 Table of Contents

* [🟢 Basic Interview Questions (10)](#-basic-interview-questions-10)
* [🟡 Moderate-Level Questions (10)](#-moderate-level-questions-10)
* [🔴 Advanced Questions (10)](#-advanced-questions-10)
* [🧠 Scenario-Based Questions (10)](#-scenario-based-questions-10)

---

## 🟢 Basic Interview Questions (10)

| #  | Question                                                                               |
| -- | -------------------------------------------------------------------------------------- |
| 1  | What is Route 53 and why is it called “53”?                                            |
| 2  | What is a Hosted Zone in Route 53?                                                     |
| 3  | What is the difference between a **Public Hosted Zone** and a **Private Hosted Zone**? |
| 4  | What are **Alias Records** in Route 53?                                                |
| 5  | What is the purpose of a **CNAME record**?                                             |
| 6  | Can a CNAME record be used at the root domain? Why or why not?                         |
| 7  | What are **Routing Policies** in Route 53? Name a few.                                 |
| 8  | What is a **Health Check** in Route 53?                                                |
| 9  | Which DNS record type maps a domain name to an IPv4 address?                           |
| 10 | Which AWS services commonly integrate with Route 53?                                   |

---

## 🟡 Moderate-Level Questions (10)

| #  | Question                                                                                    |
| -- | ------------------------------------------------------------------------------------------- |
| 11 | When should you use **Weighted Routing** over **Latency-Based Routing**?                    |
| 12 | Explain the difference between **Alias** and **CNAME records** with an example.             |
| 13 | How does **Failover Routing** work in Route 53?                                             |
| 14 | What is **Multi-Value Answer Routing**, and how does it differ from a Load Balancer?        |
| 15 | Which routing policy helps in **A/B testing**, and how?                                     |
| 16 | Can Route 53 be used for **on-premises environments**? If yes, how?                         |
| 17 | What is the **TTL (Time to Live)** value in DNS, and how does it affect Route 53 responses? |
| 18 | Explain **Geolocation Routing** vs **Geoproximity Routing**.                                |
| 19 | What mechanisms ensure **high availability** in Route 53?                                   |
| 20 | How do **Health Checks** integrate with **CloudWatch** for monitoring?                      |

---

## 🔴 Advanced Questions (10)

| #  | Question                                                                                        |
| -- | ----------------------------------------------------------------------------------------------- |
| 21 | How does Route 53 achieve **global fault tolerance** and **low-latency routing**?               |
| 22 | How does **DNS-based load balancing** differ from **Application Load Balancer routing**?        |
| 23 | Can Route 53 route traffic based on **user device type (mobile/web)**? Explain why or why not.  |
| 24 | What is the **Route 53 Resolver**, and when would you use it?                                   |
| 25 | How can you implement **private DNS resolution** across multiple VPCs?                          |
| 26 | How does Route 53 support **hybrid cloud DNS setups**?                                          |
| 27 | How does **DNS caching** impact failover timing in Route 53?                                    |
| 28 | What happens if **all endpoints fail health checks** in Multi-Value Answer Routing?             |
| 29 | Why are **Alias queries** free while **CNAME queries** are billed?                              |
| 30 | Compare **Route 53**, **Google Cloud DNS**, and **Azure DNS** from an architecture perspective. |

---

## 🧠 Scenario-Based Questions (10)

| #   | Scenario                         | Question                                                                                                                     |
| --- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| S1  | 🌎 **Latency Issue**             | Your website is hosted in `us-east-1`, and users in India face high latency. Which routing policy will you use and why?      |
| S2  | 🧩 **Blue/Green Deployment**     | You want 90% of traffic on old version and 10% on new. Which routing policy suits this scenario?                             |
| S3  | 💀 **Disaster Recovery**         | Your primary website is down. How can Route 53 automatically send traffic to a DR site?                                      |
| S4  | 🌍 **Regional Routing**          | You want EU traffic to go to Frankfurt and Asia traffic to Singapore. Which routing policy will you use?                     |
| S5  | 🔄 **Traffic Shifting**          | You want to shift 20% of US traffic to the EU temporarily. Which policy fits best?                                           |
| S6  | 🧱 **Private DNS Across VPCs**   | You need DNS resolution for internal services across 3 VPCs. How will you configure this?                                    |
| S7  | 🏢 **Hybrid DNS**                | Your app uses both on-prem and AWS DNS. How will you integrate them for seamless resolution?                                 |
| S8  | 💓 **Unhealthy Endpoints**       | You use Multi-Value Routing with 6 IPs; 3 become unhealthy. What will Route 53 return?                                       |
| S9  | ⚡ **Combined Policies**          | You want latency-based routing but also need to remove unhealthy endpoints. What two features should you combine?            |
| S10 | 🗺 **Multi-Region App Delivery** | A client wants a single domain to serve users in US, India, and Japan via their nearest servers. Design this Route 53 setup. |

---

## 🧩 Quick Revision Summary

| Concept                   | Description                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| **Route 53**              | AWS’s fully managed DNS and domain registration service             |
| **Hosted Zone**           | Container for all DNS records of a domain                           |
| **Alias Record**          | AWS-optimized record type for services like S3, CloudFront, and ALB |
| **Routing Policies**      | Define how Route 53 responds to DNS queries                         |
| **Health Checks**         | Monitor endpoint health and enable automatic failover               |
| **Latency-Based Routing** | Sends users to the AWS region with lowest latency                   |
| **Failover Routing**      | Automatically redirects traffic to standby site during failure      |
| **Private Hosted Zone**   | DNS for internal resolution within VPC                              |
| **Route 53 Resolver**     | Enables hybrid DNS (AWS ↔ On-premises integration)                  |

---

✅ **Final Tip:**
When preparing for Route 53 interviews — focus on:

* Understanding **Routing Policies** (Weighted, Latency, Failover, Geolocation).
* Knowing **Alias vs CNAME differences** with examples.
* Designing **High Availability architectures** using Health Checks + Failover.
* Explaining **Hybrid DNS** setups using Route 53 Resolver.
