# 🧩 Practical 11 — Run Multiple Containers Simultaneously

### 🎯 **Objective**
Learn how to run and manage multiple containers at the same time using Docker CLI — such as running a web server and a database together manually without Docker Compose.

---

## 🧠 Key Concepts

| Concept | Description |
|----------|--------------|
| **Container** | An isolated environment where an application runs. |
| **Detached Mode (-d)** | Allows containers to run in the background. |
| **Port Mapping (-p)** | Maps container ports to host ports for access. |
| **Inter-container Communication** | Containers can communicate if they share a network. |

---

## ⚙️ Step 1: Verify Docker Setup

Check Docker installation and running containers:
```bash
docker --version
docker ps
```

If Docker is not running, start the service:

```bash
sudo systemctl start docker
```

---

## 🧱 Step 2: Run First Container — Web Server (NGINX)

Run an NGINX container on port **8080**:

```bash
docker run -d -p 8080:80 --name web1 nginx
```

Verify:

```bash
docker ps
```

Output:

```
CONTAINER ID   IMAGE     STATUS         PORTS                  NAMES
a1b2c3d4e5f6   nginx     Up 10 seconds  0.0.0.0:8080->80/tcp   web1
```

Check in browser:
👉 [http://localhost:8080](http://localhost:8080)

You’ll see the NGINX welcome page.

---

## 🐳 Step 3: Run Second Container — Another Web Server

Run another instance of NGINX on a different port (8081):

```bash
docker run -d -p 8081:80 --name web2 nginx
```

List running containers:

```bash
docker ps
```

Output:

```
CONTAINER ID   IMAGE     STATUS         PORTS                  NAMES
a1b2c3d4e5f6   nginx     Up 30 seconds  0.0.0.0:8080->80/tcp   web1
b2c3d4e5f6a7   nginx     Up 10 seconds  0.0.0.0:8081->80/tcp   web2
```

Now visit both in browser:

* [http://localhost:8080](http://localhost:8080) → Container 1
* [http://localhost:8081](http://localhost:8081) → Container 2

✅ Both containers run simultaneously!

---

## 🧩 Step 4: Run a Database Container

Let’s run **MySQL** alongside both web servers:

```bash
docker run -d --name mysql-db -e MYSQL_ROOT_PASSWORD=admin -p 3306:3306 mysql:latest
```

### Explanation:

| Flag                           | Description                               |
| ------------------------------ | ----------------------------------------- |
| `-d`                           | Detached (background) mode                |
| `--name mysql-db`              | Name of the container                     |
| `-e MYSQL_ROOT_PASSWORD=admin` | Environment variable to set root password |
| `-p 3306:3306`                 | Expose MySQL port to host                 |

Verify all containers are running:

```bash
docker ps
```

Output:

```
CONTAINER ID   IMAGE     STATUS         PORTS                  NAMES
a1b2c3d4e5f6   nginx     Up 2 mins      0.0.0.0:8080->80/tcp   web1
b2c3d4e5f6a7   nginx     Up 1 min       0.0.0.0:8081->80/tcp   web2
c3d4e5f6a7b8   mysql     Up 10 seconds  0.0.0.0:3306->3306/tcp mysql-db
```

---

## 🔗 Step 5: Connect Containers (Optional Networking)

By default, containers on the same **bridge network** can communicate using container names.

To confirm networks:

```bash
docker network ls
```

To inspect:

```bash
docker inspect bridge
```

If needed, you can create a custom network:

```bash
docker network create mynetwork
```

Run containers on that network:

```bash
docker run -d -p 8080:80 --network mynetwork --name web1 nginx
docker run -d --network mynetwork --name mysql-db -e MYSQL_ROOT_PASSWORD=admin mysql
```

Now `web1` can reach `mysql-db` using the hostname `mysql-db`.

---

## 🧪 Step 6: Manage Multiple Containers

| Task                    | Command                         | Description                 |
| ----------------------- | ------------------------------- | --------------------------- |
| List running containers | `docker ps`                     | Show all running containers |
| Stop a container        | `docker stop <container_name>`  | Stop specific container     |
| Stop all containers     | `docker stop $(docker ps -q)`   | Stop all running            |
| Start a container       | `docker start <container_name>` | Restart a stopped one       |
| Remove a container      | `docker rm <container_name>`    | Delete a container          |
| Remove all stopped      | `docker container prune`        | Clean up unused             |

---

## 🧹 Step 7: Stop and Remove All Containers (Optional Cleanup)

Stop all containers:

```bash
docker stop $(docker ps -q)
```

Remove all containers:

```bash
docker rm $(docker ps -aq)
```

---

## ✅ Step 8: Summary

| Step | Task                    | Command                                 | Description                         |
| ---- | ----------------------- | --------------------------------------- | ----------------------------------- |
| 1    | Verify Docker           | `docker ps`                             | Check Docker status                 |
| 2    | Run First Container     | `docker run -d -p 8080:80 nginx`        | Start NGINX server                  |
| 3    | Run Multiple Containers | Run multiple `docker run` commands      | Manage multiple services            |
| 4    | Add Database            | `docker run -d -p 3306:3306 mysql`      | Run MySQL with others               |
| 5    | Connect Containers      | `--network <name>`                      | Allow inter-container communication |
| 6    | Manage Containers       | `docker ps`, `docker stop`, `docker rm` | Manage lifecycle                    |
| 7    | Cleanup                 | `docker stop $(docker ps -q)`           | Stop all containers                 |

---

## 📘 References

* [Docker Run Command](https://docs.docker.com/engine/reference/run/)
* [Docker Network Basics](https://docs.docker.com/network/)
* [Docker CLI Management Commands](https://docs.docker.com/engine/reference/commandline/docker/)
