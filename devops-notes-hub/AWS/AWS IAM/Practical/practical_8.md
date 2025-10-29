## 🧠 Practical 8 — Implement Least Privilege Principle

### 🎯 **Goal**
Audit IAM users and roles to **remove unnecessary permissions** using **IAM Access Advisor**, following the **Principle of Least Privilege**.

---

### 🔹 **Step-by-Step Guide**

### **Step 1: Open IAM Console**

1. Go to the **AWS Management Console → IAM → Users** (or **Roles** if auditing roles).  
2. You’ll see a list of all users with attached policies.

🖼️ _Add Screenshot: IAM users list screen_

---

### **Step 2: Select a User or Role**

1. Click on any **user** or **role** (e.g., `developer-user`).  
2. Go to the **Access Advisor** tab.  
3. You’ll see a list of AWS services the entity has permissions for, along with **Last Accessed** timestamps.

🖼️ _Add Screenshot: Access Advisor tab showing service access details_

---

### **Step 3: Analyze Usage**

1. Review which services have **“Not accessed in last 90 days”** or **“Never accessed.”**  
2. Identify unnecessary permissions that can be safely removed.

🧩 **Example:**  
If a user has access to **Amazon RDS**, but **Access Advisor** shows “Never accessed,” that permission can likely be removed.

🖼️ _Add Screenshot: Access Advisor showing unused permissions_

---

### **Step 4: Modify or Remove Unused Permissions**

1. Go to the **Permissions** tab → **Edit** or **Detach** the unused policies.  
2. You can either:  
   - **Detach** entire policies that are not used.  
   - Or **create a custom policy** with only the necessary permissions.

🖼️ _Add Screenshot: Editing or detaching unused IAM policies_

---

### **Step 5: Validate Access**

1. After cleanup, test that the **user** or **application** still performs its required tasks.  
2. Adjust as needed until the user has only the **minimum permissions** required.

🖼️ _Add Screenshot: Testing IAM user access after permission cleanup_

---

### ✅ **Outcome**

You have successfully implemented the **Principle of Least Privilege** — ensuring every **IAM user**, **group**, or **role** has just enough permissions to perform their work, and nothing more.

---

### 🧠 **Best Practice Tips**

- 🔁 Review **IAM Access Advisor** monthly.  
- 🕵️‍♂️ Use **AWS IAM Access Analyzer** for organization-wide permission analysis.  
- 🔒 Combine this with **MFA** and **no root user usage** for maximum security posture.

