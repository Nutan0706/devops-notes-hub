# 🔌 7️⃣ Install and Manage Jenkins Plugins

Jenkins becomes powerful when you expand it with plugins.
In this section, you will:

---

# 📝 **Step 1: Go to Manage Plugins**

Navigate to:

```
Dashboard → Manage Jenkins → Plugins
```

You will see tabs:

* **Updates**
* **Available Plugins**
* **Installed**
* **Advanced**

---

# 📝 **Step 2: Install Git Plugin**

Search:

```
Git plugin
```

Install:

```
Git plugin
Git client plugin
```

📌 **Purpose:**
Enables Jenkins to pull code from GitHub, GitLab, Bitbucket, etc.

<img width="434" height="317" alt="image" src="https://github.com/user-attachments/assets/b51c0b9f-769c-481a-821d-19943be9a9cf" />


---

# 📝 **Step 3: Install Pipeline Plugin**

Search:

```
Pipeline
```

Install these:

* **Pipeline**
* **Pipeline: Groovy**
* **Pipeline: Stage View**
* **Pipeline: SCM Step**
* **Pipeline: Declarative**

📌 **Purpose:**
Allows writing CI/CD pipelines using **Jenkinsfile**.

---

# 📝 **Step 4: Install Blue Ocean Plugin**

Search:

```
Blue Ocean
```

Install:

* **Blue Ocean**
* **Blue Ocean: GitHub Integration** (optional)

📌 **Purpose:**
Provides a **modern UI** for creating and visualizing pipelines.

<img width="450" height="242" alt="image" src="https://github.com/user-attachments/assets/96ddda81-4501-41da-b451-6024c05ce95b" />


---

# 📝 **Step 5: Install Docker Plugins**

Search:

```
Docker
```

Install:

* **Docker Pipeline**
* **Docker Commons**
* **Docker API**
* **Docker Authentication**

📌 **Purpose:**
For running Docker commands inside pipeline stages.

👉 *(Add screenshot)*
`![DockerPlugin](images/docker-plugin.png)`

---

# 📝 **Step 6: Install Credentials Binding Plugin**

Search:

```
Credentials Binding
```

Install:

* **Credentials Binding Plugin**

📌 **Purpose:**
Secures secrets (password, tokens, SSH keys) for use inside pipelines.

Example usage:

```groovy
withCredentials([string(credentialsId: 'GIT_TOKEN', variable: 'TOKEN')]) {
    sh 'echo $TOKEN'
}
```

---

# 📝 **Step 7: Restart Jenkins After Plugin Installation**

After installing plugins:

```
Dashboard → Manage Jenkins → Reload Configuration from Disk
```

Or use:

```
http://<jenkins-url>/restart
```


---

# 📝 **Step 8: Verify Installed Plugins**

Navigate to:

```
Manage Jenkins → Plugins → Installed
```

Check entries:

* ✔ Git plugin
* ✔ Pipeline plugins
* ✔ Blue Ocean
* ✔ Docker plugins
* ✔ Credentials Binding

---

# 📦 Optional: Update or Remove Plugins

### 🔄 **Update Plugin**

Go to **Updates tab** → select plugin → **Download now and install after restart**

### ❌ **Uninstall Plugin**

Go to **Installed** tab → scroll → click **Uninstall**

### 🔐 **Check Plugin Dependencies**

Jenkins will warn you if uninstalling a plugin breaks others.

---

# 🎉 Plugins Installed Successfully!

You now have all essential plugins for DevOps:

| Plugin              | Purpose                          |
| ------------------- | -------------------------------- |
| Git                 | Clone GitHub repos               |
| Pipeline            | Scripted/Declarative pipelines   |
| Blue Ocean          | Visual pipeline UI               |
| Docker              | Build/Run containers in pipeline |
| Credentials Binding | Securely use secrets             |

-
