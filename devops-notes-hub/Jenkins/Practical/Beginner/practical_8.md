# 🛡️ 8️⃣ Create Jenkins Users and Roles (RBAC)

## 📝 **Step 1: Install “Role-Based Strategy” Plugin**

Navigate to:

```
Dashboard → Manage Jenkins → Plugins → Available Plugins
```

Search:

```
Role-based Authorization Strategy
```

Install:

✔ **Role-based Authorization Strategy**

<img width="427" height="415" alt="image" src="https://github.com/user-attachments/assets/e251e426-9519-4fe6-84fc-2a717839a81f" />


---

# 📝 **Step 2: Enable Role-Based Authorization**

Navigate to:

```
Dashboard → Manage Jenkins → Configure Global Security
```

Under **Authorization**, select:

```
Role-Based Strategy
```

Click **Save**.

<img width="440" height="324" alt="image" src="https://github.com/user-attachments/assets/bdeef7b5-e3fd-4c33-b6a5-26a6ef71674d" />


---

# 📝 **Step 3: Create New Jenkins Users**

Go to:

```
Dashboard → Manage Jenkins → Manage Users → Create User
```

Fill:

* Username
* Password
* Full Name
* Email

Example users:

| User    | Usage            |
| ------- | ---------------- |
| devuser | development team |
| tester  | QA               |
| viewer  | read-only user   |



---

# 📝 **Step 4: Open “Manage and Assign Roles”**

Go to:

```
Dashboard → Manage Jenkins
```

You will now see two new options:

* **Manage Roles**
* **Assign Roles**

<img width="440" height="424" alt="image" src="https://github.com/user-attachments/assets/d941243a-ed6c-49ff-aee7-8d511587c483" />


---

# 📝 **Step 5: Create Global Roles**

Navigate to:

```
Manage Roles
```

Under **Global Roles**, create roles like:

### 🟢 Admin

Grant all permissions.

### 🟠 Developer

Grant:

* Job → Read, Build, Configure
* Workspace → Read
* SCM → Tag
* View → Read

### 🔵 Viewer

Grant:

* Job → Read
* View → Read

➡ Select checkboxes accordingly.
➡ Click **Save**.

---

# 📝 **Step 6: Assign Users to Roles**

Navigate to:

```
Assign Roles
```

Under **Global Roles Assignments**, map:

| Username   | Role      |
| ---------- | --------- |
| admin_user | admin     |
| devuser    | developer |
| viewer     | viewer    |

Click **Save**.

---

# 📝 **Step 7: Test the Access Control**

### 🔐 Login as **developer**

Should be able to:

* View jobs
* Build jobs
* Configure jobs (if allowed)

### 👀 Login as **viewer**

Should only be able to:

* View jobs
* View console output
* No build or configure access


---

# 📝 **Optional: Project Roles (Folder/Job Level Security)**

If you want per-project permissions:

Go to **Manage Roles → Project Roles**
Add roles such as:

| Role           | Permissions      |
| -------------- | ---------------- |
| project-dev    | Build, Configure |
| project-viewer | Read only        |

Then under **Assign Roles → Project Roles**, map users to specific jobs using regex patterns:

Example:

```
^project1-.*$
```

