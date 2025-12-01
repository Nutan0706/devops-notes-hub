# 🧩 Practical 15 — Clean Up Docker Resources

### 🎯 **Objective**
Learn how to clean up unused Docker resources — including containers, images, volumes, and networks — using commands like `docker system prune`, `docker image prune`, and others.

---

## 🧠 Key Concepts

| Resource | Description |
|-----------|--------------|
| **Container** | An active or stopped instance of an image. |
| **Image** | Template used to create containers. |
| **Volume** | Used for data persistence between containers. |
| **Network** | Enables communication between containers. |
| **Prune** | A command used to remove unused or dangling Docker resources. |

---

## ⚙️ Step 1: Verify Existing Docker Resources

Check what’s currently running and stored on your system.

List all running containers:
```bash
docker ps
```

List all containers (including stopped):

```bash
docker ps -a
```

List all images:

```bash
docker images
```

List all networks:

```bash
docker network ls
```

List all volumes:

```bash
docker volume ls
```

---

## 🧩 Step 2: Remove Stopped Containers

To remove containers that are **stopped**:

```bash
docker container prune
```

Confirm prompt:

```
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N]
```

Type `y` and press **Enter**.

---

## 🧱 Step 3: Remove Unused Images

Remove **dangling images** (unused intermediate layers):

```bash
docker image prune
```

Remove **all unused images**:

```bash
docker image prune -a
```

✅ *Use this with caution — it removes all images not associated with any running container.*

---

## 🧹 Step 4: Remove Unused Volumes

Check for existing volumes:

```bash
docker volume ls
```

Remove all unused volumes:

```bash
docker volume prune
```

Confirm with `y` to delete.

---

## 🌐 Step 5: Remove Unused Networks

Check existing networks:

```bash
docker network ls
```

Remove all unused networks:

```bash
docker network prune
```

Networks used by active containers will not be deleted.

---

## ⚡ Step 6: Clean Everything — System Prune

To clean **all unused resources** (containers, images, networks, build cache):

```bash
docker system prune
```

You’ll see a warning like:

```
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - all build cache
Are you sure you want to continue? [y/N]
```

Confirm by typing `y`.

---

## 🧨 Step 7: Deep Clean — Remove All Unused Resources

To remove **all unused containers, images, volumes, and networks** (not just dangling):

```bash
docker system prune -a --volumes
```

### ⚠️ Be Careful:

This command removes **everything** not currently in use — even volumes and cached data.

---

## 🧾 Step 8: Check Disk Usage

View current Docker disk space usage:

```bash
docker system df
```

Example output:

```
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          10        2         3.5GB     2.9GB (83%)
Containers      4         1         200MB     150MB (75%)
Local Volumes   3         1         500MB     400MB (80%)
Build Cache     0         0         0B        0B
```

After cleanup, run the same command again to confirm reduced usage.

---

## ✅ Step 9: Summary

| Step | Task              | Command                                             | Description                  |
| ---- | ----------------- | --------------------------------------------------- | ---------------------------- |
| 1    | View Resources    | `docker ps -a`, `docker images`, `docker volume ls` | Check current usage          |
| 2    | Remove Containers | `docker container prune`                            | Delete stopped containers    |
| 3    | Remove Images     | `docker image prune -a`                             | Delete unused images         |
| 4    | Remove Volumes    | `docker volume prune`                               | Delete unused volumes        |
| 5    | Remove Networks   | `docker network prune`                              | Delete unused networks       |
| 6    | Clean System      | `docker system prune`                               | Remove all unused resources  |
| 7    | Full Cleanup      | `docker system prune -a --volumes`                  | Deep clean (⚠️ irreversible) |
| 8    | Check Space       | `docker system df`                                  | Verify disk usage            |

---

## 🧩 Pro Tips

* Automate cleanup with a cron job (Linux example):

  ```bash
  0 0 * * 0 docker system prune -af --volumes
  ```

  *(Runs cleanup every Sunday at midnight)*

* Use `--filter` to be selective:

  ```bash
  docker image prune --filter "until=24h"
  ```

  *(Removes images older than 24 hours)*

---

## 📘 References

* [Docker System Prune Documentation](https://docs.docker.com/engine/reference/commandline/system_prune/)
* [Docker Disk Usage Command](https://docs.docker.com/engine/reference/commandline/system_df/)
* [Docker Image and Volume Management](https://docs.docker.com/config/pruning/)
