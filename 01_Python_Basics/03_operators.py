# ============================================================
# 03 - Operators in Python
# ============================================================

# ── 1. Arithmetic Operators ──────────────────────────────────
a, b = 15, 4

print("Addition       :", a + b)    # 19
print("Subtraction    :", a - b)    # 11
print("Multiplication :", a * b)    # 60
print("Division       :", a / b)    # 3.75  (always float)
print("Floor Division :", a // b)   # 3     (removes decimal)
print("Modulus        :", a % b)    # 3     (remainder)
print("Exponent       :", a ** b)   # 50625 (a to the power b)

# ── 2. Comparison Operators (return True/False) ──────────────
x, y = 10, 20
print(x == y)    # False - equal
print(x != y)    # True  - not equal
print(x > y)     # False
print(x < y)     # True
print(x >= 10)   # True
print(y <= 20)   # True

# ── 3. Logical Operators ─────────────────────────────────────
p, q = True, False
print(p and q)   # False - both must be True
print(p or q)    # True  - at least one True
print(not p)     # False - reverses the boolean

# Practical example
age = 20
has_id = True
print("Can enter:", age >= 18 and has_id)

# ── 4. Assignment Operators ──────────────────────────────────
n = 10
n += 5;   print("+=  :", n)    # 15
n -= 3;   print("-=  :", n)    # 12
n *= 2;   print("*=  :", n)    # 24
n //= 5;  print("//= :", n)    # 4
n **= 3;  print("**= :", n)    # 64
n %= 10;  print("%=  :", n)    # 4

# ── 5. Bitwise Operators ─────────────────────────────────────
i, j = 6, 3   # 6 = 110, 3 = 011 in binary
print("AND  :", i & j)   # 010 = 2
print("OR   :", i | j)   # 111 = 7
print("XOR  :", i ^ j)   # 101 = 5
print("NOT  :", ~i)      # -(6+1) = -7
print("L Shift:", i << 1) # 1100 = 12
print("R Shift:", i >> 1) # 011  = 3

# ── 6. Membership Operators ──────────────────────────────────
fruits = ["apple", "mango", "banana"]
print("mango" in fruits)       # True
print("grape" not in fruits)   # True

# ── 7. Identity Operators ────────────────────────────────────
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst1

print(lst1 is lst3)     # True  - same object in memory
print(lst1 is lst2)     # False - same content, different object
print(lst1 is not lst2) # True
