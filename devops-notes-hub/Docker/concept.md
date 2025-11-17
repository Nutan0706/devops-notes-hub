# 🐳 Docker – Complete Dev Notes

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

## 🧱 3. Docker Architecture 

| Component | Role |
|------------|-------|
| Docker Client | CLI that sends commands to daemon. |
| Docker Daemon (dockerd) | Builds, runs & manages containers. |
| Registry | Stores images (Hub, ECR, GitHub, Private). |
| Objects | Images, Containers, Networks, Volumes. |

---

## 🧑‍🍳 4. Dockerfile Must-Knows

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
> - Use **ENTRYPOINT** for fixed command  
> - Use **CMD** for default arguments  

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

---

## 🌐 7. Docker Networking

| Network Mode            | Description                                             |
| ----------------------- | ------------------------------------------------------- |
| **Bridge (default)**    | Containers communicate within the same host             |
| **Host**                | Container shares host machine’s network stack           |
| **None**                | Fully isolated container with no network                |
| **User-Defined Bridge** | Custom network for container-to-container communication |


---

## 🧩 8. Container Lifecycle

| Stage             | Action                           |
| ----------------- | -------------------------------- |
| **Create**        | `docker create`                  |
| **Start**         | `docker start`                   |
| **Run**           | `docker run`                     |
| **Pause/Unpause** | `docker pause`, `docker unpause` |
| **Stop**          | `docker stop`                    |
| **Restart**       | `docker restart`                 |
| **Kill**          | `docker kill`                    |
| **Remove**        | `docker rm`                      |

---

## 🧬 9. Docker Compose

### 📌 Features

| Feature      | Description                                   |
| ------------ | --------------------------------------------- |
| **File**     | `docker-compose.yml`                          |
| **Use**      | Run multi-container applications              |
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

---

## 🧊 10. Image Management

### 📌 Concepts

| Concept                  | Description                                      |
| ------------------------ | ------------------------------------------------ |
| **Layered Architecture** | Each Dockerfile instruction creates a new layer  |
| **Cache**                | Speeds up build time by reusing unchanged layers |
| **Important Commands**   | `docker pull`, `docker push`                     |

---

## ✅ 11. Best Practices

### 🏆 Docker Best Practices

| Best Practice                            | Why?                                 |
| ---------------------------------------- | ------------------------------------ |
| **Use small base images (e.g., Alpine)** | Reduces image size                   |
| **Keep containers stateless**            | Enables easy scaling and replacement |
| **Minimize layers**                      | Faster build time and smaller image  |
| **Use `.dockerignore`**                  | Cleaner & faster build context       |
| **Use Multi-Stage Builds**               | Reduces final image size             |
| **Don’t run as root**                    | Improves container security          |

---

## 🧯 12. Common Issues & Fixes

### 🚨 Frequent Docker Issues & Solutions

| Issue                           | Reason                                           | Fix                                            |
| ------------------------------- | ------------------------------------------------ | ---------------------------------------------- |
| **Container exits immediately** | App finishes execution with no running process   | Add a `CMD` or `ENTRYPOINT` to keep it running |
| **Port conflicts**              | Port already in use on host machine              | Change the host mapped port                    |
| **File permission errors**      | Incorrect file/user permissions inside container | Set proper user or use `chmod`                 |
| **Large image size**            | Using heavy base image or unnecessary layers     | Use Alpine + Multi-stage builds                |

---

## 🆚 13. Docker vs Virtual Machines

### ⚔️ Key Differences: Docker vs Virtual Machines

| Feature                 | Docker                               | Virtual Machine (VM) |
| ----------------------- | ------------------------------------ | -------------------- |
| **Virtualization Type** | OS-level                             | Hardware-level       |
| **OS**                  | Shares host kernel                   | Runs a full guest OS |
| **Size & Speed**        | Lightweight & fast                   | Heavy and slower     |
| **Consistency**         | High consistency across environments | Varies per VM        |

---

## 🔐 14. Security Basics

### 🛡️ Secure Your Docker Environment

| Practice                           | Description                                                                                                     |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Use trusted base images**        | Avoid vulnerabilities by pulling images from verified sources (e.g., Docker Hub Official, AWS, GitHub Registry) |
| **Run non-root containers**        | Ensure least privilege access — avoid running as `root` inside containers                                       |
| **Read-only file system**          | Prevent unauthorized or accidental writes to the container FS                                                   |
| **Scan images**                    | Use `docker scan` (or tools like Trivy, Anchore) to find vulnerabilities                                        |
| **Update Docker engine regularly** | Get the latest security patches and fixes                                                                       |

---

## 🌍 15. Registries

### 🏷️ Types of Docker Registries

| Type        | Examples                                                             |
| ----------- | -------------------------------------------------------------------- |
| **Public**  | Docker Hub                                                           |
| **Private** | AWS ECR, GitHub Container Registry (GHCR), Harbor, JFrog Artifactory |

---

## 🚀 16. Real-World Scenarios

### 📍 Where Docker Is Used in Real Projects

| Use Case              | Explanation                                                        |
| --------------------- | ------------------------------------------------------------------ |
| **CI/CD**             | Build → Test → Ship container images as part of pipeline           |
| **Microservices**     | One container per service for independent development & deployment |
| **Local Development** | Same image used across Dev, Stage & Prod for consistency           |
| **Scaling**           | Scale containers using Kubernetes or Docker Swarm                  |


---

# **🐳 Docker Concepts – Category-wise Table (Badges in First Column + One-liner Definitions)**

---

# **1️⃣ Docker Basics** ![](https://img.shields.io/badge/Category-Basics-blue)

| Badge                                                     | Concept       | Definition                                                |
| --------------------------------------------------------- | ------------- | --------------------------------------------------------- |
| ![](https://img.shields.io/badge/Docker-Engine-blue)      | Docker Engine | Core container runtime for building & running containers. |
| ![](https://img.shields.io/badge/Docker-Client-lightgrey) | Docker Client | CLI used to interact with Docker Daemon.                  |
| ![](https://img.shields.io/badge/Docker-Daemon-yellow)    | Docker Daemon | Background process managing images & containers.          |
| ![](https://img.shields.io/badge/Container-green)         | Container     | Lightweight executable environment.                       |
| ![](https://img.shields.io/badge/Image-orange)            | Image         | Read-only template used to create containers.             |
| ![](https://img.shields.io/badge/DockerHub-blueviolet)    | Docker Hub    | Public registry for storing/pulling images.               |

---

# **2️⃣ Docker Images** ![](https://img.shields.io/badge/Category-Images-orange)

| Badge                                                     | Concept        | Definition                                        |
| --------------------------------------------------------- | -------------- | ------------------------------------------------- |
| ![](https://img.shields.io/badge/Dockerfile-green)        | Dockerfile     | Script containing instructions to build an image. |
| ![](https://img.shields.io/badge/Build-Image-brightgreen) | docker build   | Command to build an image from Dockerfile.        |
| ![](https://img.shields.io/badge/Tag-Image-blue)          | docker tag     | Adds tag name to an image.                        |
| ![](https://img.shields.io/badge/Push-Image-yellow)       | docker push    | Upload image to Docker registry.                  |
| ![](https://img.shields.io/badge/Pull-Image-red)          | docker pull    | Download image from Docker registry.              |
| ![](https://img.shields.io/badge/Inspect-Image-lightblue) | docker inspect | View detailed metadata of images/containers.      |

---

# **3️⃣ Docker Containers** ![](https://img.shields.io/badge/Category-Containers-green)

| Badge                                                 | Concept      | Definition                               |
| ----------------------------------------------------- | ------------ | ---------------------------------------- |
| ![](https://img.shields.io/badge/Run-Container-green) | docker run   | Creates and starts a new container.      |
| ![](https://img.shields.io/badge/Start-blue)          | docker start | Starts an existing stopped container.    |
| ![](https://img.shields.io/badge/Stop-red)            | docker stop  | Gracefully stops a running container.    |
| ![](https://img.shields.io/badge/RM-grey)             | docker rm    | Deletes a container.                     |
| ![](https://img.shields.io/badge/Logs-teal)           | docker logs  | Shows container logs.                    |
| ![](https://img.shields.io/badge/Exec-lightgrey)      | docker exec  | Run commands inside a running container. |
| ![](https://img.shields.io/badge/PS-yellowgreen)      | docker ps    | List running containers.                 |

---

# **4️⃣ Docker Storage** ![](https://img.shields.io/badge/Category-Storage-purple)

| Badge                                                   | Concept               | Definition                              |
| ------------------------------------------------------- | --------------------- | --------------------------------------- |
| ![](https://img.shields.io/badge/Volumes-green)         | Volume                | Persistent storage for containers.      |
| ![](https://img.shields.io/badge/Bind--Mount-yellow)    | Bind Mount            | Mounts a host directory to a container. |
| ![](https://img.shields.io/badge/TMPFS-lightgrey)       | tmpfs Mount           | In-memory filesystem for containers.    |
| ![](https://img.shields.io/badge/Volume-Create-blue)    | docker volume create  | Create a volume.                        |
| ![](https://img.shields.io/badge/Volume-Inspect-orange) | docker volume inspect | View volume details.                    |
| ![](https://img.shields.io/badge/Volume-LS-red)         | docker volume ls      | List volumes.                           |

---

# **5️⃣ Docker Networking** ![](https://img.shields.io/badge/Category-Networking-blueviolet)

| Badge                                                 | Concept         | Definition                                |
| ----------------------------------------------------- | --------------- | ----------------------------------------- |
| ![](https://img.shields.io/badge/Bridge-green)        | Bridge Network  | Default network for containers on a host. |
| ![](https://img.shields.io/badge/Host-orange)         | Host Network    | Container uses host network namespace.    |
| ![](https://img.shields.io/badge/None-grey)           | None Network    | No networking for container.              |
| ![](https://img.shields.io/badge/Overlay-lightblue)   | Overlay Network | Multi-host networking (Swarm/K8s).        |
| ![](https://img.shields.io/badge/Port-Mapping-yellow) | Port Mapping    | Maps host port to container port.         |
| ![](https://img.shields.io/badge/Docker-Network-blue) | docker network  | Manages container networks.               |

---

# **6️⃣ Docker Compose** ![](https://img.shields.io/badge/Category-Compose-brightgreen)

| Badge                                                 | Concept             | Definition                                |
| ----------------------------------------------------- | ------------------- | ----------------------------------------- |
| ![](https://img.shields.io/badge/Compose--File-blue)  | docker-compose.yml  | YAML file to define multi-container apps. |
| ![](https://img.shields.io/badge/Compose--Up-green)   | docker compose up   | Start entire multi-container setup.       |
| ![](https://img.shields.io/badge/Compose--Down-red)   | docker compose down | Stop & remove containers/networks.        |
| ![](https://img.shields.io/badge/Services-yellow)     | Services            | Defines containers in compose.            |
| ![](https://img.shields.io/badge/Depends--On-orange)  | depends_on          | Defines container startup order.          |
| ![](https://img.shields.io/badge/Env--File-lightgrey) | .env File           | External environment variable file.       |

---

# **7️⃣ Docker Registry & Distribution** ![](https://img.shields.io/badge/Category-Registry-grey)

| Badge                                                   | Concept          | Definition                         |
| ------------------------------------------------------- | ---------------- | ---------------------------------- |
| ![](https://img.shields.io/badge/Registry-blueviolet)   | Registry         | Storage for Docker images.         |
| ![](https://img.shields.io/badge/Private--Registry-red) | Private Registry | Self-hosted secure image registry. |
| ![](https://img.shields.io/badge/Tagging-green)         | Tagging          | Labelling images with versions.    |
| ![](https://img.shields.io/badge/Repository-yellow)     | Repository       | Collection of related images.      |

---

# **8️⃣ Docker Swarm (Orchestration)** ![](https://img.shields.io/badge/Category-Swarm-orange)

| Badge                                                 | Concept       | Definition                                    |
| ----------------------------------------------------- | ------------- | --------------------------------------------- |
| ![](https://img.shields.io/badge/Swarm-Cluster-blue)  | Swarm Cluster | Docker’s built-in orchestration system.       |
| ![](https://img.shields.io/badge/Manager-green)       | Manager Nodes | Schedule tasks & manage cluster state.        |
| ![](https://img.shields.io/badge/Worker-lightgrey)    | Worker Nodes  | Execute tasks assigned by manager.            |
| ![](https://img.shields.io/badge/Service-purple)      | Service       | Running app definition in Swarm.              |
| ![](https://img.shields.io/badge/Task-yellowgreen)    | Task          | Single container in a service.                |
| ![](https://img.shields.io/badge/Scaling-brightgreen) | Scaling       | Increase/decrease number of service replicas. |

---

# **9️⃣ Docker Security** ![](https://img.shields.io/badge/Category-Security-red)

| Badge                                                   | Concept        | Definition                        |
| ------------------------------------------------------- | -------------- | --------------------------------- |
| ![](https://img.shields.io/badge/Rootless-blue)         | Rootless Mode  | Runs Docker without root access.  |
| ![](https://img.shields.io/badge/Secrets-green)         | Secrets        | Store sensitive data securely.    |
| ![](https://img.shields.io/badge/Content--Trust-orange) | Content Trust  | Ensures image authenticity.       |
| ![](https://img.shields.io/badge/Scanning-yellow)       | Image Scanning | Detect vulnerabilities in images. |

---

# **🔟 Docker Best Practices** ![](https://img.shields.io/badge/Category-BestPractices-teal)

| Badge                                                     | Concept           | Definition                                     |
| --------------------------------------------------------- | ----------------- | ---------------------------------------------- |
| ![](https://img.shields.io/badge/Small-Images-green)      | Small Images      | Reduce size with minimal base images.          |
| ![](https://img.shields.io/badge/Multi--Stage-blue)       | Multi-Stage Build | Build efficiently using stages.                |
| ![](https://img.shields.io/badge/Non--Root-red)           | Non-root User     | Run containers without root.                   |
| ![](https://img.shields.io/badge/Healthcheck-orange)      | HEALTHCHECK       | Add health monitoring to containers.           |
| ![](https://img.shields.io/badge/Version--Pinning-yellow) | Version Pinning   | Always specify exact versions of dependencies. |

---


