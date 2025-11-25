# ⚙️ 3️⃣ Create Your First Freestyle Project

# 📝 **Step 1: Click “New Item” on Jenkins Dashboard**

Navigate to:

```
Dashboard → New Item
```

Enter the job name:

```
hello-freestyle-job
```

Select:

✔ **Freestyle Project**
and click **OK**.

<img width="939" height="858" alt="image" src="https://github.com/user-attachments/assets/4a9ccf77-0937-4d73-b0f0-455e2309c620" />


---

# 📝 **Step 2: Add Description (Optional)**

You can add a small description like:

```
This is my first freestyle Jenkins job. It prints Hello Jenkins.
```

<img width="1278" height="228" alt="image" src="https://github.com/user-attachments/assets/c30d1713-acfe-491f-a6c5-69f39bd8357b" />


---

# 📝 **Step 3: Go to “Build” Section → Add Build Step**

Scroll down to the **Build** section.

Click:

```
Add build step → Execute shell
```

---

# 📝 **Step 4: Add Shell Command**

Inside the shell command box, write:

```bash
echo "Hello Jenkins"
echo "Current date and time:"
date
```

This will print a message and current timestamp.

<img width="787" height="443" alt="image" src="https://github.com/user-attachments/assets/b975ddb6-1973-4296-93ae-d259aab33eac" />


---

# 📝 **Step 5: Save the Job**

Click on:

```
Save
```

<img width="473" height="230" alt="image" src="https://github.com/user-attachments/assets/179b0b5f-ab63-4df4-91bb-a855673ae441" />


---

# 📝 **Step 6: Build the Job**

Now click:

```
Build Now
```

This triggers the job.

<img width="843" height="585" alt="image" src="https://github.com/user-attachments/assets/105b9032-a81a-455c-a3f1-71d2ad95f211" />


---

# 📝 **Step 7: View Console Output**

Click on:

```
Build #1 → Console Output
```

You should see:

```
Hello Jenkins
Current date and time:
<timestamp>
Finished: SUCCESS
```

<img width="633" height="302" alt="image" src="https://github.com/user-attachments/assets/22ff9ae6-c1e7-4e54-8bd2-9c1b17c254dd" />

