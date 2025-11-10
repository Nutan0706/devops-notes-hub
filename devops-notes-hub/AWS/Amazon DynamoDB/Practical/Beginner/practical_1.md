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

🖼️ *→ Add Screenshot 4 here (filled table creation form)*

---

### **Step 5: Keep Default Settings for Capacity Mode**

* Leave the default as **“Provisioned”** or select **“On-demand”** if available.
* For practice, you can **keep all defaults**.

🖼️ *→ Add Screenshot 5 here (Capacity mode section)*

---

### **Step 6: (Optional) Configure Table Settings**

* You can expand:

  * **Encryption** → leave as default (AWS managed key)
  * **Auto scaling** → leave as default
  * **TTL (Time to Live)** → disable for now

🖼️ *→ Add Screenshot 6 here (optional configuration section)*

---

### **Step 7: Click on “Create table”**

* Once done, scroll to the bottom and click the **“Create table”** button.
* Wait a few seconds for the table to be created.

🖼️ *→ Add Screenshot 7 here (creation in progress)*

---

### **Step 8: Verify the Table**

* Once created, you’ll see your new table listed under **“Tables”**.
* Click on the table name (e.g., `EmployeeTable`) to open its details.
* Check:

  * **Primary key** (Partition + Sort key)
  * **Table status** → should show as `Active`

🖼️ *→ Add Screenshot 8 here (final table details view)*

---

✅ **Result:**
You have successfully created your **first DynamoDB table** with:

* **Partition key:** EmployeeID
* **Sort key:** Department

