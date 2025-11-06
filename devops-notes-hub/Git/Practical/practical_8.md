## 🪜 Step 8: Create and Switch Branches

Branches in Git allow you to **work on new features or fixes** without affecting the main codebase.
They help in **parallel development**, making collaboration safe and efficient.

---

### 🔹 1. View All Branches

To see all local branches in your repository:

```bash
git branch
```

**Output Example:**

```
* main
  feature/login
  bugfix/header
```

⭐ The `*` indicates the branch you’re currently on.

---

### 🔹 2. Create a New Branch

Create a new branch from the current branch (usually `main`):

```bash
git branch <branch-name>
```

**Example:**

```bash
git branch feature/login
```

This creates a new branch named `feature/login`, but **does not switch** to it.

---

### 🔹 3. Switch Between Branches

There are two ways to switch branches:

#### ✅ Option 1: Using `git switch` (Recommended for modern Git)

```bash
git switch <branch-name>
```

**Example:**

```bash
git switch feature/login
```

#### ✅ Option 2: Using `git checkout` (Older but still valid)

```bash
git checkout <branch-name>
```

**Example:**

```bash
git checkout feature/login
```

---

### 🔹 4. Create and Switch in One Command

To create a new branch **and switch** to it immediately:

```bash
git switch -c <branch-name>
```

**Example:**

```bash
git switch -c feature/signup
```

Equivalent old syntax:

```bash
git checkout -b feature/signup
```

---

### 🔹 5. Delete a Branch

Once a feature is merged or no longer needed, you can delete it.

#### Delete a local branch:

```bash
git branch -d <branch-name>
```

Force delete (if branch not merged yet):

```bash
git branch -D <branch-name>
```

#### Delete a remote branch:

```bash
git push origin --delete <branch-name>
```

---

### 🔹 6. Rename a Branch

If you want to rename your current branch:

```bash
git branch -m <new-branch-name>
```

**Example:**

```bash
git branch -m feature/authentication
```

---

### ✅ Quick Summary

| Command                                  | Purpose                      | Example                        |
| ---------------------------------------- | ---------------------------- | ------------------------------ |
| `git branch`                             | List all local branches      | `git branch`                   |
| `git branch feature/login`               | Create a new branch          | `git branch feature/login`     |
| `git switch feature/login`               | Switch to an existing branch | `git switch feature/login`     |
| `git switch -c feature/signup`           | Create and switch in one go  | `git switch -c feature/signup` |
| `git branch -d feature/login`            | Delete a branch              | `git branch -d feature/login`  |
| `git push origin --delete feature/login` | Delete a remote branch       | —                              |

---

### 💡 Tips

* Keep your **branch names meaningful**, e.g., `feature/payment`, `bugfix/navbar`.
* Always **commit or stash** changes before switching branches.
* Use short-lived branches to keep the repo clean and easy to manage.
