# **Attach an Internet Gateway (IGW) & Configure Public Route Table**

You can add screenshots after each step.

---

# 🌐 **Attach an Internet Gateway (IGW) to VPC**

Make the Public Subnet capable of accessing the internet.

---

# 🚀 Step-by-Step Guide

---

## **1️⃣ Open VPC Console**

1. Go to **AWS Console → VPC Dashboard**
2. From the left panel, click **Internet Gateways**

👉 *Add Screenshot Here*

---

## **2️⃣ Create a New Internet Gateway**

1. Click **Create Internet Gateway**
2. Enter Name:

   * `my-vpc-igw`
3. Click **Create Internet Gateway**

👉 *Add Screenshot Here*

---

## **3️⃣ Attach IGW to Your Custom VPC**

1. Select the newly created IGW
2. Click **Actions → Attach to VPC**
3. Choose your VPC (Example: `my-custom-vpc`)
4. Click **Attach Internet Gateway**

👉 *Add Screenshot Here*

---

# 🛣️ **Configure Route Table for Public Subnet**

---

## **4️⃣ Open Route Tables**

1. In the VPC dashboard, click **Route Tables**
2. Select the route table associated with the **public subnet**

   * If unsure, filter by the subnet ID of `public-subnet-1`

👉 *Add Screenshot Here*

---

## **5️⃣ Edit Routes to Allow Internet Access**

1. Select the public route table
2. Go to the **Routes** tab
3. Click **Edit Routes**
4. Add a new route:

| Destination | Target                                              |
| ----------- | --------------------------------------------------- |
| `0.0.0.0/0` | *Your Internet Gateway ID* (e.g., `igw-0abcd12ef3`) |

5. Click **Save Changes**

👉 *Add Screenshot Here*

---

## **6️⃣ Associate Route Table with Public Subnet**

1. Select the same route table
2. Go to the **Subnet associations** tab
3. Click **Edit subnet associations**
4. Select: `public-subnet-1`
5. Click **Save associations**

👉 *Add Screenshot Here*

---

# ✔️ **Your Public Subnet Is Now Internet-Enabled**

You completed:

* Created IGW
* Attached IGW to VPC
* Added default route to IGW
* Linked route table to Public Subnet

Now any EC2 launched in the **Public Subnet** (with auto-assign public IP enabled) will have internet access.

