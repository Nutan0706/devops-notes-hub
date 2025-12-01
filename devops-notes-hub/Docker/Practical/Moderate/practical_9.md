# 🧩 Practical 9 — Manage Resource Limits (CPU & Memory)

### 🎯 Objective
Learn how to control and limit Docker container resource usage using:
- `--memory`
- `--memory-swap`
- `--cpus`
- `--cpuset-cpus`

This ensures containers do not overuse system resources.

---

## 🧠 Key Concepts

| Option | Purpose |
|--------|----------|
| `--memory` | Sets the maximum RAM a container can use. |
| `--memory-swap` | Total memory limit = memory + swap. |
| `--cpus` | Limit CPU cores (e.g., 0.5 CPU, 1.5 CPU). |
| `--cpuset-cpus` | Pin container to specific CPU cores. |

---

# ----------------------------------------------------
# ⚙️ Step 1 — Create a Test Container
# ----------------------------------------------------

We will use the `stress` tool to generate CPU and memory load.

Run a test container:
```bash
docker run -it --name stress-demo alpine sh
```

Install stress:

```bash
apk update && apk add stress
```

Exit the container (optional):

```bash
exit
```

---

# ----------------------------------------------------

# 🧩 Step 2 — Limit Memory Usage

# ----------------------------------------------------

Run a container with **256 MB** memory limit:

```bash
docker run -d \
  --name mem-limit \
  --memory=256m \
  alpine \
  sh -c "apk add stress && stress --vm 1 --vm-bytes 300M --vm-hang 1"
```

### Expected Behavior

* Container will be **killed** when trying to use > 256 MB.
* Check container status:

  ```bash
  docker ps -a
  ```
* Status will show:

  ```
  Exited (137)
  ```

  Exit code **137** = Killed due to memory limit.

---

# ----------------------------------------------------

# 🧾 Step 3 — Limit CPU Usage

# ----------------------------------------------------

Run a container limited to **0.5 CPU cores**:

```bash
docker run -d \
  --name cpu-limit \
  --cpus="0.5" \
  alpine \
  sh -c "apk add stress && stress --cpu 4"
```

### Result

Container will use **50% of a single core maximum**, regardless of workload.

Check usage:

```bash
docker stats cpu-limit
```

CPU should show ~50%.

---

# ----------------------------------------------------

# 🔧 Step 4 — Use CPU Pinning (Assign Specific CPUs)

# ----------------------------------------------------

Pin container to CPU core 0 only:

```bash
docker run -d \
  --name cpu-pin \
  --cpuset-cpus="0" \
  alpine \
  sh -c "apk add stress && stress --cpu 2"
```

Container will only run on **CPU core 0**, even if system has multiple cores.

Pin to cores 0 and 2:

```bash
docker run -d --cpuset-cpus="0,2" alpine ...
```

---

# ----------------------------------------------------

# 🧪 Step 5 — Combine CPU + Memory Limits

# ----------------------------------------------------

```bash
docker run -d \
  --name resource-demo \
  --cpus="1.0" \
  --memory="512m" \
  alpine \
  sh -c "apk add stress && stress --cpu 4 --vm 1 --vm-bytes 400M"
```

This container:

* Uses max **1 CPU**
* Uses max **512 MB RAM**

---

# ----------------------------------------------------

# 📊 Step 6 — Monitor Containers

# ----------------------------------------------------

Use Docker stats:

```bash
docker stats
```

You will see:

```
NAME            CPU %   MEM USAGE / LIMIT   MEM %   NET I/O    BLOCK I/O
mem-limit       0%      128MiB / 256MiB     50%     ...        ...
cpu-limit       50%     5MiB / ...          ...     ...        ...
```

---

# ----------------------------------------------------

# 🧹 Step 7 — Cleanup

# ----------------------------------------------------

```bash
docker rm -f mem-limit cpu-limit cpu-pin resource-demo stress-demo
```

---

# ----------------------------------------------------

# ✅ Summary

# ----------------------------------------------------

| Feature           | Command Example                    | Description                  |
| ----------------- | ---------------------------------- | ---------------------------- |
| Memory limit      | `--memory=256m`                    | Max RAM allowed              |
| Memory + swap     | `--memory=256m --memory-swap=512m` | Combined memory + swap limit |
| CPU limit         | `--cpus="0.5"`                     | Half CPU core                |
| CPU cores pinning | `--cpuset-cpus="0,2"`              | Bind to CPU 0 & 2            |
| Monitoring        | `docker stats`                     | View live usage              |

---

## ⭐ Best Practices

* Always apply memory limits in production (`--memory`, `--memory-swap`)
* Use CPU limits for noisy-neighbor control in shared environments
* For microservices, create resource profiles per service
* Combine Docker limits with Kubernetes resource requests/limits for full control

---

## 📘 References

* [https://docs.docker.com/config/containers/resource_constraints/](https://docs.docker.com/config/containers/resource_constraints/)
* [https://github.com/containerd/cgroups](https://github.com/containerd/cgroups)
* [https://man7.org/linux/man-pages/man7/cgroups.7.html](https://man7.org/linux/man-pages/man7/cgroups.7.html)

