# 🧩 Practical 10 — Docker Logs & Debugging  
### 🎯 Objective  
Learn how to debug containers using:  
- `docker logs`  
- `docker stats`  
- `docker inspect`  
- `docker exec`  
- Common troubleshooting techniques  

This practical helps diagnose application errors, crashes, resource issues, and container misconfigurations.

---

# ----------------------------------------------------
# 🧠 Key Concepts  
# ----------------------------------------------------

| Command | Description |
|---------|-------------|
| `docker logs` | View container standard output (stdout/stderr) |
| `docker stats` | Live resource usage (CPU, memory, network, I/O) |
| `docker inspect` | Detailed container config, mounts, networks |
| `docker exec` | Enter running containers for debugging |
| `docker events` | Monitor container lifecycle and daemon events |

---

# ----------------------------------------------------
# ⚙️ Step 1 — Create a Test Container  
# ----------------------------------------------------

Run a simple web server:

```bash
docker run -d --name web-demo -p 8080:80 nginx
````

Check container list:

```bash
docker ps
```

---

# ----------------------------------------------------

# 📜 Step 2 — View Logs with docker logs

# ----------------------------------------------------

### View logs:

```bash
docker logs web-demo
```

### Follow logs in real-time:

```bash
docker logs -f web-demo
```

### Show timestamps:

```bash
docker logs -t web-demo
```

### View last 20 lines:

```bash
docker logs --tail 20 web-demo
```

---

# ----------------------------------------------------

# 📊 Step 3 — Monitor Resource Usage with docker stats

# ----------------------------------------------------

Run:

```bash
docker stats
```

Example output:

```
CONTAINER ID   NAME       CPU %   MEM USAGE / LIMIT     MEM %  
c1ab23d4e5f6   web-demo   0.12%   5.3MiB / 1.94GiB       0.27%
```

This helps debug:

* High CPU usage
* Memory leaks
* Network traffic spikes
* Container throttling from resource limits

---

# ----------------------------------------------------

# 🔍 Step 4 — Inspect Container Details

# ----------------------------------------------------

Use `docker inspect` to view container metadata:

```bash
docker inspect web-demo
```

Common sections to check:

### Check container IP:

```bash
docker inspect web-demo | grep -i "IPAddress"
```

### Check mounted volumes:

```bash
docker inspect web-demo | grep -i Mounts -A 10
```

### Check environment variables:

```bash
docker inspect web-demo | grep -i Env -A 10
```

### Check entrypoint & commands:

```bash
docker inspect web-demo | grep -i '"Cmd"' -A 3
```

---

# ----------------------------------------------------

# 🐚 Step 5 — Debug Inside the Container Using docker exec

# ----------------------------------------------------

### Start an interactive shell inside the container:

```bash
docker exec -it web-demo bash
```

(If image doesn't include bash, use sh):

```bash
docker exec -it web-demo sh
```

Now you can:

```bash
ls /var/log
cat /etc/nginx/nginx.conf
curl http://localhost
```

Exit:

```bash
exit
```

---

# ----------------------------------------------------

# 🧪 Step 6 — View Docker Daemon Events

# ----------------------------------------------------

Monitor Docker daemon activity in real-time:

```bash
docker events
```

Useful for debugging:

* Crashed containers
* Restarts
* Network disconnects
* Volume attach/detach issues

Stop with **Ctrl + C**.

---

# ----------------------------------------------------

# 💥 Step 7 — Debugging Common Issues

# ----------------------------------------------------

### 1️⃣ Container Starts Then Immediately Exits

Check logs:

```bash
docker logs <container>
```

Check command:

```bash
docker inspect <container> | grep Cmd -A 3
```

---

### 2️⃣ Port Already in Use

```bash
docker run -p 8080:80 nginx
```

Error:

```
Bind: address already in use
```

Find process using port:

```bash
sudo lsof -i :8080
```

---

### 3️⃣ Container Cannot Reach Other Containers

Check network:

```bash
docker network inspect <network>
```

Ping another container:

```bash
docker exec -it <container> ping <service_name>
```

---

### 4️⃣ File Permission Issues

Check mounted volume permissions:

```bash
docker exec -it <container> ls -l /app
```

---

### 5️⃣ Container Crashing Due to Memory Limit

Check exit code:

```bash
docker ps -a | grep Exited
```

Exit code **137** → Out of memory (OOMKill).

---

# ----------------------------------------------------

# 🧹 Step 8 — Cleanup

# ----------------------------------------------------

```bash
docker rm -f web-demo
```

---

# ----------------------------------------------------

# ✅ Summary

# ----------------------------------------------------

| Tool             | Use Case                             |
| ---------------- | ------------------------------------ |
| `docker logs`    | Debug app output, crashes, errors    |
| `docker stats`   | Live resource monitoring             |
| `docker inspect` | View configuration details           |
| `docker exec`    | Shell access for real-time debugging |
| `docker events`  | Monitor daemon/system-level events   |

Together these tools make Docker troubleshooting significantly easier.

---

## 📘 References

* [https://docs.docker.com/config/containers/logging/](https://docs.docker.com/config/containers/logging/)
* [https://docs.docker.com/engine/reference/commandline/stats/](https://docs.docker.com/engine/reference/commandline/stats/)
* [https://docs.docker.com/engine/reference/commandline/inspect/](https://docs.docker.com/engine/reference/commandline/inspect/)




