# 🧩 Practical 6 — Setup a MySQL + WordPress Stack (Docker Compose)

### 🎯 **Objective**
Deploy a production-like WordPress CMS + MySQL stack using Docker Compose with persistent volumes, environment configuration, and basic troubleshooting steps.

---

## 🧠 Key Concepts

| Concept | Description |
|---------|-------------|
| **Docker Compose** | Define multi-container apps with a single YAML file. |
| **Volumes** | Persist MySQL data and WordPress uploads across restarts. |
| **Environment variables** | Configure DB credentials, WordPress salts, etc. |
| **Networking** | Services in the same Compose project communicate by service name. |

---

## ⚙️ Prerequisites

- Docker & Docker Compose (v2) installed.
- At least 1–2 GB free RAM for the stack.
- Port 80 (or chosen host port) available on your machine.

Check versions:
```bash
docker --version
docker compose version
```

---

## 🧱 Step 1 — Create Project Directory

```bash
mkdir wp-compose
cd wp-compose
```

---

## 📝 Step 2 — Create `.env` (Optional but recommended)

Create a `.env` file to store credentials (keeps `docker-compose.yml` cleaner):

```env
# .env
MYSQL_ROOT_PASSWORD=change_me_root_pw
MYSQL_DATABASE=wordpress
MYSQL_USER=wp_user
MYSQL_PASSWORD=change_me_wp_pw

WORDPRESS_PORT=8080
```

> ⚠️ Replace `change_me_*` with strong passwords before use. Do **not** commit secrets to public repos.

---

## 🧾 Step 3 — Create `docker-compose.yml`

Create file `docker-compose.yml` with the content below:

```yaml
version: "3.9"

services:
  db:
    image: mysql:8.0
    container_name: wp_db
    restart: unless-stopped
    env_file: 
      - .env
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - wp_network

  wordpress:
    image: wordpress:6.5-apache
    container_name: wp_app
    depends_on:
      - db
    restart: unless-stopped
    ports:
      - "${WORDPRESS_PORT}:80"
    env_file:
      - .env
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: ${MYSQL_USER}
      WORDPRESS_DB_PASSWORD: ${MYSQL_PASSWORD}
      WORDPRESS_DB_NAME: ${MYSQL_DATABASE}
    volumes:
      - wp_data:/var/www/html
    networks:
      - wp_network

  # Optional: phpMyAdmin for DB GUI (comment out if not needed)
  phpmyadmin:
    image: phpmyadmin/phpmyadmin:latest
    container_name: wp_phpmyadmin
    restart: unless-stopped
    depends_on:
      - db
    ports:
      - "8081:80"
    environment:
      PMA_HOST: db
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
    networks:
      - wp_network

volumes:
  db_data:
  wp_data:

networks:
  wp_network:
    driver: bridge
```

Notes:

* `wordpress:6.5-apache` is an example; change tag to your preferred version.
* WordPress files are persisted to `wp_data`. Database stored in `db_data`.
* phpMyAdmin is optional and exposed on port `8081`.

---

## 🚀 Step 4 — Start the Stack

From project root:

```bash
docker compose up -d
```

Check services:

```bash
docker compose ps
```

You should see `wp_db`, `wp_app` (and optionally `wp_phpmyadmin`) listed as `Up`.

---

## 🌐 Step 5 — Access WordPress

Open browser:

* WordPress site: `http://localhost:8080/` (or `http://<host-ip>:${WORDPRESS_PORT}`)
* phpMyAdmin (if enabled): `http://localhost:8081/` (login with root user and `MYSQL_ROOT_PASSWORD`)

Complete WordPress setup via the web UI (site title, admin username, password, email).

---

## 🔐 Step 6 — Secure & Production Tips

* Use strong passwords (store in a secrets manager for production).
* Consider using Docker secrets for sensitive data in swarm/Kubernetes.
* Put WordPress behind a reverse-proxy (nginx/caddy) for TLS termination.
* Run regular backups of `db_data` and `wp_data` (see Cleanup section).
* Consider setting `restart: unless-stopped` (set already) and resource limits if needed.

---

## 🧪 Step 7 — Common Commands & Troubleshooting

View logs:

```bash
docker compose logs -f wordpress
docker compose logs -f db
```

Inspect DB connectivity (exec into WordPress container):

```bash
# open shell in wordpress container
docker exec -it wp_app bash

# test MySQL connection (install mysql client if needed inside container)
apt-get update && apt-get install -y default-mysql-client
mysql -h db -u${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DATABASE}
```

If WordPress shows database connection errors:

* Confirm DB container is `Up`: `docker compose ps`
* Check DB logs: `docker compose logs db`
* Confirm credentials in `.env` match `docker-compose.yml` environment values
* Remove `depends_on` does NOT wait for DB readiness — use retry logic / healthchecks for production.

Add a basic healthcheck for db (optional):

```yaml
    healthcheck:
      test: ["CMD", "mysqladmin" ,"ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
```

---

## 🧹 Step 8 — Backup & Cleanup

### Backup DB (quick dump using a temporary container)

```bash
docker exec -i wp_db mysqldump -u${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DATABASE} > backup.sql
```

### Backup WordPress files

```bash
docker run --rm -v $(pwd)/wp_backups:/backup -v wp_data:/data alpine \
  sh -c "cp -a /data/. /backup/"
```

### Stop & remove containers (preserve volumes)

```bash
docker compose down
```

### Stop & remove containers + volumes (destroys DB & uploads)

```bash
docker compose down -v
```

---

## ✅ Summary

* `docker compose up -d` starts WordPress + MySQL stack.
* `.env` centralizes credentials and ports.
* Volumes `db_data` and `wp_data` keep data persistent.
* Use phpMyAdmin for DB GUI (optional).
* Always back up volumes before destructive operations.

---

## 📘 References

* [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
* [https://hub.docker.com/_/wordpress](https://hub.docker.com/_/wordpress)
* [https://hub.docker.com/_/mysql](https://hub.docker.com/_/mysql)

