
# 2. OOPs (Object-Oriented Programming in Python)

## 1. Class and Object
- **Class:** Blueprint for creating objects.
- **Object:** Instance of a class with attributes and methods.

```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Nutan")
print(p1.name)
```

## 2. **init** Constructor

* Special method used to initialize object properties.
* Automatically called when object is created.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

## 3. Instance vs Class vs Static Variables

* **Instance variable:** Unique to each object (`self.var`)
* **Class variable:** Shared across all instances.
* **Static variable:** Usually defined outside class scope (less common in Python OOP).

```python
class Example:
    count = 0  # class variable
    def __init__(self, name):
        self.name = name  # instance variable
```

## 4. Instance vs Class vs Static Methods

* **Instance Method:** Works with instance data (`self`).
* **Class Method:** Works with class data (`@classmethod`).
* **Static Method:** Independent of class or instance (`@staticmethod`).

```python
class Demo:
    def instance_method(self): pass
    @classmethod
    def class_method(cls): pass
    @staticmethod
    def static_method(): pass
```

## 5. Inheritance

* Enables one class to derive from another.

**Types:**

* Single
* Multiple
* Multilevel
* Hierarchical

```python
class A: pass
class B(A): pass  # single inheritance
```

## 6. Method Overriding

* Child class redefines a parent class method.

```python
class Parent:
    def greet(self): print("Hello Parent")

class Child(Parent):
    def greet(self): print("Hello Child")
```

## 7. Encapsulation (_, __)

* Protects data by restricting access.
* `_var` → protected (convention)
* `__var` → private (name mangling)

## 8. Abstraction (ABC Module)

* Hides implementation details using **abstract base classes**.

```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
```

## 9. Polymorphism

* Same function name behaves differently for different classes.

```python
class Dog:
    def sound(self): print("Bark")

class Cat:
    def sound(self): print("Meow")

for animal in [Dog(), Cat()]:
    animal.sound()
```

## 10. Magic / Dunder Methods

* Special methods starting and ending with `__`.
* Examples:

  * `__init__()` – constructor
  * `__str__()` – string representation
  * `__len__()` – defines `len(obj)`
  * `__add__()` – defines `+` operator

## 11. Classmethod and Staticmethod

* `@classmethod`: Works on class-level data.
* `@staticmethod`: Utility function inside class.

## 12. super() Keyword

* Used to call parent class methods/constructors.

```python
class Parent:
    def __init__(self): print("Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child")
```

## 13. Property Decorators (@property, setters, getters)

* Used for encapsulation and controlled access.

```python
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
```

