
# 5. Flask (Backend Framework)

Flask is a lightweight and powerful **Python web framework** used for building APIs and web applications.

---

## 1. Flask Setup & Project Structure
- Install Flask:  
  ```bash
  pip install flask
```

* Basic structure:

  ```
  /project
  ├── app.py
  ├── static/
  ├── templates/
  └── requirements.txt
  ```

---

## 2. Routing (@app.route)

* Define routes using decorators.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"
```

---

## 3. URL Parameters & Query Strings

* **URL Parameters:**

  ```python
  @app.route('/user/<name>')
  def user(name):
      return f"Hello, {name}"
  ```
* **Query Strings:**

  ```python
  from flask import request
  @app.route('/search')
  def search():
      q = request.args.get('q')
      return f"Search term: {q}"
  ```

---

## 4. Templates (Jinja2)

* Use dynamic HTML templates.
* Stored in `/templates` folder.

```python
from flask import render_template
@app.route('/welcome/<user>')
def welcome(user):
    return render_template('welcome.html', user=user)
```

```html
<!-- templates/welcome.html -->
<h1>Hello {{ user }}</h1>
```

---

## 5. Handling Forms & Requests (GET, POST)

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f"Logged in as {username}"
    return render_template('login.html')
```

---

## 6. REST APIs with Flask (Flask-RESTful)

* Simplify RESTful API creation.

```bash
pip install flask-restful
```

```python
from flask_restful import Api, Resource
api = Api(app)

class Hello(Resource):
    def get(self):
        return {"message": "Hello, World"}

api.add_resource(Hello, '/')
```

---

## 7. JSON Response (jsonify)

* Return structured JSON data.

```python
from flask import jsonify

@app.route('/data')
def data():
    return jsonify({"name": "Nutan", "role": "DevOps Engineer"})
```

---

## 8. Flask Configurations & Environment Variables

* Manage configs dynamically.

```python
app.config['DEBUG'] = True
app.config.from_envvar('APP_SETTINGS')
```

Or via `.env` file using `python-dotenv`.

---

## 9. Database Integration

* Common Databases: **SQLite, MySQL, PostgreSQL**
* Example with SQLite:

```python
import sqlite3
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
```

---

## 10. SQLAlchemy ORM

* Object Relational Mapper for Flask.

```bash
pip install flask_sqlalchemy
```

```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
```

---

## 11. Authentication & JWT

* Use **Flask-JWT-Extended** for token-based auth.

```bash
pip install flask-jwt-extended
```

```python
from flask_jwt_extended import JWTManager, create_access_token

jwt = JWTManager(app)
token = create_access_token(identity="user1")
```

---

## 12. Middleware / Request Hooks

* Execute functions before or after requests.

```python
@app.before_request
def before_req():
    print("Before request")

@app.after_request
def after_req(response):
    print("After request")
    return response
```

---

## 13. Error Handling & Custom Error Pages

```python
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
```

---

## 14. Deployment (Gunicorn + Nginx, Docker)

* **Gunicorn:** WSGI server for production.
* **Nginx:** Reverse proxy & load balancer.
* **Docker:** Containerize your app.

```bash
gunicorn app:app
```

**Dockerfile Example:**

```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
```
