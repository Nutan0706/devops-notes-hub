

# 🧩 Practical 1: Create a Custom VPC

**Goal:** Create a new VPC with a specific CIDR block (e.g., `10.0.0.0/16`) using the AWS Management Console and understand its default components.

---

## 🧠 Objective

You will learn how to:

* Create a custom VPC with a specific IP range.
* Identify default VPC components.
* Compare Custom VPC vs Default VPC.

---

## 🪜 Step-by-Step Procedure

### **Step 1: Log in to AWS Management Console**

1. Open the [AWS Console](https://console.aws.amazon.com/).
2. In the **search bar**, type **VPC** and select **VPC** from the services list.
3. You’ll be redirected to the **VPC Dashboard**.

<img width="1425" height="569" alt="image" src="https://github.com/user-attachments/assets/19b53310-dc37-4762-a0fe-d02bf0731beb" />


---

### **Step 2: Create a New VPC**

1. Click on **“Your VPCs”** in the left navigation panel.
2. Select **Create VPC** button.
3. Choose **“VPC only”** option (not VPC and more).

<img width="1115" height="814" alt="image" src="https://github.com/user-attachments/assets/bdd86f6c-84ea-4b33-b40a-13e950f85b9a" />


---

### **Step 3: Configure VPC Settings**

Fill in the details as below:

| Field               | Value              |
| ------------------- | ------------------ |
| **Name tag**        | `Custom-VPC`       |
| **IPv4 CIDR block** | `10.0.0.0/16`      |
| **IPv6 CIDR block** | No IPv6 CIDR block |
| **Tenancy**         | Default            |

Then click **Create VPC**.

<img width="914" height="592" alt="image" src="https://github.com/user-attachments/assets/88ea09b8-4171-46c8-8267-816c9dee4865" />


---

### **Step 4: Verify Your VPC**

Once created, you’ll see a confirmation message:
✅ *“Successfully created VPC”*

Check that:

* VPC ID is created (`vpc-xxxxxxx`)
* CIDR block is `10.0.0.0/16`
* State shows **available**

<img width="1503" height="627" alt="image" src="https://github.com/user-attachments/assets/37298917-be49-4c22-bad3-b68ac1046f42" />


---

### **Step 5: Understand Default Components**

When a new VPC is created, AWS does **not** automatically create:

* **Subnets**
* **Route Tables**
* **Internet Gateways**
* **Security Groups**

But you can manually add them later.

---

## 🧩 Key Notes

| Concept         | Description                                                                           |
| --------------- | ------------------------------------------------------------------------------------- |
| **Default VPC** | Automatically created by AWS, includes subnets in each AZ, route tables, IGW, and SG. |
| **Custom VPC**  | Fully controlled by you, no default subnets or gateways.                              |
| **CIDR Block**  | Defines the IP range used by your VPC (e.g., `10.0.0.0/16` means 65,536 IPs).         |


