# 🌐 AWS Route 53 Practical Learning Guide


## 🟢 10 Beginner-Level Practicals — Core Route 53 Concepts

These exercises will help you understand the **foundations of AWS Route 53**, including DNS basics, hosted zones, and record management.

| No. | Practical                                | Description                                                                                                  |
| --- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 1️⃣ | **Register a Domain (Optional)**         | Register a new domain in Route 53 (or use an existing one) to start managing DNS records.                    |
| 2️⃣ | **Create a Public Hosted Zone**          | Create a hosted zone for your domain (e.g., `mydevopslab.com`) and explore the default NS & SOA records.     |
| 3️⃣ | **Add an A Record (Simple Routing)**     | Create an A record that points your domain to an EC2 instance’s Elastic IP. Test with `nslookup` or browser. |
| 4️⃣ | **Add CNAME Record for Subdomain**       | Create a CNAME record (e.g., `www.mydevopslab.com → mydevopslab.com`). Verify using `dig`.                   |
| 5️⃣ | **Create MX Record for Email Routing**   | Configure an MX record for custom mail routing (use AWS WorkMail or external mail service).                  |
| 6️⃣ | **Set TTL for DNS Records**              | Experiment with different TTL values and observe how quickly DNS changes propagate.                          |
| 7️⃣ | **Use Alias Record for AWS Services**    | Point your domain to an AWS resource like S3 static website or CloudFront using Alias records.               |
| 8️⃣ | **Create a Private Hosted Zone**         | Create a private hosted zone and associate it with a VPC for internal DNS resolution.                        |
| 9️⃣ | **Test DNS Resolution inside VPC**       | Launch an EC2 instance in the VPC and use `dig` to test private DNS resolution.                              |
| 🔟  | **Delete & Recreate Hosted Zone Safely** | Practice deleting a hosted zone without losing records and re-creating it properly.                          |

---

## 🟡 10 Intermediate-Level Practicals — Real-World Scenarios

These practicals cover **traffic routing policies, health checks, and automation** that make Route 53 a true global-scale DNS service.

| No. | Practical                                      | Description                                                                              |
| --- | ---------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 1️⃣ | **Simple Routing Policy Setup**                | Create two A records under a domain and understand how simple routing works.             |
| 2️⃣ | **Weighted Routing Policy**                    | Distribute traffic between two EC2 instances using 70:30 weight distribution.            |
| 3️⃣ | **Latency-Based Routing**                      | Deploy two EC2 instances in different regions and route users based on latency.          |
| 4️⃣ | **Failover Routing Policy**                    | Configure a primary EC2 instance and a backup instance with Route 53 health checks.      |
| 5️⃣ | **Geo-Location Routing Policy**                | Route traffic from India to one region and the US to another using geo-location rules.   |
| 6️⃣ | **Create Health Checks for EC2**               | Create HTTP/HTTPS health checks and attach them to records for automatic failover.       |
| 7️⃣ | **Alias Record to CloudFront**                 | Map a domain name to a CloudFront distribution using Alias records.                      |
| 8️⃣ | **Alias Record to S3 Static Website**          | Configure your S3 bucket as a static site and map it to your custom domain via Route 53. |
| 9️⃣ | **Set Up Subdomain Delegation**                | Delegate a subdomain (e.g., `dev.mydevopslab.com`) to another hosted zone.               |
| 🔟  | **Route 53 + Certificate Manager Integration** | Use Route 53 to validate domain ownership for AWS Certificate Manager SSL setup.         |

---

## 🔴 10 Advanced-Level Practicals — Production & DevOps Use Cases

These simulate **real-life production Route 53 use cases**, focusing on global scalability, hybrid setups, and automation with Infrastructure as Code (IaC).

| No. | Practical                                              | Description                                                                               |
| --- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| 1️⃣ | **Automate Route 53 Setup with Terraform**             | Write Terraform code to create hosted zones and DNS records automatically.                |
| 2️⃣ | **Route 53 with Multi-Region Failover (RDS/EC2)**      | Implement cross-region failover using health checks and failover routing policies.        |
| 3️⃣ | **Hybrid DNS with Private Hosted Zones**               | Integrate Route 53 private zones with on-prem DNS through AWS Resolver endpoints.         |
| 4️⃣ | **Centralized DNS Setup using AWS Organizations**      | Manage DNS across multiple AWS accounts using Route 53 and Resource Access Manager (RAM). |
| 5️⃣ | **Multi-Region Active-Active Setup (Latency Routing)** | Deploy EC2 in two regions and route traffic dynamically using latency-based routing.      |
| 6️⃣ | **Automate DNS Failover with Lambda**                  | Use AWS Lambda to update DNS records automatically during application failover.           |
| 7️⃣ | **Integrate Route 53 with Jenkins Pipeline**           | Automate DNS updates via Jenkins job after deploying new services or environments.        |
| 8️⃣ | **DNSSEC Implementation**                              | Enable DNSSEC for your hosted zone to protect against DNS spoofing attacks.               |
| 9️⃣ | **Monitoring Route 53 Health Checks with CloudWatch**  | Send alerts to SNS when Route 53 detects unhealthy endpoints.                             |
| 🔟  | **Blue-Green Deployment using Weighted Routing**       | Automate zero-downtime deployments by shifting traffic gradually using weighted routing.  |

---

## 🧠 Bonus Tips

* 🧩 **Understand TTL:** Shorter TTL = faster updates, higher query cost.
* 🧰 **Always Enable Health Checks:** Ensure fault tolerance and high availability.
* 🔐 **Use Private Zones for Internal Services:** Avoid exposing internal DNS to the public internet.
* ⚙️ **Integrate with CloudFront & S3:** Route 53 works seamlessly for web hosting and CDN setups.
* 🧾 **Document DNS Records:** Maintain a DNS map of all environments (Dev, Stage, Prod).
* ☁️ **Automate Everything:** Manage DNS with Terraform or AWS CLI for version-controlled infrastructure.

---

## 📚 References

* [AWS Route 53 Documentation](https://docs.aws.amazon.com/route53/)
* [Route 53 Routing Policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)
* [AWS Route 53 Best Practices](https://aws.amazon.com/route53/features/)
* [Terraform Route 53 Module](https://registry.terraform.io/modules/terraform-aws-modules/route53/aws/latest)
* [AWS CLI Route 53 Commands](https://docs.aws.amazon.com/cli/latest/reference/route53/)
