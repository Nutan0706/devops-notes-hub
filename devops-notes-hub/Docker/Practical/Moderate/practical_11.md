
# 🧩 Practical 11 — Link Containers Using Networks  
### 🎯 Objective  
Learn how to use Docker **user-defined bridge networks** to allow **frontend and backend containers** to communicate using service names instead of IP addresses.

---

# ----------------------------------------------------
# 🧠 Key Concepts  
# ----------------------------------------------------

| Concept | Description |
|---------|-------------|
| **User-defined network** | Containers can communicate using names (DNS). |
| **Service discovery** | Docker automatically resolves container names to IPs. |
| **Backend–Frontend communication** | Frontend calls backend API through the network. |

---

# ----------------------------------------------------
# ⚙️ Step 1 — Create a User-Defined Network  
# ----------------------------------------------------

```bash
docker network create app-network
```

Verify:

```bash
docker network ls
```

---

# ----------------------------------------------------

# 🧱 Step 2 — Create a Simple Backend API (NodeJS Example)

# ----------------------------------------------------

Create directory:

```bash
mkdir backend
cd backend
```

### `server.js`

```javascript
const http = require("http");

const server = http.createServer((req, res) => {
  res.end("Hello from Backend API!");
});

server.listen(3000, () => console.log("Backend running on port 3000"));
```

### `Dockerfile`

```Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
CMD ["node", "server.js"]
```

Build backend image:

```bash
docker build -t backend-app .
```

---

# ----------------------------------------------------

# 🖥️ Step 3 — Create a Simple Frontend (NGINX Static Site)

# ----------------------------------------------------

Create folder:

```bash
mkdir ../frontend
cd ../frontend
```

### `index.html`

```html
<h2>Frontend Connected to Backend</h2>
<div id="result">Loading...</div>
<script>
  fetch("http://backend-app:3000")
    .then(res => res.text())
    .then(data => document.getElementById("result").innerText = data)
    .catch(err => document.getElementById("result").innerText = "Backend unreachable");
</script>
```

### `Dockerfile`

```Dockerfile
FROM nginx:alpine
COPY . /usr/share/nginx/html
```

Build frontend image:

```bash
docker build -t frontend-app .
```

---

# ----------------------------------------------------

# 🚀 Step 4 — Run Both Containers on the Same Network

# ----------------------------------------------------

### Run backend:

```bash
docker run -d \
  --name backend-app \
  --network app-network \
  backend-app
```

### Run frontend:

```bash
docker run -d \
  -p 8080:80 \
  --name frontend-app \
  --network app-network \
  frontend-app
```

---

# ----------------------------------------------------

# 🌐 Step 5 — Test Frontend → Backend Communication

# ----------------------------------------------------

Open browser:

👉 **[http://localhost:8080](http://localhost:8080)**

Expected result:

```
Frontend Connected to Backend
Hello from Backend API!
```

### Why it works:

* Both containers are on the **same network (app-network)**.
* Frontend uses **[http://backend-app:3000](http://backend-app:3000)**, not an IP address.
* Docker’s internal DNS resolves `backend-app` → backend container’s IP.

---

# ----------------------------------------------------

# 🔍 Step 6 — Inspect the Network (Verify Connectivity)

# ----------------------------------------------------

```bash
docker network inspect app-network
```

You should see:

```json
"Containers": {
  "<id>": {
    "Name": "backend-app",
    "IPv4Address": "172.20.0.2/16"
  },
  "<id>": {
    "Name": "frontend-app",
    "IPv4Address": "172.20.0.3/16"
  }
}
```

---

# ----------------------------------------------------

# 🧪 Step 7 — Test Connectivity Manually

# ----------------------------------------------------

Enter frontend container:

```bash
docker exec -it frontend-app sh
```

Ping backend:

```bash
ping backend-app
```

Request backend API:

```bash
wget -qO- http://backend-app:3000
```

Output:

```
Hello from Backend API!
```

Exit:

```bash
exit
```

---

# ----------------------------------------------------

# 🧹 Step 8 — Cleanup

# ----------------------------------------------------

```bash
docker rm -f backend-app frontend-app
docker network rm app-network
```

---

# ----------------------------------------------------

# ✅ Summary

# ----------------------------------------------------

| Step | Purpose                  | Command                                  |
| ---- | ------------------------ | ---------------------------------------- |
| 1    | Create network           | `docker network create app-network`      |
| 2    | Backend API              | NodeJS container                         |
| 3    | Frontend UI              | NGINX container                          |
| 4    | Run both on same network | `--network app-network`                  |
| 5    | Test frontend → backend  | Frontend calls `http://backend-app:3000` |
| 6    | Inspect network          | `docker network inspect`                 |

---

## ⭐ Benefits of Using Networks

* Automatic service discovery (no hardcoded IPs)
* Clean isolation between app groups
* Easy scaling (backend replicas)
* Faster debugging and networking visibility

---

## 📘 References

* [https://docs.docker.com/network/](https://docs.docker.com/network/)
* [https://docs.docker.com/engine/userguide/networking/](https://docs.docker.com/engine/userguide/networking/)
* [https://docs.docker.com/network/network-tutorial-standalone/](https://docs.docker.com/network/network-tutorial-standalone/)

