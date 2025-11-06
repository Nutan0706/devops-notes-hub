## 🪜 Step 6: Undo Changes (Reset, Revert, Restore)

In Git, mistakes happen — maybe you committed the wrong file or modified something accidentally.
Git provides **three main commands** to undo changes safely and efficiently:
`git reset`, `git revert`, and `git restore`.

---

### 🔹 1. `git reset` — Move the HEAD (and optionally unstage or delete commits)

Use `git reset` to **undo commits or unstage files**.

#### 🧩 Types of Reset:

| Type                | Command                         | Effect                                                                  |
| ------------------- | ------------------------------- | ----------------------------------------------------------------------- |
| **Soft**            | `git reset --soft <commit-id>`  | Moves HEAD to a previous commit but **keeps changes staged**.           |
| **Mixed (default)** | `git reset --mixed <commit-id>` | Moves HEAD and **unstages files**, but keeps them in working directory. |
| **Hard**            | `git reset --hard <commit-id>`  | Moves HEAD and **deletes all changes permanently**.                     |

#### Example:

```bash
git reset --hard HEAD~1
```

➡️ This removes the **last commit** and resets everything to the previous state.
⚠️ **Be careful:** `--hard` deletes changes — they cannot be recovered easily.

---

### 🔹 2. `git revert` — Safely Undo a Commit (without changing history)

Unlike `reset`, `revert` **creates a new commit** that undoes the changes from a specific commit.
It’s the **safest way** to undo something in a **shared repository**.

#### Example:

```bash
git revert <commit-id>
```

Git will open your text editor to confirm the new commit message.
After saving and closing, the previous commit’s changes will be reversed.

**Example output:**

```
Revert "Added wrong API endpoint"
[main 1a2b3c4] Revert "Added wrong API endpoint"
```

✅ This keeps your project history **intact and clean**.

---

### 🔹 3. `git restore` — Restore Working Directory Files

Use this to **undo unstaged changes** in your working directory
(before committing anything).

#### Example 1: Restore a specific file

```bash
git restore filename.txt
```

#### Example 2: Restore all files

```bash
git restore .
```

This discards **local modifications** and resets files to their **last committed state**.

---

### ⚡ Quick Comparison Table

| Command       | Purpose                                          | Safe for shared repos? | Example                   |
| ------------- | ------------------------------------------------ | ---------------------- | ------------------------- |
| `git reset`   | Move HEAD (undo commits or unstage)              | ❌ No                   | `git reset --hard HEAD~1` |
| `git revert`  | Create a new commit that reverses a previous one | ✅ Yes                  | `git revert a1b2c3d`      |
| `git restore` | Undo local file changes (not yet staged)         | ✅ Yes                  | `git restore app.py`      |

---

### ✅ Summary

* 🧹 **Use `restore`** → to undo unstaged file changes.
* 🔙 **Use `reset`** → to move HEAD or remove commits (careful!).
* 🛡️ **Use `revert`** → to safely undo commits in public branches.
