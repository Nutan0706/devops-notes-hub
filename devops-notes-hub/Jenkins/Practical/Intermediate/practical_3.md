# 🌍 3️⃣ Use Environment Variables in Jenkins Pipeline

# 📝 **Step 1: Open/Create a Pipeline Job**

Go to:

```
Dashboard → New Item → env-vars-pipeline
```

Select:

✔ **Pipeline**

Click **OK**


---

# 📝 **Step 2: Add Jenkinsfile to Print Environment Variables**

Scroll to **Pipeline → Pipeline Script** and paste:

```groovy
pipeline {
    agent any

    stages {

        stage('Print Environment Variables') {
            steps {

                echo "🔹 Job Name: ${env.JOB_NAME}"
                echo "🔹 Build ID: ${env.BUILD_ID}"
                echo "🔹 Build Number: ${env.BUILD_NUMBER}"
                echo "🔹 Workspace: ${env.WORKSPACE}"
                echo "🔹 Jenkins URL: ${env.JENKINS_URL}"
                echo "🔹 Node Name: ${env.NODE_NAME}"
                echo "🔹 Branch (if applicable): ${env.GIT_BRANCH}"
            }
        }
    }
}
```

<img width="450" height="308" alt="image" src="https://github.com/user-attachments/assets/28356044-4250-4d75-9e41-720c57139096" />


---

# 📝 **Step 3: Save the Pipeline**

Click:

```
Save
```

---

# 📝 **Step 4: Run the Pipeline**

Click:

```
Build Now
```

---

# 📝 **Step 5: View Console Output**

Open:

```
Build #1 → Console Output
```

You should see something like:

```
🔹 Job Name: env-vars-pipeline
🔹 Build ID: 2025-11-26_12-45-32
🔹 Build Number: 1
🔹 Workspace: /var/lib/jenkins/workspace/env-vars-pipeline
🔹 Jenkins URL: http://54.xx.xx.xx:8080/
🔹 Node Name: master
🔹 Branch (if applicable): (empty or shows branch if SCM configured)
Finished: SUCCESS
```

<img width="343" height="380" alt="image" src="https://github.com/user-attachments/assets/09b7a4e5-ed10-4072-91cb-10f71ca3e07e" />


---

# ⭐ Useful Built-in Environment Variables

| Variable           | Description                             |
| ------------------ | --------------------------------------- |
| `env.JOB_NAME`     | Name of the Jenkins Job                 |
| `env.BUILD_ID`     | Unique timestamp build ID               |
| `env.BUILD_NUMBER` | Auto-increment build counter            |
| `env.WORKSPACE`    | Directory where Jenkins checks out code |
| `env.JENKINS_URL`  | Base Jenkins URL                        |
| `env.GIT_COMMIT`   | Git commit hash (if SCM added)          |
| `env.GIT_BRANCH`   | Branch name                             |
| `env.NODE_NAME`    | Jenkins agent used                      |

