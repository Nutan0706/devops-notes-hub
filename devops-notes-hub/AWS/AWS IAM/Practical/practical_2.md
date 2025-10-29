# 🧩 Practical 2 — Create a “Developers” group, attach policies, and add users to it.

## 🎯 Objective
Create a new **IAM group** named “Developers”, attach appropriate **policies** (like EC2 or S3 access), and **add existing users** to this group for simplified permission management.

---

## 🪜 Step-by-Step Implementation

### **Step 1: Open IAM Dashboard**
1. Sign in to the **AWS Management Console**.
2. Navigate to **IAM** service.
3. On the left sidebar, click **User groups**.

<img width="1892" height="717" alt="image" src="https://github.com/user-attachments/assets/0d483bc7-fe3f-4d12-9369-e255d4925c74" />


---

### **Step 2: Create a New Group**
1. Click on **“Create group”**.
2. In the **Group name** field, enter 👉 `Developers`.
3. Under **Attach permissions policies**, select policies such as:
   - `AmazonEC2ReadOnlyAccess`
   - `AmazonS3ReadOnlyAccess`
   - or any custom policy suitable for your developer team.

<img width="1877" height="854" alt="image" src="https://github.com/user-attachments/assets/55782ffb-1ad3-44ab-9fb3-6e34de54ed77" />


---

### **Step 3: Add Users to the Group**
1. Scroll down to **Users** section.
2. Check the box next to users you want to add — for example, `devops-user`.
3. Click **Create group**.

<img width="1872" height="775" alt="image" src="https://github.com/user-attachments/assets/a6aa4cc3-0b2f-4782-81c2-bb7ddea855e3" />


---

### **Step 4: Verify Group and Permissions**
1. Once created, click on the group name **Developers**.
2. Navigate to the **Permissions** tab to verify attached policies.
3. Go to the **Users** tab and confirm your users are listed.

<img width="1604" height="634" alt="image" src="https://github.com/user-attachments/assets/2adefeab-3aca-4d1e-a5d2-adfc2a866f45" />


---

### **Step 5: Test Group Permissions**
1. Log in as one of the users added to the group (e.g., `devops-user`).
2. Try accessing AWS services like EC2 or S3.
3. Verify that the user can access **only the services** permitted by the group’s policies.

---

## ✅ **Verification Checklist**
- [x] IAM group named `Developers` created successfully.  
- [x] Appropriate AWS policies attached.  
- [x] Desired users added to the group.  
- [x] Permissions applied as expected.  

---
