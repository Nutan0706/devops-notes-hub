# 🖥️ 2️⃣ Explore Jenkins Dashboard

Once Jenkins is installed and opened in the browser, follow these steps to understand the **main components of the Jenkins Dashboard**.

---

# 📝 **Step 1: Open Jenkins Dashboard**

Open:

```
http://<EC2-Public-IP>:8080
```

Log in using your admin credentials.

<img width="1475" height="682" alt="image" src="https://github.com/user-attachments/assets/f37bc2e8-0e2e-4651-b64d-95f4eb65b0a2" />


---

# 📝 **Step 2: Understand “New Item / Jobs”**

The **New Item** button is used to create different types of Jenkins Jobs:

* Freestyle Job
* Pipeline Job
* Multi-branch Pipeline
* Folder
* External Job

This is where you build anything in Jenkins.

<img width="876" height="882" alt="image" src="https://github.com/user-attachments/assets/b12a0061-640e-4e91-b57f-88ba2946d5e7" />


---

# 📝 **Step 3: Explore “Build History”**

On the left sidebar, you will see **Build History**.

It shows:

* Past builds
* Build status (Success, Failed, Aborted)
* Time taken by each build
* Console logs for each build

Useful for debugging pipeline failures.

<img width="881" height="431" alt="image" src="https://github.com/user-attachments/assets/50da1804-f344-4c76-9753-ac814dddaf2c" />


---

# 📝 **Step 4: Check “Manage Jenkins” Section**

Go to:

```
Dashboard → Manage Jenkins
```

This is the **control center** of Jenkins, where you handle:

* Plugins
* Global tools configuration
* Credentials
* Nodes / Agents
* System configuration
* Security & user management

<img width="1892" height="778" alt="image" src="https://github.com/user-attachments/assets/8beed98e-69d4-4349-b448-03e6fcec304c" />


---

# 📝 **Step 5: Understand “Plugins”**

Navigate to:

```
Manage Jenkins → Plugins
```

Jenkins plugins allow extra features like:

* Git, GitHub, GitLab integration
* Docker plugin
* Pipeline plugin
* Node & label plugins
* Notification plugins (Slack, Email, Teams)

Plugins = Power of Jenkins.

<img width="1486" height="848" alt="image" src="https://github.com/user-attachments/assets/7eb3937d-8f9a-4bfc-99b8-55793e8e21db" />


---

# 📝 **Step 6: Explore “Nodes / Agents”**

Go to:

```
Manage Jenkins → Nodes
```

Here you can:

* Add new build agents
* Distribute workload
* Configure labels for builds
* View agent status (Connected / Offline)

Useful in real CI/CD setups.

<img width="1625" height="327" alt="image" src="https://github.com/user-attachments/assets/ee6377a6-623f-4bd6-9b6f-30a9b761d484" />


---

# 📝 **Step 7: Check “System Configuration”**

Navigate to:

```
Manage Jenkins → System
```

Here you configure:

* Global environment variables
* Jenkins URL
* Tool configurations (JDK, Git, Maven, Docker)
* Shell settings
* Build timeout settings

This decides how Jenkins behaves globally.

<img width="626" height="927" alt="image" src="https://github.com/user-attachments/assets/cd5958da-db80-4f44-aa3a-7868fc46f0dd" />


