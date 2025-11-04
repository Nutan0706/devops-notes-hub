# 🧩 Practical 9 — Understand Dockerfile Instructions

### 🎯 **Objective**
Learn and practice key Dockerfile instructions like `FROM`, `RUN`, `COPY`, `CMD`, `ENTRYPOINT`, and others to understand how Docker builds custom images layer by layer.

---

## 🧠 Key Concepts

| Instruction | Description |
|--------------|--------------|
| `FROM` | Defines the base image for your custom image. |
| `RUN` | Executes commands inside the image during build time. |
| `COPY` | Copies files/folders from your local system to the image. |
| `ADD` | Similar to COPY, but also supports URLs and archives. |
| `CMD` | Specifies the default command to run when the container starts. |
| `ENTRYPOINT` | Defines the main executable of the container. |
| `EXPOSE` | Informs Docker which port the container listens on. |
| `WORKDIR` | Sets the working directory for subsequent instructions. |
| `ENV` | Sets environment variables. |

---

## ⚙️ Step 1: Create a Project Directory

Create a folder for your practical:

```bash
mkdir dockerfile-demo
cd dockerfile-demo
```

Create a simple app file:

```bash
echo "Hello from Dockerfile Demo!" > message.txt
```

Your folder structure:

```
dockerfile-demo/
├── Dockerfile
└── message.txt
```

---

## 🧾 Step 2: Write a Dockerfile

Create a file named **`Dockerfile`** and add the following content:

```Dockerfile
# Step 1: Choose a base image
FROM ubuntu:latest

# Step 2: Set environment variable
ENV AUTHOR="DevOps Student"

# Step 3: Create a working directory
WORKDIR /app

# Step 4: Copy files from local to image
COPY message.txt /app/message.txt

# Step 5: (Optional) Update system — no need to install cat
RUN apt-get update -y && apt-get install -y coreutils

# Step 6: Expose port (for reference)
EXPOSE 8080

# Step 7: Define default command (run at container start)
CMD ["cat", "message.txt"]
```

---

## 🧩 Step 3: Understand Each Instruction

| Line                                           | Instruction                                     | Purpose |
| ---------------------------------------------- | ----------------------------------------------- | ------- |
| `FROM ubuntu:latest`                           | Uses Ubuntu as the base image.                  |         |
| `ENV AUTHOR="DevOps Student"`                  | Sets environment variable for metadata.         |         |
| `WORKDIR /app`                                 | Changes working directory inside the image.     |         |
| `COPY message.txt /app/message.txt`            | Copies local file into container.               |         |
| `RUN apt-get update && apt-get install -y cat` | Installs package at build time.                 |         |
| `EXPOSE 8080`                                  | Documents port 8080 for external communication. |         |
| `CMD ["cat", "message.txt"]`                   | Runs this command when container starts.        |         |

---

## 🧱 Step 4: Build the Docker Image

Run this command in the same directory as your Dockerfile:

```bash
docker build -t dockerfile-demo:latest .
```

Expected output:

```
Successfully built <image_id>
Successfully tagged dockerfile-demo:latest
```

---

## 🚀 Step 5: Run the Container

Now, run your image as a container:

```bash
docker run --name demo dockerfile-demo
```

Output:

```
Hello from Dockerfile Demo!
```

<img width="619" height="42" alt="image" src="https://github.com/user-attachments/assets/bfa5a6db-769c-468e-bcb1-48db63262ee2" />


---

## 🔄 Step 6: Modify and Rebuild (Try ENTRYPOINT)

Replace the last line in your Dockerfile with:

```Dockerfile
ENTRYPOINT ["cat"]
CMD ["message.txt"]
```

Rebuild the image:

```bash
docker build -t dockerfile-demo:v2 .
```

Now, run it again:

```bash
docker run --name demo2 dockerfile-demo:v2
```

Output:

```
Hello from Dockerfile Demo!
```

Try passing a custom argument:

```bash
docker run dockerfile-demo:v2 /etc/os-release
```

Output will display system info from inside the container — showing how `ENTRYPOINT` and `CMD` work together.

---

## 🔍 Step 7: Inspect Image Layers

List image layers using:

```bash
docker history dockerfile-demo
```

Output example:

```
IMAGE          CREATED        CREATED BY                                      SIZE
<image_id>     2 minutes ago  CMD ["cat" "message.txt"]                       0B
<image_id>     2 minutes ago  COPY message.txt /app/message.txt               0B
<image_id>     2 minutes ago  FROM ubuntu:latest                              72MB
```

Each instruction in your Dockerfile adds a new **layer** to the image.
<img width="861" height="237" alt="image" src="https://github.com/user-attachments/assets/5ebfab15-72af-4c46-9df8-91986b8118b4" />

---

## 🧹 Step 8: Clean Up

Stop and remove containers:

```bash
docker stop demo demo2
docker rm demo demo2
```

Remove image:

```bash
docker rmi dockerfile-demo:latest dockerfile-demo:v2
```

---

## ✅ Step 9: Summary

| Step | Instruction  | Purpose                          |
| ---- | ------------ | -------------------------------- |
| 1    | `FROM`       | Sets base image                  |
| 2    | `RUN`        | Executes commands during build   |
| 3    | `COPY`       | Copies files into image          |
| 4    | `WORKDIR`    | Sets working directory           |
| 5    | `ENV`        | Defines environment variables    |
| 6    | `EXPOSE`     | Declares open ports              |
| 7    | `CMD`        | Defines default command          |
| 8    | `ENTRYPOINT` | Defines fixed startup executable |

---

## 🧩 Pro Tip: CMD vs ENTRYPOINT

| Feature           | CMD                            | ENTRYPOINT               |
| ----------------- | ------------------------------ | ------------------------ |
| Default command   | ✅ Yes                          | ✅ Yes                    |
| Can be overridden | ✅ Easily                       | ⚠️ Needs `--entrypoint`  |
| Typical use       | Provide defaults for container | Force container behavior |

Example difference:

```bash
# CMD Example
CMD ["echo", "Hello World"]

# ENTRYPOINT Example
ENTRYPOINT ["echo"]
CMD ["Hello World"]
```

Both output the same, but `ENTRYPOINT` locks the executable while `CMD` can be replaced.

---

## 📘 References

* [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
* [Docker Build Command](https://docs.docker.com/engine/reference/commandline/build/)
* [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)


