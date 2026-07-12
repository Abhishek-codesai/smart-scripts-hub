# ============================================================
# 01 - Python Data Types Overview
# ============================================================

# Python has the following built-in data types:
# Text     : str
# Numeric  : int, float, complex
# Boolean  : bool
# Sequence : list, tuple, range
# Mapping  : dict
# Set      : set, frozenset
# Binary   : bytes, bytearray, memoryview
# None     : NoneType

# ── 1. int (Integer) ─────────────────────────────────────────
x = 10
y = -5
big = 1_000_000    # underscores for readability
binary = 0b1010    # binary literal  → 10
octal  = 0o17      # octal literal   → 15
hexa   = 0xFF      # hex literal     → 255

print(type(x))         # <class 'int'>
print(x, y, big)
print(binary, octal, hexa)

# Python int has no overflow — can be arbitrarily large
huge = 10 ** 100
print("Googol:", huge)

# ── 2. float ─────────────────────────────────────────────────
pi = 3.14
sci = 2.5e3     # scientific notation = 2500.0
neg = -0.001

print(type(pi))        # <class 'float'>
print(pi, sci, neg)

# Floating point precision issue (common gotcha)
print(0.1 + 0.2)              # 0.30000000000000004 (not exact!)
print(round(0.1 + 0.2, 2))   # 0.3 (fix with round)

# ── 3. complex ───────────────────────────────────────────────
c1 = 3 + 4j
c2 = complex(2, -1)

print(type(c1))          # <class 'complex'>
print(c1)                # (3+4j)
print(c1.real)           # 3.0
print(c1.imag)           # 4.0
print(abs(c1))           # magnitude = 5.0 (3-4-5 triangle)
print(c1 + c2)           # (5+3j)
print(c1.conjugate())    # (3-4j)

# ── 4. bool ──────────────────────────────────────────────────
is_active = True
is_closed = False

print(type(is_active))   # <class 'bool'>
print(True + True)       # 2  (bool is subclass of int)
print(True * 5)          # 5

# Falsy values in Python (evaluate to False)
print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool(None))    # False

# Truthy values
print(bool(1))       # True
print(bool("hi"))    # True
print(bool([0]))     # True (non-empty list)

# ── 5. NoneType ──────────────────────────────────────────────
result = None
print(type(result))       # <class 'NoneType'>
print(result is None)     # True (always use 'is' to check None)

# ── 6. type() and id() ───────────────────────────────────────
a = 42
print(type(a))            # <class 'int'>
print(id(a))              # memory address (unique identifier)

b = a
print(id(a) == id(b))    # True — same object (small int caching)
