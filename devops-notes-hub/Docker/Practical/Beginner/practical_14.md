# 🧩 Practical 14 — Difference Between CMD & ENTRYPOINT

### 🎯 **Objective**
Understand the difference between `CMD` and `ENTRYPOINT` instructions in a Dockerfile and how they affect container command execution behavior.

---

## 🧠 Key Concepts

| Instruction | Purpose |
|--------------|----------|
| **CMD** | Specifies the default command to run when a container starts (can be overridden). |
| **ENTRYPOINT** | Defines the main executable that always runs when the container starts. |
| **CMD + ENTRYPOINT** | Can be combined — CMD provides default arguments to ENTRYPOINT. |

---

## ⚙️ Step 1: Prepare Working Directory

Create a folder for this practical:
```bash
mkdir cmd-entrypoint-demo
cd cmd-entrypoint-demo
```

---

## 🧱 Step 2: Create Script to Execute

Create a file named `start.sh`:

```bash
#!/bin/bash
echo "Hello from the Docker container!"
echo "Arguments passed: $@"
```

Make it executable:

```bash
chmod +x start.sh
```

Your folder now looks like:

```
cmd-entrypoint-demo/
├── Dockerfile
└── start.sh
```

---

## 🧩 Step 3: Example 1 — Using CMD

Create a **Dockerfile** with only `CMD`:

```Dockerfile
# Use Ubuntu base image
FROM ubuntu:latest

# Copy script into container
COPY start.sh /usr/local/bin/start.sh

# Set working directory
WORKDIR /usr/local/bin

# Default command
CMD ["./start.sh"]
```

Build the image:

```bash
docker build -t cmd-demo .
```

Run container:

```bash
docker run cmd-demo
```

Output:

```
Hello from the Docker container!
Arguments passed:
```

Now try passing an argument:

```bash
docker run cmd-demo DevOps
```

Output:

```
Hello from the Docker container!
Arguments passed: DevOps
```

✅ The `CMD` instruction **gets replaced** when arguments are passed in `docker run`.

---

## 🧩 Step 4: Example 2 — Using ENTRYPOINT

Now, modify the **Dockerfile** to use `ENTRYPOINT` instead of `CMD`:

```Dockerfile
# Use Ubuntu base image
FROM ubuntu:latest

# Copy script
COPY start.sh /usr/local/bin/start.sh

WORKDIR /usr/local/bin

# Define ENTRYPOINT
ENTRYPOINT ["./start.sh"]
```

Rebuild image:

```bash
docker build -t entrypoint-demo .
```

Run container:

```bash
docker run entrypoint-demo
```

Output:

```
Hello from the Docker container!
Arguments passed:
```

Now pass an argument:

```bash
docker run entrypoint-demo DevOps
```

Output:

```
Hello from the Docker container!
Arguments passed: DevOps
```

✅ The `ENTRYPOINT` **always executes the specified command**, and the arguments are **appended** automatically — not replaced.

---

## 🧩 Step 5: Example 3 — Combining ENTRYPOINT and CMD

Create a third Dockerfile example:

```Dockerfile
# Use Ubuntu base image
FROM ubuntu:latest

# Copy script
COPY start.sh /usr/local/bin/start.sh

WORKDIR /usr/local/bin

# ENTRYPOINT always executes
ENTRYPOINT ["./start.sh"]

# CMD provides default arguments
CMD ["DefaultCMD"]
```

Build it:

```bash
docker build -t combo-demo .
```

Run without arguments:

```bash
docker run combo-demo
```

Output:

```
Hello from the Docker container!
Arguments passed: DefaultCMD
```

Run with arguments:

```bash
docker run combo-demo DevOps Student
```

Output:

```
Hello from the Docker container!
Arguments passed: DevOps Student
```

✅ Here, `CMD` provides default arguments for `ENTRYPOINT` but **can be overridden** at runtime.

---

## ⚖️ Step 6: Key Differences — CMD vs ENTRYPOINT

| Feature                           | CMD                                         | ENTRYPOINT                            |
| --------------------------------- | ------------------------------------------- | ------------------------------------- |
| Purpose                           | Provides default command                    | Defines fixed executable              |
| Can be overridden by `docker run` | ✅ Yes                                       | ⚠️ No (arguments appended)            |
| Syntax                            | `CMD ["executable", "param1"]`              | `ENTRYPOINT ["executable", "param1"]` |
| Typical Use                       | Run default commands or scripts             | Always execute main app               |
| Combine                           | Can provide default arguments to ENTRYPOINT | Works together with CMD               |

---

## 🧪 Step 7: Real-Life Example

### CMD Use Case:

Lightweight containers like Alpine using `CMD` for default shell.

```Dockerfile
FROM alpine
CMD ["echo", "This is default message"]
```

### ENTRYPOINT Use Case:

Utility containers like `curl` or `ping` use ENTRYPOINT for main command.

```Dockerfile
FROM alpine
ENTRYPOINT ["ping"]
CMD ["google.com"]
```

Run:

```bash
docker run ping-demo
docker run ping-demo yahoo.com
```

✅ The first pings google.com, second pings yahoo.com — `ENTRYPOINT` ensures `ping` always runs.

---

## 🧹 Step 8: Clean Up

Remove containers and images:

```bash
docker rm -f $(docker ps -aq)
docker rmi cmd-demo entrypoint-demo combo-demo
```

---

## ✅ Step 9: Summary

| Step | Concept          | Description                                                 |
| ---- | ---------------- | ----------------------------------------------------------- |
| 1    | CMD              | Defines default executable/arguments, overridden by runtime |
| 2    | ENTRYPOINT       | Defines fixed executable, cannot be overridden              |
| 3    | CMD + ENTRYPOINT | Combine for flexibility (CMD gives default args)            |
| 4    | Override         | `docker run <image> <args>` replaces CMD but not ENTRYPOINT |
| 5    | Use Case         | CMD → simple scripts, ENTRYPOINT → command-based utilities  |

---

## 📘 References

* [Dockerfile Reference — CMD & ENTRYPOINT](https://docs.docker.com/engine/reference/builder/)
* [Docker CMD Command](https://docs.docker.com/engine/reference/builder/#cmd)
* [Docker ENTRYPOINT Command](https://docs.docker.com/engine/reference/builder/#entrypoint)
* [Docker Best Practices for Image Builds](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
