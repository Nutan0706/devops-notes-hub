# 🏗️ **Create Public and Private Subnets (AWS VPC Practical)**

Add **one Public** and **one Private Subnet** in **different Availability Zones**.
Also understand **Subnet CIDR allocation**.

---

## ✅ **Prerequisites**

* A custom VPC already created (example: **10.0.0.0/16**)
* AWS Console access

---

# 🚀 **Step-by-Step Guide**

---

## **1️⃣ Open VPC Console**

1. Go to **AWS Console → VPC**
2. From the left panel, click **Subnets**

---

## **2️⃣ Click "Create Subnet"**

1. Choose your existing **Custom VPC**
2. Click **Create Subnet**

---

## **3️⃣ Create Public Subnet**

Fill the fields:

| Field                 | Value                    |
| --------------------- | ------------------------ |
| **VPC ID**            | Select your custom VPC   |
| **Subnet Name**       | `public-subnet-1`        |
| **Availability Zone** | `us-east-1a` (any 1 AZ) |
| **IPv4 CIDR block**   | `10.0.1.0/24`            |

Click **Create Subnet**

<img width="1084" height="751" alt="image" src="https://github.com/user-attachments/assets/2d7a2576-38b8-47ad-8a95-755e0e5ed343" />


---

## **4️⃣ Edit Public Subnet → Enable Auto-Assign Public IP**

1. Select **public-subnet-1**
2. Click **Actions → Edit subnet settings**
3. Enable:
   ✔️ **Auto-assign Public IPv4 address**

Click **Save**

<img width="795" height="558" alt="image" src="https://github.com/user-attachments/assets/eb9666b9-4148-412c-8381-bb691867821d" />

---

## **5️⃣ Create Private Subnet**

Again click **Create Subnet** and fill:

| Field                 | Value                                           |
| --------------------- | ----------------------------------------------- |
| **VPC ID**            | Select same custom VPC                          |
| **Subnet Name**       | `private-subnet-1`                              |
| **Availability Zone** | `us-east-1b` (different AZ than public subnet) |
| **IPv4 CIDR block**   | `10.0.2.0/24`                                   |

Click **Create Subnet**

<img width="1058" height="574" alt="image" src="https://github.com/user-attachments/assets/7831e9bb-cb21-4a6b-8d7a-beb820ab8862" />


---

## **6️⃣ Verify Both Subnets**

Check:

* **Public Subnet** is in **AZ a**
* **Private Subnet** is in **AZ b**
* CIDRs do not overlap
* Public subnet has **Auto-assign Public IP ON**

---

# 📘 **Understanding Subnet CIDR Allocation**

| Component          | CIDR Example  | Usage                                |
| ------------------ | ------------- | ------------------------------------ |
| **VPC CIDR**       | `10.0.0.0/16` | Network range for whole VPC          |
| **Public Subnet**  | `10.0.1.0/24` | Internet-facing resources (EC2, ALB) |
| **Private Subnet** | `10.0.2.0/24` | Internal resources (DB, Backend)     |

✔️ `/16` → allows 65,536 IPs
✔️ `/24` → each subnet gets 256 IPs

---

# 🎉 Subnets Successfully Created

Now your VPC has:

* **One Public Subnet (ap-south-1a)**
* **One Private Subnet (ap-south-1b)**
  Perfect for launching EC2, RDS, NAT Gateway setups later.


