# 🧩 Practical 2 — Create a Custom Bridge Network & Connect Multiple Containers

### 🎯 **Objective**
Learn how to create a **custom Docker bridge network** and connect multiple containers to enable **inter-service communication**.

---

## 🧠 Key Concepts

| Concept | Description |
|---------|-------------|
| **Bridge Network** | Default Docker network type for container-to-container communication. |
| **Custom Bridge Network** | User-defined network that provides automatic DNS resolution and better isolation. |
| **Container Name Access** | Containers on the same custom network can communicate using their container names. |

---

# ----------------------------------------------------
# ⚙️ Step 1: List Available Docker Networks
# ----------------------------------------------------

List all existing networks:
```bash
docker network ls
````

Example output:

```
NETWORK ID     NAME      DRIVER    SCOPE
8e9f21a2b8b1   bridge    bridge    local
b6f9cd345abc   host      host      local
a9c8b7d2efgh   none      null      local
```

---

# ----------------------------------------------------

# 🧱 Step 2: Create a Custom Bridge Network

# ----------------------------------------------------

Create a new bridge network named **mynet**:

```bash
docker network create mynet
```

Verify:

```bash
docker network ls
```

Output:

```
NETWORK ID     NAME      DRIVER    SCOPE
d4e5f6g7h8i9   mynet     bridge    local
```

---

# ----------------------------------------------------

# 🚀 Step 3: Run Containers on the Custom Network

# ----------------------------------------------------

Run a simple NGINX container on `mynet`:

```bash
docker run -d --name service1 --network mynet nginx
```

Run a second container (Alpine) on the same network:

```bash
docker run -d --name service2 --network mynet alpine sleep 3600
```

Check running containers:

```bash
docker ps
```

---

# ----------------------------------------------------

# 🔍 Step 4: Inspect the Custom Network

# ----------------------------------------------------

View details of `mynet`:

```bash
docker network inspect mynet
```

You should see both containers listed under `"Containers"`:

```json
"Containers": {
  "a1b2c3": {
    "Name": "service1",
    "IPv4Address": "172.19.0.2/16"
  },
  "b2c3d4": {
    "Name": "service2",
    "IPv4Address": "172.19.0.3/16"
  }
}
```

---

# ----------------------------------------------------

# 🔗 Step 5: Test Inter-Service Communication

# ----------------------------------------------------

Enter the second container (service2):

```bash
docker exec -it service2 sh
```

Install ping (Alpine minimal):

```bash
apk update && apk add iputils
```

Ping the NGINX container using its **container name**:

```bash
ping service1 -c 4
```

Expected output:

```
64 bytes from service1: icmp_seq=1 ttl=64 time=0.45 ms
```

🎉 This proves both containers can reach each other over the custom network.

Exit:

```bash
exit
```

---

# ----------------------------------------------------

# 🧠 Step 6: Connect/Disconnect Containers from a Network

# ----------------------------------------------------

### Connect a running container to a network:

```bash
docker network connect mynet service1
```

### Disconnect a running container:

```bash
docker network disconnect mynet service1
```

---

# ----------------------------------------------------

# 🧹 Step 7: Cleanup (Optional)

# ----------------------------------------------------

Stop containers:

```bash
docker stop service1 service2
```

Remove containers:

```bash
docker rm service1 service2
```

Remove network:

```bash
docker network rm mynet
```

---

# ----------------------------------------------------

# ✅ Summary

# ----------------------------------------------------

| Step | Task                      | Command                                 |
| ---- | ------------------------- | --------------------------------------- |
| 1    | List networks             | `docker network ls`                     |
| 2    | Create custom network     | `docker network create mynet`           |
| 3    | Run containers on network | `docker run --network mynet`            |
| 4    | Inspect network           | `docker network inspect mynet`          |
| 5    | Test connectivity         | `ping <container-name>`                 |
| 6    | Manage networks           | `docker network connect` / `disconnect` |
| 7    | Cleanup                   | Stop/remove containers, remove network  |

---

## 📘 References

* [https://docs.docker.com/network/](https://docs.docker.com/network/)
* [https://docs.docker.com/engine/reference/commandline/network/](https://docs.docker.com/engine/reference/commandline/network/)

