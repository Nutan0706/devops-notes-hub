# 🧩 Practical 1 — Create IAM User with Console Access and Password Policy

## 🎯 Objective
Create a new IAM user in AWS Management Console with **console access** and enforce a **password policy** to enhance security.

---

## 🪜 Step-by-Step Implementation

### **Step 1: Open IAM Dashboard**
1. Sign in to your **AWS Management Console**.
2. Navigate to **IAM** service.
3. On the left panel, click **Users**.

🖼️ _Add Screenshot: IAM Dashboard_
<img width="1794" height="863" alt="image" src="https://github.com/user-attachments/assets/4da50935-cac5-4d17-9515-c10d9e2a31e1" />




---

### **Step 2: Add New User**
1. Click on **“Add users”** button.
2. Enter a **User name** — e.g., `devops-user`.
3. Under **Select AWS access type**, check ✅ **AWS Management Console access**.
4. Choose **“Auto-generate password”** or create a custom password.
5. Optionally, check the box **“User must create a new password at next sign-in”**.

🖼️ _Add Screenshot:
<img width="1668" height="715" alt="image" src="https://github.com/user-attachments/assets/218db65e-39ee-4598-b4f3-33e558363fca" />


---

### **Step 3: Set User Permissions**
You have 3 options:
- **Add user to group** — (recommended) if you already have a `Developers` or `Admins` group.
- **Copy permissions from existing user**.
- **Attach policies directly** — e.g., `AmazonS3ReadOnlyAccess`.

✅ For this practical, choose **Attach policies directly**  
✅ Select **`AmazonS3ReadOnlyAccess`** policy.

<img width="1369" height="632" alt="image" src="https://github.com/user-attachments/assets/0417b199-4c1b-4e05-b1c3-478a184f927d" />


---

### **Step 4: Review and Create User**
1. Review all the details carefully.
2. Click **Next then Create user**.
3. Note down the **Console sign-in URL** and **username/password** (for first login).

<img width="1661" height="546" alt="image" src="https://github.com/user-attachments/assets/1258b33c-f98c-4c1a-a36c-a9e1bdf810a5" />


---

### **Step 5: Configure Account Password Policy**
1. Go to **IAM → Account settings → Password policy**.
2. Click **Edit password policy**.
3. Enable the following options:
   - Require at least **one uppercase letter**
   - Require at least **one lowercase letter**
   - Require at least **one number**
   - Require at least **one non-alphanumeric character**
   - Minimum password length = **8**
   - Enable **password expiration (optional)**

4. Click **Save changes**.

<img width="1625" height="608" alt="image" src="https://github.com/user-attachments/assets/2a00e702-4ce8-4668-b536-d8d73eeb487a" />


---

## ✅ **Verification**
- Log in using the newly created user credentials.
- Check if:
  - You can access only allowed services (S3 Read-Only).
  - The password policy is enforced.
  - MFA (if applied later) works correctly.

---






