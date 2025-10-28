# 📌 AWS IAM (Identity and Access Management)

IAM helps securely manage **users, groups, roles, and policies** to control access to AWS resources.

---

## 1️⃣ What is IAM?
- Identity & Access Management (IAM) for AWS.
- Securely manages **users, groups, roles, and policies**.
- Controls **who can access what** and **how** in AWS.

---

## 2️⃣ Core IAM Concepts

| Concept | Description |
|--------|--------------|
| **User** | Represents an individual person or application |
| **Group** | Collection of users with similar permissions |
| **Role** | Provides temporary credentials for AWS services or external users |
| **Principal** | Entity (user/role/root) making the request |
| **Root User** | AWS account owner – unlimited access |
| **Access Keys** | For programmatic access (CLI/SDK) |
| **MFA** | Multi-Factor Authentication for added security |

---

## 3️⃣ IAM Policies

| Policy Type | Description |
|-------------|--------------|
| **Managed Policy** | AWS pre-built or customer-managed (reusable) |
| **Inline Policy** | Embedded directly into a user/group/role |
| **Identity-Based Policy** | Attached to IAM users, groups, or roles |
| **Resource-Based Policy** | Attached to resources (e.g., S3, SNS, SQS) |

---

## 4️⃣ IAM Policy Elements

| Element | Description |
|---------|--------------|
| **Effect** | Allow or Deny |
| **Action** | API operations (e.g., `s3:PutObject`) |
| **Resource** | ARN of the target AWS resource |
| **Condition** | Additional rules for fine-grained control |

---

## 5️⃣ IAM Role Use Cases
- **EC2 Instance Role:** Access S3, DynamoDB, etc. without hardcoding keys.
- **Cross-Account Access:** Assume role from another AWS account.
- **Federation:** Integrate with AD, SAML, Google, Azure AD, OIDC.
- **AWS Services:** Lambda, ECS, Glue assume roles to access other AWS services.

---

## 6️⃣ IAM Best Practices
- 🔒 **Root User:** Enable MFA, lock away, never use daily.
- ✅ **Use Roles:** For EC2, Lambda, ECS instead of storing access keys.
- 🛑 **Least Privilege:** Grant only required permissions.
- 🔐 **Enable MFA** for privileged users & admins.
- ♻️ **Rotate Access Keys** regularly.
- 🧩 Use **customer-managed policies** for custom needs.
- 🕵️ **Enable CloudTrail** for IAM security auditing.
- 🧱 Use **permissions boundaries** to limit maximum allowed permissions.
- 📄 Use **IAM Access Analyzer** to detect unintended resource sharing.

---

## 7️⃣ IAM Policy Evaluation Logic
1. **Explicit Deny** overrides everything.
2. If no explicit Allow → **Implicit Deny**.
3. Multiple policies = Union of Allows (except deny wins).

---

## 8️⃣ AWS STS (Security Token Service)
- Issues **temporary security credentials**.
- Used with **roles & federated identity providers**.
- `AssumeRole` API is used for cross-account access and delegation.

---

## 9️⃣ Password & Credential Security
- Apply **Password Policy** (min length, complexity, rotate policy).
- Use **Credential Reports** to monitor unused credentials.
- Disable unused access keys.

---

## 🔟 Common IAM CLI Commands

| Task | Command |
|-------|-----------|
| List IAM users | `aws iam list-users` |
| Create IAM user | `aws iam create-user --user-name myuser` |
| Attach policy to user | `aws iam attach-user-policy --user-name myuser --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess` |
| Create role | `aws iam create-role --role-name myrole --assume-role-policy-document file://trust.json` |
| List attached user policies | `aws iam list-attached-user-policies --user-name myuser` |

---

## 🔥 Additional Important IAM Concepts (Often Missed in Interviews)

| Feature | Why It’s Important |
|---------|---------------------|
| **Permissions Boundary** | Restricts maximum permissions a role/user can have |
| **Service Control Policies (SCPs)** | Used in AWS Organizations to restrict accounts |
| **IAM Access Analyzer** | Detects public or cross-account access risks |
| **Session Policies** | Apply temporary session-time permission limits |
| **Resource Tags for IAM Conditions** | Restrict access based on tags (e.g., environment=dev) |

---
