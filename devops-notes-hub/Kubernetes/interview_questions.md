# ☸️ Kubernetes Interview Questions

> A structured collection of **30 Kubernetes interview questions** divided into three levels —  
> Commonly Asked 🔹 Moderate 🔸 Advanced & Scenario-based 🚀  

---

## 🧩 Table of Contents
- [Commonly Asked Questions](#commonly-asked-questions)
- [Moderate Level Questions](#moderate-level-questions)
- [Advanced & Scenario-Based Questions](#advanced--scenario-based-questions)

---

<details>
<summary><strong>🔹 Commonly Asked Questions (Beginner Level)</strong></summary>

| No. | Question | Key Focus Area |
|-----|-----------|----------------|
| 1 | What is Kubernetes and why is it used? | Core concept, container orchestration |
| 2 | What is the difference between Docker and Kubernetes? | Container vs Orchestrator |
| 3 | Explain the role of the API Server in Kubernetes. | Control Plane Component |
| 4 | What is a Pod? | Smallest deployable unit |
| 5 | Difference between ReplicaSet and Deployment? | Object management & versioning |
| 6 | What is a Service in Kubernetes? | Networking abstraction |
| 7 | What is a Namespace? | Logical separation |
| 8 | What are Labels and Selectors used for? | Grouping and filtering resources |
| 9 | How do ConfigMaps differ from Secrets? | Configuration vs Sensitive data |
| 10 | What is `kubectl` and how is it used? | Kubernetes CLI |

</details>

---

<details>
<summary><strong>🔸 Moderate Level Questions</strong></summary>

| No. | Question | Key Focus Area |
|-----|-----------|----------------|
| 1 | Explain the architecture of Kubernetes. | Control Plane & Worker Nodes |
| 2 | What are DaemonSets and StatefulSets? | Workload types |
| 3 | How does a Service discover Pods internally? | DNS & kube-proxy |
| 4 | What is an Ingress Controller and why use it? | External routing |
| 5 | How does Kubernetes handle rolling updates and rollbacks? | Deployment strategies |
| 6 | What are Probes (liveness/readiness/startup)? | Health checking |
| 7 | What is a Persistent Volume (PV) and Persistent Volume Claim (PVC)? | Storage management |
| 8 | Explain the difference between ClusterIP, NodePort, and LoadBalancer services. | Networking layers |
| 9 | How does the Scheduler decide where to place a Pod? | Node selection process |
| 10 | What are Taints and Tolerations? | Node workload control |

</details>

---

<details>
<summary><strong>🚀 Advanced & Scenario-Based Questions</strong></summary>

| No. | Question | Scenario or Concept |
|-----|-----------|--------------------|
| 1 | How would you debug a CrashLoopBackOff pod? | Troubleshooting |
| 2 | How do you scale an application in Kubernetes? | HPA / VPA / Cluster Autoscaler |
| 3 | Explain how you’d secure a Kubernetes cluster. | RBAC, Network Policies, Secrets |
| 4 | Your pod is not connecting to the DB service — steps to diagnose? | Networking / DNS |
| 5 | How does Kubernetes handle multi-AZ or multi-region deployments? | HA design |
| 6 | What is the difference between Horizontal Pod Autoscaler and Cluster Autoscaler? | Scaling levels |
| 7 | How do you upgrade a Kubernetes cluster with zero downtime? | Version management |
| 8 | How do you back up and restore etcd? | Disaster recovery |
| 9 | How do Network Policies work in Kubernetes? | Security & Isolation |
| 10 | A pod uses 100% CPU constantly — how would you limit it? | Resource limits & QoS |

</details>

---

## 🧠 Quick Reference Table

| Category | Focus | Example Question |
|-----------|--------|------------------|
| Core Concepts | Basics of K8s | What is a Pod? |
| Workloads | Deployments, DaemonSets | Difference between ReplicaSet and Deployment |
| Networking | Services, Ingress | What is ClusterIP vs NodePort? |
| Storage | PV & PVC | Explain Persistent Volume |
| Security | RBAC, Secrets | How to secure a cluster? |
| Troubleshooting | Logs, Status | Debugging CrashLoopBackOff |
| Scaling | Autoscalers | Difference between HPA & Cluster Autoscaler |

---

## 📘 Pro Tip
> ✅ **Revise Commands Daily**
> ```
> kubectl get pods
> kubectl describe pod <pod-name>
> kubectl logs <pod-name>
> kubectl exec -it <pod> -- /bin/bash
> ```
> Mastering these gives 70% of real-time troubleshooting confidence.

---
