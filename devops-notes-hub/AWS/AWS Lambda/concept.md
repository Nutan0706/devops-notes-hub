# 🧠 AWS Lambda – Complete Concept Sheet

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers.

---

## ✅ Key Highlights

| Feature | Description |
|--------|--------------|
| **Type** | Serverless Compute |
| **Runtime** | Pay only for execution time |
| **Trigger Based** | Executes on events from AWS services |
| **Scalability** | Auto-scales instantly |
| **Pricing** | Based on requests & duration |

---

<details>
<summary><strong>🔸 1. What is AWS Lambda?</strong></summary>

AWS Lambda is a serverless compute service that allows you to run code without managing servers.  
It automatically scales based on the number of incoming requests and charges only for the execution time.

</details>

---

<details>
<summary><strong>⚙️ 2. Supported Languages & Runtime</strong></summary>

| Language | Runtime |
|----------|----------|
| Node.js | nodejs18.x / 20.x |
| Python | python3.8 – 3.12 |
| Java | java11, java17 |
| Go | go1.x |
| .NET | dotnet6 |
| Custom Runtime | Provided.al2 |

</details>

---

<details>
<summary><strong>🚀 3. How Lambda Works (Flow)</strong></summary>

1. Event is triggered (API Gateway, S3, CloudWatch, DynamoDB, etc.).
2. Lambda receives event input as JSON.
3. Code executes inside ephemeral environment.
4. Outputs response or triggers other AWS services.

</details>

---

<details>
<summary><strong>🧵 4. Lambda Event Sources (Triggers)</strong></summary>

| Category | Service Examples |
|----------|------------------|
| API Trigger | API Gateway, ALB |
| Storage Trigger | S3 (Object Upload/Delete) |
| Database Trigger | DynamoDB Streams |
| Messaging | SQS, SNS, EventBridge |
| Cron Jobs | CloudWatch Events |
| IoT | AWS IoT |

</details>

---

<details>
<summary><strong>📦 5. Lambda Deployment Package</strong></summary>

- Can be uploaded as Zip file or Container Image
- Max Deployment Size:
  - **Zip**: 50 MB (compressed) / 250 MB (extracted)
  - **Container**: 10 GB
- Use **Lambda Layers** to include libraries

</details>

---

<details>
<summary><strong>🥞 6. Lambda Layers</strong></summary>

✅ Helps reduce package size by keeping dependencies separate.  
Used for:

- Common libraries
- Language dependencies (NumPy, Pandas)
- Config or shared modules

Max 5 layers per function.

</details>

---

<details>
<summary><strong>📈 7. Concurrency & Scaling</strong></summary>

| Type | Description |
|-------|----------------|
| **Concurrency** | Number of instances running at the same time |
| **Default Limit** | 1,000 concurrent executions per region |
| **Reserved Concurrency** | Limit for a specific function to avoid throttling |
| **Provisioned Concurrency** | Keeps environments warm to reduce cold start |

</details>

---

<details>
<summary><strong>❄️ 8. Cold Start vs Warm Start</strong></summary>

| Cold Start | Warm Start |
|------------|-------------|
| Container needs to be initialized | Already running instance reused |
| Causes delay | Faster execution |
| Frequent in VPC or less-used Lambda | Happens when Lambda recently invoked |

</details>

---

<details>
<summary><strong>🔐 9. Lambda Security</strong></summary>

- IAM Role required for permissions  
- Environment Variables Encryption with KMS  
- VPC Access for private networking  

</details>

---

<details>
<summary><strong>💰 10. Pricing Model</strong></summary>

| Component | Pricing Basis |
|----------|----------------|
| Requests | Per 1M requests |
| Duration | GB-seconds (Execution time × Memory) |
| Free Tier | 1M requests + 400,000 GB-sec |

</details>

---

<details>
<summary><strong>👨‍💻 11. Lambda Best Practices</strong></summary>

- Use environment variables for config
- Keep functions small and single-purpose (**micro-function architecture**)
- Use **async processing** with SQS or EventBridge
- Minimize cold starts via **Provisioned Concurrency**
- Implement **structured logging** (JSON logs)

</details>

---

## 📍 Architecture Diagram (High-Level)
Client → API Gateway → Lambda → DynamoDB

---

## 🧠 Quick Memory Hooks (for Revision)

| Concept | One-Line Memory Trick |
|--------|--------------------------|
| Lambda | Run code without servers |
| Trigger | Lambda wakes up on events |
| Layer | Shared libraries = Less bundle size |
| Cold Start | First request = Slow |
| Provisioned Concurrency | Always warm = No lag |

---


