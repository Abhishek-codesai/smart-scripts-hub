# ============================================================
# 01 - Lists: Creation, Indexing, Slicing
# ============================================================

# ── Creating Lists ───────────────────────────────────────────
empty = []
nums  = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]     # can hold any type
nested= [[1, 2], [3, 4], [5, 6]]           # list of lists

print(nums)
print(mixed)
print(nested)
print(type(nums))    # <class 'list'>

# list() constructor
from_range  = list(range(1, 11))     # [1, 2, 3, ..., 10]
from_string = list("Python")         # ['P','y','t','h','o','n']
from_tuple  = list((10, 20, 30))     # [10, 20, 30]
print(from_range)
print(from_string)

# ── Indexing ─────────────────────────────────────────────────
fruits = ["apple", "banana", "cherry", "mango", "kiwi"]
#          0        1          2         3        4
#         -5       -4         -3        -2       -1

print(fruits[0])     # apple
print(fruits[-1])    # kiwi
print(fruits[2])     # cherry

# Nested list indexing
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])   # 6  (row 1, col 2)
print(matrix[0][0])   # 1

# ── Slicing ──────────────────────────────────────────────────
nums = [10, 20, 30, 40, 50, 60, 70]

print(nums[1:4])      # [20, 30, 40]
print(nums[:3])       # [10, 20, 30]
print(nums[4:])       # [50, 60, 70]
print(nums[::2])      # [10, 30, 50, 70]  every 2nd
print(nums[::-1])     # [70, 60, 50, 40, 30, 20, 10]  reversed
print(nums[1:6:2])    # [20, 40, 60]

# ── len(), in, not in ────────────────────────────────────────
print(len(fruits))             # 5
print("mango" in fruits)       # True
print("grape" not in fruits)   # True

# ── Lists are MUTABLE ────────────────────────────────────────
colors = ["red", "green", "blue"]
colors[1] = "yellow"       # modify in place
print(colors)              # ['red', 'yellow', 'blue']

# Modify a slice
nums = [1, 2, 3, 4, 5]
nums[1:3] = [20, 30]
print(nums)    # [1, 20, 30, 4, 5]

# ── Concatenation & Repetition ───────────────────────────────
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)      # [1, 2, 3, 4, 5, 6]
print(a * 3)      # [1, 2, 3, 1, 2, 3, 1, 2, 3]
