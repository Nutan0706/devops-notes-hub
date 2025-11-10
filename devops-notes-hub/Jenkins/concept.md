# 🧩 Jenkins – Complete Concepts Sheet

**Jenkins** is an open-source **CI/CD automation server** that helps automate the **build, test, and deploy** lifecycle.

* Automates build, test, and deployment processes
* Highly extensible via plugins
* Supports pipelines, webhooks, and integrations
* Provides both GUI and **Jenkinsfile-as-Code** approach

---

## 📍 1️⃣ Jenkins Core Concepts

| Concept                  | Description                                             |
| ------------------------ | ------------------------------------------------------- |
| **Job / Project**        | A unit of work (Freestyle, Pipeline, Multibranch, etc.) |
| **Build**                | A single execution of a job                             |
| **Node / Agent / Slave** | A machine where builds run                              |
| **Master / Controller**  | Orchestrates jobs & stores configurations               |
| **Executor**             | Slot to run builds on a node                            |
| **Workspace**            | Directory where Jenkins checks out and builds code      |
| **Pipeline**             | CI/CD workflow written using Groovy syntax              |

💡 Jenkins Controller manages scheduling, while Agents execute builds.

---

## 🧱 2️⃣ Types of Jobs

| Job Type                 | Description                                       |
| ------------------------ | ------------------------------------------------- |
| **Freestyle Project**    | Basic, UI-driven job configuration                |
| **Pipeline Project**     | CI/CD workflow as code using `Jenkinsfile`        |
| **Multibranch Pipeline** | Automatically discovers branches & runs pipelines |
| **Folder**               | Used for grouping related jobs or pipelines       |

---

## 🚀 3️⃣ Pipeline Basics

| Term                     | Meaning                                         |
| ------------------------ | ----------------------------------------------- |
| **Declarative Pipeline** | Simple, structured syntax (recommended)         |
| **Scripted Pipeline**    | Flexible, Groovy-based custom logic             |
| **Stages**               | Logical blocks of work (Build, Test, Deploy)    |
| **Steps**                | Smallest task (e.g., `echo`, `sh`, `checkout`)  |
| **Agent**                | Defines where the pipeline will run             |
| **Post**                 | Runs after stage (e.g., cleanup, notifications) |

💡 Always start pipelines with `pipeline { agent any }`.

---

## 🔌 4️⃣ Important Jenkins Plugins

| Plugin                         | Purpose                             |
| ------------------------------ | ----------------------------------- |
| **Git Plugin**                 | Integrates with Git, GitHub, GitLab |
| **Pipeline Plugin**            | Enables Pipeline-as-Code            |
| **Blue Ocean**                 | Modern UI for pipelines             |
| **Credentials Plugin**         | Manage secrets securely             |
| **Docker Plugin**              | Build & run containers              |
| **Slack Plugin**               | Send build notifications            |
| **Email Extension Plugin**     | Custom email alerts                 |
| **NodeLabel Parameter Plugin** | Run jobs on specific labeled agents |

💡 Keep plugins updated regularly — outdated ones cause build instability.

---

## ⏱️ 5️⃣ Build Triggers

| Trigger            | Description                                        |
| ------------------ | -------------------------------------------------- |
| **SCM Polling**    | Periodically polls repo for changes                |
| **Webhook**        | Triggered on code push (GitHub, GitLab, Bitbucket) |
| **Timer (CRON)**   | Scheduled builds (e.g., nightly builds)            |
| **Manual Trigger** | Build started by a user from UI or API             |

💡 Use **webhooks** for real-time CI/CD instead of polling.

---

## 🌐 6️⃣ Distributed Builds (Master-Agent Setup)

* **Master (Controller)** handles scheduling and coordination
* **Agents** execute builds and tests
* Agents can be configured via:

  * SSH
  * JNLP (Java Network Launch Protocol)
  * Docker agents
  * Kubernetes plugin

💡 Best practice: **Run no builds on the master**, use agents for isolation and scalability.

---

## 🧠 7️⃣ Jenkins Pipeline Best Practices

✅ Keep Jenkinsfile version-controlled in the repo
✅ Use **Declarative syntax** for readability
✅ Use **parallel stages** for faster execution
✅ Clean workspace after every build using `cleanWs()`
✅ Use `agent none` and define agents per stage to optimize resources
✅ Send notifications on build failures (Slack, email)
✅ Use **parameters** to control deployment environments

💡 Example:

```groovy
pipeline {
  agent any
  stages {
    stage('Build') { steps { sh 'mvn clean package' } }
    stage('Deploy') { steps { sh './deploy.sh' } }
  }
  post {
    failure { mail to: 'dev-team@company.com', subject: 'Build Failed' }
  }
}
```

---

## 🔐 8️⃣ Jenkins Security

| Security Feature               | Description                                |
| ------------------------------ | ------------------------------------------ |
| **Matrix Authorization**       | Fine-grained user and role access          |
| **Role-Based Strategy Plugin** | Role-based access control                  |
| **HTTPS / Reverse Proxy**      | Secure Jenkins interface                   |
| **Run as Non-Root**            | Minimizes privilege exposure               |
| **Credential Rotation**        | Regularly rotate access tokens and secrets |
| **Script Approval**            | Review Groovy scripts before execution     |

💡 Enforce **Least Privilege Access** for all Jenkins users.

---

## 🗄️ 9️⃣ Backup & Restore

| Item                      | Backup Location / Method                 |
| ------------------------- | ---------------------------------------- |
| **Jenkins Config**        | `$JENKINS_HOME/config.xml`               |
| **Jobs & Pipelines**      | `$JENKINS_HOME/jobs/`                    |
| **Plugins**               | `$JENKINS_HOME/plugins/`                 |
| **Credentials & Secrets** | `$JENKINS_HOME/secrets/`                 |
| **Full Backup**           | Backup entire `$JENKINS_HOME` folder     |
| **Tools**                 | ThinBackup plugin or SCM version control |

💡 Back up **before Jenkins upgrades** or plugin updates.

---

## 🧯 🔟 Jenkins Troubleshooting Guide

| Issue                    | Check                                      |
| ------------------------ | ------------------------------------------ |
| **Stuck Builds**         | Agent availability, labels, executors      |
| **SCM Checkout Failure** | Repo URL, branch name, credentials         |
| **Missing Env Vars**     | Print with `echo env`                      |
| **Workspace Conflicts**  | Use `cleanWs()` before build               |
| **Disk Full / Slow**     | Rotate old builds, enable cleanup policies |

💡 Always monitor **build queue** and **system logs** at `/var/log/jenkins/jenkins.log`.

---

## 📂 1️⃣1️⃣ Jenkins Directory Structure

```bash
/var/lib/jenkins/jobs/           # All jobs and pipeline definitions
/var/lib/jenkins/nodes/          # Agent/slave configurations
/var/lib/jenkins/users/          # User configuration files
/var/lib/jenkins/plugins/        # Installed plugins (.hpi files)
/var/lib/jenkins/secrets/        # Secret keys and credentials
/var/lib/jenkins/workspace/      # Job workspaces
/var/lib/jenkins/logs/           # System and job logs
/var/lib/jenkins/config.xml      # Main Jenkins configuration file
```

💡 `$JENKINS_HOME` = the heart of Jenkins — back it up frequently!

---

## 🧩 Bonus Section – Jenkins Key Advantages

| Category          | Benefit                                 |
| ----------------- | --------------------------------------- |
| **Automation**    | End-to-end CI/CD                        |
| **Extensibility** | 1,800+ plugins available                |
| **Integration**   | Works with Git, Docker, AWS, Kubernetes |
| **Scalability**   | Distributed build agents                |
| **Flexibility**   | Pipelines as code with Groovy           |
| **Observability** | Real-time build monitoring & reporting  |

---

✅ **Final Tips for Interviews**

* Jenkins = “**CI/CD Engine**” of your DevOps pipeline.
* Focus on **Pipelines, Agents, Plugins, and Security**.
* Be ready to explain **Declarative vs Scripted**, **Webhook setup**, and **Jenkinsfile design**.
* Expect a **hands-on question**: write a 3-stage Jenkinsfile (Build → Test → Deploy).
* Mention **Jenkins + Docker + Kubernetes integration** for modern pipelines.
