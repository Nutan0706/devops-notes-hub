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

👉 *Add Screenshot Here*

---

## **2️⃣ Click "Create Subnet"**

1. Choose your existing **Custom VPC**
2. Click **Create Subnet**

👉 *Add Screenshot Here*

---

## **3️⃣ Create Public Subnet**

Fill the fields:

| Field                 | Value                    |
| --------------------- | ------------------------ |
| **VPC ID**            | Select your custom VPC   |
| **Subnet Name**       | `public-subnet-1`        |
| **Availability Zone** | `ap-south-1a` (any 1 AZ) |
| **IPv4 CIDR block**   | `10.0.1.0/24`            |

Click **Create Subnet**

👉 *Add Screenshot Here*

---

## **4️⃣ Edit Public Subnet → Enable Auto-Assign Public IP**

1. Select **public-subnet-1**
2. Click **Actions → Edit subnet settings**
3. Enable:
   ✔️ **Auto-assign Public IPv4 address**

Click **Save**

👉 *Add Screenshot Here*

---

## **5️⃣ Create Private Subnet**

Again click **Create Subnet** and fill:

| Field                 | Value                                           |
| --------------------- | ----------------------------------------------- |
| **VPC ID**            | Select same custom VPC                          |
| **Subnet Name**       | `private-subnet-1`                              |
| **Availability Zone** | `ap-south-1b` (different AZ than public subnet) |
| **IPv4 CIDR block**   | `10.0.2.0/24`                                   |

Click **Create Subnet**

👉 *Add Screenshot Here*

---

## **6️⃣ Verify Both Subnets**

Check:

* **Public Subnet** is in **AZ a**
* **Private Subnet** is in **AZ b**
* CIDRs do not overlap
* Public subnet has **Auto-assign Public IP ON**

👉 *Add Screenshot Here*

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

