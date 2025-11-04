# 🧩 Practical 8 — Use Volumes for Data Persistence

### 🎯 **Objective**
Learn how to create and mount Docker volumes using the `-v` option to persist data even after a container is removed.

---

## 🧠 Key Concepts

| Concept | Description |
|----------|--------------|
| **Volume** | A special directory outside the container’s filesystem used for persistent data storage. |
| **Bind Mount** | Maps a host directory to a container directory. |
| **Anonymous Volume** | Automatically created by Docker without a specific name. |
| **Named Volume** | A user-defined, reusable volume managed by Docker. |

---

## ⚙️ Step 1: Verify Docker Setup

Check Docker installation:
```bash
docker --version
docker info
```

---

## 🧱 Step 2: Create a Docker Volume

Create a named volume called `mydata`:

```bash
docker volume create mydata
```

List available volumes:

```bash
docker volume ls
```

Example output:

```
DRIVER    VOLUME NAME
local     mydata
```

Inspect the volume:

```bash
docker volume inspect mydata
```

---

## 📂 Step 3: Run a Container and Mount the Volume

Let’s use the `nginx` image and mount the `mydata` volume to store website files.

```bash
docker run -d -p 8080:80 --name webapp -v mydata:/usr/share/nginx/html nginx
```

### Explanation:

| Flag                              | Description                                         |
| --------------------------------- | --------------------------------------------------- |
| `-d`                              | Run container in detached mode                      |
| `-p 8080:80`                      | Map host port 8080 to container port 80             |
| `--name webapp`                   | Name of the container                               |
| `-v mydata:/usr/share/nginx/html` | Mounts the Docker volume `mydata` to NGINX web root |
| `nginx`                           | Image name                                          |

---

## 🌐 Step 4: Verify the Container and Volume Mount

List running containers:

```bash
docker ps
```

Check the volume mount inside the container:

```bash
docker inspect webapp
```

Search for the `Mounts` section in the output:

```json
"Mounts": [
  {
    "Type": "volume",
    "Name": "mydata",
    "Destination": "/usr/share/nginx/html"
  }
]
```

---

## ✏️ Step 5: Write Data into the Volume

Access the container shell:

```bash
docker exec -it webapp /bin/bash
```

Now, inside the container, create a new HTML file:

```bash
echo "<h1>Hello from Persistent Volume!</h1>" > /usr/share/nginx/html/index.html
exit
```

---

## 🌍 Step 6: Test in Browser

Open your browser and visit:
👉 [http://localhost:8080](http://localhost:8080)

You should see:

```
Hello from Persistent Volume!
```

---

## 🧪 Step 7: Remove Container (Data Should Persist)

Stop and remove the container:

```bash
docker stop webapp
docker rm webapp
```

Now create a new container using the same volume:

```bash
docker run -d -p 8080:80 --name webapp2 -v mydata:/usr/share/nginx/html nginx
```

Visit again in the browser:
👉 [http://localhost:8080](http://localhost:8080)

✅ You’ll still see **“Hello from Persistent Volume!”**, proving the data is stored in the volume.

---

## 🧹 Step 8: Clean Up (Optional)

Stop and remove containers:

```bash
docker stop webapp2
docker rm webapp2
```

Remove the volume (⚠️ deletes all data):

```bash
docker volume rm mydata
```

---

## ✅ Step 9: Summary

| Step | Task              | Command                       | Description             |
| ---- | ----------------- | ----------------------------- | ----------------------- |
| 1    | Create Volume     | `docker volume create mydata` | Create named volume     |
| 2    | List Volumes      | `docker volume ls`            | View available volumes  |
| 3    | Run Container     | `docker run -v mydata:/path`  | Mount volume            |
| 4    | Inspect Volume    | `docker inspect <container>`  | Check volume mount info |
| 5    | Write Data        | `echo "..." > file.html`      | Store persistent data   |
| 6    | Restart Container | `docker run -v mydata:/path`  | Verify persistence      |
| 7    | Clean Up          | `docker volume rm mydata`     | Delete volume           |

---

## 📘 References

* [Docker Volumes Documentation](https://docs.docker.com/storage/volumes/)
* [Docker Exec Command](https://docs.docker.com/engine/reference/commandline/exec/)
* [Nginx Docker Hub Page](https://hub.docker.com/_/nginx)
