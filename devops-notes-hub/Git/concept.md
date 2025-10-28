# 🧠 Git – Complete Notes for Interviews & Revision

A clean and structured Git cheat sheet + interview prep — formatted to read easily on GitHub.

---

## 📍 What is Git?

> **Git** is a **Distributed Version Control System (DVCS)** used to track changes in code, collaborate with teams, maintain history, and manage branching & merging.  
It stores the **entire history locally**, enabling offline usage.

---

## 🧩 Core Git Concepts

| Concept | Description |
|---------|--------------|
| **Repository (Repo)** | Version-controlled project directory |
| **Working Directory** | Files on your system you are editing |
| **Staging Area (Index)** | Snapshot of changes to be committed |
| **Commit** | Saved snapshot with message & unique SHA |
| **Branch** | Pointer to a series of commits |
| **HEAD** | Reference to current branch/commit |
| **Remote** | Repo hosted on GitHub/GitLab/Bitbucket |

---

<details>
<summary><strong>💻 Must-Know Git Commands (Click to Expand)</strong></summary>

| Command Purpose | Command |
|-----------------|----------|
| Init repo | `git init` |
| Clone repo | `git clone <url>` |
| Check status | `git status` |
| Add changes | `git add <file>` / `git add .` |
| Commit changes | `git commit -m "Message"` |
| View history | `git log --oneline --graph --all` |
| See diff | `git diff` |
| Create branch | `git branch new-branch` |
| Switch branch | `git checkout new-branch` / `git switch new-branch` |
| Create + switch branch | `git checkout -b new-branch` |
| Merge | `git checkout main` → `git merge new-branch` |
| Delete branch | `git branch -d new-branch` |
| Add remote | `git remote add origin <url>` |
| Push branch | `git push origin main` |
| Pull updates | `git pull` |
| Fetch | `git fetch` |
| Stash changes | `git stash` / `git stash pop` |

</details>

---

## 🌿 Git Branching Model

| Branch Type | Usage |
|-------------|--------|
| `main` | Production-ready code |
| `feature/*` | New features development |
| `bugfix/*` | Bug fixes |
| `release/*` | Pre-release stabilization |
| `hotfix/*` | Urgent fixes directly to `main` |

---

## 🔀 Merge vs Rebase

| Merge | Rebase |
|--------|--------|
| Keeps full history & merges changes with a new commit | Rewrites history to create a clean linear timeline |
| Best for shared branches | Best for local & feature branches |
| Safe for teamwork | Avoid rebasing public branches |

---

## ⚔️ Resolving Merge Conflicts

1. Pull latest changes: `git pull`
2. Edit conflicted files and resolve
3. Mark resolved: `git add <file>`
4. Complete merge: `git commit`

---

## ♻️ Undo & Reset Commands

| Action | Command |
|--------|-----------|
| Unstage a file | `git reset HEAD <file>` |
| Amend last commit | `git commit --amend` |
| Discard file changes | `git checkout -- <file>` |
| Hard reset (delete commit + changes) | `git reset --hard HEAD~1` |
| Delete commit but keep changes | `git reset --soft HEAD~1` |

---

## 🏷️ Tags (Versioning)

| Action | Command |
|--------|-----------|
| Create tag | `git tag v1.0` |
| List tags | `git tag` |
| Push tag | `git push origin v1.0` |

---

## ⚡ Useful Shortcuts

| Need | Command |
|------|-----------|
| One-line logs | `git log --oneline --graph --decorate` |
| Who changed which line | `git blame <file>` |
| Track changes to function | `git log -L :func_name:<file>` |

---

## ✅ Best Practices

- Commit early & often with meaningful messages.
- Always pull before push to avoid conflicts.
- Use branches for features & fixes.
- Keep `main` always deployment-ready.
- Use `.gitignore` to skip temp or local files.
- Use **merge for shared**, **rebase for local history cleanup**.
- Use PR/MR review before merging.

---

<details>
<summary><strong>📘 Typical Git Interview Questions (Click to Expand)</strong></summary>

1. Explain Git architecture.  
2. Difference between Git and SVN?  
3. Explain `clone` vs `fetch` vs `pull`.  
4. Explain merge vs rebase.  
5. What is `stash` and when do we use it?  
6. How do you resolve merge conflicts?  
7. How to undo the last commit?  
8. What is HEAD in Git?  
9. How to revert a pushed commit?  
10. Why do we use `.gitignore`?  

</details>

---

> 🔥 Pro Tip: 80% of Git interview questions revolve around **branching, merging, rebasing, undo, and resolving conflicts**.

---


