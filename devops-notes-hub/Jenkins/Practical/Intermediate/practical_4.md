# 🐳 4️⃣ Integrate Jenkins with Docker

# 🛠️ Part A — Install Docker on Jenkins Host (EC2 or Ubuntu Machine)

## 📝 **Step 1: Update System**

```bash
sudo apt update -y
```

---

## 📝 **Step 2: Install Docker Engine**

```bash
sudo apt install docker.io -y
```
---

## 📝 **Step 3: Start & Enable Docker**

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

---

## 📝 **Step 4: Add Jenkins User to Docker Group**

This allows Jenkins to run `docker` commands.

```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

---

## 📝 **Step 5: Verify Docker Works from Jenkins User**

```bash
sudo su - jenkins
docker --version
docker ps
```

<img width="439" height="76" alt="image" src="https://github.com/user-attachments/assets/b29ac1f6-65a5-4ee9-a37e-a3f31c8df21f" />


---

# 🛠️ Part B — Jenkins Pipeline: Build a Docker Image From Source

Now create a Pipeline job that uses Docker to build images.

---

# 📝 **Step 6: Create Pipeline Job**

Go to:

```
Dashboard → New Item → docker-build-pipeline
```

Select:

✔ **Pipeline**

Click **OK**

---

# 📝 **Step 7: Add Jenkinsfile — Build Docker Image**

Scroll to **Pipeline → Pipeline Script** and paste:

```groovy
pipeline {
    agent any

    stages {

        stage('Checkout Source Code') {
            steps {
                git url: 'https://github.com/<your-username>/<your-repo>.git', branch: 'main'
            }
        }

        stage('Docker Build') {
            steps {
                echo "Building Docker Image..."
                sh '''
                    docker build -t myapp:latest .
                    docker images | grep myapp
                '''
            }
        }
    }
}
```

<img width="455" height="289" alt="image" src="https://github.com/user-attachments/assets/7cf9ad86-29bc-433a-924a-eace5e2ed49c" />


---

# 📝 **Step 8: Save the Job**

Click:

```
Save
```

---

# 📝 **Step 9: Run the Pipeline**

Click:

```
Build Now
```

Jenkins will:

1. Clone repo
2. Build Docker image using the Dockerfile
3. List the built image


---

# 📝 **Step 10: View Console Output**

Open:

```
Build #1 → Console Output
```

You should see something like:

```
Sending build context to Docker daemon  4.096kB
Step 1/4 : FROM python:3.10
Step 2/4 : COPY . /app
Step 3/4 : RUN pip install -r requirements.txt
Step 4/4 : CMD ["python3", "app.py"]
Successfully tagged myapp:latest

REPOSITORY   TAG      IMAGE ID       SIZE
myapp        latest   7a4bdac12345   163MB
```

<img width="386" height="329" alt="image" src="https://github.com/user-attachments/assets/f50c32cb-1bc2-4451-9f80-d4f0b8ac13a5" />

---

# 🎉 Docker Integration with Jenkins is Successful!
