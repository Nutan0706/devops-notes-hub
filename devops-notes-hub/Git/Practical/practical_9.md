## 🪜 Step 9: Merge Branches

After developing a new feature or fixing a bug in a separate branch, you’ll want to **merge those changes** into your main branch (e.g., `main` or `dev`).
Git provides commands like `git merge` to combine code — and sometimes, you’ll need to resolve **merge conflicts** manually.

---

### 🔹 1. Switch to the Target Branch

Before merging, make sure you’re on the branch **where you want to merge changes into**.
For example, to merge a feature branch into `main`:

```bash
git switch main
```

or

```bash
git checkout main
```

---

### 🔹 2. Merge the Source Branch

Now, merge your feature branch into the current branch:

```bash
git merge <branch-name>
```

**Example:**

```bash
git merge feature/login
```

✅ This applies all commits from `feature/login` into `main`.

**Output example:**

```
Updating a1b2c3d..d4e5f6g
Fast-forward
 login.html | 10 ++++++++++
 1 file changed, 10 insertions(+)
```

---

### 🔹 3. Fast-Forward Merge vs. Three-Way Merge

| Type                   | Description                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| **Fast-forward merge** | Happens when the target branch has not diverged. Git just moves the pointer forward.       |
| **Three-way merge**    | Happens when both branches have new commits. Git combines changes and may cause conflicts. |

---

### 🔹 4. Handling Merge Conflicts

Sometimes, Git cannot automatically merge two branches — for example, if both branches changed the same line in a file.
You’ll see something like this:

```
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and commit the result.
```

#### ✅ Steps to Resolve a Conflict:

1. Open the conflicted file — it will look like this:

   ```python
   <<<<<<< HEAD
   print("Hello from main")
   =======
   print("Hello from feature branch")
   >>>>>>> feature/login
   ```

2. **Manually edit** the file to keep the correct version:

   ```python
   print("Hello from merged code")
   ```

3. After fixing all conflicts:

   ```bash
   git add <file>
   git commit
   ```

Git will create a new **merge commit** to record the merge resolution.

---

### 🔹 5. Abort a Merge (Optional)

If you realize you want to stop the merge process:

```bash
git merge --abort
```

This restores your branch to the state before the merge started.

---

### 🔹 6. View Merge History

To see which commits were merges:

```bash
git log --oneline --graph --decorate
```

Merge commits are usually labeled with `(HEAD -> main, MERGE)`.

---

### ✅ Quick Summary

| Command                   | Purpose                        | Example                   |
| ------------------------- | ------------------------------ | ------------------------- |
| `git switch main`         | Move to main branch            | `git switch main`         |
| `git merge feature/login` | Merge feature branch into main | `git merge feature/login` |
| `git merge --abort`       | Cancel an ongoing merge        | —                         |
| `git add . && git commit` | Resolve merge conflicts        | —                         |
| `git log --graph`         | View merge history             | —                         |

---

### 💡 Tips

* Always **pull latest changes** before merging:

  ```bash
  git pull origin main
  ```
* Use **feature branches** for new work and merge them after testing.
* Prefer **fast-forward merges** when possible for a clean history.
* For large teams, consider **pull requests (PRs)** instead of direct merges.
