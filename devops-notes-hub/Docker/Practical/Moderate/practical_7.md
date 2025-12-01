# 🧩 Practical 7 — Use .dockerignore File

### 🎯 **Objective**
Learn how to use a `.dockerignore` file to **exclude unnecessary files** from the Docker build context.  
This improves build performance, reduces image size, and prevents sensitive files from being copied into images.

---

## 🧠 Key Concepts

| Concept | Description |
|---------|-------------|
| **docker build context** | All files sent to Docker engine before building the image. |
| **.dockerignore file** | Tells Docker which files/directories NOT to include in the build context. |
| **Why use it?** | Faster builds, smaller images, avoids leaking credentials. |

---

# ----------------------------------------------------
# ⚙️ Step 1: Create Project Directory
# ----------------------------------------------------

```bash
mkdir dockerignore-demo
cd dockerignore-demo
```

Your folder structure:

```
dockerignore-demo/
    ├── app.py
    ├── notes.txt
    ├── temp/
    ├── secrets.env
    └── Dockerfile
```

---

# ----------------------------------------------------

# 🧱 Step 2: Create a Sample Python App

# ----------------------------------------------------

### `app.py`

```python
print("Hello from Docker with .dockerignore!")
```

---

# ----------------------------------------------------

# 🧩 Step 3: Create a Dockerfile

# ----------------------------------------------------

### `Dockerfile`

```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

CMD ["python", "app.py"]
```

---

# ----------------------------------------------------

# 🚫 Step 4: Create .dockerignore File

# ----------------------------------------------------

Create a file named:

### `.dockerignore`

```
# Ignore temporary files
temp/
*.tmp

# Ignore logs
logs/
*.log

# Ignore virtual environment
venv/

# Ignore OS/system files
.DS_Store

# Ignore documentation
notes.txt

# Ignore secrets (NEVER include secrets in images)
secrets.env
```

This ensures these files NEVER reach the Docker build context.

---

# ----------------------------------------------------

# 🧪 Step 5: Test the Build Context

# ----------------------------------------------------

Run:

```bash
docker build -t dockerignore-demo .
```

Now check the build context files using:

```bash
docker build -t test . --no-cache --progress=plain
```

You will see that ignored files **are not sent** to Docker daemon.

---

# ----------------------------------------------------

# 🔍 Step 6: Verify Ignored Files Inside Container

# ----------------------------------------------------

Run the container:

```bash
docker run --name test-container dockerignore-demo
```

Then inspect the file system:

```bash
docker exec -it test-container ls /app
```

Expected output:

```
app.py
Dockerfile
```

**No temp folder, notes.txt, or secrets.env appear.**

---

# ----------------------------------------------------

# 🧹 Step 7: Cleanup

# ----------------------------------------------------

```bash
docker rm -f test-container
docker rmi dockerignore-demo
```

---

# ----------------------------------------------------

# ✅ Summary

# ----------------------------------------------------

| Feature        | Benefit                                                |
| -------------- | ------------------------------------------------------ |
| Faster builds  | Smaller build context → faster upload to Docker daemon |
| Smaller images | Only required files copied                             |
| More secure    | Prevent accidental copy of secrets and env files       |
| Cleaner builds | Avoid unnecessary clutter in the image                 |

---

### ⭐ Best Practices for .dockerignore

```
# Ignore Git repository
.git/
.gitignore

# Python virtual environment
venv/

# Node modules (if using JS)
node_modules/

# Log files
*.log

# Local environment variables
.env
*.env

# OS files
.DS_Store
Thumbs.db
```

---

## 📘 References

* [https://docs.docker.com/engine/reference/builder/#dockerignore-file](https://docs.docker.com/engine/reference/builder/#dockerignore-file)
* [https://docs.docker.com/develop/develop-images/dockerfile_best-practices/](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

`
