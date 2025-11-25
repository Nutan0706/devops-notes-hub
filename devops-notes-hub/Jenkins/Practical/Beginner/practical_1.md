# 🚀 Install Jenkins on Ubuntu EC2 (Step-by-Step Guide)

This guide will help you install **Jenkins on an Ubuntu EC2 instance**, start the service, and verify that Jenkins is accessible on port **8080**.

---

## 📌 **Prerequisites**

* Ubuntu EC2 instance (t2.micro or larger)
* Open port **8080** in Security Group (Inbound Rule: TCP 8080, 0.0.0.0/0 or your IP)
* SSH access to EC2
<img width="1409" height="156" alt="image" src="https://github.com/user-attachments/assets/afbd4b5f-8719-4343-b9a7-b7ebf8e041d6" />

---

# 📝 **Step 1: Update System Packages**

```bash
sudo apt update
sudo apt upgrade -y
```

<img width="808" height="198" alt="image" src="https://github.com/user-attachments/assets/fdabf683-effb-46a0-a3dc-c99d14be3e99" />


---

# 📝 **Step 2: Install Java (Required for Jenkins)**

Jenkins needs Java 11 or above.

```bash
sudo apt install openjdk-17-jdk -y
java -version
```
<img width="660" height="212" alt="image" src="https://github.com/user-attachments/assets/51254bf3-d3b9-4a33-bb44-cde3bcbccca0" />

---

# 📝 **Step 3: Add Jenkins Repository & Key**

```bash
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
```

<img width="827" height="180" alt="image" src="https://github.com/user-attachments/assets/594fcdde-3aa2-4755-8ad5-0920ce6216b0" />


---

# 📝 **Step 4: Install Jenkins**

```bash
sudo apt update
sudo apt install jenkins -y
```

<img width="522" height="312" alt="image" src="https://github.com/user-attachments/assets/6020b244-9b37-45e4-afcf-6b1714f9fee3" />


---

# 📝 **Step 5: Start & Enable Jenkins Service**

```bash
sudo systemctl start jenkins
sudo systemctl enable jenkins
sudo systemctl status jenkins
```

<img width="857" height="259" alt="image" src="https://github.com/user-attachments/assets/ff1434c3-9b4b-4ec3-987e-cf9ce8ddff13" />

---

# 📝 **Step 6: Allow Port 8080 in Firewall (If UFW Enabled)**

```bash
sudo ufw allow 8080
sudo ufw reload
```

<img width="411" height="91" alt="image" src="https://github.com/user-attachments/assets/44640538-86c3-4376-b7bd-789bc9181c59" />


---

# 📝 **Step 7: Access Jenkins in Browser**

Open:

```
http://<EC2-Public-IP>:8080
```

<img width="1462" height="488" alt="image" src="https://github.com/user-attachments/assets/25aac004-873a-408e-b722-22743c1ca4f2" />


---

# 📝 **Step 8: Get the Initial Jenkins Admin Password**

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

Copy this password and paste it into the Jenkins UI.

👉 **(Add screenshot showing the password output — hide sensitive part)**
`![Step8](images/step8.png)`

---

# 📝 **Step 9: Install Suggested Plugins**

On Jenkins UI → Choose:

✔ **Install Suggested Plugins**
(wait for installation)

<img width="1009" height="527" alt="image" src="https://github.com/user-attachments/assets/169f90df-7870-4826-866a-4f8b5b37faf4" />

---

# 📝 **Step 10: Create Admin User**

Fill your:

* Username
* Password
* Full Name
* Email

Click **Save & Continue**

<img width="793" height="632" alt="image" src="https://github.com/user-attachments/assets/5de82ebc-d805-420d-8bec-9fa876e090ca" />



