# 🚀 Pipeline with Multiple Stages (Build → Test → Deploy)

In this task, you will create a Jenkins pipeline with **three stages** using Declarative Pipeline syntax:

✔ Build
✔ Test
✔ Deploy

This is the standard structure of any CI/CD pipeline.

---

# 📝 **Step 1: Create a New Pipeline Job**

Go to:

```
Jenkins Dashboard → New Item
```

Enter name:

```
multi-stage-pipeline
```

Select:

✔ Pipeline
Click **OK**


---

# 📝 **Step 2: Add Declarative Jenkinsfile with Three Stages**

Scroll to **Pipeline → Pipeline script**
Paste this:

```groovy
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo "🔨 Starting Build Stage..."
                sh 'echo Compiling application...'
                sh 'sleep 2'
            }
        }

        stage('Test') {
            steps {
                echo "🧪 Running Tests..."
                sh 'echo Running unit tests...'
                sh 'sleep 2'
            }
        }

        stage('Deploy') {
            steps {
                echo "🚀 Deploying Application..."
                sh 'echo Deploying to server...'
                sh 'sleep 2'
            }
        }
    }

    post {
        success {
            echo "🎉 Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
```

<img width="442" height="160" alt="image" src="https://github.com/user-attachments/assets/78cc555c-21dc-455b-a7e4-fbaf68f5c993" />


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

You will see the three stages run sequentially:

* Build
* Test
* Deploy

<img width="507" height="126" alt="image" src="https://github.com/user-attachments/assets/5ccb2fe3-4ad1-4c60-8016-e466ada7b2c5" />


---

# 📝 **Step 5: View Console Output**

Open:

```
Build #1 → Console Output
```

Expected output:

```
🔨 Starting Build Stage...
Compiling application...

🧪 Running Tests...
Running unit tests...

🚀 Deploying Application...
Deploying to server...

🎉 Pipeline completed successfully!
```

<img width="239" height="340" alt="image" src="https://github.com/user-attachments/assets/56976d6d-e9c6-403a-993a-7ae371447401" />


---

# ⭐ Explanation of Each Stage

### 🔨 **Build Stage**

Simulates compiling, packaging, or preparing code.

### 🧪 **Test Stage**

Simulates running unit tests or integration tests.

### 🚀 **Deploy Stage**

Simulates deploying code to your server.

You can replace `sh 'echo ...'` with real commands:

* Build Java: `mvn clean package`
* Build Node: `npm install`
* Deploy to cloud: `scp`, `docker run`, `ansible`, etc.

---

# 🎉 Multi-Stage Pipeline Completed!

You now understand how to:

✔ Use Declarative Pipeline syntax
✔ Create multiple stages
✔ Add build/test/deploy commands
✔ Add success/failure notifications

