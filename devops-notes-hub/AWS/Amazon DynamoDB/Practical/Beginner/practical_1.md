# 🧩 Practical 1 — Create Your First DynamoDB Table

### 🎯 Objective:

Create a **DynamoDB table** with a **Partition Key** and **Sort Key** using the **AWS Console**.

---

## 🪜 Step-by-Step Guide

---

### **Step 1: Login to AWS Console**

* Open your browser and go to 👉 [https://aws.amazon.com/console](https://aws.amazon.com/console)
* Login using your **AWS account credentials** (Root or IAM user).

---

### **Step 2: Open DynamoDB Service**

* In the **AWS Management Console**, go to the **search bar** at the top.
* Type **“DynamoDB”** and click on **DynamoDB** from the list.

---

### **Step 3: Click on “Create table”**

* On the left-hand side, under **“Tables”**, click on **“Create table”** button.

<img width="909" height="463" alt="image" src="https://github.com/user-attachments/assets/ca4b8fb1-c2c5-498f-8d9f-c4802999de8d" />


---

### **Step 4: Enter Basic Table Details**

1. **Table name:**
   Enter a name — for example: `EmployeeTable`

2. **Partition key (Primary Key):**

   * Key name: `EmployeeID`
   * Type: `String`

3. **Sort key (Optional but required here):**

   * Key name: `Department`
   * Type: `String`

<img width="401" height="309" alt="image" src="https://github.com/user-attachments/assets/705bc536-b395-4f2c-b2b4-7e36b3702af1" />


---

### **Step 5: Keep Default Settings for Capacity Mode**

* Leave the default as **“Provisioned”** or select **“On-demand”** if available.
* For practice, you can **keep all defaults**.

---

### **Step 6: (Optional) Configure Table Settings**

* You can expand:

  * **Encryption** → leave as default (AWS managed key)
  * **Auto scaling** → leave as default
  * **TTL (Time to Live)** → disable for now


---

### **Step 7: Click on “Create table”**

* Once done, scroll to the bottom and click the **“Create table”** button.
* Wait a few seconds for the table to be created.

<img width="416" height="284" alt="image" src="https://github.com/user-attachments/assets/cff771f1-33bb-40b5-8121-f9608b42960a" />


---

### **Step 8: Verify the Table**

* Once created, you’ll see your new table listed under **“Tables”**.
* Click on the table name (e.g., `EmployeeTable`) to open its details.
* Check:

  * **Primary key** (Partition + Sort key)
  * **Table status** → should show as `Active`

<img width="208" height="247" alt="image" src="https://github.com/user-attachments/assets/09c6c7c1-659e-4df1-a0a6-053657e99485" />


---

✅ **Result:**
You have successfully created your **first DynamoDB table** with:

* **Partition key:** EmployeeID
* **Sort key:** Department



