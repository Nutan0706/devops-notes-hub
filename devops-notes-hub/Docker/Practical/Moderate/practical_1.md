# 🧩 Practical 1 — Dockerize a Simple Python / NodeJS App

### 🎯 **Objective**
Learn how to create **app-specific Dockerfiles** for Python and NodeJS applications and run them inside Docker containers.

---

# ---------------------------------------------------------
# 🐍 PART A — DOCKERIZE A SIMPLE PYTHON APP
# ---------------------------------------------------------

## 🧱 Step 1: Create Project Folder

```bash
mkdir python-app
cd python-app
```

## 📄 Step 2: Create `app.py`

```python
print("Hello from Python Docker Container!")
```

---

## 📦 Step 3: Create `requirements.txt` (optional)

If your app needs dependencies:

```
flask
```

(For this simple example, dependencies are optional.)

---

## 🐳 Step 4: Create Dockerfile for Python App

Create a file named **Dockerfile**:

```Dockerfile
# Use official Python runtime
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files into container
COPY . .

# Install dependencies (if any)
RUN pip install -r requirements.txt || true

# Default command
CMD ["python", "app.py"]
```

---

## ⚙️ Step 5: Build the Docker Image

```bash
docker build -t python-demo .
```

---

## 🚀 Step 6: Run the Python Container

```bash
docker run --name py-container python-demo
```

Expected output:

```
Hello from Python Docker Container!
```

---

# ---------------------------------------------------------

# 🟦 PART B — DOCKERIZE A SIMPLE NODEJS APP

# ---------------------------------------------------------

## 🧱 Step 1: Create Project Folder

```bash
mkdir node-app
cd node-app
```

## 📄 Step 2: Create `app.js`

```javascript
console.log("Hello from NodeJS Docker Container!");
```

---

## 📦 Step 3: Create `package.json`

```json
{
  "name": "node-app",
  "version": "1.0.0",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  }
}
```

---

## 🐳 Step 4: Create Dockerfile for NodeJS App

Create a file named **Dockerfile**:

```Dockerfile
# Use official Node image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files first (for caching)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy rest of the project
COPY . .

# Default command
CMD ["npm", "start"]
```

---

## ⚙️ Step 5: Build the NodeJS Image

```bash
docker build -t node-demo .
```

---

## 🚀 Step 6: Run the NodeJS Container

```bash
docker run --name node-container node-demo
```

Expected output:

```
Hello from NodeJS Docker Container!
```

---

# ---------------------------------------------------------

# 🧩 PRACTICAL SUMMARY

# ---------------------------------------------------------

| Step | Python App         | NodeJS App         |
| ---- | ------------------ | ------------------ |
| 1    | Create `app.py`    | Create `app.js`    |
| 2    | Create Dockerfile  | Create Dockerfile  |
| 3    | Build Image        | Build Image        |
| 4    | Run Container      | Run Container      |
| 5    | App prints message | App prints message |

---

## 🧹 Cleanup (Optional)

Remove containers:

```bash
docker rm -f py-container node-container
```

Remove images:

```bash
docker rmi python-demo node-demo
```

---

## 📘 References

* [https://docs.docker.com/language/python/](https://docs.docker.com/language/python/)
* [https://docs.docker.com/language/nodejs/](https://docs.docker.com/language/nodejs/)
* [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
