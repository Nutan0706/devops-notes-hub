# 🧩 Practical 3 — Create Your First RDS Instance

### 🎯 Objective:

Launch a **MySQL or PostgreSQL RDS instance** using the **AWS Console** with proper DB name, username, and password setup.

---

## 🪜 Step-by-Step Guide

---

### **Step 1: Login to AWS Console**

* Open 👉 [https://aws.amazon.com/console](https://aws.amazon.com/console)
* Login with your **AWS credentials** (Root or IAM user).
---

### **Step 2: Open the RDS Service**

* In the **search bar** at the top, type **“RDS”**.
* Select **RDS (Relational Database Service)** from the search results.


---

### **Step 3: Click “Create database”**

* On the RDS dashboard, click the **“Create database”** button.
* This starts the **database creation wizard**.


---

### **Step 4: Choose a Database Creation Method**

* Select **“Standard create”** (recommended for full control).
* For **Engine options**, choose:

  * Either **MySQL** or **PostgreSQL**.
<img width="1323" height="590" alt="image" src="https://github.com/user-attachments/assets/9e1eeaa0-83c8-4d02-8faa-f7f93d350bea" />

---

### **Step 5: Choose the Version and Template**

* Select a **DB engine version** (e.g., MySQL 8.0 or PostgreSQL 15).
* Under **Templates**, choose **Free tier** if available (for learning/practice).

<img width="1335" height="745" alt="image" src="https://github.com/user-attachments/assets/01b8f83e-f223-4841-ade1-5284af50ed28" />


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

<img width="1299" height="530" alt="image" src="https://github.com/user-attachments/assets/b3589609-2146-4323-98ef-ff2630c99525" />


---

### **Step 7: Choose Instance Size**

Under **DB instance class**:

* For free tier → select `db.t3.micro`
* Storage type → choose **General Purpose (SSD)**

<img width="881" height="274" alt="image" src="https://github.com/user-attachments/assets/f502a781-68f3-4416-909e-910d6729cb32" />

---

### **Step 8: Configure Connectivity**

In the **Connectivity** section:

1. **Virtual Private Cloud (VPC):** select default VPC
2. **Public access:** choose **Yes** (for easy access during practice)
3. **VPC security group:**

   * You can use **default** security group
     OR
   * Create a new one that allows **inbound traffic on port 3306** (for MySQL) or **5432** (for PostgreSQL)

<img width="989" height="654" alt="image" src="https://github.com/user-attachments/assets/dc2aba7b-1f8b-46dd-a8b8-cadf794ca6e5" />


---

### **Step 9: Additional Configurations**

Expand **Additional configuration**:

* **Initial database name:** `mydb`
* Keep other options as default:

  * **Backup:** enabled
  * **Encryption:** enabled
  * **Monitoring:** disabled (for free tier)

<img width="882" height="714" alt="image" src="https://github.com/user-attachments/assets/2e553aa3-9a2a-41df-b291-204264100db3" />


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

<img width="1277" height="179" alt="image" src="https://github.com/user-attachments/assets/74b69b09-cb45-4dcd-8201-952450a18bfc" />


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


