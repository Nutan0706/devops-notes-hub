# 🎛️ 2️⃣ Parameterized Builds (String & Choice Parameters)

## 📝 **Step 1: Open Your Pipeline Job**

Go to:

```
Dashboard → simple-pipeline → Configure
```

or create a new job:

```
parameterized-pipeline
```

Select **Pipeline**.

---

## 📝 **Step 2: Enable “This project is parameterized”**

Scroll to **General** → Check:

✔ **This project is parameterized**

Click **Add Parameter** → Add:

### 1️⃣ **String Parameter**

* Name: `USERNAME`
* Default value: `jenkins-user`
* Description: "Enter username"

### 2️⃣ **Choice Parameter**

* Name: `ENVIRONMENT`
* Choices:

  ```
  dev
  qa
  prod
  ```

<img width="255" height="279" alt="image" src="https://github.com/user-attachments/assets/4de14bb9-bf78-45d9-9d06-4d63988ea11e" />


---

## 📝 **Step 3: Add Jenkinsfile Using Parameters**

Scroll to **Pipeline → Script** and paste:

```groovy
pipeline {
    agent any

    parameters {
        string(name: 'USERNAME', defaultValue: 'jenkins-user', description: 'User name input')
        choice(name: 'ENVIRONMENT', choices: ['dev', 'qa', 'prod'], description: 'Select Environment')
    }

    stages {
        stage('Show Parameters') {
            steps {
                echo "Username selected: ${params.USERNAME}"
                echo "Environment selected: ${params.ENVIRONMENT}"
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (params.ENVIRONMENT == "prod") {
                        echo "Deploying to PRODUCTION ⚠️"
                    } else {
                        echo "Deploying to ${params.ENVIRONMENT} environment..."
                    }
                }
            }
        }
    }
}
```

<img width="458" height="257" alt="image" src="https://github.com/user-attachments/assets/9d48d99f-0cd4-46c3-8c74-f0e76a752f99" />


---

## 📝 **Step 4: Save the Job**

Click:

```
Save
```

---

## 📝 **Step 5: Build with Parameters**

Click:

```
Build with Parameters
```

Now select:

* **USERNAME:** e.g., “nutan-dev”
* **ENVIRONMENT:** choose “qa”

Click **Build**.

<img width="246" height="194" alt="image" src="https://github.com/user-attachments/assets/41ef4c14-228a-45e0-846e-1fd4f0055d3c" />


---

## 📝 **Step 6: View Console Output**

Open:

```
Build #1 → Console Output
```

You should see:

```
Username selected: nutan-dev
Environment selected: qa
Deploying to qa environment...
Finished: SUCCESS
```

<img width="295" height="372" alt="image" src="https://github.com/user-attachments/assets/ae847b34-8cc8-4bb1-b9e1-f70ddd5f45be" />

