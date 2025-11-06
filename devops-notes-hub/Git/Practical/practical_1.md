# 🧰 Git Setup Guide

This guide explains how to **install Git** and **configure user information** before starting version control.

---

## 🪜 Step 1: Install Git

### 🔹 On Windows

1. Download Git from the official website:
   👉 [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Run the installer and follow the setup wizard.
3. Verify installation:

   ```bash
   git --version
   ```

### 🔹 On macOS

```bash
brew install git
```

Verify:

```bash
git --version
```

### 🔹 On Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git -y
```

Verify:

```bash
git --version
```

---

## 🪜 Step 2: Configure Git User Information

Set your **global username** and **email** (these will be used in all your commits):

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

✅ Verify the configuration:

```bash
git config --list
```

Expected output:

```
user.name=Your Name
user.email=your_email@example.com
```

---

## 🪜 Step 3: Set Default Branch Name (optional but recommended)

Modern Git uses `main` as the default branch name instead of `master`. You can set it globally:

```bash
git config --global init.defaultBranch main
```

---

## 🪜 Step 4: Create and Initialize a Git Repository

1. Go to your project folder:

   ```bash
   cd path/to/your/project
   ```
2. Initialize Git:

   ```bash
   git init
   ```
3. Add files and commit:

   ```bash
   git add .
   git commit -m "Initial commit"
   ```

---

## 🪜 Step 5: Link Local Repo with GitHub

1. Create a **new repository** on [GitHub](https://github.com/).
2. Copy the repository URL (HTTPS or SSH).
3. Link it to your local repo:

   ```bash
   git remote add origin https://github.com/username/repo-name.git
   ```
4. Push your code:

   ```bash
   git branch -M main
   git push -u origin main
   ```

---

## ✅ Quick Summary

| Step | Command                                            | Description           |
| ---- | -------------------------------------------------- | --------------------- |
| 1    | `git --version`                                    | Verify installation   |
| 2    | `git config --global user.name "Your Name"`        | Set username          |
| 3    | `git config --global user.email "you@example.com"` | Set email             |
| 4    | `git init`                                         | Initialize local repo |
| 5    | `git remote add origin <url>`                      | Connect GitHub repo   |
| 6    | `git push -u origin main`                          | Push code to GitHub   |

---
