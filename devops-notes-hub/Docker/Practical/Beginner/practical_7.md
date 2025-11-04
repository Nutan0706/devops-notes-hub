# 🧩 Practical 7 — Expose Ports and Access Containers

### 🎯 **Objective**
Learn how to expose and map container ports to the host system using the `-p` flag in the `docker run` command, allowing access to containerized applications from your local machine.

---

## 🧠 Key Concepts

| Concept | Description |
|----------|--------------|
| **Port Mapping** | Connects a port on the container to a port on the host machine |
| **Expose** | Tells Docker which ports the container listens on |
| **-p flag** | Used in `docker run` to bind host and container ports in the format `<host_port>:<container_port>` |

---

## ⚙️ Step 1: Verify Docker Installation

Check Docker setup before starting:
```bash
docker --version
docker info
```

---

## 🧱 Step 2: Pull a Web Server Image

Let’s use the **nginx** image for demonstration:

```bash
docker pull nginx
```

Check if the image is available:

```bash
docker images
```

Output example:

```
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    605c77e624dd   2 weeks ago    142MB
```

---

## 🚀 Step 3: Run a Container with Port Mapping

Run an Nginx container and expose it to your host machine’s port **8080**.

```bash
docker run -d -p 8080:80 --name webserver nginx
```

### Explanation:

| Flag               | Meaning                                 |
| ------------------ | --------------------------------------- |
| `-d`               | Detached mode (run in background)       |
| `-p 8080:80`       | Map host port 8080 to container port 80 |
| `--name webserver` | Assigns a name to the container         |
| `nginx`            | Image to run                            |

Check if it’s running:

```bash
docker ps
```

Output:

```
CONTAINER ID   IMAGE     STATUS         PORTS                  NAMES
a1b2c3d4e5f6   nginx     Up 10 seconds  0.0.0.0:8080->80/tcp   webserver
```

---

## 🌐 Step 4: Access the Application

Now open your browser and visit:
👉 [http://localhost:8080](http://localhost:8080)

You should see the **default NGINX welcome page**, confirming that the port mapping works.

---

## 🧪 Step 5: Map Multiple Ports (Optional)

You can map multiple ports by repeating the `-p` flag:

```bash
docker run -d -p 8080:80 -p 8443:443 --name webserver2 nginx
```

Now your container serves:

* HTTP on port **8080**
* HTTPS on port **8443**

---

## 🧩 Step 6: View Exposed Ports

To verify port mapping details:

```bash
docker port webserver
```

Example output:

```
80/tcp -> 0.0.0.0:8080
```

You can also inspect the container for detailed network info:

```bash
docker inspect webserver | grep -i "port"
```

---

## 🧹 Step 7: Stop and Remove Containers

To stop the running container:

```bash
docker stop webserver
```

To remove it:

```bash
docker rm webserver
```

To clean all stopped containers:

```bash
docker container prune
```

---

## ✅ Step 8: Summary

| Step | Task               | Command                           | Description           |
| ---- | ------------------ | --------------------------------- | --------------------- |
| 1    | Verify Docker      | `docker info`                     | Check Docker setup    |
| 2    | Pull Image         | `docker pull nginx`               | Get base image        |
| 3    | Run Container      | `docker run -d -p 8080:80 nginx`  | Map ports             |
| 4    | Access Container   | Browser → `http://localhost:8080` | Test mapping          |
| 5    | Map Multiple Ports | `-p 8080:80 -p 8443:443`          | Expose multiple ports |
| 6    | Check Mapped Ports | `docker port <container>`         | Verify mappings       |
| 7    | Stop & Remove      | `docker stop` / `docker rm`       | Cleanup resources     |

---

## 📘 References

* [Docker Run Command Reference](https://docs.docker.com/engine/reference/run/)
* [Networking in Docker Containers](https://docs.docker.com/network/)
* [Nginx Official Docker Image](https://hub.docker.com/_/nginx)
