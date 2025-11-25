# 🔗 4️⃣ Integrate Git with Jenkins (GitHub + Freestyle Job)

In this section, you will:

* Connect Jenkins with Git
* Create a job that clones a GitHub repository
* Print the list of files using `ls` command

---

# 📝 **Step 1: Install Git Plugin (If Not Installed)**

Go to:

```
Dashboard → Manage Jenkins → Plugins → Available Plugins
```

Search for:

```
Git Plugin
```

Click **Install without restart**.

<img width="1456" height="643" alt="image" src="https://github.com/user-attachments/assets/e77d160c-e0e2-4407-a4cc-14860a835794" />


---

# 📝 **Step 2: Verify Git is Installed on Jenkins Server**

SSH into your EC2 and check:

```bash
git --version
```

If not installed:

```bash
sudo apt install git -y
```

<img width="385" height="50" alt="image" src="https://github.com/user-attachments/assets/c5afa137-caf2-4a79-aaa3-ef781fc465b5" />


---

# 📝 **Step 3: Create a New Freestyle Job**

Navigate to:

```
Dashboard → New Item
```

Job name:

```
git-clone-job
```

Select:

✔ Freestyle Project
Click **OK**.

<img width="494" height="888" alt="image" src="https://github.com/user-attachments/assets/32b7a099-d140-4f75-b4fb-b37a793804d5" />

---

# 📝 **Step 4: Configure GitHub Repo (Source Code Management)**

Scroll to **Source Code Management**
Select:

✔ **Git**

In “Repository URL” enter your GitHub repo:

```
https://github.com/<your-username>/<repo-name>.git
```

If it is a **public repo**, no credentials needed.
If **private repo**, add credentials using the **Add → Username/Password** option.

<img width="589" height="624" alt="image" src="https://github.com/user-attachments/assets/f2ec9d68-1836-400b-826f-887703facafe" />


---

# 📝 **Step 5: Add Build Step – Execute Shell**

Scroll down to **Build**
Click:

```
Add build step → Execute shell
```

Add command:

```bash
echo "Repository cloned successfully!"
echo "Listing files inside workspace:"
ls -l
```

<img width="521" height="549" alt="image" src="https://github.com/user-attachments/assets/622ce2cb-7451-4c97-9811-91e170b4c9e4" />


---

# 📝 **Step 6: Save the Job**

Click:

```
Save
```

<img width="573" height="381" alt="image" src="https://github.com/user-attachments/assets/90714b9a-0e88-4f34-980e-e0e02532477d" />

---

# 📝 **Step 7: Build the Job**

Click:

```
Build Now
```

Jenkins will:

✔ Create workspace
✔ Clone repo
✔ Run shell commands

<img width="1053" height="731" alt="image" src="https://github.com/user-attachments/assets/761a0535-9d70-4b15-a471-62a72cfaaee6" />


---

# 📝 **Step 8: Check Console Output**

Go to:

```
Build #1 → Console Output
```

You will see something like:

```
Cloning the remote Git repository
> git clone https://github.com/<your-username>/<repo-name>.git
Repository cloned successfully!
Listing files inside workspace:
total 12
-rw-r--r-- 1 jenkins jenkins README.md
-rw-r--r-- 1 jenkins jenkins app.py
-rw-r--r-- 1 jenkins jenkins requirements.txt
Finished: SUCCESS
```

<img width="1053" height="731" alt="image" src="https://github.com/user-attachments/assets/732313d4-053e-4596-9bf9-8a154b2fab83" />


