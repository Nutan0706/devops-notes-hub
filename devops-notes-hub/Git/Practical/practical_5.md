## 🪜 Step 5: View Commit History

To understand how your project evolved over time, you can use Git’s history commands.
The most powerful among them is `git log` — it shows who made changes, when, and what they did.

---

### 🔹 1. Basic Commit History

```bash
git log
```

**This shows:**

* Commit hash
* Author name and email
* Date and time
* Commit message

**Example Output:**

```
commit 8f5c1a2b9a9d3f4a...
Author: Your Name <your_email@example.com>
Date:   Thu Nov 6 10:45:12 2025 +0530

    Added login validation feature
```

---

### 🔹 2. Short & Clean History (oneline view)

```bash
git log --oneline
```

**Output Example:**

```
a1b2c3d Fix login bug
4e5f6g7 Add HTML template
8h9i0j1 Initial commit
```

This shows each commit in a **compact format** — perfect for quick overviews.

---

### 🔹 3. Visual Commit Tree with Branches

```bash
git log --oneline --graph --decorate
```

This command adds **visual structure** to your commit history.

**Breakdown:**

| Option       | Description                                             |
| ------------ | ------------------------------------------------------- |
| `--oneline`  | Displays commits in a single line for readability       |
| `--graph`    | Adds a branch and merge visualization using ASCII lines |
| `--decorate` | Shows branch names, tags, and HEAD pointer info         |

**Example Output:**

```
* a1b2c3d (HEAD -> main, origin/main) Fix login bug
* 4e5f6g7 Add CSS styles
|\
| * 9i8u7y6 (feature/login) Add login API
|/
* 8h9i0j1 Initial commit
```

You can now **see merges, branches, and their relationships** clearly.

---

### 🔹 4. Limit the Number of Commits

If you want to see only the last few commits:

```bash
git log --oneline -5
```

This will show only the **5 most recent commits**.

---

### ✅ Quick Summary

| Command                                | Purpose                           |
| -------------------------------------- | --------------------------------- |
| `git log`                              | Full detailed commit history      |
| `git log --oneline`                    | Compact summary view              |
| `git log --oneline --graph --decorate` | Visual and labeled commit history |
| `git log --oneline -5`                 | Limit to last 5 commits           |

