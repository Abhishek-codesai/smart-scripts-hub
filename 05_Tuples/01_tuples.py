# ============================================================
# 01 - Tuples: Creation, Indexing, Methods & Immutability
# ============================================================

# ── Creating Tuples ───────────────────────────────────────────
empty    = ()
single   = (42,)          # ← COMMA is required for single-element tuple!
not_tuple= (42)           # This is just int 42, NOT a tuple
coords   = (10.5, 20.3)
mixed    = (1, "hello", True, 3.14)
nested   = ((1, 2), (3, 4), (5, 6))

print(single, type(single))       # (42,) <class 'tuple'>
print(not_tuple, type(not_tuple)) # 42    <class 'int'>
print(mixed)
print(nested)

# tuple() constructor
from_list  = tuple([1, 2, 3])
from_range = tuple(range(5))
from_str   = tuple("abc")
print(from_list)   # (1, 2, 3)
print(from_range)  # (0, 1, 2, 3, 4)
print(from_str)    # ('a', 'b', 'c')

# Packing without parentheses (Python infers tuple)
packed = 1, 2, 3
print(packed, type(packed))    # (1, 2, 3) <class 'tuple'>

# ── Indexing & Slicing (same as list) ────────────────────────
t = (10, 20, 30, 40, 50)

print(t[0])      # 10
print(t[-1])     # 50
print(t[1:4])    # (20, 30, 40)
print(t[::-1])   # (50, 40, 30, 20, 10)
print(t[::2])    # (10, 30, 50)

# Nested indexing
matrix = ((1, 2, 3), (4, 5, 6))
print(matrix[1][2])   # 6

# ── IMMUTABILITY ─────────────────────────────────────────────
t = (1, 2, 3)
# t[0] = 99     # ❌ TypeError: 'tuple' object does not support item assignment
# t.append(4)   # ❌ AttributeError

# But if tuple holds a mutable object, that object CAN change
t_with_list = (1, [2, 3], 4)
t_with_list[1].append(99)
print(t_with_list)   # (1, [2, 3, 99], 4) ← inner list changed!

# ── TUPLE METHODS (only 2) ───────────────────────────────────
t = (1, 2, 3, 2, 4, 2, 5)

print(t.count(2))     # 3  — how many times 2 appears
print(t.index(4))     # 4  — index of first occurrence of 4
# print(t.index(99))  # ❌ ValueError

# ── TUPLE UNPACKING ──────────────────────────────────────────
coords = (10, 20, 30)
x, y, z = coords
print(x, y, z)   # 10 20 30

# Swap using tuple unpacking
a, b = 5, 10
a, b = b, a
print(a, b)   # 10 5

# Extended unpacking with * (star)
first, *rest = (1, 2, 3, 4, 5)
print(first)   # 1
print(rest)    # [2, 3, 4, 5]  ← becomes a list

*start, last = (1, 2, 3, 4, 5)
print(start)   # [1, 2, 3, 4]
print(last)    # 5

first, *middle, last = (10, 20, 30, 40, 50)
print(first, middle, last)   # 10 [20, 30, 40] 50

# ── TUPLE vs LIST — When to use which? ───────────────────────
# Use TUPLE when:
#   - Data should NOT change (coordinates, RGB colors, DB records)
#   - You want to use it as a dict key (tuples are hashable)
#   - Slightly faster than list for iteration

# Use LIST when:
#   - You need to add/remove/modify elements

# Tuple as dict key (lists can't do this)
locations = {(28.7, 77.1): "Delhi", (19.0, 72.8): "Mumbai"}
print(locations[(28.7, 77.1)])   # Delhi

# ── BUILT-IN FUNCTIONS with tuples ───────────────────────────
t = (3, 1, 4, 1, 5, 9, 2, 6)
print(len(t))       # 8
print(min(t))       # 1
print(max(t))       # 9
print(sum(t))       # 31
print(sorted(t))    # [1, 1, 2, 3, 4, 5, 6, 9] ← returns list!

# ── Convert between tuple and list ───────────────────────────
my_list  = [1, 2, 3]
my_tuple = tuple(my_list)
back     = list(my_tuple)
print(my_tuple, back)

# ── Named Tuple (bonus — very useful in real projects) ────────
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "branch"])
s1 = Student("Abhishek", 20, "CSE AI/ML")

print(s1.name)     # Abhishek
print(s1.age)      # 20
print(s1[0])       # Abhishek  (index access still works)
print(s1)          # Student(name='Abhishek', age=20, branch='CSE AI/ML')
