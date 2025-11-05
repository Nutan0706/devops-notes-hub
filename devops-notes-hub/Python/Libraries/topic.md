# 🧠 9. Libraries You Must Know

These libraries are essential for day-to-day Python development, scripting, automation, and backend projects.

---

## 1. requests → HTTP Requests
- Used for sending HTTP/HTTPS requests.
- Common for REST API integration.

```python
import requests
response = requests.get("https://api.github.com")
print(response.json())
```

---

## 2. json / yaml → Config Parsing

* Handle configuration and structured data.

```python
import json, yaml

data = json.load(open("config.json"))
yaml_data = yaml.safe_load(open("config.yaml"))
```

---

## 3. argparse → Command-line Argument Parser

* Build CLI tools easily.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Enter your name")
args = parser.parse_args()
print(args.name)
```

---

## 4. logging → Log Management

* Replace print statements with structured logging.

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Service started successfully.")
```

---

## 5. pandas, numpy → Data Manipulation

* **pandas:** DataFrames, CSV handling
* **numpy:** Numerical and array operations

```python
import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")
arr = np.array([1, 2, 3])
```

---

## 6. os, sys, subprocess, pathlib → Scripting

* Core system interaction modules.

```python
import os, sys, subprocess
from pathlib import Path

print(os.getcwd())
subprocess.run(["ls", "-l"])
```

---

## 7. flask, fastapi → Web Frameworks

* **Flask:** Lightweight and flexible
* **FastAPI:** Async, high-performance, modern APIs

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask!"
```

---

## 8. pytest, unittest → Testing

* Used for writing and automating test cases.

```python
def test_sum():
    assert 2 + 2 == 4
```

Run using:

```bash
pytest -v
```

---

## 9. boto3 → AWS Automation

* Python SDK for AWS (EC2, S3, Lambda, etc.)

```python
import boto3
s3 = boto3.client('s3')
for bucket in s3.list_buckets()['Buckets']:
    print(bucket['Name'])
```

---

## 10. paramiko → SSH Automation

* Automate server tasks via SSH.

```python
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("host", username="user", password="pass")
stdin, stdout, stderr = ssh.exec_command("ls")
```

---

## 11. re → Regex

* Pattern-based text search and manipulation.

```python
import re
result = re.findall(r"\d+", "Item123Price456")
print(result)
```
