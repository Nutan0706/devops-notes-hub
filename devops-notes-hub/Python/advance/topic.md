# Advanced Python Concepts (For Experienced-Level Interviews & Production Use)

These concepts are crucial for writing efficient, scalable, and production-ready Python code.

---

## 1. Iterators and Generators (__iter__, yield)
- **Iterator:** Object that implements `__iter__()` and `__next__()`.
- **Generator:** Function that uses `yield` to produce a stream of values.

```python
class MyIter:
    def __init__(self, n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.n:
            val = self.i
            self.i += 1
            return val
        raise StopIteration

def my_generator(n):
    for i in range(n):
        yield i
```

---

## 2. Decorators (Function & Class-based)

* Used to modify function/class behavior dynamically.

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def greet():
    print("Hello!")
```

**Class-based Decorator:**

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("Before call")
        return self.func(*args, **kwargs)
```

---

## 3. Context Managers (with, **enter**, **exit**)

* Automatically manage resources (like files, DB connections).

```python
class FileManager:
    def __init__(self, file):
        self.file = file
    def __enter__(self):
        self.f = open(self.file, 'r')
        return self.f
    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()

with FileManager('test.txt') as f:
    print(f.read())
```

---

## 4. Type Hinting and Annotations

* Improve code readability and static analysis.

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## 5. Dataclasses (@dataclass)

* Automatically generates methods like `__init__`, `__repr__`, and `__eq__`.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

---

## 6. Virtual Environments (venv, pipenv)

* Isolate project dependencies.

```bash
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows
```

**Pipenv:**

```bash
pip install pipenv
pipenv install flask
```

---

## 7. Dependency Management

* **requirements.txt:**

  ```bash
  pip freeze > requirements.txt
  pip install -r requirements.txt
  ```
* **Poetry:**

  ```bash
  poetry init
  poetry add requests
  ```

---

## 8. Packaging (setup.py, pip install .)

* Create installable Python packages.

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0',
    packages=find_packages(),
)
```

```bash
pip install .
```

---

## 9. Unit Testing (unittest, pytest)

* Write testable and maintainable code.

```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()
```

**pytest:**

```bash
pip install pytest
pytest -v
```

---

## 10. Mocking and Fixtures

* **Mocking:** Replace dependencies during tests.
* **Fixtures:** Reusable setup/teardown code in pytest.

```python
from unittest.mock import patch

@patch('requests.get')
def test_api(mock_get):
    mock_get.return_value.status_code = 200
```

---

## 11. Asyncio (Asynchronous Programming)

* Run concurrent tasks efficiently.

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    print("Data fetched")

asyncio.run(fetch_data())
```

---

## 12. Memory Management and Garbage Collection

* Python uses reference counting + garbage collector.
* Manually trigger GC if needed.

```python
import gc
gc.collect()
```

---

## 13. Performance Profiling and Optimization

* Tools: `cProfile`, `timeit`, `line_profiler`.

```python
import cProfile
cProfile.run('sum(range(1000000))')
```

* Optimize using:

  * Better algorithms
  * List comprehensions
  * Async operations
  * Multiprocessing or Cython for heavy tasks
