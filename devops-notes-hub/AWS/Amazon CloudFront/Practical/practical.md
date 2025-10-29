# 🧠 AWS CloudFront Practical Learning — For 5 Years Experienced DevOps Engineer

---

## 🟢 Beginner Level (Fundamentals)

| # | Practical Task | Description |
|---|----------------|-------------|
| 1 | **Create Your First CloudFront Distribution** | Deliver content from an S3 bucket using a basic CloudFront setup. |
| 2 | **Understand Edge Locations & Caching** | Learn how CloudFront caches content at edge locations to reduce latency. |
| 3 | **Use Custom Origin (EC2 / ALB)** | Configure CloudFront to deliver content from a custom origin server. |
| 4 | **Enable HTTPS Using Default SSL Certificate** | Serve content securely via HTTPS using the default CloudFront certificate. |
| 5 | **Invalidate Cached Objects** | Manually invalidate outdated files from CloudFront cache. |

---

## 🟡 Intermediate Level (Real-World Scenarios)

| # | Practical Task | Description |
|---|----------------|-------------|
| 6 | **Integrate CloudFront with S3 (Private Bucket)** | Restrict direct S3 access and use Origin Access Control (OAC) for secure delivery. |
| 7 | **Add Custom Domain with ACM Certificate** | Use a custom domain (e.g., cdn.example.com) with AWS Certificate Manager for SSL. |
| 8 | **Enable Access Logs** | Store CloudFront access logs in S3 for monitoring and analytics. |
| 9 | **Configure Geo-Restriction** | Allow or block content delivery to specific countries. |
| 10 | **Set Cache Behaviors & Path Patterns** | Serve different content types (e.g., images, APIs) with different caching rules. |

---

## 🔴 Advanced Level (Enterprise & Automation)

| # | Practical Task | Description |
|---|----------------|-------------|
| 11 | **Integrate CloudFront with WAF (Web Application Firewall)** | Protect your application from SQL injection, XSS, and DDoS attacks. |
| 12 | **Enable Field-Level Encryption** | Encrypt sensitive data fields (like PII) before sending to origin servers. |
| 13 | **Use Lambda@Edge for Request Modification** | Customize headers, URLs, or authentication at edge locations using Lambda@Edge. |
| 14 | **Deploy CloudFront Using Terraform / CloudFormation** | Automate distribution setup with IaC for consistent deployments. |
| 15 | **Optimize Performance Using Origin Shield** | Add an extra caching layer to reduce load on your origins and improve latency. |

---

## ✅ Bonus Practical Tasks for DevOps Engineers

- Integrate **CloudFront with CloudWatch** to monitor cache hit ratio, latency, and error rates.  
- Automate **cache invalidations** using Lambda or CI/CD pipelines.  
- Use **Signed URLs / Signed Cookies** for secure, time-limited content delivery.  
- Combine **CloudFront + S3 + Route 53** for a globally distributed, serverless website.  
- Enable **Real-Time Logs** and push metrics to **Kinesis Data Streams** for analytics dashboards.  

---

> 💡 **Pro Tip:**  
> Always use **Origin Access Control (OAC)** instead of public S3 buckets, enable **WAF for security**, monitor with **CloudWatch metrics**, and deploy CloudFront via **Terraform** for repeatable, version-controlled setups.
