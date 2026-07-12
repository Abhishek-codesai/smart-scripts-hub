# ============================================================
# 01 - Strings: Creation, Indexing, Slicing
# ============================================================

# ── Creating Strings ──────────────────────────────────────────
s1 = 'single quotes'
s2 = "double quotes"
s3 = """triple quoted
spans multiple
lines"""
s4 = r"C:\Users\name\file.txt"   # raw string — backslash is literal
s5 = b"bytes string"              # bytes (not str)

print(s1, s2)
print(s3)
print(s4)
print(type(s5))   # <class 'bytes'>

# ── Escape Characters ─────────────────────────────────────────
print("Tab:\there")
print("Newline:\nhere")
print("Quote: \"Python\"")
print("Backslash: C:\\Users")
print("Unicode: \u00B2")    # ² superscript 2

# ── String Immutability ───────────────────────────────────────
name = "Python"
# name[0] = "J"   # ❌ TypeError: strings are immutable
name = "Jython"   # ✅ reassign entire string

# ── Indexing (0-based, supports negative) ─────────────────────
word = "ABCDEFG"
#        0123456
#       -7-6-5-4-3-2-1

print(word[0])     # A  (first)
print(word[-1])    # G  (last)
print(word[3])     # D
print(word[-3])    # E

# ── Slicing: string[start:stop:step] ─────────────────────────
s = "HelloWorld"

print(s[0:5])      # Hello      (stop is exclusive)
print(s[5:])       # World      (till end)
print(s[:5])       # Hello      (from beginning)
print(s[:])        # HelloWorld (full copy)
print(s[::2])      # HloWrd     (every 2nd character)
print(s[1:8:2])    # elWr
print(s[::-1])     # dlroWolleH (REVERSE the string)
print(s[-5:])      # World      (last 5 chars)

# ── len() ────────────────────────────────────────────────────
print(len("Hello"))   # 5
print(len(""))        # 0

# ── String repetition and concatenation ──────────────────────
print("Ha" * 3)            # HaHaHa
print("Hello" + " " + "World")  # Hello World

# ── in / not in ──────────────────────────────────────────────
msg = "Python is awesome"
print("Python" in msg)        # True
print("Java" not in msg)      # True
