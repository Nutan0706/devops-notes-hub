# 🧩 Practical 10 — Tag and Push Image to Docker Hub

### 🎯 **Objective**
Learn how to tag a Docker image and push it to Docker Hub for image publishing and sharing.

---

## 🧠 Key Concepts

| Concept | Description |
|----------|--------------|
| **Tagging** | Assigns a unique name or version to an image. |
| **Docker Hub** | A public cloud registry where Docker images are stored and shared. |
| **docker push** | Uploads your tagged image to Docker Hub. |
| **docker pull** | Downloads images from Docker Hub. |

---

## ⚙️ Step 1: Prerequisites

✅ Ensure:
- Docker is installed and running.
- You have a **Docker Hub account**.  
  👉 [https://hub.docker.com/](https://hub.docker.com/)
- You’re logged in from your terminal.

Login using:
```bash
docker login
```

You’ll be prompted for your **Docker Hub username** and **password**.
Successful login message:

```
Login Succeeded
```

---

## 🧱 Step 2: Create or Reuse an Existing Image

If you don’t have a local image, create one quickly:

```bash
docker run -d -p 8080:80 --name webapp nginx
```

List available images:

```bash
docker images
```

Example output:

```
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
nginx         latest    605c77e624dd   2 weeks ago     142MB
```

---

## 🏷️ Step 3: Tag the Image

Tag the existing image to prepare it for Docker Hub.

```bash
docker tag nginx:latest your_dockerhub_username/mynginx:v1
```

Example:

```bash
docker tag nginx:latest nutanpatel/mynginx:v1
```

Verify the tagged image:

```bash
docker images
```

Output:

```
REPOSITORY                TAG       IMAGE ID       CREATED         SIZE
nginx                     latest    605c77e624dd   2 weeks ago     142MB
nutanpatel/mynginx        v1        605c77e624dd   2 weeks ago     142MB
```

---

## ☁️ Step 4: Push Image to Docker Hub

Now push the tagged image:

```bash
docker push your_dockerhub_username/mynginx:v1
```

Example:

```bash
docker push nutanpatel/mynginx:v1
```

Expected output:

```
The push refers to repository [docker.io/nutanpatel/mynginx]
v1: digest: sha256:6a6b7b7e5f5d... size: 1234
```

✅ Your image is now live on Docker Hub!

---

## 🌐 Step 5: Verify on Docker Hub

1. Open your browser and go to
   👉 [https://hub.docker.com/repositories](https://hub.docker.com/repositories)
2. You’ll see your repository `mynginx`.
3. Click on it to view available tags and metadata.

---

## 📥 Step 6: Pull and Test the Uploaded Image

You can now pull your image from **any machine**:

```bash
docker pull your_dockerhub_username/mynginx:v1
```

Example:

```bash
docker pull nutanpatel/mynginx:v1
```

Run it:

```bash
docker run -d -p 8081:80 --name test-nginx nutanpatel/mynginx:v1
```

Open your browser:
👉 [http://localhost:8081](http://localhost:8081)

You’ll see your NGINX welcome page confirming that the pulled image works perfectly.

---

## 🧹 Step 7: Clean Up (Optional)

Stop and remove containers:

```bash
docker stop webapp test-nginx
docker rm webapp test-nginx
```

Remove images:

```bash
docker rmi nutanpatel/mynginx:v1 nginx
```

Logout from Docker Hub:

```bash
docker logout
```

---

## ✅ Step 8: Summary

| Step | Task                | Command                                            | Description               |
| ---- | ------------------- | -------------------------------------------------- | ------------------------- |
| 1    | Login to Docker Hub | `docker login`                                     | Authenticate your account |
| 2    | Tag Image           | `docker tag <source> <user>/<repo>:<tag>`          | Rename for Hub            |
| 3    | Push Image          | `docker push <user>/<repo>:<tag>`                  | Upload to Hub             |
| 4    | Verify              | Check on [hub.docker.com](https://hub.docker.com/) | Confirm upload            |
| 5    | Pull Image          | `docker pull <user>/<repo>:<tag>`                  | Test from another system  |
| 6    | Clean Up            | `docker rm` / `docker rmi`                         | Remove containers/images  |

---

## 🧩 Pro Tip

You can tag multiple versions for version control:

```bash
docker tag nginx:latest nutanpatel/mynginx:v2
docker push nutanpatel/mynginx:v2
```

---

## 📘 References

* [Docker Tag Command](https://docs.docker.com/engine/reference/commandline/tag/)
* [Docker Push Command](https://docs.docker.com/engine/reference/commandline/push/)
* [Docker Hub Documentation](https://docs.docker.com/docker-hub/)

