# 📊 Grafana – Important Concepts (Cheat Sheet)

A quick and well-organized reference to understand core Grafana concepts for **Observability**, **Monitoring**, and **Dashboards**.

---

## 🚀 What is Grafana?

Grafana is an **open-source observability & analytics platform** used for **monitoring, visualization, and alerting** across logs, metrics, and traces.

---

## ✅ Core Concepts of Grafana

| Concept           | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| **Dashboard**     | Visual collection of charts, graphs & widgets                 |
| **Panel**         | A single visualization block (graph, table, gauge, logs etc.) |
| **Data Source**   | The backend from where Grafana fetches metrics/logs           |
| **Query**         | The actual data request executed against a data source        |
| **Visualization** | The chart type used to present data                           |
| **Alerting**      | Trigger notifications based on metric/log thresholds          |
| **Organization**  | Logical grouping of dashboards and permissions                |
| **Users & Teams** | Access control for collaboration                              |
| **Plugins**       | Extend Grafana with extra data sources, UI components, apps   |

---

## 📡 Supported Data Sources

Grafana supports **100+ data sources**.

| Category             | Examples                                      |
| -------------------- | --------------------------------------------- |
| **Metrics**          | Prometheus, Graphite, InfluxDB, Datadog       |
| **Logs**             | Loki, Elasticsearch, Splunk                   |
| **Traces**           | Tempo, Jaeger, Zipkin                         |
| **Cloud Monitoring** | AWS CloudWatch, GCP Monitoring, Azure Monitor |
| **Databases**        | MySQL, PostgreSQL, MongoDB, BigQuery          |
| **Others**           | GitHub, Jira, Opsgenie, ServiceNow            |

---

## 📊 Dashboard & Panels

| Component       | Description                                                   |
| --------------- | ------------------------------------------------------------- |
| **Dashboard**   | Full monitoring page with panels                              |
| **Panel**       | Single visualization (graph, heatmap, logs view, stat, gauge) |
| **Variables**   | Dynamic filters for dashboards                                |
| **Templating**  | Reuse dashboards with parameters (env, region, service etc.)  |
| **Time Picker** | Select time range for data: last 5m → 24h → custom            |

**Popular Panel Types**

* Graph
* Gauge
* Table
* Heatmap
* Logs Panel
* Alert Panel
* Bar/Line/Time-Series Chart

---

## 🧠 Queries & Transformations

| Term                | Meaning                                              |
| ------------------- | ---------------------------------------------------- |
| **Query Builder**   | GUI to build queries for the selected data source    |
| **Raw Query**       | Writing native query (PromQL, SQL, LogQL etc.)       |
| **Transformations** | Modify data after query (merge, join, group, filter) |
| **Annotations**     | Add event markers on graphs (deployments, outages)   |

**Examples**

* PromQL → `rate(http_requests_total[5m])`
* LogQL → `{app="payment"} |= "error"`

---

## 🔔 Alerting & Notifications

| Feature            | Description                                                     |
| ------------------ | --------------------------------------------------------------- |
| **Alert Rules**    | Define thresholds to trigger alerts                             |
| **Alert Manager**  | Central control for alerting                                    |
| **Contact Points** | Where alerts are sent (Email, Slack, Teams, PagerDuty, Webhook) |
| **Alert Groups**   | Group alerts by service/environment to avoid noise              |
| **Silence**        | Mute alerts during maintenance                                  |

**Example Use Cases**

* CPU > 80% for 5 min
* 500 Errors > 100 req/min
* Pod restarts > 10 per hour

---

## 🧩 Grafana Plugins

Plugins enhance Grafana's capabilities.

| Plugin Type     | Example                               |
| --------------- | ------------------------------------- |
| **Data Source** | Loki, Prometheus, MySQL               |
| **Panel**       | Pie Chart, Gauge Panel, Status Map    |
| **App**         | Kubernetes App, AWS Observability App |

Install via:
`Configuration → Plugins → Install`

---

## 🔐 Authentication, RBAC & Security

| Concept                | Description                                |
| ---------------------- | ------------------------------------------ |
| **Users, Teams, Orgs** | Manage grouping & access                   |
| **RBAC**               | Fine-grained access control                |
| **SSO Support**        | OAuth, LDAP, SAML, Azure AD, Google Auth   |
| **API Keys**           | Integrate programmatically                 |
| **Folder Permissions** | Restrict dashboard access environment-wise |

---

## 🏗️ Advanced Concepts

| Topic                         | Description                                                    |
| ----------------------------- | -------------------------------------------------------------- |
| **Provisioning**              | Automate dashboards, data sources using YAML/JSON              |
| **Folder Structure**          | Organize dashboards logically (app, env, team)                 |
| **Multi-Tenant Setup**        | Separate dashboards per team/department                        |
| **Loki + Tempo + Prom Stack** | Complete observability with logs, traces & metrics             |
| **Grafana On-prem vs Cloud**  | Cloud version includes built-in alerting & enterprise features |

---

## 🔥 Quick Visual Architecture

```
┌──────────┐
│  Users    │
└────┬─────┘
     │
Web UI / API
     │
┌────▼──────┐
│  Grafana  │
└────┬──────┘
     │
 Queries
     ▼
Data Sources (Prometheus, Loki, Tempo…)
```
