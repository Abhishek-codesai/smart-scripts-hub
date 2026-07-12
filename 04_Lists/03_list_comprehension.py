# ============================================================
# 03 - List Comprehension (Pythonic way to build lists)
# ============================================================

# Syntax: [expression for item in iterable if condition]

# ── Basic examples ───────────────────────────────────────────

# Without list comprehension (traditional)
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)   # [1, 4, 9, 16, 25]

# With list comprehension (Pythonic)
squares = [i ** 2 for i in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# Characters of a string
chars = [c for c in "Python"]
print(chars)     # ['P', 'y', 't', 'h', 'o', 'n']

# Multiply each element
nums = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in nums]
print(doubled)   # [2, 4, 6, 8, 10]

# ── With condition (filter) ──────────────────────────────────
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)     # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Odd numbers
odds = [x for x in range(20) if x % 2 != 0]
print(odds)

# Words longer than 3 letters
words = ["hi", "hello", "bye", "goodbye", "ok", "python"]
long_words = [w for w in words if len(w) > 3]
print(long_words)   # ['hello', 'goodbye', 'python']

# ── With transformation + condition ──────────────────────────
# Square of even numbers only
sq_evens = [x**2 for x in range(1, 11) if x % 2 == 0]
print(sq_evens)   # [4, 16, 36, 64, 100]

# Upper-case fruits that start with 'b'
fruits = ["apple", "banana", "blueberry", "cherry", "blackberry"]
b_fruits = [f.upper() for f in fruits if f.startswith("b")]
print(b_fruits)   # ['BANANA', 'BLUEBERRY', 'BLACKBERRY']

# ── Nested list comprehension ────────────────────────────────
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3x3 multiplication table
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for row in table:
    print(row)

# ── if-else in comprehension ─────────────────────────────────
# Label numbers as even/odd
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 8)]
print(labels)   # ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

# Replace negatives with 0
data = [3, -1, 4, -1, 5, -9, 2, 6]
clean = [x if x >= 0 else 0 for x in data]
print(clean)   # [3, 0, 4, 0, 5, 0, 2, 6]
