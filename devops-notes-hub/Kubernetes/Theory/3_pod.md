# 🚀 **Pod — Smallest Deployable Unit in Kubernetes**

### **Definition (simple & direct):**

**A Pod is the smallest deployable object in Kubernetes. It can contain one or multiple containers that share:**

* **Network (same IP)**
* **Storage (Volumes)**
* **Process namespace (optional)**

---

# 🔹 **Key Points to Remember**

* Pod is the basic building block of Kubernetes.
* Containers inside one pod run **together**, always scheduled on the **same node**.
* They share **localhost**, so communication is very fast.
* Pods are **ephemeral** — they get recreated, not repaired.
* For auto-scaling or auto-recovery, we use **ReplicaSet / Deployment**, not pods directly.

---

# 🔹 **When Pods have multiple containers?**

Only when they must work **together tightly**, such as:

* Sidecar container (e.g., logging)
* Ambassador container
* Adapter container

Example: **nginx + log collector container** in the same pod.
