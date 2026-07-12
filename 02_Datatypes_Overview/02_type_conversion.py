# ============================================================
# 02 - Type Conversion (Casting)
# ============================================================

# ── Implicit Conversion (Python does it automatically) ────────
a = 5       # int
b = 2.5     # float
result = a + b
print(result, type(result))   # 7.5 <class 'float'>

# ── Explicit Conversion (you do it manually) ─────────────────

# int()
print(int(3.9))       # 3   → truncates, does NOT round
print(int(-3.9))      # -3
print(int("42"))      # 42  → string to int
print(int(True))      # 1
print(int(False))     # 0
# print(int("3.5"))   # ❌ ValueError — can't skip float step

# float()
print(float(5))       # 5.0
print(float("3.14"))  # 3.14
print(float(True))    # 1.0

# str()
print(str(100))       # "100"
print(str(3.14))      # "3.14"
print(str(True))      # "True"

# bool()
print(bool(0))        # False
print(bool(42))       # True
print(bool(""))       # False
print(bool("False"))  # True ← "False" string is truthy!

# complex()
print(complex(3, 4))  # (3+4j)
print(complex("3+4j"))# (3+4j)

# ── Common use case: input() always gives string ─────────────
# age = input("Enter age: ")
# age = int(age)   # convert before using in arithmetic

# ── Converting between int bases ─────────────────────────────
num = 255
print(bin(num))    # '0b11111111'
print(oct(num))    # '0o377'
print(hex(num))    # '0xff'

# From binary/hex string back to int
print(int('11111111', 2))   # 255
print(int('ff', 16))        # 255
print(int('377', 8))        # 255
