# 🧩 Practical 4 — Use Multi-Stage Docker Builds

### 🎯 **Objective**
Learn how to optimize Docker image size and build performance using **multi-stage builds**, where separate stages handle building, compiling, and final packaging.

---

## 🧠 Key Concepts

| Concept | Description |
|---------|-------------|
| **Multi-Stage Build** | Uses multiple `FROM` statements to create lightweight final images. |
| **Builder Stage** | Handles heavy tasks like compiling, installing dev dependencies, etc. |
| **Final Stage** | Contains only the necessary runtime files → Smaller images. |
| **COPY --from** | Copies artifacts from previous stages. |

---

# ----------------------------------------------------
# ⚙️ Step 1: Create Project Directory
# ----------------------------------------------------

```bash
mkdir multistage-demo
cd multistage-demo
```

---

# ----------------------------------------------------

# 🐍 Step 2: Create a Sample Python App (For Build Example)

# ----------------------------------------------------

Create a simple Python file:

### `app.py`

```python
print("Hello from a Multi-Stage Python App!")
```

Create `requirements.txt`:

```
flask
```

---

# ----------------------------------------------------

# 📦 Step 3: Create Multi-Stage Dockerfile

# ----------------------------------------------------

Create a file named **Dockerfile**:

```Dockerfile
############### STAGE 1 — BUILDER #################
FROM python:3.10-slim AS builder

WORKDIR /app

# Install build dependencies
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Copy application source
COPY app.py .

############### STAGE 2 — FINAL IMAGE #################
FROM python:3.10-slim AS final

WORKDIR /app

# Copy only what is needed from builder stage
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/app.py .

# Make sure Python can find installed packages
ENV PATH=/root/.local/bin:$PATH

CMD ["python", "app.py"]
```

---

## 🧩 Step 4: Build the Multi-Stage Image

```bash
docker build -t multistage-python .
```

---

## 🚀 Step 5: Run the Container

```bash
docker run multistage-python
```

Expected output:

```
Hello from a Multi-Stage Python App!
```

---

# ----------------------------------------------------

# 🧪 Step 6: Compare Image Sizes

# ----------------------------------------------------

Create a "non-optimized" image for comparison:

### Sample basic Dockerfile:

```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

Build it:

```bash
docker build -t normal-python .
```

Now list image sizes:

```bash
docker images
```

Expected comparison:

```
REPOSITORY           SIZE
normal-python        ~150MB
multistage-python    ~50MB
```

🎉 The multi-stage build reduced image size significantly.

---

# ----------------------------------------------------

# 🧱 Step 7: Multi-Stage Build for NodeJS (Optional)

# ----------------------------------------------------

Create the following files:

### `app.js`

```javascript
console.log("Hello from Multi-Stage Node App!");
```

### `package.json`

```json
{
  "name": "node-multi-stage",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  }
}
```

### Multi-stage Dockerfile

```Dockerfile
############ BUILDER ############
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

############ FINAL ############
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app .
CMD ["npm", "start"]
```

Build:

```bash
docker build -t multistage-node .
```

Run:

```bash
docker run multistage-node
```

Expected output:

```
Hello from Multi-Stage Node App!
```

Image size will be much smaller than a regular NodeJS image.

---

# ----------------------------------------------------

# 🧹 Step 8: Cleanup (Optional)

# ----------------------------------------------------

Remove images:

```bash
docker rmi multistage-python normal-python multistage-node
```

---

# ----------------------------------------------------

# ✅ Summary

# ----------------------------------------------------

| Step | Task                         | Description                       |
| ---- | ---------------------------- | --------------------------------- |
| 1    | Create Python/Node app       | Build sample application          |
| 2    | Write multi-stage Dockerfile | Use builder + final stages        |
| 3    | Build image                  | `docker build -t <name> .`        |
| 4    | Run container                | Confirm functionality             |
| 5    | Compare sizes                | Multi-stage = smaller image       |
| 6    | Optional Node example        | Demonstrates multi-stage workflow |

---

## 🧩 Benefits of Multi-Stage Builds

* 🚀 **Smaller images** → faster deployment
* 🔒 **Improved security** → removes build tools
* ⚡ **Better performance** → faster builds via caching
* 🧹 **Cleaner image layers**

---

## 📘 References

* [https://docs.docker.com/build/building/multi-stage/](https://docs.docker.com/build/building/multi-stage/)
* [https://docs.docker.com/develop/develop-images/multistage-build/](https://docs.docker.com/develop/develop-images/multistage-build/)

