# 🧩 Practical 8 — Pass Secrets and Configs Securely  
### 🎯 Objective  
Learn how to pass sensitive data like passwords, API keys, and configuration values securely using:  
- **Environment files (`.env`)**  
- **Docker Secrets** (Swarm mode)  

This prevents hardcoding secrets inside Dockerfiles or Compose files.

---

# ----------------------------------------------------
# 🧠 Key Concepts
# ----------------------------------------------------

| Method | Best For | Security Level |
|--------|----------|----------------|
| **Environment Variables (`-e`)** | Quick local tests | 🔓 Low |
| **`.env` file** | Local development | 🔐 Medium |
| **Docker Secrets** | Production (Swarm) | 🔐🔐 High |

---

# ====================================================
# 🧩 PART A — USING `.env` FILES (Recommended for Dev)
# ====================================================

# ----------------------------------------------------
## ⚙️ Step 1 — Create Project Folder
# ----------------------------------------------------
```bash
mkdir secure-config-demo
cd secure-config-demo
````

# ----------------------------------------------------

## 📝 Step 2 — Create a `.env` File

# ----------------------------------------------------

Create `.env`:

```
DB_USER=admin
DB_PASSWORD=SuperSecretPassword
API_KEY=12345-ABCDE-67890
```

> ⚠️ **Never commit `.env` files to GitHub. Add it to `.gitignore`.**

---

# ----------------------------------------------------

## 🧾 Step 3 — Use `.env` in docker-compose.yml

# ----------------------------------------------------

Create a `docker-compose.yml`:

```yaml
version: "3.9"

services:
  app:
    image: alpine
    container_name: env-demo
    env_file:
      - .env
    command: sh -c "echo User: $DB_USER && echo Password: $DB_PASSWORD && echo API: $API_KEY"
```

---

# ----------------------------------------------------

## 🚀 Step 4 — Run the Container

# ----------------------------------------------------

```bash
docker compose up
```

Expected Output:

```
User: admin
Password: SuperSecretPassword
API: 12345-ABCDE-67890
```

---

# ----------------------------------------------------

## 📦 Step 5 — View Env Variables Inside Container

# ----------------------------------------------------

```bash
docker exec -it env-demo env
```

---

# ====================================================

# 🧩 PART B — USING DOCKER SECRETS (Production-Grade)

# ====================================================

Docker Secrets require **Swarm Mode**.

---

# ----------------------------------------------------

## 🐳 Step 6 — Enable Docker Swarm (1-time setup)

# ----------------------------------------------------

```bash
docker swarm init
```

---

# ----------------------------------------------------

## 🔐 Step 7 — Create a Docker Secret

# ----------------------------------------------------

```bash
echo "ProdPassword123" | docker secret create db_password -
```

List secrets:

```bash
docker secret ls
```

Output:

```
NAME           DRIVER    CREATED
db_password              2s ago
```

---

# ----------------------------------------------------

## 🧾 Step 8 — Use Secrets in a Docker Stack

# ----------------------------------------------------

Create a file named `stack.yml`:

```yaml
version: "3.9"

services:
  app:
    image: alpine
    container_name: secret-demo
    command: sh -c "echo DB Password: $(cat /run/secrets/db_password)"
    secrets:
      - db_password

secrets:
  db_password:
    external: true
```

---

# ----------------------------------------------------

## 🚀 Step 9 — Deploy the Stack

# ----------------------------------------------------

```bash
docker stack deploy -c stack.yml secureapp
```

Check logs:

```bash
docker service logs secureapp_app
```

Output:

```
DB Password: ProdPassword123
```

---

# ----------------------------------------------------

## 🎯 Why Docker Secrets Are Better

# ----------------------------------------------------

| Feature                     | Env Vars | `.env` | Docker Secrets |
| --------------------------- | -------- | ------ | -------------- |
| Encrypted at rest           | ❌        | ❌      | ✅              |
| Visible in `docker inspect` | ❌        | ❌      | ⚠️ No          |
| Visible in process list     | ❌        | ❌      | ❌              |
| Best for                    | Dev      | Dev    | **Production** |

---

# ----------------------------------------------------

# 🧹 Step 10 — Cleanup

# ----------------------------------------------------

Remove stack:

```bash
docker stack rm secureapp
```

Remove secret:

```bash
docker secret rm db_password
```

Leave swarm:

```bash
docker swarm leave --force
```

---

# ----------------------------------------------------

# ✅ Summary

# ----------------------------------------------------

| Method         | Use Case          | Command                        |
| -------------- | ----------------- | ------------------------------ |
| `.env` file    | Local development | `env_file: .env`               |
| Env vars       | Quick testing     | `docker run -e KEY=value`      |
| Docker Secrets | Production        | `docker secret create` + Swarm |

---

## 📘 References

* [https://docs.docker.com/engine/swarm/secrets/](https://docs.docker.com/engine/swarm/secrets/)
* [https://docs.docker.com/compose/environment-variables/](https://docs.docker.com/compose/environment-variables/)
* [https://12factor.net/config](https://12factor.net/config)


