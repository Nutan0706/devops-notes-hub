# 🧠 Git Interview Questions (Beginner → Advanced → Scenario-Based)

A structured Git interview preparation sheet formatted for GitHub.  
Includes collapsible sections, tabular format & short hints.

---

## 📍 Table of Contents
- [✅ Commonly Asked Questions](#-commonly-asked-questions)
- [📘 Moderate Level Questions](#-moderate-level-questions)
- [🔥 Advanced Questions](#-advanced-questions)
- [🧪 Scenario-Based Questions](#-scenario-based-questions)

---

### ✅ Commonly Asked Questions

<details>
<summary><strong>Click to Expand (10 Questions)</strong></summary>

| # | Question | Hint |
|---|-----------|-------|
| 1 | What is Git and why is it used? | DVCS, version control |
| 2 | Difference between Git and GitHub? | Tool vs platform |
| 3 | What is a commit in Git? | Snapshot of changes |
| 4 | What is a branch in Git? | Parallel development line |
| 5 | Command to check the status of files? | `git status` |
| 6 | How do you stage and commit changes? | `git add`, `git commit` |
| 7 | What is `.gitignore` used for? | Ignore unwanted files |
| 8 | What is the difference: `git pull` vs `git fetch`? | Fetch doesn’t merge |
| 9 | What is a merge conflict? | Conflicting file edits |
|10 | How to view commit history? | `git log` |

</details>

---

### 📘 Moderate Level Questions

<details>
<summary><strong>Click to Expand (10 Questions)</strong></summary>

| # | Question | Hint |
|---|-----------|-------|
| 1 | What does HEAD mean in Git? | Pointer to current branch |
| 2 | Difference between merge and rebase? | New commit vs rewrite |
| 3 | What is `git stash` and when do you use it? | Temporary save work |
| 4 | Explain `git revert` vs `git reset`. | Undo commit safely vs remove |
| 5 | What are remote repositories? | GitHub, GitLab, Bitbucket |
| 6 | How to create and switch to new branch? | `checkout -b` |
| 7 | What is a tag in Git? | Mark release version |
| 8 | How do you rename a branch? | `git branch -m` |
| 9 | How do you delete a branch locally & remotely? | `-d` & `push origin --delete` |
|10 | What is fast-forward merge? | Direct pointer move |

</details>

---

### 🔥 Advanced Questions

<details>
<summary><strong>Click to Expand (10 Questions)</strong></summary>

| # | Question | Hint |
|---|-----------|-------|
| 1 | Explain Git internal architecture (Objects: Blob, Tree, Commit, Tag). | Key-value store |
| 2 | What is a bare repository? | No working directory |
| 3 | What is `git cherry-pick` used for? | Pick specific commit |
| 4 | What is `git rebase -i` used for? | Squash, reorder commits |
| 5 | How do submodules work in Git? | Repo inside repo |
| 6 | What is `git reflog` and when is it used? | Recover lost commits |
| 7 | Explain Git hooks. | Pre-commit, pre-push |
| 8 | What is the purpose of `git bisect`? | Binary search for bug |
| 9 | How to sign commits? | GPG signature |
|10 | What is shallow clone? | `--depth` limited history |

</details>

---

### 🧪 Scenario-Based Questions

<details>
<summary><strong>Click to Expand (10 Questions)</strong></summary>

| # | Question | Hint |
|---|-----------|-------|
| 1 | You committed to `main` instead of `feature` branch. How will you fix it? | `reset` + `checkout -b` |
| 2 | You pushed incorrect code. How do you undo it safely? | `revert` |
| 3 | Two developers changed the same file and conflict occurred — how do you resolve it? | Manual merge resolve |
| 4 | You want to clean messy commit history before merging to `main`. What do you do? | Interactive rebase |
| 5 | One file always shows `modified` but nothing changed. Why? | Line endings, `.gitattributes` |
| 6 | You need code from one branch to another but not entire branch — only one commit. | Cherry-pick |
| 7 | Accidentally deleted branch — how to recover? | `reflog` |
| 8 | CI/CD failing due to large repo size — how to reduce repo size? | Remove history, BFG tool |
| 9 | You want to work on a feature but pull request review is pending — how to stack work? | `stash` / new branch |
|10 | How do you enforce coding rules before commits? | Git hooks |

</details>

---


---

Would you like me to now create a **Git + GitHub + GitLab Combined Interview Master Sheet** in same format with collapsible sections, diagrams & commands?
