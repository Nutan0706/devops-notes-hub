# 🚀 AWS CloudFront — Complete Concepts Guide

AWS **CloudFront** is a **global Content Delivery Network (CDN)** service that securely delivers data, videos, applications, and APIs to users with **low latency**, **high transfer speed**, and **built-in security** — using AWS **Edge Locations**.

---

## 📘 Table of Contents

* [What is CloudFront?](#-what-is-cloudfront)
* [Key Components](#-key-components)
* [How CloudFront Works](#-how-cloudfront-works)
* [Cache Behavior & Policies](#-cache-behavior--policies)
* [Security in CloudFront](#-security-in-cloudfront)
* [Integration with AWS Services](#-integration-with-aws-services)
* [Pricing Model](#-pricing-model)
* [Common Use Cases](#-common-use-cases)
* [Important CLI Commands](#-important-cli-commands)

---

## 📍 What is CloudFront?

CloudFront is a **global CDN** that accelerates the delivery of content such as HTML, images, videos, APIs, and software across the globe using distributed **Edge Locations**.

| Feature              | Description                                         |
| -------------------- | --------------------------------------------------- |
| **Type**             | Global Content Delivery Network                     |
| **Edge Locations**   | 600+ Points of Presence worldwide                   |
| **Protocol Support** | HTTP, HTTPS, HTTP/2, QUIC                           |
| **Integrates With**  | S3, EC2, ALB, API Gateway, MediaStore, MediaPackage |

💡 **Benefit:** Improves performance, reduces load on origin servers, and provides DDoS protection & encryption via AWS Shield and WAF.

---

## 🧱 Key Components

| Component                   | Description                                                                     |
| --------------------------- | ------------------------------------------------------------------------------- |
| **Origin**                  | The source of your content (e.g., S3 bucket, ALB, EC2, API, or on-prem server). |
| **Edge Location**           | Local caching servers placed globally to serve content closer to users.         |
| **Distribution**            | The CDN configuration — defines origins, cache behaviors, and settings.         |
| **Origin Group / Failover** | Ensures high availability by switching to a secondary origin on failure.        |
| **Cache Behavior**          | Rules that control cache settings, HTTP methods, headers, and cookies.          |

---

## 🛠️ How CloudFront Works

### 📦 Request Flow

```
User Request → Nearest Edge Location → Cache Hit? → Yes → Served from Cache
                                           ↓ No
                                 Request sent to Origin → Cache → Serve
```

* **Cache Hit** → Content served instantly from nearest edge = ⚡ Faster
* **Cache Miss** → Fetched from origin → Stored in cache for next requests

💡 **Goal:** Minimize origin fetches by using optimized cache behaviors.

---

## 🎚️ Cache Behavior & Policies

| Policy Type                 | Description                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| **Cache Policy**            | Controls what CloudFront caches (headers, cookies, query strings). |
| **Origin Request Policy**   | Defines what CloudFront forwards to your origin.                   |
| **Response Headers Policy** | Adds headers like HSTS, CSP, and Security Headers.                 |

### 🔄 Cache Invalidation

```bash
aws cloudfront create-invalidation \
  --distribution-id ABC123 \
  --paths "/*"
```

> 💡 **Tip:** Use **object versioning** (`index_v2.html`) instead of frequent invalidations to save cost.

---

## 🛡️ Security in CloudFront

| Security Feature                | Description                                                                   |
| ------------------------------- | ----------------------------------------------------------------------------- |
| **AWS WAF**                     | Protects against SQL injection, XSS, and other attacks.                       |
| **AWS Shield Standard**         | Free automatic DDoS protection.                                               |
| **Origin Access Control (OAC)** | Restricts S3 buckets to allow access **only from CloudFront** (replaces OAI). |
| **Geo-Restriction**             | Allow or deny content access based on country.                                |
| **HTTPS Only**                  | Enforce SSL/TLS to secure content delivery.                                   |
| **Signed URLs / Cookies**       | Restrict access to paid or premium content.                                   |

💡 **Best Practice:** Always use **OAC + HTTPS + WAF** for production-grade security.

---

## 🔗 Integration with AWS Services

| AWS Service                   | Integration Purpose                                             |
| ----------------------------- | --------------------------------------------------------------- |
| **S3**                        | Deliver static websites securely with OAC restriction.          |
| **ALB / EC2**                 | Accelerate dynamic web content delivery.                        |
| **API Gateway**               | Reduce latency for API responses.                               |
| **Lambda@Edge**               | Execute custom logic near users (e.g., redirects, auth).        |
| **CloudFront Functions**      | Lightweight JavaScript functions for quick header manipulation. |
| **MediaPackage / MediaStore** | Enable optimized video streaming (HLS/DASH).                    |

💡 Use **CloudFront Functions** for lightweight edge logic and **Lambda@Edge** for complex transformations.

---

## 💰 Pricing Model

| Area               | Cost Drivers                                          |
| ------------------ | ----------------------------------------------------- |
| **Data Transfer**  | Based on region and destination (cheaper near users). |
| **Requests**       | Charged per million HTTP/HTTPS requests.              |
| **Invalidations**  | 1,000 paths/month free; beyond that billed per path.  |
| **Edge Functions** | CloudFront Functions & Lambda@Edge billed separately. |

✅ **Optimization Tips:**

* Enable **compression** (GZIP, Brotli).
* Use **cache-control headers** effectively.
* Keep invalidations minimal and rely on **versioned file names**.

---

## 📦 Common Use Cases

| Use Case                        | Description                                             |
| ------------------------------- | ------------------------------------------------------- |
| 🌐 **Static Website Delivery**  | S3 + CloudFront combo for fast global static hosting.   |
| 🎬 **Video Streaming**          | Stream videos via HLS or DASH for low-latency playback. |
| ⚡ **API Acceleration**          | Cache GET API responses close to end users.             |
| 🔐 **Premium Content Delivery** | Use Signed URLs or Cookies for restricted access.       |
| 🛡️ **Security Layer**          | Protect origins with WAF, Shield, and OAC.              |

💡 *CloudFront is ideal for global scalability and edge-level security.*

---

## 🧑‍💻 Important CLI Commands

| Purpose                        | Command                                                                                                              |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **Create Invalidation**        | `aws cloudfront create-invalidation --distribution-id DIST_ID --paths "/*"`                                          |
| **List Distributions**         | `aws cloudfront list-distributions`                                                                                  |
| **Get Distribution Config**    | `aws cloudfront get-distribution-config --id DIST_ID`                                                                |
| **Update Distribution Config** | `aws cloudfront update-distribution --id DIST_ID --if-match E2QWRUHAPOMF69 --distribution-config file://config.json` |

> 🔹 Replace `DIST_ID` with your CloudFront Distribution ID.
> 🔹 Use `--if-match` header for version consistency when updating distributions.

---

## 🧠 Quick Revision Hooks

| Concept           | Memory Trick                             |
| ----------------- | ---------------------------------------- |
| **CloudFront**    | Global CDN = Faster content delivery     |
| **Edge Location** | Local cache server near user             |
| **OAC**           | Secure S3 access only via CloudFront     |
| **Lambda@Edge**   | Run custom logic globally                |
| **Cache Policy**  | Controls what CloudFront stores          |
| **Invalidation**  | Clears old cache (costly, use carefully) |

---

✅ **Final Tip:**
Use CloudFront for **global scale, security, and performance** — combine it with **S3 + OAC** for static sites, **ALB/API Gateway** for APIs, and **Lambda@Edge** for dynamic personalization at the edge.
