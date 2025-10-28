# 🧩 Jenkins – Complete Concepts Sheet

A structured overview of Jenkins with collapsible sections, tables, and visuals for easy GitHub reading.

---

## ✅ What is Jenkins?

> **Jenkins** is an open-source **CI/CD automation server** that helps automate **build, test, and deploy** workflows.

- Automates builds, testing & deployments  
- Highly extensible via plugins  
- Supports Pipelines, Webhooks & Integrations  
- Provides UI + Jenkinsfile as Code  

---

<details>
<summary><strong>📍 1. Jenkins Core Concepts</strong></summary>

| Concept | Description |
|---------|--------------|
| Job / Project | A unit of work (Freestyle, Pipeline, Multibranch, etc.) |
| Build | A single execution of a job |
| Node / Agent / Slave | A machine where builds run |
| Master / Controller | Orchestrates jobs & stores configurations |
| Executor | Slot to run builds on a node |
| Workspace | Directory where Jenkins checks out and builds code |
| Pipeline | CI/CD workflow written using Groovy |

</details>

---

<details>
<summary><strong>🧱 2. Types of Jobs</strong></summary>

- **Freestyle Project** – Basic UI-based job configuration  
- **Pipeline Project** – CI/CD as code using Jenkinsfile  
- **Multibranch Pipeline** – Auto-detect branches & run pipelines  
- **Folder** – Organize jobs hierarchically  

</details>

---

<details>
<summary><strong>🚀 3. Pipeline Basics</strong></summary>

| Term | Meaning |
|-------|------------|
| Declarative Pipeline | Structured, simpler pipeline syntax |
| Scripted Pipeline | Full Groovy-based flexible scripting |
| Stages | Logical blocks (Build, Test, Deploy) |
| Steps | Small tasks (e.g., `echo`, `sh`) |
| Agent | Defines where the pipeline runs |
| Post | Actions after stage (e.g., cleanup) |

</details>

---

<details>
<summary><strong>🔌 4. Important Plugins</strong></summary>

- **Git Plugin** – SCM integration  
- **Pipeline Plugin** – Enables Pipeline as code  
- **Blue Ocean** – Modern UI for pipelines  
- **Credentials Plugin** – Manage secrets securely  
- **Docker Plugin** – Build & run containers  
- **Slack Plugin** – Send build notifications  
- **Email Extension Plugin** – Advanced email alerts  
- **NodeLabel Parameter Plugin** – Select specific agent to run job  

</details>

---

<details>
<summary><strong>⏱️ 5. Build Triggers</strong></summary>

| Trigger Type | Description |
|----------------|--------------------------|
| SCM Polling | Poll repository for changes |
| Webhook | Trigger on push (GitHub, GitLab, Bitbucket) |
| Timer | Scheduled builds (CRON) |
| Manual | On-demand triggered by user |

</details>

---

<details>
<summary><strong>🌐 6. Distributed Builds</strong></summary>

- **Master/Controller** → Only orchestrates  
- **Agents/Slaves** → Run builds  
- Setup agents using:  
  ✅ SSH  
  ✅ JNLP  
  ✅ Docker Agents  
  ✅ Kubernetes Plugin  

</details>

---

<details>
<summary><strong>🧠 7. Pipeline Best Practices</strong></summary>

- Keep pipeline code in **Jenkinsfile** (Version-controlled)  
- Prefer **Declarative pipelines**  
- Use **stages + parallel steps**  
- Clean workspace after builds  
- Use `agent none` and define agent per stage for optimization  
- Send notifications on failure  
- Parameterize builds when useful  

</details>

---

<details>
<summary><strong>🔐 8. Jenkins Security</strong></summary>

- Enable **Matrix Authorization**  
- Use **Role-based strategy plugin**  
- Run Jenkins as **non-root**  
- Enforce **HTTPS**  
- Rotate secrets & credentials  
- Restrict script approvals  

</details>

---

<details>
<summary><strong>🗄️ 9. Backup & Restore</strong></summary>

| Item | Backup Location |
|--------|----------------|
| Jenkins Config | `$JENKINS_HOME` |
| Jobs & Pipelines | In SCM + `$JENKINS_HOME/jobs` |
| Plugins | Keep plugin list + backup `.hpi` files |
| Full backup | Copy entire `$JENKINS_HOME` |
| Tools | ThinBackup / SCM versioning |

</details>

---

<details>
<summary><strong>🧯 10. Troubleshooting Guide</strong></summary>

| Issue | Check |
|--------|---------|
| Stuck builds | Agent availability, queue, labels |
| SCM checkout failure | Repo URL, credentials |
| Missing env vars | Print using `echo env` |
| Workspace conflicts | Use `cleanWs()` |
| Disk full | Rotate builds & workspace cleanup |

</details>

---

<details>
<summary><strong>📂 11. Jenkins Directory Structure</strong></summary>

```bash
/var/lib/jenkins/jobs/           # all jobs/pipelines
/var/lib/jenkins/nodes/          # all agent/slave nodes
/var/lib/jenkins/users/          # user configs
/var/lib/jenkins/plugins/        # plugins .hpi files
/var/lib/jenkins/secrets/        # secret keys, credentials store
/var/lib/jenkins/workspace/      # job build workspaces
/var/lib/jenkins/logs/           # controller logs
/var/lib/jenkins/config.xml      # main Jenkins config
```
</details>
