# 🧠 AWS S3 — Setup S3 Lifecycle Policy

---

## 🎯 Objective
Configure **S3 Lifecycle Rules** to automatically transition objects from **Standard → Glacier** or **delete them** after a specific number of days.

---

## 🧩 Step-by-Step Guide

### Step 1: Open S3 Console and Select Your Bucket
1. Go to **AWS Management Console → S3 → Buckets**.  
2. Select the bucket for which you want to create the lifecycle rule (e.g., `my-lifecycle-demo-bucket`).
3. Click on the **Management** tab.

<!-- Add snapshot here -->

> 💡 **Tip:** Lifecycle rules help automate storage cost optimization by moving infrequently accessed data to cheaper storage classes.

---

### Step 2: Create a New Lifecycle Rule
1. Under the **Management** tab, scroll to **Lifecycle rules**.  
2. Click on **Create lifecycle rule**.  
3. Enter a rule name — for example, `TransitionToGlacier`.  
4. Choose **Apply to all objects in the bucket**, or define filters if you want to target specific prefixes or tags.

<!-- Add snapshot here -->

> ✅ **Note:** Using filters is useful when you want to apply different rules to different folders or file types.

---

### Step 3: Define Transition Actions
1. Under **Lifecycle rule actions**, choose:  
   - ✅ “Transition current versions of objects between storage classes.”  
2. Then configure:  
   - **Transition to Glacier Instant Retrieval** after **30 days** (example).  
   - Optionally, add further transitions, such as **Glacier Deep Archive** after **90 days**.

<!-- Add snapshot here -->

> 💡 **Tip:** Choose the right storage class based on your data access frequency — Glacier Instant Retrieval is faster but slightly more expensive than Deep Archive.

---

### Step 4: (Optional) Add Expiration Rule
1. Enable the option **Expire current versions of objects**.  
2. Set the **Days after creation** — for example, `180 days`.  
   This will permanently delete the objects after 180 days.

<!-- Add snapshot here -->

> ✅ **Note:** Expiration rules are irreversible — use them carefully for non-critical or versioned data.

---

### Step 5: Review and Save the Rule
1. Review your lifecycle configuration summary.  
2. Ensure the rule status is set to **Enabled**.  
3. Click **Create rule**.

<!-- Add snapshot here -->

> 💡 **Tip:** You can create multiple rules per bucket, each handling different folders, prefixes, or tags.

---

### Step 6: Verify the Lifecycle Rule
1. Go back to the **Management → Lifecycle rules** section.  
2. Confirm your rule is listed and **Enabled**.  
3. Objects will automatically transition or expire as per your configuration after the set duration.

<!-- Add snapshot here -->

> ✅ **Note:** Lifecycle transitions are executed once per day by S3 — so effects may not be immediate.

---

## ⚙️ (Optional) Create Lifecycle Rule Using AWS CLI

You can also configure lifecycle policies using a JSON file and AWS CLI.

### Step 1: Create a Lifecycle JSON File
Create a file named `lifecycle.json` with the following content:

```json
{
  "Rules": [
    {
      "ID": "TransitionToGlacier",
      "Filter": {
        "Prefix": ""
      },
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "GLACIER"
        }
      ],
      "Expiration": {
        "Days": 180
      }
    }
  ]
}
```

### Step 2: Apply the Rule to Your Bucket
``` bash
   aws s3api put-bucket-lifecycle-configuration \
  --bucket my-lifecycle-demo-bucket \
  --lifecycle-configuration file://lifecycle.json
```
<!-- Add snapshot here -->
💡 Tip: This approach is useful for automation or infrastructure-as-code setups (like Terraform or CloudFormation).

---
### Step 3: Verify the Applied Configuration
```bash 
   aws s3api get-bucket-lifecycle-configuration \
  --bucket my-lifecycle-demo-bucket
```
Expected output will display your active lifecycle rule in JSON format.
<!-- Add snapshot here -->

---

### ✅ Outcome
1. By completing this task, you will:
   Automate data archiving and cleanup in S3
   Optimize storage costs using lifecycle transitions
   Manage long-term retention with Glacier or Deep Archive
   Learn both console and CLI approaches for lifecycle configuration

