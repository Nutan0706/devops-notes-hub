# Amazon VPC Interview Questions

# 🧠 AWS VPC – Interview Questions (Beginner → Advanced + Scenarios)

A structured list of VPC interview questions commonly asked in AWS/Cloud/DevOps interviews.

---

<details>
<summary><h2>🔥 10 Commonly Asked VPC Questions</h2></summary>

1. **What is a VPC in AWS?**  
2. **What is the difference between Public and Private Subnet?**  
3. **What is an Internet Gateway (IGW)? Why is it used?**  
4. **How can an EC2 instance in a private subnet access the Internet?**  
5. **What is the difference between Security Groups and NACLs?**  
6. **What is a Route Table and why do we need it?**  
7. **What is VPC Peering?**  
8. **What are VPC Endpoints and why do we use them?**  
9. **What is CIDR in VPC?**  
10. **What is a NAT Gateway and how is it different from a NAT Instance?**  

</details>

---

<details>
<summary><h2>⚙️ 10 Moderate Level Questions</h2></summary>

1. **Can a Security Group span across multiple VPCs?**  
2. **Can a Subnet span multiple Availability Zones? Explain why.**  
3. **Explain Stateful vs Stateless with examples in VPC.**  
4. **Why is VPC Peering not transitive?**  
5. **Difference between Interface Endpoint and Gateway Endpoint?**  
6. **When would you choose Transit Gateway instead of VPC Peering?**  
7. **What is an Egress-Only Internet Gateway and when is it used?**  
8. **How do Flow Logs help in troubleshooting connectivity issues?**  
9. **What is AWS PrivateLink? How is it different from VPC Peering?**  
10. **How can you restrict public access to S3 while accessing it from VPC?**  
   *(Hint: VPC Endpoint + Bucket Policy)*  

</details>

---

<details>
<summary><h2>🚀 10 Advanced VPC Questions</h2></summary>

1. **How does Transit Gateway enable multi-VPC and hybrid connectivity?**  
2. **What is the difference between Transit Gateway, VPC Peering, and PrivateLink?**  
3. **Explain how DNS resolution works inside VPC. (Route 53 Resolver, DHCP Options Set)**  
4. **How do you design a multi-account VPC architecture following AWS best practices?**  
5. **Explain the role of Prefix Lists in managing network access.**  
6. **What is VPC Sharing and when should you use it?**  
7. **How would you secure workloads inside VPC using NACLs + SGs + WAF + Firewall Manager?**  
8. **How does AWS Direct Connect differ from VPN? When do we use both together?**  
9. **How do you implement centralized egress for multiple VPCs?**  
10. **Explain the packet flow from a Private EC2 instance to S3 using a VPC Endpoint.**  

</details>

---

<details>
<summary><h2>🧩 10 Scenario-Based VPC Questions (Real-World)</h2></summary>

> These are asked for 4+ years DevOps / Cloud Engineer roles.

**Scenario 1:**  
Your EC2 instance in a private subnet cannot reach the internet. How will you troubleshoot?  
*(Hint: Route table → NAT → SG → NACL → IGW in public subnet)*  

**Scenario 2:**  
Two VPCs (A & B) are peered. A can reach B, but B cannot reach A. Why?  
*(Hint: Routing + SG + NACL misconfig)*  

**Scenario 3:**  
You need to securely expose a service in your VPC to **only one customer’s VPC** in another account. What will you choose?  
*(Hint: PrivateLink)*  

**Scenario 4:**  
Your organisation has 10 VPCs and must connect them + on-prem. What solution is best and why?  
*(Hint: Transit Gateway)*  

**Scenario 5:**  
A Private Subnet EC2 needs to pull Docker images from ECR without internet. How?  
*(Hint: VPC Endpoint for ECR + S3)*  

**Scenario 6:**  
Traffic between two VPCs in different regions is slow. How to optimize?  
*(Hint: Inter-region VPC peering → uses AWS backbone network)*  

**Scenario 7:**  
Your database in private subnet should only accept traffic from one application subnet. Describe configuration.  
*(Hint: SG rules + avoid wide NACL rules)*  

**Scenario 8:**  
How do you allow on-prem systems to securely connect to your VPC? Provide 3 architectures.  
*(Hint: VPN, DX, VPN + DX, TGW + DX)*  

**Scenario 9:**  
You need to give developers restricted access to only one subnet in VPC. How?  
*(Hint: IAM + SCP + NACL + SG + SSM Session Manager)*  

**Scenario 10:**  
Your NAT Gateway bill is too high. How do you reduce cost?  
**Possible solutions:**  
- Use **1 NAT per AZ only if required**  
- Use **S3 + DynamoDB VPC Endpoints**  
- **Proxy** or **split traffic**  

</details>

---
