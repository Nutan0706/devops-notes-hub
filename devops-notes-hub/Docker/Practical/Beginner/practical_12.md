# 🧩 Practical 12 — Environment Variables in Containers

### 🎯 **Objective**
Learn how to set and manage environment variables in Docker containers using the `-e` flag and `.env` files.

---

## 🧠 Key Concepts

| Concept | Description |
|----------|--------------|
| **Environment Variable (ENV)** | A key-value pair that configures container behavior at runtime. |
| **-e flag** | Used with `docker run` to set environment variables directly from CLI. |
| **.env file** | A file containing environment variables, automatically loaded during container creation. |
| **Dockerfile ENV** | Sets default values inside the image build. |

---

## ⚙️ Step 1: Verify Docker Installation

Before starting, check that Docker is up and running:
```bash
docker --version
docker info
```

---

## 🧱 Step 2: Use `-e` Flag to Pass Environment Variables

Run a container with environment variables using `-e`:

```bash
docker run -d --name env-demo -e USERNAME=admin -e PASSWORD=secret alpine sleep 3600
```

### Explanation:

| Flag                | Description                                      |
| ------------------- | ------------------------------------------------ |
| `-d`                | Run container in detached mode                   |
| `--name env-demo`   | Assigns a name to the container                  |
| `-e KEY=VALUE`      | Sets environment variables                       |
| `alpine sleep 3600` | Lightweight image running a simple sleep command |

<img width="560" height="101" alt="image" src="https://github.com/user-attachments/assets/87ce1223-eb90-4325-930a-8c6537fcc6d5" />

---

## 🧩 Step 3: Verify Environment Variables Inside the Container

Check environment variables inside the container:

```bash
docker exec -it env-demo env
```

Output:

```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
USERNAME=admin
PASSWORD=secret
```
<img width="372" height="94" alt="image" src="https://github.com/user-attachments/assets/463e4aab-22a4-4bdd-9d1e-197626b5b1fa" />

You can also inspect specific variables:

```bash
docker exec -it env-demo printenv USERNAME
docker exec -it env-demo printenv PASSWORD
```
<img width="395" height="53" alt="image" src="https://github.com/user-attachments/assets/86754473-165c-44f4-b5c6-93cfad237fe9" />

---

## 🗂️ Step 4: Create a `.env` File

Instead of passing variables manually, create a `.env` file for cleaner management.

Create a file named **`.env`** in your current directory:

```bash
touch .env
```

Add the following content:

```
APP_NAME=EnvDemoApp
APP_ENV=development
DB_USER=root
DB_PASS=admin123
```

Your directory should look like:

```
.
├── .env
```

---

## 🧱 Step 5: Run Container Using `.env` File

Use the `--env-file` option to load environment variables from the `.env` file.

```bash
docker run -d --name env-file-demo --env-file .env alpine sleep 3600
```

Check variables inside the container:

```bash
docker exec -it env-file-demo env
```

Expected output:

```
APP_NAME=EnvDemoApp
APP_ENV=development
DB_USER=root
DB_PASS=admin123
```
<img width="407" height="117" alt="image" src="https://github.com/user-attachments/assets/bc09e33b-0fb1-424c-8b08-799b15776b9d" />

---

## 🧩 Step 6: Using Environment Variables in a Dockerfile

Create a simple **Dockerfile**:

```Dockerfile
# Use Ubuntu base image
FROM ubuntu:latest

# Set environment variable inside image
ENV APP_VERSION=1.0 AUTHOR="DevOps Student"

# Default command
CMD ["bash", "-c", "echo App Version: $APP_VERSION && echo Author: $AUTHOR"]
```

Build the image:

```bash
docker build -t env-dockerfile-demo .
```
<img width="416" height="230" alt="image" src="https://github.com/user-attachments/assets/69850c48-974f-4117-86b1-37908539d0b5" />

Run the container:

```bash
docker run --name env-test env-dockerfile-demo
```

Output:

```
App Version: 1.0
Author: DevOps Student
```
<img width="473" height="40" alt="image" src="https://github.com/user-attachments/assets/60cf418c-fcd5-4d22-a6c2-24dac9556c88" />

---

## 🧠 Step 7: Override Environment Variables at Runtime

You can override Dockerfile ENV variables at runtime using `-e`:

```bash
docker run --name override-demo -e APP_VERSION=2.5 env-dockerfile-demo
```

Output:

```
App Version: 2.5
Author: DevOps Student
```
<img width="568" height="53" alt="image" src="https://github.com/user-attachments/assets/b2f4774f-8cf5-45d2-a764-bb962f09b485" />

✅ Dockerfile defaults are overridden by runtime environment variables.

---

## 🧹 Step 8: Clean Up

Stop and remove containers:

```bash
docker stop env-demo env-file-demo env-test override-demo
docker rm env-demo env-file-demo env-test override-demo
```

Remove image:

```bash
docker rmi env-dockerfile-demo
```
<img width="524" height="132" alt="image" src="https://github.com/user-attachments/assets/eb9faffe-4a40-449e-9063-f5ec88b7dc1e" />

---

## ✅ Step 9: Summary

| Step | Task                   | Command / File                    | Description                |
| ---- | ---------------------- | --------------------------------- | -------------------------- |
| 1    | Pass Variables via CLI | `docker run -e KEY=VALUE`         | Set env vars manually      |
| 2    | Inspect Variables      | `docker exec -it <container> env` | View inside container      |
| 3    | Use .env File          | `.env` + `--env-file`             | Load from file             |
| 4    | Use in Dockerfile      | `ENV KEY=value`                   | Set during build           |
| 5    | Override Variables     | `-e KEY=value`                    | Change defaults at runtime |
| 6    | Clean Up               | `docker rm` / `docker rmi`        | Remove containers/images   |

---

## 🧩 Pro Tip

You can mix `.env` and CLI variables — CLI takes **higher priority**:

```bash
docker run --env-file .env -e APP_ENV=production alpine env
```

Result → `.env` values + overridden `APP_ENV=production`.

---

## 📘 References

* [Docker Environment Variables](https://docs.docker.com/compose/environment-variables/)
* [Docker Run Command Reference](https://docs.docker.com/engine/reference/run/)
* [Dockerfile ENV Instruction](https://docs.docker.com/engine/reference/builder/#env)

