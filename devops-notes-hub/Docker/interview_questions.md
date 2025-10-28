# 🐳 Docker Interview Questions – Complete Sheet

This document contains **30 Docker Interview Questions** categorized into:
- ✅ Commonly Asked (10)
- 🔸 Moderate Level (10)
- 🚀 Advanced & Scenario-Based (10)

---

## 📌 Quick Summary Table

| Level | Questions Count | Difficulty |
|--------|----------------|--------------|
| ✅ Common | 10 | Easy |
| 🔸 Moderate | 10 | Medium |
| 🚀 Advanced & Scenario Based | 10 | Hard |

---

<details>
<summary><strong>✅ 1. Commonly Asked Docker Interview Questions (Click to Expand)</strong></summary>

| No. | Question |
|-----|-----------|
| 1 | What is Docker and why do we use it? |
| 2 | Difference between a Docker Image and a Docker Container? |
| 3 | What is Dockerfile? |
| 4 | Explain the role of Docker Engine. |
| 5 | What is Docker Hub? |
| 6 | What is a Docker Volume? |
| 7 | What is the purpose of `.dockerignore` file? |
| 8 | How do you check running containers? |
| 9 | What is the difference between `CMD` and `ENTRYPOINT`? |
| 10 | How do you expose ports in Docker? |

</details>

---

<details>
<summary><strong>🔸 2. Moderate Level Docker Questions (Click to Expand)</strong></summary>

| No. | Question |
|-----|-----------|
| 11 | Explain the Docker architecture in detail (Client, Daemon, Registry). |
| 12 | Difference between Docker Image layers & how Union File System works? |
| 13 | What is Multi-Stage build in Docker? |
| 14 | What is Docker Compose and when to use it? |
| 15 | What is the difference between `ADD` and `COPY` in Dockerfile? |
| 16 | How do you persist data in Docker? |
| 17 | What is the use of Docker Networking? |
| 18 | Explain overlay, host, and bridge networks in Docker. |
| 19 | How do you reduce Docker image size? |
| 20 | What is the difference between `docker stop` and `docker kill`? |

</details>

---

<details>
<summary><strong>🚀 3. Advanced + Scenario-Based Docker Interview Questions (Click to Expand)</strong></summary>

| No. | Question |
|-----|-----------|
| 21 | How would you secure a Docker container in production? |
| 22 | How do you handle secrets inside Docker containers? |
| 23 | How can you troubleshoot a container that exits immediately after run? |
| 24 | What are Docker Best Practices for writing Dockerfile? |
| 25 | How does Docker handle container isolation? |
| 26 | In a microservices setup, how do containers communicate across hosts? |
| 27 | You have a container using 90% CPU — how do you limit resources? |
| 28 | A container restarts again & again — how do you debug it? |
| 29 | Scenario: Your image size is 2GB. DevOps team asks to reduce to < 400MB. What steps will you take? |
| 30 | Scenario: Container needs to connect with a DB running on host machine. How will you setup networking? |

</details>

---

## 📍 Bonus: Docker Important Commands (Quick Reference)

| Task | Command |
|-------|----------|
| List running containers | `docker ps` |
| Build an image | `docker build -t name .` |
| Run a container | `docker run -d -p 8080:80 image` |
| View logs | `docker logs container_id` |
| Enter container shell | `docker exec -it container_id sh` |
| Remove unused images/containers | `docker system prune -a` |

---

## 📚 Recommended Practice Scenarios

- Build a Dockerfile for a Python or Node app
- Convert a monolithic application into multi-container with Docker Compose
- Reduce a large image from 1GB → 250MB using Alpine & multi-stage builds
- Setup container networking for microservices
- Deploy containerized app to AWS ECS/Kubernetes later

---


