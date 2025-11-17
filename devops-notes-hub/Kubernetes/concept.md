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

Here is your **GitHub markdown file updated with colored badges** using **Shields.io**.
All badges are lightweight, static, and GitHub-friendly.

You can paste this directly into **kubernetes_concepts.md**.

---

# `kubernetes_concepts.md`

# **Kubernetes Concepts – Category-wise Table (with Badges + One-liners)**

---

# **🏗️ Cluster Architecture** ![badge](https://img.shields.io/badge/Category-Architecture-blue)

| Concept           | Definition                           | Badge                                                        |
| ----------------- | ------------------------------------ | ------------------------------------------------------------ |
| Node              | Machine where workloads run.         | ![](https://img.shields.io/badge/Node-grey)                  |
| Control Plane     | Manages cluster state.               | ![](https://img.shields.io/badge/Control%20Plane-blueviolet) |
| Worker Node       | Runs pods & workloads.               | ![](https://img.shields.io/badge/Worker%20Node-green)        |
| Kubelet           | Node-level pod manager.              | ![](https://img.shields.io/badge/Kubelet-orange)             |
| Kube Proxy        | Handles cluster networking.          | ![](https://img.shields.io/badge/Kube%20Proxy-yellowgreen)   |
| Container Runtime | Runs containers (Docker/containerd). | ![](https://img.shields.io/badge/Runtime-lightgrey)          |

---

# **📦 Workloads (Pods & Controllers)** ![badge](https://img.shields.io/badge/Category-Workloads-orange)

| Concept             | Definition                         | Badge                                                   |
| ------------------- | ---------------------------------- | ------------------------------------------------------- |
| Pod                 | Smallest deployable unit.          | ![](https://img.shields.io/badge/Pod-blue)              |
| Multi-Container Pod | Multiple containers in one pod.    | ![](https://img.shields.io/badge/Multi--Container-teal) |
| Deployment          | Manages ReplicaSets & updates.     | ![](https://img.shields.io/badge/Deployment-green)      |
| ReplicaSet          | Ensures desired replicas.          | ![](https://img.shields.io/badge/ReplicaSet-lightgreen) |
| StatefulSet         | Stable identity for stateful apps. | ![](https://img.shields.io/badge/StatefulSet-purple)    |
| DaemonSet           | Runs one pod per node.             | ![](https://img.shields.io/badge/DaemonSet-red)         |
| Job                 | Runs tasks to completion.          | ![](https://img.shields.io/badge/Job-yellow)            |
| CronJob             | Scheduled jobs.                    | ![](https://img.shields.io/badge/CronJob-blueviolet)    |

---

# **🌐 Networking** ![badge](https://img.shields.io/badge/Category-Networking-success)

| Concept            | Definition                   | Badge                                                         |
| ------------------ | ---------------------------- | ------------------------------------------------------------- |
| ClusterIP          | Internal-only service.       | ![](https://img.shields.io/badge/ClusterIP-green)             |
| NodePort           | Exposes service on node IP.  | ![](https://img.shields.io/badge/NodePort-blue)               |
| LoadBalancer       | Exposes externally via LB.   | ![](https://img.shields.io/badge/LoadBalancer-orange)         |
| ExternalName       | Maps service to DNS CNAME.   | ![](https://img.shields.io/badge/ExternalName-grey)           |
| Headless Service   | Direct pod DNS, no LB.       | ![](https://img.shields.io/badge/HeadlessService-yellowgreen) |
| Ingress            | HTTP/HTTPS routing.          | ![](https://img.shields.io/badge/Ingress-lightblue)           |
| Ingress Controller | Implements ingress rules.    | ![](https://img.shields.io/badge/Ingress%20Controller-purple) |
| NetworkPolicy      | Controls pod network access. | ![](https://img.shields.io/badge/NetworkPolicy-red)           |

---

# **💾 Storage** ![badge](https://img.shields.io/badge/Category-Storage-blueviolet)

| Concept          | Definition                       | Badge                                                    |
| ---------------- | -------------------------------- | -------------------------------------------------------- |
| Volume           | Pod-attached storage.            | ![](https://img.shields.io/badge/Volume-grey)            |
| EmptyDir         | Temporary pod storage.           | ![](https://img.shields.io/badge/EmptyDir-lightgrey)     |
| HostPath         | Host filesystem path.            | ![](https://img.shields.io/badge/HostPath-yellow)        |
| ConfigMap Volume | Mount config as files.           | ![](https://img.shields.io/badge/ConfigMap--Volume-blue) |
| Secret Volume    | Mount secrets as files.          | ![](https://img.shields.io/badge/Secret--Volume-red)     |
| PersistentVolume | Actual storage resource.         | ![](https://img.shields.io/badge/PV-green)               |
| PVC              | Requests for persistent storage. | ![](https://img.shields.io/badge/PVC-brightgreen)        |
| StorageClass     | Defines storage provisioning.    | ![](https://img.shields.io/badge/StorageClass-purple)    |
| CSI Volume       | Storage plugin system.           | ![](https://img.shields.io/badge/CSI--Volume-orange)     |

---

# **🔐 Security** ![badge](https://img.shields.io/badge/Category-Security-red)

| Concept               | Definition                       | Badge                                                            |
| --------------------- | -------------------------------- | ---------------------------------------------------------------- |
| RBAC                  | Access control system.           | ![](https://img.shields.io/badge/RBAC-blue)                      |
| Role / ClusterRole    | Permissions (namespace/cluster). | ![](https://img.shields.io/badge/Roles-yellow)                   |
| RoleBinding           | Assigns roles.                   | ![](https://img.shields.io/badge/RoleBinding-green)              |
| ServiceAccount        | Pod-level identity.              | ![](https://img.shields.io/badge/ServiceAccount-orange)          |
| SecurityContext       | Security rules for pods.         | ![](https://img.shields.io/badge/SecurityContext-red)            |
| PodSecurity Standards | Restricted/baseline/privileged.  | ![](https://img.shields.io/badge/PodSecurity-purple)             |
| Admission Controller  | Validates/Mutates requests.      | ![](https://img.shields.io/badge/AdmissionController-blueviolet) |

---

# **🧭 Scheduling** ![badge](https://img.shields.io/badge/Category-Scheduling-lightgreen)

| Concept              | Definition                      | Badge                                                             |
| -------------------- | ------------------------------- | ----------------------------------------------------------------- |
| Scheduler            | Assigns pods to nodes.          | ![](https://img.shields.io/badge/Scheduler-blue)                  |
| NodeSelector         | Simple node matching.           | ![](https://img.shields.io/badge/NodeSelector-grey)               |
| Node Affinity        | Advanced node placement.        | ![](https://img.shields.io/badge/NodeAffinity-yellow)             |
| Pod Affinity         | Group pods together.            | ![](https://img.shields.io/badge/PodAffinity-green)               |
| Pod Anti-Affinity    | Spread pods apart.              | ![](https://img.shields.io/badge/PodAntiAffinity-red)             |
| Taints & Tolerations | Controls pod placement.         | ![](https://img.shields.io/badge/Taints%20&%20Tolerations-purple) |
| Topology Spread      | Even distribution across nodes. | ![](https://img.shields.io/badge/TopologySpread-lightblue)        |

---

# **📈 Scaling & Availability** ![badge](https://img.shields.io/badge/Category-Scaling-yellow)

| Concept            | Definition               | Badge                                                    |
| ------------------ | ------------------------ | -------------------------------------------------------- |
| HPA                | Auto-scales pods.        | ![](https://img.shields.io/badge/HPA-brightgreen)        |
| VPA                | Adjusts CPU/memory.      | ![](https://img.shields.io/badge/VPA-green)              |
| Cluster Autoscaler | Adds/removes nodes.      | ![](https://img.shields.io/badge/ClusterAutoscaler-blue) |
| Liveness Probe     | Checks container health. | ![](https://img.shields.io/badge/LivenessProbe-red)      |
| Readiness Probe    | Ready for traffic?       | ![](https://img.shields.io/badge/ReadinessProbe-yellow)  |
| Startup Probe      | Checks startup complete. | ![](https://img.shields.io/badge/StartupProbe-orange)    |

---

# **📊 Observability** ![badge](https://img.shields.io/badge/Category-Observability-blue)

| Concept        | Definition                 | Badge                                                 |
| -------------- | -------------------------- | ----------------------------------------------------- |
| Logs           | Container output.          | ![](https://img.shields.io/badge/Logs-grey)           |
| Events         | Cluster alerts/warnings.   | ![](https://img.shields.io/badge/Events-yellow)       |
| Metrics Server | Resource metrics provider. | ![](https://img.shields.io/badge/MetricsServer-green) |
| Prometheus     | Monitoring/alerting.       | ![](https://img.shields.io/badge/Prometheus-orange)   |
| Grafana        | Metrics dashboards.        | ![](https://img.shields.io/badge/Grafana-lightblue)   |

---

# **📦 Deployment & Packaging** ![badge](https://img.shields.io/badge/Category-Packaging-purple)

| Concept       | Definition                  | Badge                                             |
| ------------- | --------------------------- | ------------------------------------------------- |
| Helm          | Kubernetes package manager. | ![](https://img.shields.io/badge/Helm-blue)       |
| Kustomize     | YAML customization tool.    | ![](https://img.shields.io/badge/Kustomize-green) |
| YAML Manifest | Declarative config file.    | ![](https://img.shields.io/badge/Manifest-grey)   |
| CRD           | Custom resource type.       | ![](https://img.shields.io/badge/CRD-orange)      |
| Operator      | App lifecycle automation.   | ![](https://img.shields.io/badge/Operator-red)    |

---

# **🛠️ Cluster Administration** ![badge](https://img.shields.io/badge/Category-Administration-black)

| Concept       | Definition              | Badge                                                   |
| ------------- | ----------------------- | ------------------------------------------------------- |
| Kubeadm       | Cluster setup tool.     | ![](https://img.shields.io/badge/Kubeadm-blue)          |
| Etcd          | Cluster state database. | ![](https://img.shields.io/badge/Etcd-green)            |
| Namespace     | Resource isolation.     | ![](https://img.shields.io/badge/Namespace-yellow)      |
| ResourceQuota | Namespace limits.       | ![](https://img.shields.io/badge/ResourceQuota-orange)  |
| LimitRange    | Default limit/req.      | ![](https://img.shields.io/badge/LimitRange-red)        |
| Certificates  | TLS security.           | ![](https://img.shields.io/badge/Certificate-lightgrey) |

---

# **🔗 Service Mesh** ![badge](https://img.shields.io/badge/Category-ServiceMesh-teal)

| Concept | Definition                       | Badge                                            |
| ------- | -------------------------------- | ------------------------------------------------ |
| Istio   | Full-featured service mesh.      | ![](https://img.shields.io/badge/Istio-blue)     |
| Linkerd | Lightweight mesh.                | ![](https://img.shields.io/badge/Linkerd-green)  |
| Envoy   | Sidecar proxy.                   | ![](https://img.shields.io/badge/Envoy-purple)   |
| Sidecar | Helper container.                | ![](https://img.shields.io/badge/Sidecar-orange) |
| mTLS    | Encrypted service communication. | ![](https://img.shields.io/badge/mTLS-red)       |

---

# **☁️ Cloud Integrations** ![badge](https://img.shields.io/badge/Category-CloudIntegration-blue)

| Concept | Definition        | Badge                                           |
| ------- | ----------------- | ----------------------------------------------- |
| CNI     | Network plugin.   | ![](https://img.shields.io/badge/CNI-lightblue) |
| CSI     | Storage plugin.   | ![](https://img.shields.io/badge/CSI-green)     |
| CCM     | Cloud controller. | ![](https://img.shields.io/badge/CCM-yellow)    |

---




