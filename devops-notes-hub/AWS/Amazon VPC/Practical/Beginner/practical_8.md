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

👉 *Add Screenshot Here*

---

## **2️⃣ Allocate a New Elastic IP**

1. Click **Allocate Elastic IP address**
2. Choose:

   * **AWS Pool** (default)
3. Click **Allocate**

You will now see an Elastic IP address (e.g., `3.110.xx.xx`)

👉 *Add Screenshot Here*

---

## **3️⃣ Go to NAT Gateways**

1. Open **VPC Console**
2. Click **NAT Gateways**

👉 *Add Screenshot Here*

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

👉 *Add Screenshot Here*

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

👉 *Add Screenshot Here*

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

👉 *Add Screenshot Here*

---

# 🎉 **Elastic IP + NAT Setup Complete**

You now understand:

* How to allocate an Elastic IP
* How to attach it to NAT Gateway
* How NAT enables internet for Private Subnet
* Why NAT ensures private EC2s stay **secure**


