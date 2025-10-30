# 🧠 AWS S3 — Enable Static Website Hosting

---

## 🎯 Objective
Host a simple HTML website on an **S3 bucket** and access it via the **bucket website endpoint**.

---

## 🧩 Step-by-Step Guide

### Step 1: Create a New S3 Bucket
1. Go to **AWS Management Console → S3 → Create Bucket**.  
2. Enter a globally unique bucket name (e.g., `my-static-website-demo`).  
3. Choose your preferred region (e.g., `ap-south-1`).  
4. **Uncheck** “Block all public access” (since we need public access for static hosting).  
5. Acknowledge the warning and click **Create Bucket**.

<!-- Add snapshot here -->

> 💡 **Tip:** S3 static websites must be public to serve content to browsers. For secure use, combine with CloudFront later.

---

### Step 2: Upload Your Website Files
1. Open the bucket you just created.  
2. Go to the **Objects** tab.  
3. Click **Upload → Add files** and select your `index.html` and `error.html`.  
4. Click **Upload** to add the files to your bucket.

<!-- Add snapshot here -->

---

### Step 3: Make Files Public
Make the uploaded files publicly readable so users can access them via the website endpoint.

#### Option 1: Using AWS Console
- Select the uploaded files → Click **Actions → Make public using ACL**.

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
<!-- Add snapshot here -->

---

### Step 5: Get the Website Endpoint
After enabling hosting, you’ll see a Website endpoint similar to:
```bash 
http://my-static-website-demo.s3-website.ap-south-1.amazonaws.com
```
Copy this link — this is your live website URL.
<!-- Add snapshot here -->
💡 Tip: Bookmark this endpoint or add it to a README file for quick testing.

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
<!-- Add snapshot here -->
