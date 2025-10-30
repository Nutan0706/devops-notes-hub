# 🧠 AWS S3 — Enable Static Website Hosting

---

## 🎯 Objective
Host a simple HTML website on an **S3 bucket** and access it via the **bucket website endpoint**.

---

## 🧩 Step-by-Step Guide

### Step 1: Create a New S3 Bucket
1. Go to **AWS Management Console → S3 → Create Bucket**.  
2. Enter a globally unique bucket name (e.g., `my-static-website-demo`).  
3. Choose your preferred region (e.g., `us-east-1`).  
4. **Uncheck** “Block all public access” (since we need public access for static hosting).  
5. Acknowledge the warning and click **Create Bucket**.

> 💡 **Tip:** S3 static websites must be public to serve content to browsers. For secure use, combine with CloudFront later.

---

### Step 2: Upload Your Website Files
1. Open the bucket you just created.  
2. Go to the **Objects** tab.  
3. Click **Upload → Add files** and select your `index.html` and `error.html`.  
4. Click **Upload** to add the files to your bucket.

<img width="770" height="295" alt="image" src="https://github.com/user-attachments/assets/616b4a0e-02b3-4423-8664-33af6ec7b470" />

---

### Step 3: Make Files Public
Make the uploaded files publicly readable so users can access them via the website endpoint.

#### Option 1: Using AWS Console
- Select the uploaded files → Click **Actions → Make public using ACL**.
``` bash
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-static-website-demo-877046/*"
    }
  ]
}
```

#### Option 2: Using AWS CLI
```bash
aws s3api put-object-acl \
  --bucket my-static-website-demo \
  --key index.html \
  --acl public-read
```
Do the same for error.html:
```bash
aws s3api put-object-acl \
  --bucket my-static-website-demo \
  --key error.html \
  --acl public-read
```
<!-- Add snapshot here -->
✅ Note: You must enable “ACLs enabled” under bucket permissions before using this command.

---

### Step 4: Enable Static Website Hosting
1. Go to the Properties tab of your S3 bucket.
2. Scroll to the Static website hosting section.
3. Click Edit → Select Enable.
4. Choose Host a static website.
5. Enter the following:
   Index document: index.html
   Error document: error.html
6. Click Save Changes.
<img width="1509" height="552" alt="image" src="https://github.com/user-attachments/assets/843eab57-93ab-4502-a901-0023c8a1bb3c" />

---

### Step 5: Get the Website Endpoint
After enabling hosting, you’ll see a Website endpoint similar to:
```bash 
http://my-static-website-demo.s3-website.ap-south-1.amazonaws.com
```
Copy this link — this is your live website URL.
<!-- Add snapshot here -->
💡 Tip: Bookmark this endpoint or add it to a README file for quick testing.
<img width="1472" height="833" alt="image" src="https://github.com/user-attachments/assets/dc15557c-b29f-452a-ad64-afe74ef720b0" />

for Error.
<img width="1377" height="745" alt="image" src="https://github.com/user-attachments/assets/b699621e-bbd4-4169-99ba-8d0b89a88397" />

---

### Step 6: Test the Website
1. Open the website endpoint URL in your browser.
2. You should see your index.html page.
3. Try accessing a non-existing page to confirm error.html works correctly.
<!-- Add snapshot here -->
✅ Note: If you get “Access Denied”, check that:
     Your bucket objects are public.
     Block public access is disabled.
     Correct index and error document names are configured.

---

### Step 7: (Optional) Upload via AWS CLI
You can also upload your entire website folder from the CLI:
``` bash 
aws s3 sync ./website s3://my-static-website-demo/ --acl public-read
```
This uploads all files in your local website directory and makes them publicly readable.




