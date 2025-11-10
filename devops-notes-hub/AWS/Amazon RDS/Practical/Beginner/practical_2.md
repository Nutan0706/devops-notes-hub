# 🧩 Practical 2 — Connect RDS with EC2 Instance

### 🎯 Objective:

Launch an **EC2 instance**, install the **database client** (MySQL or PostgreSQL), and connect it to your **RDS endpoint**.

---

## 🪜 Step-by-Step Guide

---

### **Step 1: Login to AWS Console**

* Go to 👉 [https://aws.amazon.com/console](https://aws.amazon.com/console)
* Login using your **AWS account credentials**.
  🖼️ *→ Add Screenshot 1 (AWS Console homepage)*

---

### **Step 2: Launch a New EC2 Instance**

1. In the search bar, type **“EC2”** and select it.
2. Click **“Launch instance”**.
3. Fill in the following:

   * **Name:** `EC2-DB-Client`
   * **AMI:** Amazon Linux 2 (Free tier eligible)
   * **Instance type:** `t2.micro`
   * **Key pair:** Create or select an existing one (you’ll use it to SSH into the instance).
   * **Network settings:**

     * Select **the same VPC and subnet** as your RDS instance.
     * Enable **Auto-assign Public IP**.
   * **Security group:** Create or use one that allows:

     * **Outbound traffic:** all
     * **Inbound traffic:** SSH (port 22) from your IP

🖼️ *→ Add Screenshot 2 (Launch instance configuration page)*

---

### **Step 3: Verify Instance Launch**

* Click **Launch instance**.
* Wait until the status is **Running**.
* Copy the **Public IPv4 address** — you’ll need it for SSH.

🖼️ *→ Add Screenshot 3 (instance running page)*

---

### **Step 4: Update RDS Security Group**

Your EC2 instance needs permission to access RDS.

1. Go to **RDS → Databases → your RDS instance**.
2. Note the **VPC security group** used by the RDS instance.
3. Open **EC2 → Security Groups → that same group**.
4. Click **Edit inbound rules → Add rule**:

   * Type: **MySQL/Aurora** (if MySQL) or **PostgreSQL**
   * Port: `3306` (MySQL) or `5432` (PostgreSQL)
   * Source: **Your EC2 instance’s security group**

✅ This allows only your EC2 instance to connect to the RDS database.

🖼️ *→ Add Screenshot 4 (security group inbound rule setup)*

---

### **Step 5: Connect to EC2 Using SSH**

From your local terminal (replace with your `.pem` key path and public IP):

```bash
ssh -i "your-key.pem" ec2-user@<EC2-Public-IP>
```

🖼️ *→ Add Screenshot 5 (successful SSH login into EC2)*

---

### **Step 6: Install Database Client on EC2**

#### For MySQL RDS:

```bash
sudo yum update -y
sudo yum install mysql -y
```

#### For PostgreSQL RDS:

```bash
sudo yum update -y
sudo yum install postgresql -y
```

🖼️ *→ Add Screenshot 6 (client installation success message)*

---

### **Step 7: Connect to RDS from EC2**

Go to your **RDS console**, copy the **endpoint** (e.g., `my-first-rds.abcdefgh1234.us-east-1.rds.amazonaws.com`).

Now connect:

#### For MySQL:

```bash
mysql -h <RDS-ENDPOINT> -u admin -p
```

Then enter your password (e.g., `Password@123`).

#### For PostgreSQL:

```bash
psql -h <RDS-ENDPOINT> -U admin -d mydb
```

Enter the password when prompted.

🖼️ *→ Add Screenshot 7 (successful DB connection prompt)*

---

### **Step 8: Verify Connection**

Once connected, run a few simple SQL commands to confirm everything works:

#### For MySQL:

```sql
SHOW DATABASES;
USE mydb;
CREATE TABLE test (id INT PRIMARY KEY, name VARCHAR(50));
INSERT INTO test VALUES (1, 'AWS Test');
SELECT * FROM test;
```

#### For PostgreSQL:

```sql
\l
\c mydb
CREATE TABLE test (id INT PRIMARY KEY, name VARCHAR(50));
INSERT INTO test VALUES (1, 'AWS Test');
SELECT * FROM test;
```

🖼️ *→ Add Screenshot 8 (query output inside RDS database)*

---

### **Step 9: Close Connection**

* Exit the SQL prompt:

  * For MySQL → `exit;`
  * For PostgreSQL → `\q`
* Logout from EC2 → `exit`

🖼️ *→ Add Screenshot 9 (return to EC2 terminal)*

---

✅ **Result:**
You’ve successfully connected your **EC2 instance to an RDS database** 🎉

| Component      | Configuration              |
| -------------- | -------------------------- |
| RDS Engine     | MySQL / PostgreSQL         |
| EC2 Type       | t2.micro                   |
| Network        | Same VPC as RDS            |
| Security Group | Allows DB port from EC2 SG |
| Status         | Connected successfully     |

