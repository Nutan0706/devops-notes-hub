# 🧩 Practical 1 — Install Docker on Linux/Windows

### 🎯 **Objective**
Set up Docker Engine, CLI, and Docker Desktop on your system to build, run, and manage containers efficiently.

---

## 🖥️ Step 1: Check System Requirements

Before installation, ensure your system meets these requirements:

- **OS:** Windows 10/11 (Pro, Enterprise, or Education) or Linux (Ubuntu, CentOS, etc.)
- **Processor:** 64-bit
- **Virtualization:** Enabled in BIOS
- **RAM:** Minimum 4 GB recommended

---

## 🪟 Step 2: Install Docker on Windows

### ✅ **Option 1: Using Docker Desktop**

1. Go to the official Docker website:  
   👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

2. Download **Docker Desktop for Windows** (choose your architecture — x64 or ARM64).

3. Run the downloaded installer `.exe` file.

4. Follow the setup wizard and ensure **“Use WSL 2 instead of Hyper-V”** is checked.

5. After installation, start Docker Desktop from the Start Menu.

6. Verify installation by opening **Command Prompt** or **PowerShell**:
   ```bash
   docker --version
   docker run hello-world
   ```

7. You should see a message:

   ```
   Hello from Docker!
   This message shows that your installation appears to be working correctly.
   ```

---

## 🐧 Step 3: Install Docker on Linux (Ubuntu)

1. **Update existing packages**

   ```bash
   sudo apt-get update
   ```

2. **Install prerequisites**

   ```bash
   sudo apt-get install ca-certificates curl gnupg lsb-release -y
   ```

3. **Add Docker’s official GPG key**

   ```bash
   sudo mkdir -p /etc/apt/keyrings
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   ```

4. **Set up the stable repository**

   ```bash
   echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
     https://download.docker.com/linux/ubuntu \
     $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

5. **Install Docker Engine, CLI, and Containerd**

   ```bash
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
   ```

6. **Verify Docker Installation**

   ```bash
   sudo docker --version
   sudo docker run hello-world
   ```

7. You should see output confirming Docker is running correctly.

---

## ⚙️ Step 4: Manage Docker Service (Linux Only)

* **Start Docker**

  ```bash
  sudo systemctl start docker
  ```

* **Enable Docker at Boot**

  ```bash
  sudo systemctl enable docker
  ```

* **Check Docker Status**

  ```bash
  sudo systemctl status docker
  ```

---

## 👤 Step 5: Run Docker Without `sudo` (Optional on Linux)

1. Add your user to the `docker` group:

   ```bash
   sudo usermod -aG docker $USER
   ```

2. Log out and log back in, then verify:

   ```bash
   docker ps
   ```

---

## 🧪 Step 6: Test Docker Installation

Run a sample NGINX container:

```bash
docker run -d -p 8080:80 nginx
```

Then open your browser and visit:
👉 [http://localhost:8080](http://localhost:8080)

You should see the **NGINX welcome page** — meaning Docker is working perfectly!

---

## ✅ **Practical Summary**

| Step | Task                           | Description                       |
| ---- | ------------------------------ | --------------------------------- |
| 1    | Check Requirements             | Ensure system meets prerequisites |
| 2    | Install Docker (Windows/Linux) | Setup Docker Engine and CLI       |
| 3    | Start and Verify Docker        | Test using `hello-world`          |
| 4    | Manage Service                 | Start/Enable Docker Daemon        |
| 5    | Optional Config                | Run Docker without sudo           |
| 6    | Run Container                  | Verify by running NGINX           |

---

## 📘 References

* [Docker Official Documentation](https://docs.docker.com/)
* [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
* [Install Docker Desktop on Windows](https://docs.docker.com/desktop/install/windows-install/)




