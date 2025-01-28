# SafeDict

Python does not natively support a chaining operator (like `?.` in JavaScript) for safely accessing nested dictionary keys. This often leads to verbose code to check if a key exists or if its value is `None` before accessing deeper levels.

**SafeDict** is here to solve this problem.

SafeDict is a Python library that provides a safe way to access nested dictionary keys. When a key does not exist or its value is None, it returns None by default (or a user-specified default value). Unlike standard dictionaries, it prevents errors when accessing deeper levels of nested keys, making your code cleaner, easier to read, and less error-prone.

---

## **Key Features**
- Safely access nested dictionary keys without manual checks.
- Fully compatible with regular Python dictionaries.

---

## **Installation**

Install the library via pip:

```bash
pip install safe-dict
```

---

## **Usage**
```python
from safe_dict import SafeDict

# Example with a nested dictionary
data = SafeDict({"a": {"b": {"c": 42}}})

# Safe key access using get
print(data.get("a").get("b").get("c"))  # Output: 42
print(data.get("a").get("x").get("y"))  # Output: None

# Safe key access with a default value
print(data.get("a").get("x", "default"))  # Output: default
```

---

## **Comparison**
### Traditional Way:
Using a standard dictionary, you would need to manually check each key:

```python
data = {
    "a": {
        "b": {
            "c": 42
        },
        "d": None
    }
}

# Safe access
if "a" in data and data["a"] is not None:
    if "b" in data["a"] and data["a"]["b"] is not None:
        if "c" in data["a"]["b"]:
            print(data["a"]["b"]["c"])

# You can also use the "get" method, but if you access a key whose value is None, an error will occur:
print(data.get("a", {}).get("d", {}).get("c")) # AttributeError: 'NoneType' object has no attribute 'get', because "d" is not a dictionary.
```

### With SafeDict:
You can write the same logic much more cleanly:
```python
data = SafeDict({"a": {"b": {"c": 42}}})

print(data.get("a", {}).get("b", {}).get("c"))  # Output: 42
print(data.get("a", {}).get("d", {}).get("c"))  # Output: None
```
---

## **License**
SafeDict is licensed under the MIT License, allowing you to use and modify it freely.
