# 🐳 Docker – Complete Dev Notes (For GitHub)

A clean, developer-friendly, and interview-ready Docker notes sheet using tables, collapses, and GitHub-optimized formatting.

---

## 📍 1. What is Docker?

| Feature | Description |
|--------|-------------|
| Definition | Docker is a **containerization platform** that packages applications with dependencies for consistent execution across environments. |
| Virtualization | Uses **OS-level virtualization** (not hardware level). |
| Benefits | Lightweight, portable, fast startup, scalable, environment-consistent. |

---

## ⚙️ 2. Core Concepts

| Term | Meaning |
|------|----------|
| Image | Read-only template to create containers. |
| Container | Runnable instance of an image. |
| Dockerfile | Script with instructions to build an image. |
| Docker Engine | Client + Daemon for managing containers. |
| Docker Hub | Public registry for container images. |
| Volumes | Data persistence & sharing. |
| Networks | Communication between containers. |

---

## 🧱 3. Docker Architecture (Missing – Added)

| Component | Role |
|------------|-------|
| Docker Client | CLI that sends commands to daemon. |
| Docker Daemon (dockerd) | Builds, runs & manages containers. |
| Registry | Stores images (Hub, ECR, GitHub, Private). |
| Objects | Images, Containers, Networks, Volumes. |

---

## 🧑‍🍳 4. Dockerfile Must-Knows

<details>
<summary>Click to Expand</summary>

| Instruction | Purpose |
|-------------|-----------|
| `FROM` | Base image |
| `RUN` | Execute commands during build |
| `COPY` / `ADD` | Copy files into image |
| `WORKDIR` | Set working directory |
| `CMD` | Default container command (override allowed) |
| `ENTRYPOINT` | Makes container behave like an executable |
| `EXPOSE` | Documents the port for application |
| `.dockerignore` | Ignore files from build context |

> 💡 **CMD vs ENTRYPOINT**  
- Use **ENTRYPOINT** for fixed command  
- Use **CMD** for default arguments  

</details>

---

## 🧪 5. Basic Commands – Cheat Sheet

| Purpose | Command |
|----------|----------|
| Check version/info | `docker --version`, `docker info` |
| List running containers | `docker ps` |
| List all containers | `docker ps -a` |
| Build image | `docker build -t myimage:tag .` |
| Run container | `docker run -d -p 8080:80 myimage` |
| Stop container | `docker stop <id>` |
| Remove container | `docker rm <id>` |
| Remove image | `docker rmi <id>` |
| View logs | `docker logs <id>` |
| Exec into container | `docker exec -it <id> /bin/sh` |

---

## 📂 6. Volumes & Data Management

| Type | Use Case | Notes |
|------|-----------|--------|
| Volumes | Persistent container data | Managed by Docker |
| Bind Mount | Use host path | Great for local dev |
| tmpfs | Temp in-memory storage | Removed on stop |

**Commands**

```bash
docker volume create myvol
docker run -v myvol:/app/data ...
```
---

## 🌐 7. Docker Networking

| Network Mode | Description |
|--------------|--------------|
| **Bridge (default)** | Containers communicate within the same host |
| **Host** | Container shares host machine’s network stack |
| **None** | Fully isolated container with no network |
| **User-Defined Bridge** | Custom network for container-to-container communication |

**Commands**

```bash
docker network ls
docker network create mynetwork
docker run --network=mynetwork ...
```
---

<details>
<summary><h2>🧩 8. Container Lifecycle</h2></summary>

| Stage            | Action                           |
|------------------|-----------------------------------|
| **Create**        | `docker create`                   |
| **Start**         | `docker start`                    |
| **Run**           | `docker run`                      |
| **Pause/Unpause** | `docker pause`, `docker unpause`  |
| **Stop**          | `docker stop`                     |
| **Restart**       | `docker restart`                  |
| **Kill**          | `docker kill`                     |
| **Remove**        | `docker rm`                       |

</details>

---

<details>
<summary><h2>🧬 9. Docker Compose (Click to Expand)</h2></summary>

### 📌 Features

| Feature   | Description |
|-----------|-------------|
| **File**  | `docker-compose.yml` |
| **Use**   | Run multi-container applications |
| **Commands** | `docker compose up -d`, `docker compose down` |

### 🧱 Example

```yaml
services:
  web:
    image: nginx
    ports:
      - "8080:80"
  redis:
    image: redis
```

</details>

---

<details>

<summary><h2>🧊 10. Image Management (Click to Expand)</h2></summary>

### 📌 Concepts

| Concept | Description |
|---------|--------------|
| **Layered Architecture** | Each Dockerfile instruction creates a new layer |
| **Cache** | Speeds up build time by reusing unchanged layers |
| **Important Commands** | `docker pull`, `docker push` |

</details>
---

<details>
<summary><h2>✅ 11. Best Practices (Click to Expand)</h2></summary>

### 🏆 Docker Best Practices

| Best Practice | Why? |
|-------------------------------|--------------------------------|
| **Use small base images (e.g., Alpine)** | Reduces image size |
| **Keep containers stateless** | Enables easy scaling and replacement |
| **Minimize layers** | Faster build time and smaller image |
| **Use `.dockerignore`** | Cleaner & faster build context |
| **Use Multi-Stage Builds** | Reduces final image size |
| **Don’t run as root** | Improves container security |

</details>

---

<details>
<summary><h2>🧯 12. Common Issues & Fixes (Click to Expand)</h2></summary>

### 🚨 Frequent Docker Issues & Solutions

| Issue | Reason | Fix |
|--------|---------|------|
| **Container exits immediately** | App finishes execution with no running process | Add a `CMD` or `ENTRYPOINT` to keep it running |
| **Port conflicts** | Port already in use on host machine | Change the host mapped port |
| **File permission errors** | Incorrect file/user permissions inside container | Set proper user or use `chmod` |
| **Large image size** | Using heavy base image or unnecessary layers | Use Alpine + Multi-stage builds |

</details>

---

<details>
<summary><h2>🆚 13. Docker vs Virtual Machines (Click to Expand)</h2></summary>

### ⚔️ Key Differences: Docker vs Virtual Machines

| Feature | Docker | Virtual Machine (VM) |
|---------|---------|------------------------|
| **Virtualization Type** | OS-level | Hardware-level |
| **OS** | Shares host kernel | Runs a full guest OS |
| **Size & Speed** | Lightweight & fast | Heavy and slower |
| **Consistency** | High consistency across environments | Varies per VM |

</details>

---

<details>
<summary><h2>🔐 14. Security Basics (Click to Expand)</h2></summary>

### 🛡️ Secure Your Docker Environment

| Practice | Description |
|----------|--------------|
| **Use trusted base images** | Avoid vulnerabilities by pulling images from verified sources (e.g., Docker Hub Official, AWS, GitHub Registry) |
| **Run non-root containers** | Ensure least privilege access — avoid running as `root` inside containers |
| **Read-only file system** | Prevent unauthorized or accidental writes to the container FS |
| **Scan images** | Use `docker scan` (or tools like Trivy, Anchore) to find vulnerabilities |
| **Update Docker engine regularly** | Get the latest security patches and fixes |

</details>

---

<details>
<summary><h2>🌍 15. Registries (Click to Expand)</h2></summary>

### 🏷️ Types of Docker Registries

| Type | Examples |
|-------|------------|
| **Public** | Docker Hub |
| **Private** | AWS ECR, GitHub Container Registry (GHCR), Harbor, JFrog Artifactory |

</details>

---

<details>
<summary><h2>🚀 16. Real-World Scenarios (Click to Expand)</h2></summary>

### 📍 Where Docker Is Used in Real Projects

| Use Case | Explanation |
|----------|--------------|
| **CI/CD** | Build → Test → Ship container images as part of pipeline |
| **Microservices** | One container per service for independent development & deployment |
| **Local Development** | Same image used across Dev, Stage & Prod for consistency |
| **Scaling** | Scale containers using Kubernetes or Docker Swarm |

</details>








