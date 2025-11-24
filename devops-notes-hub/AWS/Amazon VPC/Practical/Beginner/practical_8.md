# **8️⃣ Elastic IP and NAT Overview**

Allocate an Elastic IP (EIP) & understand how NAT Gateway provides internet for private subnets.

Add your screenshots after each step.

---

# 🌐 **8. Elastic IP and NAT Gateway Overview**

This section explains how to:

* Allocate an **Elastic IP**
* Create a **NAT Gateway**
* Understand how NAT enables **internet access for private EC2 instances**

---

# 🚀 **Step-by-Step Guide**

---

## **1️⃣ Go to Elastic IP Section**

1. Open **AWS Console → EC2 Dashboard**
2. From the left panel, click **Elastic IPs**

<img width="1899" height="239" alt="image" src="https://github.com/user-attachments/assets/333d27f4-6f06-4e14-9ff7-3cb2d0d941c8" />


---

## **2️⃣ Allocate a New Elastic IP**

1. Click **Allocate Elastic IP address**
2. Choose:

   * **AWS Pool** (default)
3. Click **Allocate**

You will now see an Elastic IP address (e.g., `3.110.xx.xx`)

<img width="1015" height="206" alt="image" src="https://github.com/user-attachments/assets/2b17d24b-36bc-4862-85c0-69de8dd0e6ec" />


---

## **3️⃣ Go to NAT Gateways**

1. Open **VPC Console**
2. Click **NAT Gateways**

<img width="1711" height="180" alt="image" src="https://github.com/user-attachments/assets/4a801fb3-2637-4ca4-8496-8120bc6c3d6c" />


---

## **4️⃣ Create a NAT Gateway**

1. Click **Create NAT Gateway**
2. Fill the details:

| Field          | Value                    |
| -------------- | ------------------------ |
| **Name**       | `my-nat-gateway`         |
| **Subnet**     | Select **Public Subnet** |
| **Elastic IP** | Choose the allocated EIP |

3. Click **Create NAT Gateway**

<img width="1308" height="730" alt="image" src="https://github.com/user-attachments/assets/798b4506-376e-46a6-bd3f-3e03aa80f8eb" />


---

## **5️⃣ Update Route Table for Private Subnet**

To allow Private EC2 to access the internet:

1. Go to **Route Tables**
2. Select the **private route table**
3. Go to **Routes → Edit Routes**
4. Add:

| Destination | Target                                    |
| ----------- | ----------------------------------------- |
| `0.0.0.0/0` | **NAT Gateway ID** (e.g., `nat-0abd1234`) |

5. Save changes

<img width="1310" height="265" alt="image" src="https://github.com/user-attachments/assets/32c64bf9-067a-48d5-a6c2-ce13a09d8eae" />


---

# 🧠 **Understanding How NAT Gateway Works**

### ✔ Public Subnet

* Has **IGW route**
* EC2 gets **Public IP**
* Can communicate with the internet **directly**

### ✔ Private Subnet

* Has no direct internet access
* Instead uses the **NAT Gateway**, which:

  * Uses **Elastic IP**
  * Forwards **outbound** traffic from Private Subnet → Internet
  * Prevents **inbound** connections from the Internet
  * Acts as a secure middle layer

### 🔄 Flow Example

Private EC2 → NAT Gateway → Internet
Internet → NAT Gateway → **blocked** (no inbound to private)

---

# 🧪 **Test Internet Access From Private EC2**

SSH into **Public EC2**, then connect to Private EC2:

```bash
ssh -i my-key.pem ec2-user@<PRIVATE_IP>
```

Now from the Private EC2:

```bash
ping google.com
sudo yum update -y   # or sudo apt update
```

Expected:
✔ Ping & updates work (outbound allowed)
❌ No one can SSH into private EC2 from the internet


---

# 🎉 **Elastic IP + NAT Setup Complete**

You now understand:

* How to allocate an Elastic IP
* How to attach it to NAT Gateway
* How NAT enables internet for Private Subnet
* Why NAT ensures private EC2s stay **secure**



