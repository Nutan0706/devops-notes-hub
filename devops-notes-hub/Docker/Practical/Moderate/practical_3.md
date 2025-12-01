# 🧩 Practical 3 — Use Bind Mounts for Local Development

### 🎯 **Objective**
Learn how to use **bind mounts** to sync local source code with a running Docker container in **real time**, ideal for development workflows.

---

## 🧠 Key Concepts

| Concept | Description |
|---------|-------------|
| **Bind Mount** | Maps a host directory to a container directory. Changes appear instantly. |
| **Hot Reloading** | Real-time code updates without rebuilding the image. |
| **-v (volume) flag** | Used to mount directories: `<host_path>:<container_path>` |

Bind mounts are perfect for developers because the **container always sees the latest local code**.

---

# ----------------------------------------------------
# ⚙️ Step 1: Create a Sample Project
# ----------------------------------------------------

Create a project folder:

```bash
mkdir live-dev
cd live-dev
```

Create a simple file `index.html`:

```html
<h1>Hello from Docker Bind Mount!</h1>
```

Folder structure:

```
live-dev/
└── index.html
```

---

# ----------------------------------------------------

# 🐳 Step 2: Run an NGINX Container With a Bind Mount

# ----------------------------------------------------

Run container and mount the current project directory:

```bash
docker run -d \
  -p 8080:80 \
  --name dev-nginx \
  -v $(pwd):/usr/share/nginx/html \
  nginx
```

### Explanation of Flags:

| Flag                              | Meaning                                     |
| --------------------------------- | ------------------------------------------- |
| `-d`                              | Detached mode                               |
| `-p 8080:80`                      | Maps host port 8080 → container port 80     |
| `--name dev-nginx`                | Container name                              |
| `-v $(pwd):/usr/share/nginx/html` | Bind mount local folder into NGINX web root |

---

# ----------------------------------------------------

# 🌐 Step 3: Test in Browser

# ----------------------------------------------------

Visit:

👉 [http://localhost:8080](http://localhost:8080)

You should see:

```
Hello from Docker Bind Mount!
```

---

# ----------------------------------------------------

# ✏️ Step 4: Real-Time Code Sync Test

# ----------------------------------------------------

Modify `index.html`:

```html
<h1>Updated Live Reload Using Bind Mount!</h1>
```

**Refresh your browser**.

🎉 New content appears **instantly**, without rebuilding or restarting the container.

This is the magic of **bind mounts**.

---

# ----------------------------------------------------

# 🧪 Step 5: Bind Mount for NodeJS Development (Example)

# ----------------------------------------------------

Here is an optional NodeJS example showing real-time code execution.

Create files:

### `app.js`

```javascript
const http = require("http");

const server = http.createServer((req, res) => {
  res.end("Hello from NodeJS with Bind Mount!");
});

server.listen(3000, () => console.log("Server running on port 3000"));
```

Run container with auto-reload tools (nodemon):

```bash
docker run -d \
  -p 3000:3000 \
  --name dev-node \
  -v $(pwd):/app \
  -w /app \
  node:18 \
  bash -c "npm install -g nodemon && nodemon app.js"
```

Update `app.js`, refresh browser → changes take effect instantly.

---

# ----------------------------------------------------

# 🔎 Step 6: Inspect Container Mount Info

# ----------------------------------------------------

```bash
docker inspect dev-nginx | grep -i mount -A 5
```

Sample output:

```json
"Mounts": [
  {
    "Type": "bind",
    "Source": "/home/user/live-dev",
    "Destination": "/usr/share/nginx/html"
  }
]
```

---

# ----------------------------------------------------

# 🧹 Step 7: Cleanup (Optional)

# ----------------------------------------------------

Stop and remove the containers:

```bash
docker stop dev-nginx dev-node
docker rm dev-nginx dev-node
```

---

# ----------------------------------------------------

# ✅ Summary

# ----------------------------------------------------

| Step | Task                          | Command                           |
| ---- | ----------------------------- | --------------------------------- |
| 1    | Create project                | `mkdir live-dev`                  |
| 2    | Run container with bind mount | `-v $(pwd):/usr/share/nginx/html` |
| 3    | View live output              | Browser → `localhost:8080`        |
| 4    | Update code                   | Changes appear instantly          |
| 5    | Optional Node example         | Bind mount + nodemon              |
| 6    | Inspect mount                 | `docker inspect <container>`      |
| 7    | Cleanup                       | Remove containers                 |

---

## 📘 References

* [https://docs.docker.com/storage/bind-mounts/](https://docs.docker.com/storage/bind-mounts/)
* [https://docs.docker.com/get-started/08_using_bind_mounts/](https://docs.docker.com/get-started/08_using_bind_mounts/)


Would you like the next one — **Practical 4: Create Multi-Stage Docker Builds** — in the same GitHub `.md` format?
```
