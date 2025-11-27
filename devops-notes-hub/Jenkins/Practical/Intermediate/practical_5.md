# 🤖 5️⃣ Set Up Jenkins Agents (Slave Nodes)

Connect an **EC2 Ubuntu machine** as a Jenkins agent and run specific jobs on that node.

# 🛠️ Part A — Prepare EC2 Ubuntu Node

## 📝 **Step 1: Launch EC2 Instance**

* OS: **Ubuntu 22.04 or 20.04**
* Security Group:

  * Allow **SSH (22)** from Jenkins server
  * Allow **Port 8080** only if needed (not required for agents)

---

## 📝 **Step 2: Install Java on EC2 Agent**

```bash
sudo apt update
sudo apt install openjdk-17-jdk -y
java -version
```


---

## 📝 **Step 3: Create Directory for Jenkins Agent**

```bash
mkdir ~/jenkins-agent
```

---

# 🛠️ Part B — Configure Jenkins Master to Add Agent

## 📝 **Step 4: Go to “Manage Nodes”**

```
Jenkins Dashboard → Manage Jenkins → Nodes → New Node
```
<img width="468" height="263" alt="image" src="https://github.com/user-attachments/assets/25916187-b032-4765-8068-ac68389dabed" />

---

## 📝 **Step 5: Create a New Node**

Name:

```
ubuntu-agent-1
```

Select:

✔ **Permanent Agent**
Click **OK**

---

## 📝 **Step 6: Configure the Agent Settings**

Fill the required fields:

| Field                     | Value                                    |
| ------------------------- | ---------------------------------------- |
| **Remote Root Directory** | `/home/ubuntu/jenkins-agent`             |
| **Labels**                | `docker-node` or `linux-node`            |
| **Usage**                 | "Only build jobs with label expressions" |
| **Launch Method**         | *Launch agents via SSH*                  |

<img width="468" height="212" alt="image" src="https://github.com/user-attachments/assets/62111dc0-e0aa-40bf-af9c-9761b3232347" />

---

## 📝 **Step 7: Add SSH Credentials**

Under **Launch Method → SSH**:

* Host: `EC2_PUBLIC_IP`
* Credentials:
  Add →

  * Kind: SSH Username with Private Key
  * Username: `ubuntu`
  * Private Key: Paste your `.pem` file

Choose credential ID:

```
EC2_AGENT_KEY
```

---

## 📝 **Step 8: Save & Connect Agent**

Click **Save** → Jenkins will try to connect.

If successful, you will see:

```
Connected  
Online
```

---

# 🛠️ Part C — Run Job on the Agent

## 📝 **Step 9: Create a Job for This Agent**

Go to:

```
New Item → agent-test-job
```

Select:

✔ Pipeline Job
Click **OK**


---

## 📝 **Step 10: Add Jenkinsfile to Use Agent Label**

Paste this:

```groovy
pipeline {
    agent { label 'docker-node' }

    stages {
        stage('Test Agent') {
            steps {
                echo "Running on agent: ${env.NODE_NAME}"
                sh 'hostname'
                sh 'whoami'
            }
        }
    }
}
```

---

## 📝 **Step 11: Run the Job**

Click:

```
Build Now
```

Jenkins will schedule the build on the **ubuntu-agent-1** node.


---

## 📝 **Step 12: View Console Output**

You will see:

```
Running on ubuntu-agent-1
ubuntu-agent-1
ubuntu
```
<img width="389" height="299" alt="image" src="https://github.com/user-attachments/assets/d818b5c9-e46f-4859-a069-da6a0cbbe030" />


---

# 🎉 Jenkins Agent Setup Completed Successfully!

You now have:

✔ EC2 Ubuntu machine as Jenkins agent
✔ SSH-based agent connection
✔ Pipeline job executed on agent
✔ Label-based scheduling

---
