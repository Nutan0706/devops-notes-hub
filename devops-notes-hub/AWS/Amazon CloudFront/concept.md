# 🚀 AWS CloudFront — Complete Concepts Guide

CloudFront is AWS's **global Content Delivery Network (CDN)** that delivers content with **low latency**, **high performance**, and **security** using AWS edge locations.

---

## 📘 Table of Contents
- [What is CloudFront?](#-what-is-cloudfront)
- [Key Components](#-key-components)
- [How CloudFront Works](#-how-cloudfront-works)
- [Cache Behavior & Policies](#-cache-behavior--policies)
- [Security in CloudFront](#-security-in-cloudfront)
- [Integration with AWS Services](#-integration-with-aws-services)
- [Pricing Model](#-pricing-model)
- [Common Use Cases](#-common-use-cases)
- [Important CLI Commands](#-important-cli-commands)

---

<details>
<summary><h2>📍 What is CloudFront?</h2></summary>

CloudFront is a **global CDN** that delivers web content such as HTML, images, videos, APIs, and software with **low latency** and **high transfer speeds**.

| Feature | Description |
|--------|--------------|
| Type | Global CDN |
| Edge Locations | 600+ points of presence globally |
| Protocol Support | HTTP, HTTPS, HTTP/2, QUIC |
| Works With | S3, EC2, ALB, API Gateway, MediaStore, MediaPackage |

> **Benefit:** Improves performance, reduces load on origin, adds security and DDoS protection.

</details>

---

<details>
<summary><h2>🧱 Key Components</h2></summary>

| Component | Description |
|-----------|--------------|
| **Origin** | Source of content (S3, ALB, EC2, on-prem, API) |
| **Edge Location** | Caching servers where CloudFront stores cached content |
| **Distribution** | CDN configuration; contains origins + settings |
| **Origin Group/Failover** | Uses secondary origin if primary fails |
| **Cache Behavior** | Rules for cache, path patterns, HTTP methods, headers, cookies |

</details>

---

<details>
<summary><h2>🛠️ How CloudFront Works</h2></summary>

**Flow:**

```text
User Request → Nearest Edge Location → Cache Hit? → Yes → Served from Cache  
                                         ↓ No  
                               Request sent to Origin → Store in Edge Cache → Serve
```
Cache Hit → Faster, no origin call
Cache Miss → Fetch from origin, then cache

</details>

<details> <summary><h2>🎚️ Cache Behavior & Policies</h2></summary>

| Policy Type                 | Usage                                                      |
| --------------------------- | ---------------------------------------------------------- |
| **Cache Policy**            | Controls what gets cached (headers, cookies, query params) |
| **Origin Request Policy**   | Controls what CloudFront sends to origin                   |
| **Response Headers Policy** | Add headers like HSTS, Security headers                    |

Cache Invalidation
```
aws cloudfront create-invalidation \
  --distribution-id ABC123 \
  --paths "/*"
```

Tip: Use versioning instead of frequent invalidations to reduce cost.

</details>

<details> <summary><h2>🛡️ Security in CloudFront</h2></summary>
Security Feature	Description
AWS WAF	Block malicious traffic
Shield Standard	Free DDoS protection
Origin Access Control (OAC)	Secure S3 so only CloudFront can access
Geo-Restriction	Allow/deny countries
HTTPS Only	Enforce secure traffic
Signed URLs/Cookies	Restrict premium content access

OAC replaces OAI for improved S3 origin security (2023+).

</details>

<details> <summary><h2>🔗 Integration with AWS Services</h2></summary>
Service	Integration
S3	Static website hosting, restrict bucket to CloudFront only
ALB / EC2	Dynamic content acceleration
API Gateway	Low-latency API delivery
Lambda@Edge	Run code near users for request/response manipulation
CloudFront Functions	Lightweight JavaScript functions at edge
MediaPackage	Video streaming with DRM
</details>

<details> <summary><h2>💰 Pricing Model</h2></summary>

Costs depend on:

Area	Cost Drivers
Data Transfer	Region-based pricing
HTTP/HTTPS Requests	Charged per million requests
Invalidation Requests	1,000 paths/month free
Functions	CloudFront Functions & Lambda@Edge billed separately

Tip: Enable compression + caching to reduce cost.

</details>

<details> <summary><h2>📦 Common Use Cases</h2></summary>

✅ Static website delivery (S3 + CloudFront)
🎬 Video streaming (HLS/DASH)
🌍 Global API acceleration
🔐 DRM-based premium content delivery
🛡️ Secure content access with Signed URLs/Cookies

</details>

<details> <summary><h2>🧑‍💻 Important CLI Commands</h2></summary>
Purpose	Command
Create Invalidation	aws cloudfront create-invalidation
List Distributions	aws cloudfront list-distributions
Get Config	aws cloudfront get-distribution-config
Update Config	aws cloudfront update-distribution
</details>



