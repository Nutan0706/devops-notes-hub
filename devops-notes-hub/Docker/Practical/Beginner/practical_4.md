# 🧩 Practical 4 — Build a Custom Docker Image

### 🎯 **Objective**
Learn how to write a simple Dockerfile and build a custom Docker image using the `docker build` command.

---

## 🧠 Key Concepts

- **Dockerfile:** A text file containing instructions to build a Docker image.
- **Image:** A lightweight package that contains everything needed to run an application.
- **docker build:** Command used to create a Docker image from a Dockerfile.

---

## 🧰 Step 1: Prepare Your Working Directory

Create a new directory for your Docker project.

```bash
mkdir my-docker-app
cd my-docker-app
```

Inside this folder, you’ll create:

```
my-docker-app/
├── Dockerfile
└── index.html
```
<img width="389" height="55" alt="image" src="https://github.com/user-attachments/assets/85801afc-eb80-483a-aa86-481137e46fa9" />

---

## 📝 Step 2: Create a Simple Web Page

Create a file named **`index.html`**:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Docker Image</title>
</head>
<body>
    <h1>Hello from My Custom Docker Image!</h1>
</body>
</html>
```

Save and close the file.

---

## 🐳 Step 3: Write a Simple Dockerfile

Create a file named **`Dockerfile`** (no extension).

```Dockerfile
# Use official Nginx base image
FROM nginx:latest

# Copy custom HTML file to Nginx default directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 for web traffic
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
```

### 🧩 Explanation:

| Instruction | Purpose                                            |
| ----------- | -------------------------------------------------- |
| `FROM`      | Defines the base image (here, nginx)               |
| `COPY`      | Copies your local file into the image              |
| `EXPOSE`    | Opens port 80 for HTTP traffic                     |
| `CMD`       | Specifies the default command to run the container |

---

## ⚙️ Step 4: Build Your Docker Image

Run the following command from the same directory as your Dockerfile:

```bash
docker build -t my-custom-nginx .
```
<img width="678" height="251" alt="image" src="https://github.com/user-attachments/assets/617c789e-dec5-4d36-8bae-bda19f3b2fed" />


### 🔍 Explanation:

* `-t my-custom-nginx` → Tags the image with a name
* `.` → Builds the image using the Dockerfile in the current directory

Once complete, you’ll see:

```
Successfully built <image-id>
Successfully tagged my-custom-nginx:latest
```

---

## 🧾 Step 5: Verify the Built Image

List all local images:

```bash
docker images
```

Expected output:

```
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
my-custom-nginx     latest    a1b2c3d4e5f6   1 minute ago     144MB
```
<img width="517" height="61" alt="image" src="https://github.com/user-attachments/assets/ac3e5fa3-96a2-4365-a2dc-063d45f56b81" />

---

## 🚀 Step 6: Run a Container from Your Custom Image

Run the image as a container and map it to port 8080 on your host:

```bash
docker run -d -p 8080:80 --name myweb my-custom-nginx
```
<img width="717" height="35" alt="image" src="https://github.com/user-attachments/assets/8c098cf4-47e1-40e2-9820-68b589080751" />

Check if it’s running:

```bash
docker ps
```

Expected output:

```
CONTAINER ID   IMAGE              STATUS         PORTS                  NAMES
ab12cd34ef56   my-custom-nginx    Up 10 seconds  0.0.0.0:8080->80/tcp   myweb
```

---

## 🌐 Step 7: Verify in Browser

Open your browser and visit:
👉 [http://localhost:8080](http://localhost:8080)

You should see:

```
Hello from My Custom Docker Image!
```
<img width="663" height="736" alt="image" src="https://github.com/user-attachments/assets/4ff06fd3-09de-48f4-9201-155dd6eeb3bc" />

---

## 🧹 Step 8: Stop and Remove Containers (Optional)

Stop the running container:

```bash
docker stop myweb
```

Remove the container:

```bash
docker rm myweb
```

Remove the custom image:

```bash
docker rmi my-custom-nginx
```
<img width="584" height="119" alt="image" src="https://github.com/user-attachments/assets/ba81a66f-658d-45ed-a55d-0cc74f921edf" />

---

## ✅ Step 9: Summary

| Step | Task              | Command / File                             | Description           |
| ---- | ----------------- | ------------------------------------------ | --------------------- |
| 1    | Create Folder     | `mkdir my-docker-app`                      | Setup workspace       |
| 2    | Create Web Page   | `index.html`                               | Content to serve      |
| 3    | Write Dockerfile  | `Dockerfile`                               | Define build steps    |
| 4    | Build Image       | `docker build -t my-custom-nginx .`        | Create image          |
| 5    | Verify Image      | `docker images`                            | Confirm build success |
| 6    | Run Container     | `docker run -d -p 8080:80 my-custom-nginx` | Test image            |
| 7    | Verify in Browser | `http://localhost:8080`                    | Check output          |
| 8    | Clean Up          | `docker stop` / `docker rm` / `docker rmi` | Optional cleanup      |

---

## 📘 References

* [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
* [Docker Build Command](https://docs.docker.com/engine/reference/commandline/build/)
* [Nginx Official Image on Docker Hub](https://hub.docker.com/_/nginx)

