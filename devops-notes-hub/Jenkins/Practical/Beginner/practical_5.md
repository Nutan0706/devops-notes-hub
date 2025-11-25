# 🚀 5️⃣ Trigger Builds Automatically (Poll SCM / GitHub Webhook)

In this task, you will configure Jenkins to **automatically trigger builds** whenever:

✔ Code is pushed to GitHub (Webhook)
✔ Or Jenkins checks for changes periodically (Poll SCM)

---

# 📝 **Step 1: Open Your Git Project Job**

Go to:

```
Dashboard → git-clone-job
```

Click:

```
Configure
```
---

# 📝 **Step 2 (Option A): Enable Poll SCM (Jenkins Pulls Changes Periodically)**

Scroll to:

```
Build Triggers → Poll SCM
```

Tick the checkbox.

In the schedule box, enter:

```
* * * * *
```

This means Jenkins will check the GitHub repo **every minute**.

Or a better production schedule:

```
H/5 * * * *
```

Check every 5 minutes.

<img width="960" height="547" alt="image" src="https://github.com/user-attachments/assets/905d796b-4e0b-4efc-9dab-e1793c4be3df" />


---

# 📝 **Step 3: Save the Job**

Click:

```
Save
```

---

# 📝 **Step 4: Test Poll SCM Trigger**

Make any change in your repo:

```bash
git add .
git commit -m "testing poll scm"
git push
```

Within 1 minute, Jenkins will trigger a build automatically.

---

---

# 🟦 **Option B: GitHub Webhook (Recommended)**

Webhook triggers a build **instantly**, no waiting.

---

# 📝 **Step 5: Enable GitHub Webhook Trigger in Jenkins**

Open your job → Click:

```
Configure → Build Triggers → GitHub hook trigger for GITScm polling
```

---

# 📝 **Step 6: Copy Jenkins Webhook URL**

Webhook URL format:

```
http://<your-EC2-public-ip>:8080/github-webhook/
```

OR if using Nginx/Domain:

```
http://your-domain/github-webhook/
```

---

# 📝 **Step 7: Add Webhook in GitHub Repo**

Go to your GitHub:

```
Repository → Settings → Webhooks → Add Webhook
```

Enter:

* **Payload URL:**

  ```
  http://<EC2-IP>:8080/github-webhook/
  ```

* **Content type:**

  ```
  application/json
  ```

* **Events:**
  ✔ Just the push event

Click **Add Webhook**

---

# 📝 **Step 8: Push Code to Test Webhook**

Make a code change:

```bash
git add .
git commit -m "webhook test"
git push
```

You should instantly see a new Jenkins build triggered.


