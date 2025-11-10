# 🧩 Practical 3 — Create Your First RDS Instance

### 🎯 Objective:

Launch a **MySQL or PostgreSQL RDS instance** using the **AWS Console** with proper DB name, username, and password setup.

---

## 🪜 Step-by-Step Guide

---

### **Step 1: Login to AWS Console**

* Open 👉 [https://aws.amazon.com/console](https://aws.amazon.com/console)
* Login with your **AWS credentials** (Root or IAM user).

🖼️ *→ Add Screenshot 1 here (AWS console home page)*

---

### **Step 2: Open the RDS Service**

* In the **search bar** at the top, type **“RDS”**.
* Select **RDS (Relational Database Service)** from the search results.

🖼️ *→ Add Screenshot 2 here (RDS service dashboard)*

---

### **Step 3: Click “Create database”**

* On the RDS dashboard, click the **“Create database”** button.
* This starts the **database creation wizard**.

🖼️ *→ Add Screenshot 3 here (Create database button page)*

---

### **Step 4: Choose a Database Creation Method**

* Select **“Standard create”** (recommended for full control).
* For **Engine options**, choose:

  * Either **MySQL** or **PostgreSQL**.

🖼️ *→ Add Screenshot 4 here (database engine selection page)*

---

### **Step 5: Choose the Version and Template**

* Select a **DB engine version** (e.g., MySQL 8.0 or PostgreSQL 15).
* Under **Templates**, choose **Free tier** if available (for learning/practice).

🖼️ *→ Add Screenshot 5 here (engine version and template selection)*

---

### **Step 6: Configure DB Instance Details**

Under **Settings**:

1. **DB instance identifier:**
   e.g., `my-first-rds`
2. **Master username:**
   e.g., `admin`
3. **Master password:**
   e.g., `Password@123`
4. **Confirm password:**
   Re-enter the same password.

🖼️ *→ Add Screenshot 6 here (DB instance configuration)*

---

### **Step 7: Choose Instance Size**

Under **DB instance class**:

* For free tier → select `db.t3.micro`
* Storage type → choose **General Purpose (SSD)**

🖼️ *→ Add Screenshot 7 here (instance class and storage section)*

---

### **Step 8: Configure Connectivity**

In the **Connectivity** section:

1. **Virtual Private Cloud (VPC):** select default VPC
2. **Public access:** choose **Yes** (for easy access during practice)
3. **VPC security group:**

   * You can use **default** security group
     OR
   * Create a new one that allows **inbound traffic on port 3306** (for MySQL) or **5432** (for PostgreSQL)

🖼️ *→ Add Screenshot 8 here (connectivity setup page)*

---

### **Step 9: Additional Configurations**

Expand **Additional configuration**:

* **Initial database name:** `mydb`
* Keep other options as default:

  * **Backup:** enabled
  * **Encryption:** enabled
  * **Monitoring:** disabled (for free tier)

🖼️ *→ Add Screenshot 9 here (additional configuration section)*

---

### **Step 10: Create the Database**

* Scroll to the bottom.
* Click **“Create database”**.
* The instance creation process will begin (takes around 5–10 minutes).

🖼️ *→ Add Screenshot 10 here (creation in progress)*

---

### **Step 11: Verify the Database Creation**

* Once creation is complete, you’ll see the **status as “Available”**.
* Click on the DB identifier (e.g., `my-first-rds`) to open details.
* Copy the **Endpoint** — this will be used to connect from your application or client (like MySQL Workbench or pgAdmin).

🖼️ *→ Add Screenshot 11 here (DB available status and endpoint)*

---

✅ **Result:**
You have successfully launched your **first RDS instance** 🎉

| Component       | Example Value      |
| --------------- | ------------------ |
| Engine          | MySQL / PostgreSQL |
| DB Name         | mydb               |
| Master Username | admin              |
| Password        | Password@123       |
| Public Access   | Enabled            |
| Instance Class  | db.t3.micro        |
| Status          | Available          |

---
