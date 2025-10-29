## 🧠 Practical 10 — Create IAM Role for Lambda Function

**Goal:** Create an IAM role that grants a Lambda function minimal access (for example, only to read/write a specific DynamoDB table or S3 bucket).

🔹 Step-by-Step Guide
### Step 1: Open IAM Console
1.Go to AWS Management Console → IAM → Roles → Create Role
2.Under Trusted Entity Type, choose AWS Service.
3.Select Lambda as the trusted service and click Next.

---
### Step 2: Attach Minimal Permission Policy
1. You can attach existing managed policies or create a custom one.
2. Example: to allow access to one DynamoDB table, create this JSON policy 👇

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "LambdaDynamoDBAccess",
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:UpdateItem",
        "dynamodb:DeleteItem"
      ],
      "Resource": "arn:aws:dynamodb:ap-south-1:123456789012:table/MyAppTable"
    }
  ]
}
```
📘 Replace 123456789012 with your AWS account ID and MyAppTable with your actual table name.
Click Next, give a name like LambdaDynamoDBRole, and Create role.

---

### Step 3: Verify Trust Relationship

After creation:

Go to your new role → **Trust relationships** tab.

Ensure it looks like this:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```
✅ This allows AWS Lambda to assume the role.

---

### Step 4: Attach Role to Lambda Function
1. Go to **AWS Console → Lambda → Functions**.
2. Choose an existing function or create a new one.
3. In **Configuration → Permissions**, click **Edit role**.
4. Choose **Use an existing role** → select **LambdaDynamoDBRole**.
5. Click **Save**.

---

### Step 5: Test Access

You can test access with a simple Lambda handler code:

```python
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('MyAppTable')
    response = table.get_item(Key={'id': '1'})
    return response
```
✅ If permissions are correct, the function executes successfully.
❌ If access is denied, check the IAM role and attached policy.

---

### ✅ Outcome

You have successfully created a **Lambda-specific IAM role** with **least privilege access**.  
Your Lambda function can now securely interact with **only the required resource** (e.g., a single DynamoDB table or S3 bucket).

---

### 🧠 Best Practice Tips

- ✅ Always grant **only the actions needed** — avoid using `*` in policies.  
- 🔹 Keep **separate roles** for different Lambda functions.  
- 📊 Use **AWS CloudWatch Logs** to verify access and monitor **denied actions**.  
- 🔄 **Rotate roles** and review access regularly using **IAM Access Advisor**.




