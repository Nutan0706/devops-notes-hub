## 🧭 Helm — Kubernetes Package Manager

### 🧩 What is Helm?

Helm is a **package manager for Kubernetes** that helps you **define, install, and manage applications** using **Helm Charts**.

---

### ⚙️ Core Concepts

| Concept         | Description                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------- |
| **Chart**       | A Helm package (like a recipe) containing all Kubernetes manifests (YAML files).             |
| **Release**     | A deployed instance of a chart in a Kubernetes cluster.                                      |
| **Repository**  | A collection (like a store) of Helm charts.                                                  |
| **Values.yaml** | File to define configuration values for templates.                                           |
| **Templates**   | Kubernetes YAML files written using Go templating syntax (`{{ }}`).                          |
| **Chart.yaml**  | Metadata file describing the chart (name, version, dependencies, etc.).                      |
| **Subcharts**   | Child charts included inside a parent chart for modular deployments.                         |
| **Hooks**       | Scripts that run at certain points in a release lifecycle (e.g., pre-install, post-upgrade). |

---

### 🪄 Helm Commands

| Command                          | Description                                 |
| -------------------------------- | ------------------------------------------- |
| `helm create <chart-name>`       | Create a new Helm chart structure.          |
| `helm install <release> <chart>` | Install a chart into the cluster.           |
| `helm upgrade <release> <chart>` | Upgrade an existing release.                |
| `helm rollback <release> <rev>`  | Rollback to a previous release version.     |
| `helm list`                      | List all releases in the current namespace. |
| `helm uninstall <release>`       | Remove a release.                           |
| `helm repo add <name> <url>`     | Add a new chart repository.                 |
| `helm repo update`               | Update all repos.                           |
| `helm search repo <keyword>`     | Search for charts in repos.                 |
| `helm lint`                      | Validate chart syntax and structure.        |

---

### 🧱 Directory Structure

```
mychart/
├── Chart.yaml          # Chart metadata
├── values.yaml         # Default configuration
├── templates/          # Kubernetes manifests (templated)
│   ├── deployment.yaml
│   ├── service.yaml
│   └── _helpers.tpl
└── charts/             # Dependencies (subcharts)
```

---

### ⚡ Lifecycle

1. **helm create** → make chart skeleton
2. **helm package** → package into `.tgz`
3. **helm install** → deploy chart
4. **helm upgrade** → update version/config
5. **helm rollback** → revert changes
6. **helm uninstall** → delete release

---

### 🧩 Example Commands

```bash
# Create chart
helm create myapp

# Install chart
helm install myapp ./myapp

# Check status
helm status myapp

# Upgrade chart
helm upgrade myapp ./myapp -f custom-values.yaml

# Uninstall chart
helm uninstall myapp
```

---

### 💡 Best Practices

* Keep **values.yaml** generic and environment configs separate.
* Use **helpers.tpl** for reusable template snippets.
* Use **`helm lint`** before deploying.
* Maintain versioning in **Chart.yaml**.
* Store packaged charts in your own **Helm repo** or **GitHub Pages**.

---

### 🧠 Key Benefits

* Simplifies complex Kubernetes YAML management
* Supports version control & rollbacks
* Enables repeatable, consistent deployments
* Encourages modular and reusable chart design

