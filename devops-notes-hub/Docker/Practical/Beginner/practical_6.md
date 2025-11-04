# 🧩 Practical 6 — Manage Images and Containers

### 🎯 **Objective**
Learn how to manage Docker containers and images — including listing, starting, stopping, and removing them using essential Docker CLI commands.

---

## 🧠 Key Concepts

| Concept | Description |
|----------|--------------|
| **Container** | A lightweight runtime instance of a Docker image |
| **Image** | A read-only template used to create containers |
| **Lifecycle Management** | Start → Stop → Restart → Remove containers/images |

---

## ⚙️ Step 1: Verify Docker Installation

Check if Docker is working correctly:
```bash
docker --version
docker info
```

---

## 🧩 Step 2: List Containers

* **List running containers**

  ```bash
  docker ps
  ```

  Example output:

  ```
  CONTAINER ID   IMAGE     COMMAND                  STATUS         PORTS                  NAMES
  a1b2c3d4e5f6   nginx     "/docker-entrypoint.…"   Up 10 seconds  0.0.0.0:8080->80/tcp   mynginx
  ```

* **List all containers (including stopped)**

  ```bash
  docker ps -a
  ```

  Example output:

  ```
  CONTAINER ID   IMAGE     STATUS                      NAMES
  a1b2c3d4e5f6   nginx     Exited (0) 2 minutes ago    oldnginx
  ```

---

## 🧱 Step 3: Start a New Container

Run a new NGINX container:

```bash
docker run -d -p 8080:80 --name mynginx nginx
```

Check if it’s running:

```bash
docker ps
```

---

## 🛑 Step 4: Stop a Running Container

Stop the container:

```bash
docker stop mynginx
```

To confirm:

```bash
docker ps
```

You’ll notice the container is no longer running.

---

## 🔁 Step 5: Restart or Start a Stopped Container

* **Start a stopped container**

  ```bash
  docker start mynginx
  ```

* **Restart a container**

  ```bash
  docker restart mynginx
  ```

Check again:

```bash
docker ps
```

---

## 🧹 Step 6: Remove Containers

To remove a stopped container:

```bash
docker rm mynginx
```

To remove all stopped containers at once:

```bash
docker container prune
```

⚠️ *This deletes all stopped containers, so use carefully.*

---

## 🖼️ Step 7: Manage Docker Images

* **List all images**

  ```bash
  docker images
  ```

  Example:

  ```
  REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
  nginx         latest    605c77e624dd   2 weeks ago    142MB
  ```

* **Remove an image**

  ```bash
  docker rmi nginx
  ```

* **Remove all unused images**

  ```bash
  docker image prune -a
  ```

---

## 🔄 Step 8: Stop and Remove Everything (Clean Up)

To stop **all running containers**:

```bash
docker stop $(docker ps -q)
```

To remove **all containers**:

```bash
docker rm $(docker ps -aq)
```

To remove **all images**:

```bash
docker rmi $(docker images -q)
```

---

## 🧠 Step 9: Summary

| Step | Task              | Command                                         | Description                    |
| ---- | ----------------- | ----------------------------------------------- | ------------------------------ |
| 1    | List Containers   | `docker ps` / `docker ps -a`                    | View running or all containers |
| 2    | Start Container   | `docker run -d -p 8080:80 nginx`                | Run new container              |
| 3    | Stop Container    | `docker stop <name>`                            | Stop a container               |
| 4    | Restart Container | `docker restart <name>`                         | Restart container              |
| 5    | Remove Container  | `docker rm <name>`                              | Delete container               |
| 6    | List Images       | `docker images`                                 | Show all images                |
| 7    | Remove Images     | `docker rmi <image>`                            | Delete image                   |
| 8    | Clean Up          | `docker container prune` / `docker image prune` | Remove unused data             |

---

## 📘 References

* [Docker Container Management](https://docs.docker.com/engine/reference/commandline/container/)
* [Docker Image Management](https://docs.docker.com/engine/reference/commandline/image/)
* [Docker CLI Cheat Sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)
