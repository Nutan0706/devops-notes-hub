# 🚀 AWS CloudFront – Interview Questions

<details>
<summary><h2>🟢 10 Commonly Asked Questions</h2></summary>

| # | Question |
|---|-----------|
| 1 | What is Amazon CloudFront and why is it used? |
| 2 | What is a CDN and how does CloudFront work as a CDN? |
| 3 | What are Edge Locations in CloudFront? |
| 4 | What is the difference between **Edge Locations** and **Regional Edge Caches**? |
| 5 | What are **Origin** and **Origin Types** supported by CloudFront? |
| 6 | What is a **Distribution** in CloudFront? |
| 7 | What are **Cache Behaviors**? |
| 8 | What is **TTL (Time To Live)** and how does caching work in CloudFront? |
| 9 | What are **Invalidations**? When do you use them? |
| 10 | What is the difference between **CloudFront** and **S3 Transfer Acceleration**? |

</details>


<details>
<summary><h2>🟡 10 Moderate Level Questions</h2></summary>

| # | Question |
|---|-----------|
| 1 | Explain how **Signed URLs** and **Signed Cookies** work in CloudFront. |
| 2 | What is **Origin Shield** and how does it reduce load on the origin? |
| 3 | What is **Lambda@Edge**? Give a use case. |
| 4 | What is **CloudFront Functions** and how is it different from Lambda@Edge? |
| 5 | How does CloudFront handle **HTTPS, SSL/TLS Certificates**, and **Custom Domains**? |
| 6 | Explain the difference between **Viewer Request** vs **Origin Request** events. |
| 7 | What are the different **Cache Policies** in CloudFront? |
| 8 | What is **Field-Level Encryption** in CloudFront? |
| 9 | What is **Geo-Restriction** and how do you implement it? |
| 10 | How do you integrate CloudFront with **WAF** to block malicious traffic? |

</details>


<details>
<summary><h2>🔴 10 Advanced & Scenario-Based Questions</h2></summary>

| # | Question |
|---|-----------|
| 1 | You updated your website but CloudFront still serves old content. How do you resolve this without invalidating everything? |
| 2 | CloudFront costs increased suddenly due to cache misses. How do you troubleshoot and optimize? |
| 3 | How do you force CloudFront to cache responses for dynamic APIs for 5 minutes? |
| 4 | A user from Germany must be blocked from accessing a video. Explain implementation. |
| 5 | Your content must only be accessible via your mobile app. How do you secure it using CloudFront? |
| 6 | How do you protect S3 origin so that files can be accessed only via CloudFront? |
| 7 | Your application requires custom HTTP headers to be forwarded to the origin. How do you configure? |
| 8 | Explain how CloudFront handles **Multi-CDN architecture** for enterprise use cases. |
| 9 | CloudFront is serving cached content, but you need real-time data for certain API endpoints. How do you architect? |
| 10 | You need to compress images and resize them on the fly before sending to user. Architect a solution using AWS services. |

</details>


---

## 🧠 Scenario Based on "Serving `.mb` / Large Media Files"

<details>
<summary><h2>📂 Handling Large Media Files (.mp4 / .mkv / .mov / .mb etc.)</h2></summary>

| Scenario | Question | Expected Thought Process |
|----------|-----------|---------------------------|
| Large Video File Streaming | How would you design CloudFront architecture to stream a **2GB+ video file** globally with low latency? | Use S3 + CloudFront + HLS/DASH + Segmenting + Cache Behaviors |
| Range Requests | A 900MB file should support pause/resume and buffer seeking. What CloudFront feature enables this? | Enable HTTP **Range Requests** |
| Bandwidth Optimization | How will you reduce data transfer cost when streaming large media? | Use **Origin Shield**, **Cache TTL**, **Regional Edge Caches**, Compression |
| DRM Premium Content | How to restrict premium movie access to only paid users? | **Signed Cookies/URLs**, Token Auth, Lambda@Edge |
| Mobile App Access Only | A movie file should open only inside your mobile app, not browser. How? | Check **User-Agent** using Lambda@Edge + Signed URLs |
| Avoid Cache Invalidation Costs | You update a movie file frequently during editing. How to avoid expensive invalidations? | Use **Versioned File Names** |
| Geo-Blocking Copyright Rules | Movie cannot be streamed in USA due to license restrictions. What feature to use? | **Geo Restriction** (Whitelist/Blacklist) |
| Prevent Direct S3 Access | Ensure no one can download media directly from S3 public URL. | Block Public Access + **OAC** (Origin Access Control) |
| Multi-CDN for OTT Platform | How to design Netflix-like multi-CDN streaming architecture? | CloudFront + Multi CDN + DNS Failover (Route53) |
| Reduce Load on Origin for Huge Traffic | CloudFront hits origin heavily due to cache misses on a viral video. Fix? | Increase TTL, Use Origin Shield, Improve Cache Key Strategy |

</details>

---

