# 🧭 AWS S3 Cross-Region Replication (CRR) — Step-by-Step Guide

Replicate objects automatically from a **source** S3 bucket in one AWS region to a **destination** bucket in another region for **disaster recovery** and **low-latency access**.

---

## 📦 Prerequisites

* AWS CLI configured with credentials that can create S3 and IAM resources (`aws configure`).
* Permissions: `s3:*` (or scoped permissions for buckets/policies), `iam:*` (or scoped for roles/policies).
* Two regions chosen (e.g., `ap-south-1` → `eu-west-1`).
* (Optional) KMS CMKs ready if you use SSE-KMS at source/destination.

> 💡 **Tip:** CRR requires **Versioning** enabled on both buckets. If you use **SSE-KMS**, grant the replication role permissions on both KMS keys.

---

## 🔧 Variables (set once)

Create a shell section in your terminal to reuse names.

```bash
# ====== EDIT THESE ======
SRC_REGION="ap-south-1"
DST_REGION="eu-west-1"
SRC_BUCKET="my-crr-src-$(date +%Y%m%d%H%M%S)"
DST_BUCKET="my-crr-dst-$(date +%Y%m%d%H%M%S)"
ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
REPL_ROLE_NAME="S3CRRRole"
REPL_ROLE_ARN="arn:aws:iam::${ACCOUNT_ID}:role/${REPL_ROLE_NAME}"
# If using KMS, set these (CMK ARNs) or leave blank for SSE-S3
SRC_KMS_ARN=""
DST_KMS_ARN=""
```

> ✅ **Note:** Bucket names must be globally unique. Using a timestamp helps avoid collisions.

<!-- Add snapshot here -->

---

## Step 1 — Create Source & Destination Buckets (Different Regions)

```bash
aws s3api create-bucket \
  --bucket "$SRC_BUCKET" \
  --region "$SRC_REGION" \
  --create-bucket-configuration LocationConstraint="$SRC_REGION"

aws s3api create-bucket \
  --bucket "$DST_BUCKET" \
  --region "$DST_REGION" \
  --create-bucket-configuration LocationConstraint="$DST_REGION"
```

> 💡 **Tip:** `us-east-1` is the only region where `--create-bucket-configuration` is *not* required. For all other regions, include it.

<!-- Add snapshot here -->

---

## Step 2 — Enforce Bucket Ownership & Disable ACLs (Recommended)

Object Ownership `BucketOwnerEnforced` disables ACLs and simplifies cross-account scenarios.

```bash
aws s3api put-bucket-ownership-controls \
  --bucket "$SRC_BUCKET" \
  --ownership-controls 'Rules=[{ObjectOwnership=BucketOwnerEnforced}]'

aws s3api put-bucket-ownership-controls \
  --bucket "$DST_BUCKET" \
  --ownership-controls 'Rules=[{ObjectOwnership=BucketOwnerEnforced}]'
```

> ✅ **Note:** If your org still relies on ACLs, skip this step. Using `BucketOwnerEnforced` is the modern best practice.

<!-- Add snapshot here -->

---

## Step 3 — Enable Versioning on Both Buckets (Required)

```bash
aws s3api put-bucket-versioning \
  --bucket "$SRC_BUCKET" \
  --versioning-configuration Status=Enabled

aws s3api put-bucket-versioning \
  --bucket "$DST_BUCKET" \
  --versioning-configuration Status=Enabled
```

> ✅ **Note:** Replication only works for **new** objects after enabling the rule. Use **Batch Operations** for retroactive copy if needed.

<!-- Add snapshot here -->

---

## Step 4 — Create the IAM Role for Replication

S3 assumes this role to replicate from source to destination.

### 4.1 Trust Policy (allow S3 to assume the role)

```bash
cat > trust-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "s3.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
JSON

aws iam create-role \
  --role-name "$REPL_ROLE_NAME" \
  --assume-role-policy-document file://trust-policy.json
```

### 4.2 Permissions Policy (minimal required)

```bash
cat > repl-policy.json <<JSON
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SourceRead",
      "Effect": "Allow",
      "Action": [
        "s3:GetReplicationConfiguration",
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::${SRC_BUCKET}"
    },
    {
      "Sid": "SourceObjectRead",
      "Effect": "Allow",
      "Action": [
        "s3:GetObjectVersion",
        "s3:GetObjectVersionAcl",
        "s3:GetObjectVersionForReplication",
        "s3:GetObjectLegalHold",
        "s3:GetObjectRetention",
        "s3:GetObjectVersionTagging"
      ],
      "Resource": "arn:aws:s3:::${SRC_BUCKET}/*"
    },
    {
      "Sid": "DestinationWrite",
      "Effect": "Allow",
      "Action": [
        "s3:ReplicateObject",
        "s3:ReplicateDelete",
        "s3:ReplicateTags",
        "s3:ObjectOwnerOverrideToBucketOwner",
        "s3:PutObjectLegalHold",
        "s3:PutObjectRetention",
        "s3:PutBucketVersioning",
        "s3:PutBucketTagging"
      ],
      "Resource": [
        "arn:aws:s3:::${DST_BUCKET}",
        "arn:aws:s3:::${DST_BUCKET}/*"
      ]
    }
  ]
}
JSON

aws iam put-role-policy \
  --role-name "$REPL_ROLE_NAME" \
  --policy-name S3CRRInlinePolicy \
  --policy-document file://repl-policy.json
```

> 💡 **Tip:** If using **SSE-KMS**, add `kms:Decrypt`, `kms:Encrypt`, and `kms:ReEncrypt*` for the source/destination keys and update the KMS key policies to trust the role.

<!-- Add snapshot here -->

---

## Step 5 — Destination Bucket Policy (allow the role to replicate)

```bash
cat > dst-bucket-policy.json <<JSON
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowReplicationFromSourceAccount",
      "Effect": "Allow",
      "Principal": {"AWS": "${REPL_ROLE_ARN}"},
      "Action": [
        "s3:ReplicateObject",
        "s3:ReplicateDelete",
        "s3:ReplicateTags",
        "s3:ObjectOwnerOverrideToBucketOwner"
      ],
      "Resource": [
        "arn:aws:s3:::${DST_BUCKET}/*"
      ]
    }
  ]
}
JSON

aws s3api put-bucket-policy \
  --bucket "$DST_BUCKET" \
  --policy file://dst-bucket-policy.json
```

> ✅ **Note:** This is needed especially for **cross-account** replication. For same-account, permissions are still recommended and harmless.

<!-- Add snapshot here -->

---

## Step 6 — (Optional) KMS Key Policies for CRR

If you use **SSE-KMS** at source and/or destination, ensure your KMS key policies allow the replication role.

```bash
# Example policy snippet to merge into your CMK policy (source and destination keys)
cat > kms-repl-snippet.json <<'JSON'
{
  "Sid": "AllowS3ReplicationRole",
  "Effect": "Allow",
  "Principal": { "AWS": "${REPL_ROLE_ARN}" },
  "Action": [
    "kms:Encrypt", "kms:Decrypt", "kms:ReEncrypt*", "kms:GenerateDataKey*", "kms:DescribeKey"
  ],
  "Resource": "*"
}
JSON
```

> 💡 **Tip:** When both buckets use SSE-S3 (default AES-256), you don’t need KMS permissions. For KMS, reference the key ARNs in the replication rule.

<!-- Add snapshot here -->

---

## Step 7 — Create the Replication Configuration (JSON)

```bash
cat > repl-config.json <<JSON
{
  "Role": "${REPL_ROLE_ARN}",
  "Rules": [
    {
      "ID": "replicate-all-objects",
      "Priority": 1,
      "Status": "Enabled",
      "DeleteMarkerReplication": {"Status": "Enabled"},
      "Filter": {},
      "Destination": {
        "Bucket": "arn:aws:s3:::${DST_BUCKET}",
        "Account": "${ACCOUNT_ID}"$([ -n "$DST_KMS_ARN" ] && echo ",\n        \"EncryptionConfiguration\": { \"ReplicaKmsKeyID\": \"${DST_KMS_ARN}\" }")
      }$([ -n "$SRC_KMS_ARN" ] && echo ",\n      \"SourceSelectionCriteria\": { \"SseKmsEncryptedObjects\": { \"Status\": \"Enabled\" } }")
    }
  ]
}
JSON

aws s3api put-bucket-replication \
  --bucket "$SRC_BUCKET" \
  --replication-configuration file://repl-config.json
```

> ✅ **Note:** Use `Filter` to limit replication to a prefix or tag. Above, an empty filter means **replicate everything**.

<!-- Add snapshot here -->

---

## Step 8 — Validate Replication (Upload & Check)

```bash
# Upload a test file to the source bucket
TEST_FILE="hello-$(date +%s).txt"
echo "hello from $SRC_BUCKET" > "$TEST_FILE"

aws s3 cp "$TEST_FILE" "s3://${SRC_BUCKET}/demo/${TEST_FILE}"

# Wait a few seconds, then list in destination bucket
aws s3 ls "s3://${DST_BUCKET}/demo/" --region "$DST_REGION"
```

> 💡 **Tip:** Replication is asynchronous. If you don’t see the object after ~1–2 minutes, re-check role/policies, versioning, and KMS permissions.

<!-- Add snapshot here -->

---

## Step 9 — Monitor & Audit

```bash
# Get replication status on the source bucket
aws s3api get-bucket-replication --bucket "$SRC_BUCKET"

# (Optional) Enable S3 Inventory for replication reports (via Console or CLI)
```

> ✅ **Note:** For ongoing visibility, enable **Amazon S3 Inventory** (with replication status) and set up **CloudWatch** metrics/alarms for replication failures.

<!-- Add snapshot here -->

---

## Step 10 — DR Readiness Checklist (Recommended)

* Document **RTO/RPO** assumptions for S3 object replication.
* Ensure critical prefixes are included in the rule.
* Test access patterns (applications reading from the destination region).
* If using KMS, verify application IAM roles can **Decrypt** in the destination region.
* Consider **S3 Multi-Region Access Points (MRAP)** for global read/write with automated routing.

<!-- Add snapshot here -->

---

## Step 11 — (Optional) Replicate Specific Prefix or Tags Only

```bash
cat > repl-config-prefix.json <<JSON
{
  "Role": "${REPL_ROLE_ARN}",
  "Rules": [
    {
      "ID": "replicate-logs-prefix",
      "Priority": 1,
      "Status": "Enabled",
      "Filter": { "Prefix": "logs/" },
      "Destination": { "Bucket": "arn:aws:s3:::${DST_BUCKET}" }
    }
  ]
}
JSON

aws s3api put-bucket-replication \
  --bucket "$SRC_BUCKET" \
  --replication-configuration file://repl-config-prefix.json
```

> 💡 **Tip:** Use **tag-based** filtering for fine-grained control when multiple teams share a bucket.

<!-- Add snapshot here -->

---

## Step 12 — Troubleshooting Common Errors

* **`AccessControlListNotSupported` when setting ACLs** → You likely enabled `BucketOwnerEnforced`. Avoid ACL commands; use policies or roles.
* **`AccessDenied` in replication** → Verify destination bucket policy allows the replication role and (if KMS) that key policies include the role.
* **Objects not replicating** → Check that the object was created **after** the rule; confirm filters; confirm versioning enabled on both.
* **KMS-related failures** → Add `kms:Decrypt` on source CMK and `kms:Encrypt`/`kms:ReEncrypt*` on destination CMK for the role; update key policies.
* **Cross-account setup** → Use destination bucket policy with the replication role ARN from the **source account**.

<!-- Add snapshot here -->

---

## Step 13 — Clean Up (Avoid Charges)

```bash
# Remove replication config first
aws s3api delete-bucket-replication --bucket "$SRC_BUCKET"

# Empty and delete destination bucket (must remove versions)
aws s3api list-object-versions --bucket "$DST_BUCKET" --query "Versions[].{Key:Key,VersionId:VersionId}" --output text \
| awk '{print $1,$2}' \
| while read k v; do aws s3api delete-object --bucket "$DST_BUCKET" --key "$k" --version-id "$v"; done

aws s3api delete-bucket --bucket "$DST_BUCKET" --region "$DST_REGION"

# Empty and delete source bucket
aws s3api list-object-versions --bucket "$SRC_BUCKET" --query "Versions[].{Key:Key,VersionId:VersionId}" --output text \
| awk '{print $1,$2}' \
| while read k v; do aws s3api delete-object --bucket "$SRC_BUCKET" --key "$k" --version-id "$v"; done

aws s3api delete-bucket --bucket "$SRC_BUCKET" --region "$SRC_REGION"

# (Optional) Delete IAM role
aws iam delete-role-policy --role-name "$REPL_ROLE_NAME" --policy-name S3CRRInlinePolicy || true
aws iam delete-role --role-name "$REPL_ROLE_NAME" || true
```

> ✅ **Note:** Deleting versioned buckets requires removing **all versions** and **delete markers**. The loops above handle versions; add similar loops for delete markers if present.

<!-- Add snapshot here -->

---

## 📚 Appendix — Useful One-Liners

**Show bucket locations**

```bash
aws s3api get-bucket-location --bucket "$SRC_BUCKET"
aws s3api get-bucket-location --bucket "$DST_BUCKET"
```

**Check object replication status (object metadata)**

```bash
aws s3api head-object --bucket "$DST_BUCKET" --key "demo/${TEST_FILE}" \
  --query 'ReplicationStatus'
```

**Add tag-based filter example**

```json
"Filter": {
  "Tag": {"Key": "replicate", "Value": "true"}
}
```

**Add delete marker replication**

```json
"DeleteMarkerReplication": {"Status": "Enabled"}
```

---

## ✅ Summary

1. Create buckets in different regions.
2. Enforce ownership (no ACLs) and enable versioning.
3. Create an IAM role and attach minimal permissions.
4. Grant the destination bucket policy access to that role.
5. (Optional) Configure KMS key policies.
6. Apply replication rule and validate with a test upload.
7. Monitor with S3 Inventory/CloudWatch. Clean up when done.

> 💡 **Tip:** Commit this `.md` to your repo as `s3-crr-setup.md`. As your environment evolves, parameterize with tools like **Make**, **Terraform**, or **AWS CDK** for repeatability.

