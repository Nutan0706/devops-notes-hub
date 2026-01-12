                 ┌───────────────────────────────────────────┐
                 │           USER / CLIENT / JENKINS          │
                 │  (hits URL like https://proteus.company.com)│
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │              Route53 DNS Resolve           │
                 │  proteus.company.com → ALB DNS Endpoint    │
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │         AWS Application Load Balancer      │
                 │  - HTTPS Termination                       │
                 │  - forwards request to EKS Target Group     │
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │           Kubernetes Ingress Controller    │
                 │  - host/path based routing                 │
                 │  /trigger  /status  /logs                  │
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │            Proteus Services (EKS)          │
                 │  - Proteus Trigger API                     │
                 │  - Monitoring/Status Service               │
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
        ┌───────────────────────────────────────────────────────────┐
        │   Docker Images Prepared (ECR)                              │
        │  1) Account Container       2) Bogie Container              │
        └───────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌───────────────────────────────────────────────────────────────────────────┐
│             Terraform-Provisioned AWS EKS Cluster                           │
│  - Control Plane, Node Groups, VPC, Subnets, NAT/IGW, IAM                   │
└───────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │              Warmup Jobs (EKS)             │
                 │                                           │
                 │  Job-1: Account Cache Build                │
                 │  Job-2: Bogie Cache Build                  │
                 │  (Redis/Valkey/K8s Cache)                   │
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │     Combined Account–Bogie Model Build      │
                 │  - mapping logic                            │
                 │  - tracking error, volatility               │
                 │  - covariance, risk decomposition           │
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │          Run Proteus Model on EKS           │
                 │  - pulls Account + Bogie from cache         │
                 │  - runs calculations                        │
                 │  - generates outputs                        │
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │                Write to S3                 │
                 │  /tracking_error/                           │
                 │  /volatility/                               │
                 │  /risk_components/                           │
                 │  /logs/                                      │
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │      Jenkins Post Processing Pipeline       │
                 │  1) fetch CSVs from S3                      │
                 │  2) clean/enrich/validate                   │
                 │  3) transform                               │
                 │  4) load to Oracle DB                       │
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │                 Oracle DB                  │
                 │     Intermediate enterprise datastore       │
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │   Oracle → Snowflake Sync (Scheduled ETL)  │
                 │  - extract updated datasets                 │
                 │  - load into Snowflake tables              │
                 └───────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌───────────────────────────────────────────┐
                 │                 Snowflake                  │
                 │  Reporting + Dashboards (PowerBI/Tableau)  │
                 └───────────────────────────────────────────┘
