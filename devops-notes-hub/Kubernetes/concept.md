# 🚀 Kubernetes Concepts – Quick Revision Sheet

A clean, structured, and interview-friendly Kubernetes concepts sheet with tables, collapsible sections, and examples.

---

## 📌 1. Kubernetes Basics

- **Master vs Worker Nodes** → Roles & key components.
- **kubectl** — Common commands:  
  `get`, `describe`, `logs`, `exec`, `apply`, `delete`, `edit`

---

## 🧩 2. Core Components

<details>
<summary><strong>📍 Click to Expand Kubernetes Core Components</strong></summary>

| Component | Description |
|----------|--------------|
| **Pod** | Smallest deployable unit (contains 1+ containers) |
| **Node** | Worker machine (VM/Physical) |
| **Cluster** | Master + Worker nodes |
| **Namespace** | Virtual cluster within a cluster |
| **Deployment** | Declarative updates for Pods |
| **ReplicaSet** | Ensures desired number of Pods are running |
| **DaemonSet** | Run a Pod on all (or selected) nodes |
| **StatefulSet** | Manages stateful apps → ordered, fixed pod names |
| **Job** | Run tasks to completion (one-time jobs) |
| **CronJob** | Run Jobs on a schedule |
| **Service** | Expose Pods (Types: ClusterIP, NodePort, LoadBalancer) |
| **Ingress** | HTTP/HTTPS routing to services |
| **ConfigMap** | Externalize non-confidential config |
| **Secret** | Store sensitive data (base64 encoded) |
| **Volume** | Storage abstraction for containers |
| **PersistentVolume (PV)** | Cluster storage resource |
| **PersistentVolumeClaim (PVC)** | Request for PV by a Pod |

</details>

---

## 🌐 3. Networking Concepts

- **Cluster Networking** → Pod ↔ Pod communication across nodes  
- **Service Discovery** → `kube-dns` / CoreDNS  
- **Load Balancing** → Services & Ingress Controller  
- **Network Policies** → Control traffic flow at pod level  

---

## ⚙️ 4. Scheduling & Scaling

| Feature | Purpose |
|---------|-----------|
| **Scheduler** | Places Pods on nodes |
| **Affinity / Anti-Affinity** | Pod placement rules |
| **Taints & Tolerations** | Control where Pods CAN/CANNOT run |
| **HPA** | Auto-scale Pods using CPU/Memory metrics |
| **VPA** | Auto-adjust container resource requests/limits |
| **Cluster Autoscaler** | Add/remove cluster nodes automatically |

---

## 💾 5. Storage

- **Ephemeral vs Persistent Storage**
- **PV & PVC Lifecycle**
- **StorageClasses** → Enables dynamic volume provisioning

---

## 🔐 6. Security

| Security Feature | Description |
|------------------|----------------|
| **RBAC** | Roles, RoleBindings, ClusterRoles authorization |
| **Service Accounts** | Identity for Pods to access the API |
| **Pod Security Admission** | Replaces PSP (Enforce security controls) |
| **Network Policies** | Restrict traffic between Pods |
| **Secrets Management** | Store sensitive data securely |

---

## ⚙️ 7. Config Management

- ConfigMaps vs Secrets  
- Inject via **Env Variables** or **Mounted Files**  

---

## 📈 8. Logging & Monitoring

- **Logs** → `kubectl logs`, log sidecar patterns  
- **Monitoring** → Prometheus + Grafana  
- **Health Checks** → Liveness, Readiness & Startup probes  

---

## 🧠 9. Deployment Patterns

| Pattern | When to Use |
|--------|----------------|
| **Rolling Update** | Default safe gradual update |
| **Blue-Green** | Zero downtime switch between 2 environments |
| **Canary** | Release to % of users first |
| **Helm** | Package manager for Kubernetes apps |

---

## 🧯 10. Troubleshooting Tips

- `kubectl get events` → First place to check issues  
- `kubectl describe pod <pod>`  
- `kubectl logs <pod>`  
- Common Issues:  
  - `CrashLoopBackOff`  
  - `ImagePullBackOff`  
  - Resource Limit exceeded  

---

## 💡 11. Useful Commands

```bash
# Check cluster info
kubectl cluster-info

# Get nodes
kubectl get nodes

# Get all pods in all namespaces
kubectl get pods --all-namespaces

# Describe a resource
kubectl describe pod POD_NAME

# View logs
kubectl logs POD_NAME

# Exec into a pod
kubectl exec -it POD_NAME -- /bin/sh

# Apply config
kubectl apply -f file.yaml

# Dry-run manifest
kubectl apply --dry-run=client -f file.yaml

# Scale deployment
kubectl scale deployment DEPLOYMENT_NAME --replicas=5

```
