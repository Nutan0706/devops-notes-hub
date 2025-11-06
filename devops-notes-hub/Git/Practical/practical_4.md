## 🪜 Step 4: Check Repository Status & Log

Once you’ve initialized a Git repository and made some commits, it’s important to **check your repo’s current state** and **review commit history**.
Git provides multiple commands for this: `git status`, `git log`, and `git show`.

---

### 🔹 1. Check Repository Status

Use this command to see the **current state of your working directory** and **staging area**.

```bash
git status
```

**It shows:**

* Which files are **modified**, **staged**, or **untracked**
* The **current branch** you’re on
* Hints for next possible actions (e.g., `git add` or `git commit`)

**Example output:**

```
On branch main
Changes not staged for commit:
  modified:   index.html

Untracked files:
  newfile.txt
```

---

### 🔹 2. View Commit History

See a list of **all commits** in the repository.

```bash
git log
```

**Output example:**

```
commit 6e3a12b9a1f7c0c4...
Author: Your Name <your_email@example.com>
Date:   Wed Nov 6 12:34:56 2025 +0530

    Initial commit
```

**Useful variations:**

```bash
git log --oneline       # Shows concise one-line commit summary
git log --graph --decorate --all   # Shows visual branch structure
```

---

### 🔹 3. View Details of a Specific Commit

To inspect **what exactly changed** in a specific commit:

```bash
git show <commit-id>
```

Example:

```bash
git show 6e3a12b
```

**This command displays:**

* Commit author and date
* Commit message
* File changes (diffs) introduced in that commit

---

### ✅ Quick Summary

| Command                | Purpose                                          | Example             |
| ---------------------- | ------------------------------------------------ | ------------------- |
| `git status`           | View changes in working directory & staging area | `git status`        |
| `git log`              | View all commit history                          | `git log --oneline` |
| `git show <commit-id>` | View details of a specific commit                | `git show a1b2c3d`  |
