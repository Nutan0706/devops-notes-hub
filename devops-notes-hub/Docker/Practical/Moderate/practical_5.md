# 🧩 Practical 5 — Create and Use Docker Compose File (Web + Database Setup)

### 🎯 **Objective**
Learn how to use **Docker Compose** to manage a multi-container application — typically a **web application + database** running together with a single command.

---

## 🧠 Key Concepts

| Concept | Description |
|---------|-------------|
| **Docker Compose** | Tool to define and run multi-container applications. |
| **docker-compose.yml** | File describing services, networks, volumes, and configurations. |
| **Service** | A container definition inside Docker Compose. |
| **One command deploy** | `docker compose up` starts everything together. |

---

# ----------------------------------------------------
# ⚙️ Step 1: Install Docker Compose (if not installed)
# ----------------------------------------------------

Check version:
```bash
docker compose version
````

If installed, you will see something like:

```
Docker Compose version v2.x.x
```

---

# ----------------------------------------------------

# 🧱 Step 2: Create Project Structure

# ----------------------------------------------------

```bash
mkdir compose-demo
cd compose-demo
```

Create a simple web app:

### `app.py` (Flask Example)

```python
from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Web App Connected to MySQL Database!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### `requirements.txt`

```
flask
mysql-connector-python
```

Create Dockerfile for the web app:

### `Dockerfile`

```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

---

# ----------------------------------------------------

# 🐳 Step 3: Create docker-compose.yml File

# ----------------------------------------------------

Create a file named **docker-compose.yml**:

```yaml
version: "3.9"

services:

  web:
    build: .
    container_name: web-app
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      DB_HOST: db
      DB_USER: root
      DB_PASSWORD: password
    networks:
      - mynetwork

  db:
    image: mysql:8
    container_name: mysql-db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: demo
    volumes:
      - dbdata:/var/lib/mysql
    networks:
      - mynetwork

volumes:
  dbdata:

networks:
  mynetwork:
```

---

# ----------------------------------------------------

# 🚀 Step 4: Start Multi-Container Application

# ----------------------------------------------------

Run everything using a **single command**:

```bash
docker compose up -d
```

Check running services:

```bash
docker compose ps
```

Expected:

```
NAME        IMAGE        STATUS         PORTS
web-app     web-app      Up             0.0.0.0:5000->5000/tcp
mysql-db    mysql:8      Up             3306/tcp
```

---

# ----------------------------------------------------

# 🌐 Step 5: Test the Web Application

# ----------------------------------------------------

Visit in browser:

👉 [http://localhost:5000](http://localhost:5000)

Expected output:

```
Web App Connected to MySQL Database!
```

The Flask web app is running AND communicating with the MySQL container.

---

# ----------------------------------------------------

# 🔍 Step 6: View Logs

# ----------------------------------------------------

Web logs:

```bash
docker compose logs web
```

DB logs:

```bash
docker compose logs db
```

Follow live logs:

```bash
docker compose logs -f
```

---

# ----------------------------------------------------

# 🧩 Step 7: Stop and Remove All Services

# ----------------------------------------------------

Stop containers:

```bash
docker compose down
```

Clear volumes also (⚠️ deletes DB data):

```bash
docker compose down -v
```

---

# ----------------------------------------------------

# ✅ Summary

# ----------------------------------------------------

| Step | Task                     | Description                              |
| ---- | ------------------------ | ---------------------------------------- |
| 1    | Create web & db services | Defined in `docker-compose.yml`          |
| 2    | Build images             | Dockerfile for web, MySQL official image |
| 3    | Start stack              | `docker compose up -d`                   |
| 4    | Access web app           | Visit `localhost:5000`                   |
| 5    | Logs                     | `docker compose logs`                    |
| 6    | Cleanup                  | `docker compose down`, `down -v`         |

---

## 🧩 Advantages of Docker Compose

* 🧱 Full stack defined in a **single file**
* 🧹 One command start/stop (`up`, `down`)
* 🔄 Automatically networks containers
* 📦 Built-in volume support
* 🏗️ Reproducible environments

---

## 📘 References

* [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
* [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)


