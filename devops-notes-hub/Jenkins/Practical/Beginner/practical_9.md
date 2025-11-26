# ✉️ 9️⃣ Configure Email Notifications in Jenkins (SMTP + Alerts)
---

# 📝 **Step 1: Install Email & Mailer Plugins**

Go to:

```
Dashboard → Manage Jenkins → Plugins → Available Plugins
```

Search & install:

* **Email Extension Plugin**
* **Mailer Plugin**
---

# 📝 **Step 2: Configure SMTP Settings**

Navigate to:

```
Dashboard → Manage Jenkins → Configure System
```

Scroll to:

### **E-mail Notification (Mailer)**

Fill:

* **SMTP server:**

  ```
  smtp.gmail.com
  ```

* **Use SMTP Authentication:** ✔

  * Enter Gmail username
  * Enter App Password (not normal password)

* **Use SSL:** ✔

* **SMTP Port:**

  ```
  465
  ```

* **Default user e-mail suffix:**

  ```
  @gmail.com
  ```

👉 *(Add screenshot)*
`![SMTPConfig](images/smtp-config.png)`

---

# 📌 **Important (Gmail Users Only)**

You must generate an **App Password**:

1. Go to [https://myaccount.google.com](https://myaccount.google.com)
2. Security → App passwords
3. Create one for “Mail”
4. Use that 16-digit password in Jenkins SMTP

---

# 📝 **Step 3: Test Configuration**

Click **Test configuration**
Enter any email like:

```
youremail@gmail.com
```

If everything is correct → You will receive a test mail.

<img width="371" height="176" alt="image" src="https://github.com/user-attachments/assets/603e755b-fc4b-47e8-b02d-5ecab2f60fb2" />


---

# 📝 **Step 4: Add Email Notification in Freestyle Job**

Open any job → Click:

```
Configure → Post-build Actions → Add post-build action → E-mail Notification
```

Add recipients:

```
youremail@gmail.com
team@example.com
```

Select:

✔ Send e-mail for every unstable build
✔ Send e-mail for every failed build

👉 *(Add screenshot)*
`![FreestyleEmail](images/freestyle-email.png)`

---

# 📝 **Step 5: Advanced Email Notifications (Using Email Extension Plugin)**

Click:

```
Post-build Actions → Add post-build action → Editable Email Notification
```

Configure:

* **Project Recipient List:**

  ```
  you@example.com
  ```
* **Subject:**

  ```
  Build: ${PROJECT_NAME} - ${BUILD_STATUS}
  ```
* **Body:**

  ```
  Build URL: ${BUILD_URL}
  Status: ${BUILD_STATUS}
  Console Output: ${BUILD_LOG}
  ```

Profiles available:

* **Failure**
* **Success**
* **Always**

👉 *(Add screenshot)*
`![EmailExt](images/email-ext.png)`

---

# 📝 **Step 6: Send Email Notifications in Jenkins Pipeline (Jenkinsfile)**

Add this inside Pipeline:

### **Simple Failure/Success Email**

```groovy
pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        sh 'echo building...'
      }
    }
  }

  post {
    success {
      emailext subject: "SUCCESS: ${JOB_NAME}",
               body: "Build Successful\n${BUILD_URL}",
               to: "you@example.com"
    }
    failure {
      emailext subject: "FAILURE: ${JOB_NAME}",
               body: "Build Failed\n${BUILD_URL}",
               to: "you@example.com"
    }
  }
}
```

---

### **Send email to multiple recipients**

```groovy
emailext to: 'dev1@example.com, dev2@example.com'
```

---

### **Send attachments (optional)**

```groovy
emailext attachmentsPattern: "build-output.zip",
         to: "team@example.com",
         subject: "Artifact Attached",
         body: "Please find artifact attached."
```


---

# 📝 **Step 7: Verify Emails in Jenkins**

Whenever a build:

* **Fails**
* **Succeeds**
* **Is unstable**

You will automatically receive an email with a message like:

```
Build Status: FAILURE
Job: git-clone-job
Build Number: #3
Console Log URL: <link>
```


