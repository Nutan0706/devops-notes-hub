## 1. Variables, Data Types, Type Casting
- Variables store data values.
- Common data types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`.
- Type casting: converting between types using `int()`, `float()`, `str()`, etc.

## 2. Operators
- **Arithmetic:** `+`, `-`, `*`, `/`, `%`, `//`, `**`
- **Logical:** `and`, `or`, `not`
- **Bitwise:** `&`, `|`, `^`, `~`, `<<`, `>>`
- **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`, etc.

## 3. Conditional Statements
```python
if condition:
    # code
elif condition:
    # code
else:
    # code
```

## 4. Loops

* **for loop:** iterate over a sequence
* **while loop:** repeat while condition is true
* **break:** exit loop
* **continue:** skip current iteration

## 5. Functions

* Define using `def`.
* Default arguments, `*args`, and `**kwargs` for flexibility.

```python
def func(a, b=10, *args, **kwargs):
    pass
```

## 6. String Manipulation & Formatting

* Methods: `.upper()`, `.lower()`, `.replace()`, `.split()`, `.join()`
* Formatting: `f"Hello {name}"`, `"{}".format(name)`

## 7. List, Tuple, Set, Dictionary — CRUD Operations

* **List:** ordered, mutable
* **Tuple:** ordered, immutable
* **Set:** unordered, unique elements
* **Dict:** key-value pairs
* CRUD → Create, Read, Update, Delete operations.

## 8. List/Dict Comprehensions

```python
squares = [x**2 for x in range(5)]
squared_dict = {x: x**2 for x in range(5)}
```

## 9. Lambda Functions

* Anonymous one-line functions: `lambda x: x * 2`

## 10. map(), filter(), reduce()

* `map(func, iterable)`
* `filter(func, iterable)`
* `reduce(func, iterable)` (from `functools`)

## 11. zip() and enumerate()

* `zip()` combines iterables.
* `enumerate()` adds index to iterable.

## 12. Exception Handling

```python
try:
    # code
except Exception as e:
    # handle error
finally:
    # always runs
```

* Use `raise` to throw exceptions.

## 13. File Handling

```python
with open('file.txt', 'r') as f:
    data = f.read()
```

* Modes: `'r'`, `'w'`, `'a'`, `'rb'`, `'wb'`

## 14. Modules and Packages

* Use `import` to reuse code.
* Packages use `__init__.py` file to initialize.

## 15. `__name__ == "__main__"` Concept

* Used to check if the script is being run directly or imported.

```python
if __name__ == "__main__":
    main()
```

```
```
