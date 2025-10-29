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

---

### **Step 2: Add New User**
1. Click on **“Add users”** button.
2. Enter a **User name** — e.g., `devops-user`.
3. Under **Select AWS access type**, check ✅ **AWS Management Console access**.
4. Choose **“Auto-generate password”** or create a custom password.
5. Optionally, check the box **“User must create a new password at next sign-in”**.

🖼️ _Add Screenshot: Add user details screen_

---

### **Step 3: Set User Permissions**
You have 3 options:
- **Add user to group** — (recommended) if you already have a `Developers` or `Admins` group.
- **Copy permissions from existing user**.
- **Attach policies directly** — e.g., `AmazonS3ReadOnlyAccess`.

✅ For this practical, choose **Attach policies directly**  
✅ Select **`AmazonS3ReadOnlyAccess`** policy.

🖼️ _Add Screenshot: Permission selection screen_

---

### **Step 4: Review and Create User**
1. Review all the details carefully.
2. Click **Create user**.
3. Note down the **Console sign-in URL** and **username/password** (for first login).

🖼️ _Add Screenshot: User creation success page_

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

🖼️ _Add Screenshot: Password policy settings_

---

## ✅ **Verification**
- Log in using the newly created user credentials.
- Check if:
  - You can access only allowed services (S3 Read-Only).
  - The password policy is enforced.
  - MFA (if applied later) works correctly.

---

## 🧠 **Key Learnings**
- Difference between **IAM user**, **group**, and **role**.  
- How password policies improve AWS account security.  
- Importance of granting **least privilege** access.

---

> 📝 **Next Practical → [Create IAM Group and Add Users](#)**  
> Continue documenting each practical and add screenshots for visual clarity.
