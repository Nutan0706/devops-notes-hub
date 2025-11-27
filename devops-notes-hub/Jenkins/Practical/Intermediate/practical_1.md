# 🚀 1️⃣ Create a Simple Jenkins Pipeline (Jenkinsfile)

# 📝 **Step 1: Create a New Pipeline Job**

Go to:

```
Jenkins Dashboard → New Item
```

Enter job name:

```
simple-pipeline
```

Select:

✔ **Pipeline**

Click **OK**

---

# 📝 **Step 2: Add a Basic Jenkinsfile in Pipeline Script**

Scroll to the **Pipeline** section → Choose:

✔ **Pipeline script**

Paste this Jenkinsfile:

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Running the Build Stage..."
                echo "Hello from Jenkins Pipeline!"
            }
        }
    }
}
```

<img width="444" height="320" alt="image" src="https://github.com/user-attachments/assets/d2148f17-4963-498a-840b-8b8b18d1d594" />


---

# 📝 **Step 3: Save the Job**

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

Jenkins will start a build and execute the `Build` stage.


---

# 📝 **Step 5: View Console Output**

Open:

```
Build #1 → Console Output
```

You should see output like:

```
Running on Jenkins in /var/lib/jenkins/workspace/simple-pipeline
[Pipeline] Start of Pipeline
[Pipeline] stage
[Pipeline] { (Build)
Running the Build Stage...
Hello from Jenkins Pipeline!
}
[Pipeline] End of Pipeline
Finished: SUCCESS
```

<img width="394" height="312" alt="image" src="https://github.com/user-attachments/assets/210dc396-758d-47a8-82a9-6462137ac980" />


