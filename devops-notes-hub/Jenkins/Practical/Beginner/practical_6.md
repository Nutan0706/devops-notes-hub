# 🗂️ Archive Build Artifacts (Step-by-step)

When you archive artifacts, Jenkins stores files produced by a build (for example `.jar`, `.zip`, `.war`, logs). These files are visible on the build page and can be downloaded.

---

## A) Freestyle Job — Archive Artifacts

### Step 1 — Create / open a Freestyle job

Dashboard → New Item → `archive-artifact-job` → Freestyle Project → OK.
<img width="306" height="334" alt="image" src="https://github.com/user-attachments/assets/ce71403c-b101-49d4-b7da-54f648c67468" />



### Step 2 — Add build steps to create artifact

Under **Build → Add build step → Execute shell**, insert:

```bash
# prepare artifact
mkdir -p dist
echo "Hello from build" > dist/hello.txt
zip -r build-output.zip dist
# show file info
ls -lh build-output.zip
```
<img width="299" height="430" alt="image" src="https://github.com/user-attachments/assets/92ffa882-1856-4b3e-97e5-c3641df29034" />


### Step 3 — Add Post-build Action: Archive the artifacts

Scroll to **Post-build Actions → Add post-build action → Archive the artifacts**.

In the **Files to archive** field enter the pattern of files to save, for example:

```
build-output.zip
# or to archive everything in dist:
dist/**/*
# or jar files:
**/*.jar
```

Optionally set **Only archive if build is successful** (recommended).
<img width="432" height="287" alt="image" src="https://github.com/user-attachments/assets/ca19dc29-35dc-4188-891d-99b37078e45b" />


### Step 4 — Save & Build

Click **Save**, then **Build Now**.
<img width="427" height="417" alt="image" src="https://github.com/user-attachments/assets/805e2e61-4a75-4088-9762-538fd3be4b11" />


### Step 5 — View & Download artifact

Go to the build run: `Build #1` → **Artifacts** section (or left panel link). Click the file (e.g., `build-output.zip`) to download it.
<img width="427" height="417" alt="image" src="https://github.com/user-attachments/assets/d6e54dc2-2b1f-4abe-93fb-82d1fd19bb00" />


---

## B) Pipeline Job (Jenkinsfile) — Archive Artifacts

If you prefer code-as-config, use a `Jenkinsfile`. Example Declarative pipeline that builds a zip and archives it:

```groovy
pipeline {
  agent any

  stages {
    stage('Prepare') {
      steps {
        sh 'mkdir -p dist'
        sh 'echo "Hello from build" > dist/hello.txt'
        sh 'zip -r build-output.zip dist'
        sh 'ls -lh build-output.zip'
      }
    }
  }

  post {
    success {
      archiveArtifacts artifacts: 'build-output.zip', fingerprint: true
    }
    always {
      echo "Pipeline finished"
    }
  }
}
```

* `archiveArtifacts artifacts: 'build-output.zip'` — pattern may be glob like `**/*.jar` or `dist/**/*`.
* `fingerprint: true` will record a fingerprint for tracking the artifact across jobs/nodes.

*(Add screenshot: Jenkinsfile in job config or Multibranch pipeline and pipeline run.)*

### Example: Multiple files or patterns

```groovy
archiveArtifacts artifacts: 'target/*.jar, build/*.zip, logs/**/*.log'
```

---

## C) Multibranch Pipeline / Git-based Jenkinsfile

1. Put the `Jenkinsfile` in your repo root.
2. Create a Multibranch Pipeline job that points to your repo.
3. When branch builds run, artifacts will be archived per build and visible in build details.
   *(Add screenshot: Multibranch job run with artifacts.)*

---

## D) Artifact Retention & Cleanup

* Jenkins keeps artifacts until you delete the build or configure retention.
* To automatically discard old artifacts, configure **Discard Old Builds** in job config:

  * Check **Discard old builds**
  * Set **Max # of builds to keep** and **Max # of days to keep builds**
  * Optionally check **Discard old artifacts** if available.
    *(Add screenshot: Discard old builds config.)*

---

## E) Download & Use Artifacts

On a build page you can:

* Click artifact filename to download.
* Use direct URL: `http://<jenkins>/job/<job-name>/<build-number>/artifact/<path>/<file>` (copy from UI by right-click → copy link).
  *(Add screenshot: downloading the artifact.)*

---

## F) Optional — Archive to External Storage (e.g., S3)

If you need artifacts outside Jenkins (long-term storage / sharing), consider:

* S3 plugin for Jenkins (publish artifacts to S3) or
* Adding a post-build shell step to `aws s3 cp build-output.zip s3://my-bucket/path/`
  (Requires AWS CLI + credentials/configured on agent).
  *(Add screenshot if you configure S3 upload step.)*

