# 🧩 Practical 2 — Run Your First Container (hello-world)

### 🎯 **Objective**
Verify Docker installation and understand the basic container lifecycle by running the `hello-world` container.

---

## 🧠 Key Concepts

- **Image:** A lightweight, stand-alone package that includes everything needed to run a piece of software.
- **Container:** A running instance of an image.
- **Lifecycle:** Pull → Create → Start → Run → Stop → Remove

---

## 🖥️ Step 1: Verify Docker Installation

Check if Docker is properly installed and the daemon is running.

```bash
docker --version
```

If you see a version output like `Docker version 27.0.0, build ...`, Docker is installed correctly.

Next, check the Docker service status (Linux only):

```bash
sudo systemctl status docker
```

If it’s inactive, start it using:

```bash
sudo systemctl start docker
```

---

## 🐳 Step 2: Run the `hello-world` Container

Run the default test image to confirm everything works correctly.

```bash
docker run hello-world
```

### 🔍 What Happens Internally:

1. Docker CLI sends the command to the Docker Daemon.
2. Daemon checks if the `hello-world` image exists locally.
3. If not found, it **pulls** it from **Docker Hub**.
4. Docker then **creates** a new container from this image.
5. The container runs a short script that prints a confirmation message.
6. Once complete, the container **stops** automatically.

---

## 📋 Step 3: Check Downloaded Images

List all images on your local system:

```bash
docker images
```

You should see something like:

```
REPOSITORY     TAG       IMAGE ID       CREATED         SIZE
hello-world    latest    d1165f221234   2 weeks ago     13.3kB
```

---

## 🧱 Step 4: List All Containers

List **running containers**:

```bash
docker ps
```

List **all containers** (including stopped ones):

```bash
docker ps -a
```

You’ll see the `hello-world` container with a status like `Exited (0)`.

---

## 🧹 Step 5: Remove Containers and Images (Optional)

To remove the stopped container:

```bash
docker rm <container_id>
```

To remove the image:

```bash
docker rmi hello-world
```

---

## 🔄 Step 6: Run Container Again (Without Pulling)

Now that the image is cached locally, run it again:

```bash
docker run hello-world
```

This time, Docker won’t pull it again — it’ll reuse the local image.

---

## 🧠 Step 7: Understanding the Container Lifecycle

| Phase      | Command                    | Description                          |
| ---------- | -------------------------- | ------------------------------------ |
| **Pull**   | `docker pull <image>`      | Downloads image from Docker Hub      |
| **Create** | `docker create <image>`    | Prepares container from image        |
| **Start**  | `docker start <container>` | Runs an existing container           |
| **Run**    | `docker run <image>`       | Pulls, creates, and starts container |
| **Stop**   | `docker stop <container>`  | Gracefully stops container           |
| **Remove** | `docker rm <container>`    | Deletes container from system        |

---

## ✅ Step 8: Verify Installation

Successful output example:

```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

If you see this message, Docker is fully functional and ready for further practicals.

---

## 📘 Summary

| Step | Task                 | Description                            |
| ---- | -------------------- | -------------------------------------- |
| 1    | Verify Docker        | Ensure Docker is installed and running |
| 2    | Run hello-world      | Test Docker functionality              |
| 3    | List Images          | Check downloaded images                |
| 4    | List Containers      | View active and exited containers      |
| 5    | Cleanup              | Remove unnecessary containers/images   |
| 6    | Re-run Container     | Test image caching                     |
| 7    | Understand Lifecycle | Learn how containers run and stop      |

---

## 📚 References

* [Docker Documentation — Get Started](https://docs.docker.com/get-started/)
* [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/docker/)
