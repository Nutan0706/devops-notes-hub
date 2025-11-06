# 🚀 Kubernetes Practical Learning Journey

Welcome to my **Kubernetes Practical Learning Repository** 👨‍💻  
This repo is focused purely on **hands-on, real-world Kubernetes labs** — categorized into **Beginner**, **Intermediate**, and **Advanced** levels.  

Whether you're preparing for **CKA/CKAD exams**, brushing up for a **DevOps interview**, or learning Kubernetes for **production deployments**, this guide will help you **learn by doing** 💪

---

## 🧩 Beginner Level Practicals (Core Concepts)

These labs cover **fundamental Kubernetes building blocks** — Pods, Deployments, Services, ConfigMaps, etc.  
Goal: Build a strong base and understand how Kubernetes objects interact.

| No. | Practical | Concepts Covered |
|-----|------------|------------------|
| 1️⃣ | **Create Your First Pod** | Understand YAML basics, Pod lifecycle, and `kubectl` commands. |
| 2️⃣ | **Create a Deployment and Scale It** | Learn about ReplicaSets, rolling updates, and scaling replicas. |
| 3️⃣ | **Expose Pods using Services** | Understand ClusterIP, NodePort, and LoadBalancer types. |
| 4️⃣ | **Use Namespaces for Isolation** | Create and manage multiple namespaces to separate environments. |
| 5️⃣ | **Work with ConfigMaps and Secrets** | Externalize configuration and manage sensitive data. |
| 6️⃣ | **Create Liveness and Readiness Probes** | Ensure containers are healthy and ready to serve traffic. |
| 7️⃣ | **Use Labels, Selectors, and Annotations** | Organize and query resources effectively. |
| 8️⃣ | **Deploy a Simple NGINX App** | Create Deployment + Service for a web app and test it. |
| 9️⃣ | **Use kubectl Explain, Get, Describe** | Explore the Kubernetes API objects and metadata in detail. |
| 🔟 | **Understand Pod Scheduling and Node Selector** | Learn how Kubernetes decides where to place pods. |

🧠 **Outcome:** You’ll understand the entire flow from Pod → Deployment → Service and gain comfort using `kubectl` and YAML.

---

## ⚙️ Intermediate Level Practicals (Deep Dive)

Now we move toward **real-world scenarios** — resource management, storage, monitoring, and RBAC.

| No. | Practical | Concepts Covered |
|-----|------------|------------------|
| 1️⃣ | **Set Resource Requests & Limits** | Control CPU/memory usage of containers. |
| 2️⃣ | **Create Persistent Volumes and Claims** | Understand Kubernetes storage and data persistence. |
| 3️⃣ | **Configure Ingress for HTTP Routing** | Expose services with custom domains and NGINX ingress. |
| 4️⃣ | **Implement RBAC (Role-Based Access Control)** | Create Roles, RoleBindings, and ServiceAccounts. |
| 5️⃣ | **Use DaemonSets and StatefulSets** | Learn workloads for system-level and stateful applications. |
| 6️⃣ | **Perform Rolling Updates & Rollbacks** | Safely deploy new app versions with zero downtime. |
| 7️⃣ | **Manage Config Using Helm Charts** | Learn Helm basics and package an application. |
| 8️⃣ | **Monitor Cluster with Metrics Server** | Install metrics-server and view pod CPU/memory usage. |
| 9️⃣ | **Deploy CronJobs for Scheduled Tasks** | Automate jobs on schedule using Kubernetes CronJobs. |
| 🔟 | **Taint & Tolerations Lab** | Control pod placement using taints and tolerations. |

🧠 **Outcome:** You’ll understand **cluster-level configurations**, manage workloads, control access, and use **Helm** for reusable deployments.

---

## 🧠 Advanced Level Practicals (Production Scenarios)

These labs simulate **real-world Kubernetes use cases** — multi-environment setups, autoscaling, monitoring, and CI/CD integrations.

| No. | Practical | Concepts Covered |
|-----|------------|------------------|
| 1️⃣ | **Set Up a Complete Multi-Tier App (Frontend + Backend + DB)** | Deploy a full-stack app with Persistent Volumes and Ingress. |
| 2️⃣ | **Implement Horizontal Pod Autoscaling (HPA)** | Auto-scale pods based on CPU/memory metrics. |
| 3️⃣ | **Use Node Autoscaler in Cloud Cluster** | Scale nodes automatically with demand. |
| 4️⃣ | **Implement Blue-Green and Canary Deployments** | Learn advanced deployment strategies. |
| 5️⃣ | **Secure Your Cluster with Network Policies** | Control traffic flow between pods. |
| 6️⃣ | **Integrate Prometheus + Grafana for Monitoring** | Monitor pods, nodes, and visualize metrics. |
| 7️⃣ | **Centralize Logging with EFK (Elasticsearch, Fluentd, Kibana)** | Set up logging stack for cluster logs. |
| 8️⃣ | **GitOps Deployment with ArgoCD** | Automate continuous delivery using GitOps. |
| 9️⃣ | **Backup and Restore Cluster with Velero** | Learn disaster recovery best practices. |
| 🔟 | **Run Kubernetes on AWS using EKS + Terraform** | Create a production-ready Kubernetes cluster with Infrastructure as Code. |

🧠 **Outcome:** After completing these, you’ll be ready for **production-grade Kubernetes** challenges — including **autoscaling, GitOps, observability**, and **disaster recovery**.

---

## 🧭 Resources & References

- 📘 [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- 🔧 [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- 📦 [Helm Hub](https://artifacthub.io/)
- 📈 [Prometheus Docs](https://prometheus.io/docs/introduction/overview/)
- ☸️ [Kubernetes the Hard Way (by Kelsey Hightower)](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- 🎓 [CKA & CKAD Practice Labs](https://killer.sh)
