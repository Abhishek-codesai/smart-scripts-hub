# ============================================================
# 01 - Dictionaries: Creation, Access & Methods
# ============================================================

# Dictionary = key: value pairs
# Keys must be UNIQUE and IMMUTABLE (str, int, tuple)
# Values can be ANYTHING
# Ordered (Python 3.7+), Mutable

# ── Creating Dictionaries ────────────────────────────────────
empty = {}
empty2 = dict()

student = {
    "name": "Abhishek",
    "age": 20,
    "branch": "CSE AI/ML",
    "college": "PCTE",
    "gpa": 8.9
}

# dict() constructor
person = dict(name="Ravi", age=25, city="Delhi")

# From list of tuples
pairs = dict([("a", 1), ("b", 2), ("c", 3)])

# From two lists using zip
keys   = ["x", "y", "z"]
values = [10, 20, 30]
d = dict(zip(keys, values))
print(d)   # {'x': 10, 'y': 20, 'z': 30}

print(type(student))   # <class 'dict'>
print(student)

# ── ACCESSING VALUES ─────────────────────────────────────────
print(student["name"])         # Abhishek
print(student["age"])          # 20
# print(student["phone"])      # ❌ KeyError if key doesn't exist

# .get() — safer access, returns None if key missing
print(student.get("name"))      # Abhishek
print(student.get("phone"))     # None
print(student.get("phone", "N/A"))  # N/A  (default value)

# ── ADDING & MODIFYING ───────────────────────────────────────
student["email"] = "abhishek@pcte.edu"    # add new key
student["age"] = 21                        # modify existing key
print(student)

# ── DELETING ─────────────────────────────────────────────────
# del — removes key
del student["email"]
print(student)

# .pop(key) — removes and returns value
removed = student.pop("gpa")
print(removed)    # 8.9
print(student)

# .pop() with default — no error if key missing
val = student.pop("phone", "Not found")
print(val)        # Not found

# .popitem() — removes and returns LAST inserted key-value pair
last_item = student.popitem()
print(last_item)  # ('college', 'PCTE')

# .clear() — removes all items
temp = {"a": 1, "b": 2}
temp.clear()
print(temp)   # {}

# ── CHECKING KEYS ────────────────────────────────────────────
info = {"name": "Abhishek", "age": 20}

print("name" in info)         # True
print("phone" in info)        # False
print("name" not in info)     # False
print(len(info))              # 2

# ── ITERATING ────────────────────────────────────────────────
d = {"a": 1, "b": 2, "c": 3}

# Iterate over keys (default)
for key in d:
    print(key, "→", d[key])

# .keys() — view of all keys
print(d.keys())     # dict_keys(['a', 'b', 'c'])

# .values() — view of all values
print(d.values())   # dict_values([1, 2, 3])

# .items() — view of all (key, value) pairs
print(d.items())    # dict_items([('a', 1), ('b', 2), ('c', 3)])

# Unpacking items in loop
for key, value in d.items():
    print(f"{key}: {value}")

# ── UPDATE ───────────────────────────────────────────────────
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}     # "b" will overwrite d1's "b"

d1.update(d2)
print(d1)    # {'a': 1, 'b': 99, 'c': 3}

# ── COPY ─────────────────────────────────────────────────────
original = {"x": 1, "y": 2}
copy1 = original.copy()
copy2 = dict(original)      # another way
copy1["z"] = 3
print(original)   # unchanged

# For nested dicts, use deepcopy
import copy
nested = {"a": {"b": 1}}
deep = copy.deepcopy(nested)

# ── SETDEFAULT ───────────────────────────────────────────────
d = {"a": 1}
d.setdefault("a", 99)    # key exists → does nothing, returns 1
d.setdefault("b", 99)    # key missing → sets "b": 99
print(d)    # {'a': 1, 'b': 99}

# ── FROMKEYS ─────────────────────────────────────────────────
keys = ["name", "age", "city"]
template = dict.fromkeys(keys, "N/A")
print(template)   # {'name': 'N/A', 'age': 'N/A', 'city': 'N/A'}

# ── NESTED DICTIONARIES ──────────────────────────────────────
students = {
    "s1": {"name": "Abhishek", "age": 20, "marks": 95},
    "s2": {"name": "Ravi",     "age": 21, "marks": 88},
    "s3": {"name": "Priya",    "age": 19, "marks": 92},
}

print(students["s1"]["name"])     # Abhishek
print(students["s2"]["marks"])    # 88

# Iterate nested dict
for sid, info in students.items():
    print(f"{sid}: {info['name']} — {info['marks']}")

# ── DICT COMPREHENSION ───────────────────────────────────────
# {key_expr: value_expr for item in iterable}

squares = {x: x**2 for x in range(1, 6)}
print(squares)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter + transform
even_sq = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_sq)

# Invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}

# ── SUMMARY TABLE ────────────────────────────────────────────
# Method                Description
# d[key]                Access value (KeyError if missing)
# d.get(key, default)   Safe access with optional default
# d[key] = val          Add or update
# d.update(d2)          Merge dict d2 into d
# del d[key]            Delete a key
# d.pop(key, default)   Delete & return value
# d.popitem()           Delete & return last (key, value) pair
# d.clear()             Remove all items
# d.keys()              All keys (view)
# d.values()            All values (view)
# d.items()             All (key, value) pairs (view)
# d.copy()              Shallow copy
# d.setdefault(k, val)  Set key only if it doesn't exist
# dict.fromkeys(keys)   New dict with keys, same value
