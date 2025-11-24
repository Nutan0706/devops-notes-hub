# **Attach an Internet Gateway (IGW) & Configure Public Route Table**

You can add screenshots after each step.

---

# 🌐 **Attach an Internet Gateway (IGW) to VPC**

Make the Public Subnet capable of accessing the internet.

---

## 🚀 Step-by-Step Guide

---

## **1️⃣ Open VPC Console**

1. Go to **AWS Console → VPC Dashboard**
2. From the left panel, click **Internet Gateways**

<img width="1687" height="145" alt="image" src="https://github.com/user-attachments/assets/8ff09e2f-e3e1-4f15-af30-0887f9bea491" />


---

## **2️⃣ Create a New Internet Gateway**

1. Click **Create Internet Gateway**
2. Enter Name:

   * `my-vpc-igw`
3. Click **Create Internet Gateway**

<img width="1373" height="308" alt="image" src="https://github.com/user-attachments/assets/23952bb7-a79e-4d99-b2f5-d29001e4a982" />


---

## **3️⃣ Attach IGW to Your Custom VPC**

1. Select the newly created IGW
2. Click **Actions → Attach to VPC**
3. Choose your VPC (Example: `my-custom-vpc`)
4. Click **Attach Internet Gateway**

<img width="1237" height="261" alt="image" src="https://github.com/user-attachments/assets/4d30881c-43d5-43ae-b5eb-df8b56fc42c1" />


---

# 🛣️ **Configure Route Table for Public Subnet**

---

## **4️⃣ Open Route Tables**

1. In the VPC dashboard, click **Route Tables**
2. Select the route table associated with the **public subnet**

   * If unsure, filter by the subnet ID of `public-subnet-1`

<img width="1323" height="395" alt="image" src="https://github.com/user-attachments/assets/4253906c-5403-419f-95f2-eac27c6e156d" />


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

<img width="1382" height="299" alt="image" src="https://github.com/user-attachments/assets/af3135f6-3540-4a3f-ab24-d2777fd3bc57" />


---

## **6️⃣ Associate Route Table with Public Subnet**

1. Select the same route table
2. Go to the **Subnet associations** tab
3. Click **Edit subnet associations**
4. Select: `public-subnet-1`
5. Click **Save associations**

<img width="1329" height="522" alt="image" src="https://github.com/user-attachments/assets/e8bd7830-d30a-42cf-96d3-bf6fbc2d36a9" />


---

# ✔️ **Your Public Subnet Is Now Internet-Enabled**

You completed:

* Created IGW
* Attached IGW to VPC
* Added default route to IGW
* Linked route table to Public Subnet

Now any EC2 launched in the **Public Subnet** (with auto-assign public IP enabled) will have internet access.


