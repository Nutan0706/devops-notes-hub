# Python for Scripting & Automation

Highly important for **DevOps** / **System Admin** roles.

## 1. OS Module
- Interact with the operating system.
- Common uses:
  - File and directory handling (`os.listdir()`, `os.remove()`)
  - Environment variables (`os.environ`)
  - Path operations (`os.path.join()`, `os.path.exists()`)

```python
import os
print(os.getcwd())
print(os.listdir())
```

## 2. Sys Module

* Access system-specific parameters and functions.
* `sys.argv` → command-line arguments
* `sys.exit()` → exit program safely

```python
import sys
print(sys.argv)
sys.exit(0)
```

## 3. Subprocess Module

* Run shell commands directly from Python.

```python
import subprocess
subprocess.run(["ls", "-l"])
```

## 4. Shutil Module

* High-level file operations like **copy**, **move**, **delete**.

```python
import shutil
shutil.copy("source.txt", "dest.txt")
```

## 5. Logging Module

* Used for application logs instead of print statements.

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
```

## 6. JSON / YAML Parsing

* **JSON:** `json.load()`, `json.dump()`
* **YAML:** `yaml.safe_load()`, `yaml.dump()`

```python
import json
data = json.load(open("data.json"))
```

## 7. CSV Automation

* Use `csv` module for reading/writing CSV files.

```python
import csv
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

## 8. DateTime and Time Modules

* Handle date and time operations.
* Common functions: `datetime.now()`, `strftime()`, `sleep()`

```python
from datetime import datetime
import time
print(datetime.now())
time.sleep(2)
```

## 9. Regex (re Module)

* Pattern matching and text manipulation.

```python
import re
result = re.findall(r"\d+", "abc123xyz")
print(result)
```

## 10. Web Requests

* **requests**: for HTTP APIs
* **urllib**: built-in for basic requests

```python
import requests
response = requests.get("https://api.github.com")
print(response.json())
```

## 11. Automation with Selenium / Paramiko

* **Selenium:** Automate browser actions.
* **Paramiko:** Automate SSH and remote server tasks.

```python
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("hostname", username="user", password="pass")
stdin, stdout, stderr = ssh.exec_command("ls")
```

## 12. Send Email using smtplib

```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello from Python!")
msg["Subject"] = "Test Email"
msg["From"] = "sender@example.com"
msg["To"] = "receiver@example.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("sender@example.com", "password")
    server.send_message(msg)
```

## 13. Schedule Tasks

* Use `schedule` library or system cron with Python scripts.

```python
import schedule, time

def job():
    print("Running task...")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

## 14. Multi-threading and Multi-processing

* **threading**: for I/O-bound tasks
* **multiprocessing**: for CPU-bound tasks

```python
from threading import Thread
def task(): print("Running thread")

t = Thread(target=task)
t.start()
```

## 15. Handling APIs — GET, POST, PUT, DELETE

```python
import requests
response = requests.post("https://api.example.com", json={"key": "value"})
print(response.status_code)
```

## 16. Environment Variable Handling (.env files)

* Use `python-dotenv` for managing environment variables.

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
```

