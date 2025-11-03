# 🧩 Practical 3 — Pull and Run Images from Docker Hub

### 🎯 **Objective**
Learn how to pull images from Docker Hub, run containers from those images, and manage them using essential Docker commands like `docker pull`, `docker run`, and `docker ps`.

---

## 🧠 Key Concepts

- **Docker Hub:** A public cloud-based registry where you can find and share container images.
- **docker pull:** Downloads an image from Docker Hub to your local system.
- **docker run:** Creates and starts a new container from an image.
- **docker ps:** Lists running containers.

---

## 🪟 Step 1: Verify Docker Setup

Before starting, make sure Docker is installed and running properly.

```bash
docker --version
docker info
```

If you get outputs without errors, Docker is ready to use.

<img width="377" height="161" alt="image" src="https://github.com/user-attachments/assets/4e57ea0a-27aa-4ab8-a8fd-3bb59d32be5f" />

---

## 🧭 Step 2: Search for Images on Docker Hub

You can search for popular images using:

```bash
docker search nginx
```

Example output:

```
NAME                      DESCRIPTION                                     STARS     OFFICIAL
nginx                     Official build of Nginx.                        18000     [OK]
```
<img width="482" height="227" alt="image" src="https://github.com/user-attachments/assets/0d51b06f-0e1c-4ca4-92fe-9d115cf41771" />

---

## 🐳 Step 3: Pull an Image from Docker Hub

Use the `docker pull` command to download an image to your system.

```bash
docker pull nginx
```

You can also specify a version (tag):

```bash
docker pull nginx:latest
```
<img width="489" height="170" alt="image" src="https://github.com/user-attachments/assets/105a4914-db8b-474c-b3e1-36844124a02a" />

Check downloaded images:

```bash
docker images
```

Expected output:

```
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    605c77e624dd   2 weeks ago    142MB
```
<img width="344" height="59" alt="image" src="https://github.com/user-attachments/assets/8146e400-629c-4ce7-bc20-531fcb747d03" />


---

## ⚙️ Step 4: Run a Container from the Pulled Image

Now, create and start a container using the `nginx` image.

```bash
docker run -d -p 8080:80 --name mynginx nginx
```

### Explanation:

* `-d` → Run container in detached mode (in background)
* `-p 8080:80` → Map container’s port 80 to host port 8080
* `--name mynginx` → Assigns a custom name to the container
* `nginx` → Name of the image
* 
<img width="407" height="28" alt="image" src="https://github.com/user-attachments/assets/91ad69b9-815c-445c-92e3-71557680e181" />

Check if it’s running:

```bash
docker ps
```

You’ll see output like:

```
CONTAINER ID   IMAGE     COMMAND                  STATUS         PORTS                  NAMES
a1b2c3d4e5f6   nginx     "/docker-entrypoint.…"   Up 10 seconds  0.0.0.0:8080->80/tcp   mynginx
```
<img width="564" height="54" alt="image" src="https://github.com/user-attachments/assets/5581c82f-3674-4876-9e21-16e3f04d580f" />

---

## 🌐 Step 5: Verify the Container

Open your browser and go to:

👉 [http://localhost:8080](http://localhost:8080)

You should see the **Nginx Welcome Page**, confirming that your container is running successfully.
<img width="566" height="234" alt="image" src="https://github.com/user-attachments/assets/89f75b7d-4a14-4792-8da4-35be690584a0" />

---

## 🧩 Step 6: Manage Containers

* **List all containers (running + stopped)**

  ```bash
  docker ps -a
  ```
  <img width="578" height="63" alt="image" src="https://github.com/user-attachments/assets/429dd947-3af1-46cf-a7ca-f68853770daf" />


* **Stop a running container**

  ```bash
  docker stop mynginx
  ```
  <img width="278" height="32" alt="image" src="https://github.com/user-attachments/assets/13e5fac9-224a-4997-8c24-5acc50a10018" />


* **Restart a container**

  ```bash
  docker start mynginx
  ```
 <img width="298" height="26" alt="image" src="https://github.com/user-attachments/assets/3a0a5ed5-6f0a-4dd5-8dc1-ab889cfe7f3f" />

* **Remove a container**

  ```bash
  docker rm mynginx
  ```
<img width="264" height="29" alt="image" src="https://github.com/user-attachments/assets/4b5eeda5-c2ff-4ab7-bf06-d12a1c466d61" />

---

## 🧹 Step 7: Manage Images

* **List all images**

  ```bash
  docker images
  ```
  <img width="329" height="41" alt="image" src="https://github.com/user-attachments/assets/c8644ec6-ddb2-47ce-b345-b5e4caba1db8" />


* **Remove an image**

  ```bash
  docker rmi nginx
  ```
  <img width="483" height="145" alt="image" src="https://github.com/user-attachments/assets/bf1de2a4-a6a9-419b-9d4e-732adc3c16d2" />


---

## 🔄 Step 8: Combine Pull + Run (Shortcut)

You can directly run an image without manually pulling it:

```bash
docker run hello-world
```

👉 Docker automatically pulls the image if it’s not available locally.

---

## ✅ Step 9: Practical Summary

| Step | Task            | Command                                       | Description                          |
| ---- | --------------- | --------------------------------------------- | ------------------------------------ |
| 1    | Verify Setup    | `docker --version`                            | Ensure Docker is working             |
| 2    | Search Images   | `docker search <image>`                       | Find available images                |
| 3    | Pull Image      | `docker pull <image>`                         | Download image locally               |
| 4    | Run Container   | `docker run -d -p <host>:<container> <image>` | Start container                      |
| 5    | List Containers | `docker ps`                                   | View running containers              |
| 6    | Stop/Remove     | `docker stop` / `docker rm`                   | Manage containers                    |
| 7    | Remove Images   | `docker rmi <image>`                          | Clean up                             |
| 8    | Auto Pull       | `docker run <image>`                          | Pulls image automatically if missing |

---

## 📘 References

* [Docker Hub — Official Registry](https://hub.docker.com/)
* [Docker CLI Documentation](https://docs.docker.com/engine/reference/commandline/docker/)
* [Docker Run Command Guide](https://docs.docker.com/engine/reference/run/)

