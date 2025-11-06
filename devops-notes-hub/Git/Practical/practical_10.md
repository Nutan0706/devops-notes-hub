## 🪜 Step 10: Clone Remote Repository from GitHub

When you want to **work on an existing project** hosted on GitHub (or any remote Git server), you don’t start from scratch — you **clone** it.
Cloning creates a **local copy** of the entire repository, including all branches, commits, and files.

---

### 🔹 1. Copy the Repository URL

1. Go to the project’s GitHub page.
2. Click on the **“Code”** (green) button.
3. Copy the repository URL — choose either:

   * **HTTPS:** `https://github.com/username/repo-name.git`
   * **SSH:** `git@github.com:username/repo-name.git`

*(Use HTTPS if you’re new; SSH requires key setup.)*

---

### 🔹 2. Open Terminal / Command Prompt

Navigate to the folder where you want to store the project:

```bash
cd path/to/your/directory
```

---

### 🔹 3. Clone the Repository

Use the `git clone` command followed by the repository URL.

**Example (HTTPS):**

```bash
git clone https://github.com/username/repo-name.git
```

**Example (SSH):**

```bash
git clone git@github.com:username/repo-name.git
```

✅ Git will automatically:

* Create a folder named after the repo
* Download all files, commits, and branches
* Set up a connection to the remote repository (named `origin`)

---

### 🔹 4. Verify the Cloned Repository

Move into the cloned directory:

```bash
cd repo-name
```

Check the remote connection:

```bash
git remote -v
```

**Output Example:**

```
origin  https://github.com/username/repo-name.git (fetch)
origin  https://github.com/username/repo-name.git (push)
```

---

### 🔹 5. Explore the Repository

View branches:

```bash
git branch -a
```

View recent commits:

```bash
git log --oneline --graph --decorate -5
```

---

### 🔹 6. Clone into a Custom Folder (Optional)

If you want a **different folder name** for your cloned repo:

```bash
git clone https://github.com/username/repo-name.git my-folder
```

This will clone the repo into a folder named `my-folder`.

---

### ✅ Quick Summary

| Task                | Command                     | Description                       |
| ------------------- | --------------------------- | --------------------------------- |
| Copy repo URL       | —                           | Get HTTPS or SSH link from GitHub |
| Clone repo          | `git clone <url>`           | Download full project locally     |
| Change directory    | `cd repo-name`              | Move into project folder          |
| Check remote        | `git remote -v`             | Verify connection to GitHub       |
| Clone with new name | `git clone <url> my-folder` | Save project in custom folder     |

---

### 💡 Tips

* Use **SSH** for private repositories — it avoids repeated password prompts.
* After cloning, always pull the latest updates:

  ```bash
  git pull origin main
  ```


