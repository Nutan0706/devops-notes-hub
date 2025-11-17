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
