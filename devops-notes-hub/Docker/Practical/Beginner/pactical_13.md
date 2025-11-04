# 🧩 Practical 13 — Inspect Container Networking

### 🎯 **Objective**
Understand Docker networking by listing, inspecting, and exploring how containers communicate using the default and custom Docker networks.

---

## 🧠 Key Concepts

| Concept | Description |
|----------|--------------|
| **Docker Network** | Enables communication between containers and external systems. |
| **Bridge Network** | Default network for standalone containers. |
| **Host Network** | Shares the host’s network stack directly. |
| **None Network** | Completely isolates the container from networking. |
| **User-Defined Network** | Custom bridge network where containers can communicate by name. |

---

## ⚙️ Step 1: Verify Docker Installation

Check Docker setup:
```bash
docker --version
docker info
```

---

## 🌐 Step 2: List Available Docker Networks

To list all Docker networks:

```bash
docker network ls
```

Example output:

```
NETWORK ID     NAME      DRIVER    SCOPE
8e9f21a2b8b1   bridge    bridge    local
b6f9cd345abc   host      host      local
a9c8b7d2efgh   none      null      local
```

### Explanation:

* **bridge** → Default network for containers.
* **host** → Shares host networking stack.
* **none** → No networking for the container.

---

## 🧩 Step 3: Inspect a Network

Use `docker network inspect` to get detailed info about any network.

Inspect the default **bridge** network:

```bash
docker network inspect bridge
```

Sample output (simplified):

```json
[
  {
    "Name": "bridge",
    "Driver": "bridge",
    "IPAM": {
      "Config": [
        {
          "Subnet": "172.17.0.0/16"
        }
      ]
    },
    "Containers": {}
  }
]
```

This shows subnet, gateway, and connected containers.

---

## 🧱 Step 4: Create and Inspect a Custom Network

Create a user-defined bridge network:

```bash
docker network create mynetwork
```

List networks again:

```bash
docker network ls
```

Output:

```
NETWORK ID     NAME        DRIVER    SCOPE
8e9f21a2b8b1   bridge      bridge    local
b6f9cd345abc   host        host      local
a9c8b7d2efgh   none        null      local
d4e5f6g7h8i9   mynetwork   bridge    local
```

Inspect the new network:

```bash
docker network inspect mynetwork
```

Output (simplified):

```json
[
  {
    "Name": "mynetwork",
    "Driver": "bridge",
    "Containers": {},
    "IPAM": {
      "Config": [
        {
          "Subnet": "172.19.0.0/16"
        }
      ]
    }
  }
]
```

---

## 🧠 Step 5: Run Containers in Custom Network

Run two containers on the `mynetwork` network:

```bash
docker run -d --name web1 --network mynetwork nginx
docker run -d --name web2 --network mynetwork nginx
```

List containers:

```bash
docker ps
```

Inspect the network again:

```bash
docker network inspect mynetwork
```

You’ll now see both containers listed under the `"Containers"` section:

```json
"Containers": {
  "a1b2c3d4e5f6": {
    "Name": "web1",
    "IPv4Address": "172.19.0.2/16"
  },
  "b2c3d4e5f6a7": {
    "Name": "web2",
    "IPv4Address": "172.19.0.3/16"
  }
}
```

---

## 🔗 Step 6: Test Container-to-Container Communication

Access the shell of one container:

```bash
docker exec -it web1 /bin/bash
```

Ping the other container by name:

```bash
apt-get update && apt-get install -y iputils-ping
ping web2 -c 4
```

Output:

```
PING web2 (172.19.0.3): 56 data bytes
64 bytes from 172.19.0.3: icmp_seq=0 ttl=64 time=0.046 ms
```

✅ Containers can communicate by **container name** because they share the same user-defined network.

Exit the container:

```bash
exit
```

---

## 🧹 Step 7: Clean Up

Stop and remove containers:

```bash
docker stop web1 web2
docker rm web1 web2
```

Remove the custom network:

```bash
docker network rm mynetwork
```

---

## ✅ Step 8: Summary

| Step | Task                  | Command                           | Description                    |
| ---- | --------------------- | --------------------------------- | ------------------------------ |
| 1    | List Networks         | `docker network ls`               | Display all Docker networks    |
| 2    | Inspect Network       | `docker network inspect bridge`   | View network details           |
| 3    | Create Custom Network | `docker network create mynetwork` | Create new network             |
| 4    | Connect Containers    | `--network mynetwork`             | Attach containers to a network |
| 5    | Test Communication    | `ping container_name`             | Check container connectivity   |
| 6    | Clean Up              | `docker network rm mynetwork`     | Remove unused network          |

---

## 🧩 Pro Tip

You can connect a container to multiple networks:

```bash
docker network connect mynetwork web1
```

And disconnect when needed:

```bash
docker network disconnect mynetwork web1
```

---

## 📘 References

* [Docker Network Overview](https://docs.docker.com/network/)
* [Docker Network Inspect](https://docs.docker.com/engine/reference/commandline/network_inspect/)
* [Bridge Network Concepts](https://docs.docker.com/network/bridge/)
