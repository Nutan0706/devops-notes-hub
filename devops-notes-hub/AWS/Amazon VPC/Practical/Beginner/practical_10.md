# VPC Peering Basics

Create VPC Peering between two VPCs and test ping between instances.

---

# 📝 **Prerequisites**

* Two VPCs (example):

  * **VPC-A CIDR:** `10.0.0.0/16`
  * **VPC-B CIDR:** `10.1.0.0/16`
* At least **one subnet + one EC2 instance** in each VPC.
* Both EC2 instances **must be in public or private subnets** with correct routes.

---

# ✅ **Step-by-Step Practical**

---

## **1️⃣ Create Two VPCs**

1. Go to **AWS Console → VPC → Your VPCs**
2. Click **Create VPC**
3. Enter:

   * VPC Name: `VPC-A`
   * IPv4 CIDR: `10.0.0.0/16`
4. Repeat for **VPC-B**:

   * Name: `VPC-B`
   * CIDR: `10.1.0.0/16`
5. Click **Create**.

<img width="631" height="216" alt="image" src="https://github.com/user-attachments/assets/3bb7c879-1964-420e-8875-790b617351c2" />


---

## **2️⃣ Create Subnets in Both VPCs**

Example:

* VPC-A → `10.0.1.0/24`
* VPC-B → `10.1.1.0/24`
  <img width="1920" height="1032" alt="image" src="https://github.com/user-attachments/assets/d0484d0a-e890-44b2-b662-29b8672ae1f7" />

<img width="1920" height="1032" alt="image" src="https://github.com/user-attachments/assets/7c2ed1f7-6b96-41fc-a0fb-0bbf618d64c7" />

---

## **3️⃣ Launch EC2 Instances in Both VPCs**

1. Create an EC2 instance in **VPC-A subnet**.
2. Create another EC2 instance in **VPC-B subnet**.
3. Make sure both have:

   * Same security group type (SSH/ICMP Allowed)
   * Key pair available for SSH.

<img width="1920" height="1032" alt="image" src="https://github.com/user-attachments/assets/7cb1859c-7aa2-4267-ae0c-2c6b9953cf88" />

---

## **4️⃣ Create VPC Peering Connection**

1. Go to **VPC → Peering Connections**
2. Click **Create Peering Connection**
3. Enter:

   * Name: `VPC-A-to-VPC-B`
   * **Requester VPC:** VPC-A
   * **Accepter VPC:** VPC-B
4. Click **Create Peering Connection**
5. Select the peering connection → Click **Accept Request**

<img width="1920" height="1032" alt="image" src="https://github.com/user-attachments/assets/4243d1f8-1d8b-49fe-9d1c-20bbbf8bd8a9" />


---

## **5️⃣ Update Route Tables for Communication**

### **➡️ In VPC-A Route Table**

1. Open **Route Tables**
2. Select route table for VPC-A
3. Click **Edit Routes → Add Route**
4. Destination: `10.1.0.0/16`
5. Target: Select your **Peering Connection**

### **➡️ In VPC-B Route Table**

1. Select route table for VPC-B
2. Add route:

   * Destination: `10.0.0.0/16`
   * Target: **Peering Connection**

📸 *Add screenshot here*

---

## **6️⃣ Update Security Groups**

### For EC2 in **VPC-A**

Add inbound rule:

```
Type: All ICMP - IPv4
Source: 10.1.0.0/16
```

### For EC2 in **VPC-B**

Add inbound rule:

```
Type: All ICMP - IPv4
Source: 10.0.0.0/16
```

📸 *Add screenshot here*

---

## **7️⃣ SSH into EC2 Instances**

SSH into **VPC-A EC2**:

```sh
ssh -i mykey.pem ec2-user@<Public-IP-A>
```

SSH into **VPC-B EC2**:

```sh
ssh -i mykey.pem ec2-user@<Public-IP-B>
```

📸 *Add screenshot here*

---

## **8️⃣ Test Connectivity (Ping Test)**

From EC2 in **VPC-A**, ping private IP of EC2 in VPC-B:

```sh
ping <private-ip-of-ec2-in-vpc-b>
```

From EC2 in **VPC-B**, ping private IP of EC2 in VPC-A:

```sh
ping <private-ip-of-ec2-in-vpc-a>
```

If everything is correct → **ping will work**.

📸 *Add screenshot here*

---

