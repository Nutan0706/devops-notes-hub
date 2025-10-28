# ⚡ AWS Lambda – Interview Questions Set

This document contains 40 well-structured interview questions categorized into **Commonly Asked**, **Moderate**, **Advanced**, and **Scenario-Based** levels — formatted for GitHub readability.

---

## 📌 Quick Index  
- [🔹 Commonly Asked (10)](#-commonly-asked-questions-10)
- [🟡 Moderate Level (10)](#-moderate-level-questions-10)
- [🔴 Advanced Level (10)](#-advanced-level-questions-10)
- [🧩 Scenario Based (10)](#-scenario-based-questions-10)

---

## 🔹 Commonly Asked Questions (10)

| No. | Question |
|-----|------------|
| 1 | What is AWS Lambda and why is it used? |
| 2 | List a few AWS services that can trigger a Lambda function. |
| 3 | What is the maximum execution timeout for a Lambda function? |
| 4 | Explain cold start in AWS Lambda. |
| 5 | How does Lambda pricing work? |
| 6 | What are Lambda Layers? |
| 7 | Can Lambda run continuously like a server? |
| 8 | What programming languages are supported by Lambda? |
| 9 | What is the default memory and max memory you can allocate to Lambda? |
| 10 | How do you monitor Lambda performance? |

---

## 🟡 Moderate Level Questions (10)

<details>
<summary><strong>Click to Expand</strong></summary>

| No. | Question |
|-----|------------|
| 1 | What is the difference between **Reserved** and **Provisioned Concurrency**? |
| 2 | What is the use of DLQ (Dead Letter Queue) in Lambda? |
| 3 | How do you secure sensitive environment variables in Lambda? |
| 4 | What are Lambda Destinations? |
| 5 | What is the role of IAM in Lambda? |
| 6 | How do you improve cold start issues in Lambda? |
| 7 | What is the maximum deployment size allowed for Lambda? |
| 8 | Can Lambda access resources inside a VPC? How? |
| 9 | What are Lambda execution context and its reuse? |
| 10 | How do you test Lambda locally before deployment? |

</details>

---

## 🔴 Advanced Level Questions (10)

<details>
<summary><strong>Click to Expand</strong></summary>

| No. | Question |
|-----|------------|
| 1 | How does Provisioned Concurrency work internally and how is it billed? |
| 2 | Explain difference between **SQS + Lambda** vs **SNS + Lambda** architectures. |
| 3 | When should you use Step Functions with Lambda? |
| 4 | What are the limitations of Lambda (timeout, memory, storage, networking)? |
| 5 | How does Lambda handle scaling under sudden spikes? Explain throttling behavior. |
| 6 | Explain container image support for Lambda and use cases. |
| 7 | How does Lambda Versioning and Aliases help in deployments? |
| 8 | How do you handle large dependency packages in Lambda (e.g., NumPy, Pandas)? |
| 9 | What is the difference between Lambda@Edge and CloudFront Functions? |
| 10 | How would you design highly available Lambda architecture across multi-regions? |

</details>

---

## 🧩 Scenario-Based Questions (10)

<details>
<summary><strong>Click to Expand</strong></summary>

| No. | Scenario |
|-----|------------|
| 1 | Your Lambda processing SQS messages is failing randomly. How will you handle retries & failures? |
| 2 | You have a Lambda that takes 20 minutes to process a task, but Lambda max timeout is 15 mins. How will you solve this? |
| 3 | Lambda is invoked frequently and causing high cold starts. What’s the best solution? |
| 4 | You want to deploy Lambda code to Prod without downtime. How? |
| 5 | Lambda processing large files (2GB+) from S3 is failing due to memory/time limits. What’s your approach? |
| 6 | Your Lambda needs to connect to an RDS DB inside a VPC but execution is slow. What should you optimize? |
| 7 | You need to maintain state across multiple Lambda executions. How will you design it? |
| 8 | Your Lambda is triggered twice for every S3 event. How do you prevent duplicate processing? |
| 9 | You need real-time processing of millions of events per minute. Would you use Lambda or something else? Why? |
| 10 | A Lambda interacting with DynamoDB faces throttling errors. How do you fix & optimize throughput? |

</details>

---
