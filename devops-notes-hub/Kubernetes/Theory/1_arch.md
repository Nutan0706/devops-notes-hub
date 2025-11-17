# 🚀 **Kubernetes Master Node Components (Control Plane Components)**

The **master node** (now called **Control Plane**) manages the entire Kubernetes cluster.
It makes decisions, maintains cluster state, schedules workloads, and handles communication.

There are **five main components**:

---

## ✅ **1. API Server (kube-apiserver)**

**The brain + entry point of the cluster.**

### What it does:

* Exposes the Kubernetes API (kubectl uses this)
* Validates and processes all requests
* Talks to etcd, scheduler, controller manager
* Acts as a communication hub

### Interview line:

> *"API server is the front door of Kubernetes. Every operation — deploy, scale, delete — goes through it."*

---

## ✅ **2. etcd (Key-Value Store)**

**The database of Kubernetes.**

### What it stores:

* Cluster state
* Configurations
* Secrets
* Pod details
* Node information

### Interview line:

> *"etcd is the single source of truth. If etcd is down, Kubernetes can’t remember anything."*

---

## ✅ **3. Scheduler (kube-scheduler)**

**Decides *where* Pods will run.**

### What it checks:

* Resource availability
* CPU / RAM
* Node taints & tolerations
* Node selectors
* Affinity / anti-affinity

### Interview line:

> *"Scheduler picks the best node for the pod. It doesn't create the pod — just assigns a node."*

---

## ✅ **4. Controller Manager (kube-controller-manager)**

**Runs background controllers to keep the cluster stable.**

### Important controllers:

* Node Controller
* Deployment Controller
* ReplicaSet Controller
* Endpoint Controller
* Job Controller
* Service Account Controller

### Interview line:

> *"Controller Manager continuously watches the cluster and reconciles the desired state vs actual state."*

---

## ✅ **5. Cloud Controller Manager** *(Only in cloud environments)*

**Integrates Kubernetes with cloud providers.**

### What it manages:

* Load balancers
* Nodes (cloud instances)
* Networking (VPC, routes)
* Volumes (EBS, Azure Disk, GCP PD)


---

# 🎯 **Simple Diagram (Mental Model)**

```
+---------------------------------------------------+
|                Control Plane (Master)             |
|                                                   |
|   +---------------+                               |
|   | API Server    | <---- kubectl requests        |
|   +-------+-------+                               |
|           |                                       |
|   +-------v-------+                               |
|   |    etcd       |  (Cluster Database)           |
|   +---------------+                               |
|           |                                       |
|   +-------v-------+      +----------------------+ |
|   |  Scheduler    |      | Controller Manager   | |
|   +---------------+      +----------------------+ |
|                |                   |              |
|                +--------+----------+              |
|                         |                         |
|               Worker Nodes (run pods)             |
+---------------------------------------------------+
```

# 🚀 **Kubernetes Worker Node Components (Data Plane)**

Worker nodes run your **applications (Pods)**.
They contain everything required to **run containers**, **manage networking**, and **communicate** with the master.

There are **4 main worker node components**:

---

## ✅ **1. Kubelet**

**The node agent. Runs on every worker node.**

### What it does:

* Talks to the API server
* Makes sure the containers defined in PodSpec are actually running
* Monitors container health
* Registers the node with the cluster

### Interview line:

> *"Actually kubelet is like the manager of that node. It ensures pod is running exactly as the API server wants."*

---

## ✅ **2. Kube-proxy**

**Handles networking inside the cluster.**

### What it does:

* Maintains networking rules (iptables / IPVS)
* Forwards traffic to correct pods
* Enables Service → Pod communication
* Ensures load-balancing between pods

### Interview line:

> *"Basically kube-proxy manages all service networking and load balancing on the node."*

---

## ✅ **3. Container Runtime**

**Runs the actual containers.**

### Popular runtimes:

* containerd *(default in most clusters)*
* CRI-O *(OpenShift)*
* Docker *(deprecated but still works via shim)*

### What it does:

* Pulls container images
* Starts and stops containers
* Provides container filesystem

### Interview line:

> *"Container runtime is responsible for actually running the containers. Kubernetes itself does not run containers."*

---

## ✅ **4. Pod (The actual workload)**

Each pod contains:

* One or more containers
* Storage volumes
* Network namespace

### Interview line:

> *"Pods are the smallest deployable unit in Kubernetes. All containers run inside pods only."*

---

# 🎯 **Worker Node Architecture Diagram (Simple)**

```
+------------------------------------------------+
|               Worker Node (Data Plane)         |
|                                                |
|   +-----------------------------+              |
|   |         Kubelet            | <--- Talks to API Server
|   +-----------------------------+              |
|                                                |
|   +-----------------------------+              |
|   |         Kube-proxy         | <--- Networking & LB
|   +-----------------------------+              |
|                                                |
|   +-----------------------------+              |
|   |    Container Runtime       | <--- Runs containers
|   +-----------------------------+              |
|                                                |
|   +-----------------------------+              |
|   |        Pods (Apps)         | <--- Your workloads
|   +-----------------------------+              |
+------------------------------------------------+
```
