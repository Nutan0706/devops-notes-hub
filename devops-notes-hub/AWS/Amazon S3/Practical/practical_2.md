# 📁 Upload and Download Files in S3 Bucket — Step-by-step Guide (Console + AWS CLI)

> **Goal:** uploading and downloading files using **AWS Console** and **AWS CLI**.  

---
### 🪜 Step 1 — Open the S3 Console
1. Sign in to the AWS Management Console.
2. In the top search bar, type S3 and open the S3 service.
<!-- 📸 Add snapshot of AWS S3 Console search here -->

---
### 🪜 Step 2 — Open Your Target Bucket
1. From the bucket list, click on the bucket where you want to upload files
(e.g., my-first-devops-bucket).
2. You’ll be directed to the Objects tab of that bucket.
<!-- 📸 Add snapshot of Bucket → Objects tab here -->
---

### 🪜 Step 3 — Upload File
1. Click Upload → Add files.
2. Select sample.txt from your local system.
3. Scroll down and click Upload at the bottom to start uploading.
<!-- 📸 Add snapshot of Upload dialog here -->

✅ Note: You can also upload entire folders using the Add folder option.

---

### 🪜 Step 4 — Verify Upload
1. Once upload completes, check for sample.txt in the object list.
2. Verify columns like Size, Last modified, and Storage class.
<!-- 📸 Add snapshot showing file uploaded successfully -->

💡 Tip: Enable Show versions (top-right corner) to view file version history — available if Versioning is enabled on your bucket.

---

### ✅ Outcome
You’ve successfully uploaded a file (sample.txt) to your Amazon S3 Bucket using the AWS Management Console.

## Download via AWS Console

### Step 1 — Navigate to the File
1. Go to your bucket → find the file (sample.txt) in the Objects list.
<!-- Add snapshot here -->
---
### Step 2 — Download File
1. Select the file → Click Download.
2. The file will be downloaded to your local Downloads folder.
<!-- Add snapshot here -->

✅ Note: You can also copy the Object URL to share securely (if permissions allow).

---

## Upload via AWS CLI
 Assumption: AWS CLI is configured and you have the required permissions.

### Step 1 — Prepare a File for Upload
1. If you don’t already have a file:
2. echo "This is my first S3 CLI upload!" > sample.txt

<!-- Add snapshot here -->
---
### Step 2 — Upload File to S3 Bucket
1. Use the aws s3 cp command:
2. aws s3 cp sample.txt s3://my-first-devops-bucket/
<!-- Add snapshot here -->

✅ Note: The cp command automatically handles multipart uploads for large files.

---
### Step 3 — Confirm Upload
1. List objects in your bucket:
```bash 
aws s3 ls s3://my-first-devops-bucket/
```
<!-- Add snapshot here -->

💡 Tip: You can verify the upload in the console or with aws s3api list-objects for more metadata.

---

## Download via AWS CLI

### Step 1 — Download File from S3

Use the same aws s3 cp command, but in reverse:

aws s3 cp s3://my-first-devops-bucket/sample.txt ./

<!-- Add snapshot here -->

✅ Note: The ./ indicates the current local directory.

---

### Step 2 — Verify Download

Confirm the file exists locally:

ls -l sample.txt
cat sample.txt

<!-- Add snapshot here -->

💡 Tip: You can specify a different destination folder, e.g. ~/Documents/.

---

### Verification
1. Verify via Console
   Navigate to your bucket → Check that sample.txt appears under Objects.
   Check object details like Owner, Encryption, and Storage class.
<!-- Add snapshot here -->

2. Verify via CLI
   ```bash
   aws s3api head-object --bucket my-first-devops-bucket --key sample.txt
   ```
<!-- Add snapshot here -->

✅ Note: The head-object command retrieves metadata without downloading the file.
