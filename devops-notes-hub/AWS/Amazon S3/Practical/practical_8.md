# 🧠 AWS S3 — Use S3 with AWS CLI Sync

---

## 🎯 Objective
Efficiently **sync a local folder with an S3 bucket** using the AWS CLI, enabling seamless backup and synchronization between local files and cloud storage.

---

## 🧩 Step-by-Step Guide

### Step 1: Create a Local Folder with Sample Files
Create a folder on your local machine to test the sync command.

```bash
mkdir local-backup
cd local-backup
echo "This is file1.txt" > file1.txt
echo "This is file2.txt" > file2.txt
```
<!-- Add snapshot here -->
💡 Tip: Keep your test files small while experimenting to avoid unnecessary data transfer costs.

---

### Step 2: Create or Identify an Existing S3 Bucket
If you don’t already have a bucket, create one using AWS CLI.
```bash
aws s3 mb s3://my-devops-sync-bucket --region ap-south-1
```
<!-- Add snapshot here -->
✅ Note: Replace my-devops-sync-bucket with your own unique bucket name.

---

### Step 3: Sync Local Folder to S3 Bucket
Use the aws s3 sync command to upload (sync) all files from your local folder to the S3 bucket.
``` bash 
aws s3 sync ./local-backup s3://my-devops-sync-bucket/
```
This command:
   Uploads new files that don’t exist in the bucket
   Updates changed files
   Skips unchanged files
<img width="940" height="113" alt="image" src="https://github.com/user-attachments/assets/e2c7457e-ec05-40b2-b9c0-817b83a55db6" />

💡 Tip: The sync command is ideal for incremental backups — it only uploads modified or missing files.

---

###  Step 4: Verify the Synced Files
List the contents of your S3 bucket to confirm successful synchronization.
```bash
aws s3 ls s3://my-devops-sync-bucket/
```
Expected output:
```bash
2025-10-30 11:42:01     22 file1.txt
2025-10-30 11:42:01     22 file2.txt
```
<img width="659" height="95" alt="image" src="https://github.com/user-attachments/assets/9306411d-4fa1-4b5b-b46e-85c1a919c0cc" />

---

### Step 5: Sync from S3 to Local (Download)
You can also reverse the direction — sync your bucket contents back to your local folder.
```bash 
aws s3 sync s3://my-devops-sync-bucket/ ./local-restore
```

This will:
Download all files from the S3 bucket into a new folder named local-restore.
✅ Note: Use this method for restoring backups from S3 to your system.

---

### Step 6: Use Sync with Deletion
If you want your bucket and local folder to mirror each other exactly, use the --delete flag.
This removes files from the destination that no longer exist in the source.
```bash 
aws s3 sync ./local-backup s3://my-devops-sync-bucket/ --delete
```
<!-- Add snapshot here -->
⚠️ Warning: The --delete option permanently deletes extra files from the destination — use carefully!

---

### Step 7: Verify Differences Before Sync
To check what changes will occur before actually syncing, use the --dryrun flag.
```bash
aws s3 sync ./local-backup s3://my-devops-sync-bucket/ --dryrun
```
This simulates the sync and shows which files would be copied or deleted.
<!-- Add snapshot here -->
💡 Tip: Always run --dryrun before large or critical sync operations to preview changes safely.

---

### Step 8: Add Filters for Specific Files or Extensions
You can include or exclude specific files during sync.
#### Example 1: Sync only .txt files
```bash
aws s3 sync ./local-backup s3://my-devops-sync-bucket/ --exclude "*" --include "*.txt"
```
#### Example 2: Exclude log files
```bash
aws s3 sync ./local-backup s3://my-devops-sync-bucket/ --exclude "*.log"
```
<!-- Add snapshot here -->

✅ Note: Use multiple --exclude and --include options for advanced filtering.

---
### 🧾 Summary

| 🛠️ Action | 💻 Command | 📝 Description |
|------------|------------|----------------|
| **Upload Local → S3** | `aws s3 sync ./local-backup s3://my-bucket/` | Upload and sync files |
| **Download S3 → Local** | `aws s3 sync s3://my-bucket/ ./local-folder` | Restore backup locally |
| **Preview Sync** | `aws s3 sync ... --dryrun` | Simulate changes before execution |
| **Mirror Folders** | `aws s3 sync ... --delete` | Keep exact copies between source and destination |
| **Filter Files** | `--exclude`, `--include` | Fine-tune which files to include or exclude during sync |

---

### ✅ Outcome
By completing this task, you’ll:
  Understand how to use aws s3 sync for efficient backups
  Be able to upload, download, and mirror directories between local and S3
  Confidently automate periodic backups using AWS CLI commands

