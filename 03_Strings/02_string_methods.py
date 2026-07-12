# ============================================================
# 02 - String Methods (Complete Reference)
# ============================================================

# ── CASE METHODS ─────────────────────────────────────────────
s = "hello WORLD python"

print(s.upper())          # HELLO WORLD PYTHON
print(s.lower())          # hello world python
print(s.title())          # Hello World Python
print(s.capitalize())     # Hello world python  (only first letter)
print(s.swapcase())       # HELLO world PYTHON

# ── SEARCH & CHECK METHODS ───────────────────────────────────
text = "Python is fun and Python is powerful"

print(text.find("Python"))      # 0   (first occurrence index)
print(text.find("Java"))        # -1  (not found)
print(text.rfind("Python"))     # 18  (last occurrence)
print(text.index("fun"))        # 10  (like find but raises error if not found)
# text.index("Java")            # ❌ ValueError

print(text.count("Python"))     # 2   (how many times)
print(text.startswith("Python")) # True
print(text.endswith("ful"))      # True
print(text.startswith("Java"))   # False

# ── STRIP METHODS ────────────────────────────────────────────
raw = "   Hello World   "
print(raw.strip())      # "Hello World"   (removes both sides)
print(raw.lstrip())     # "Hello World   " (left only)
print(raw.rstrip())     # "   Hello World" (right only)

# Strip specific characters
messy = "###Python###"
print(messy.strip("#"))   # Python

# ── REPLACE ──────────────────────────────────────────────────
sentence = "I like cats and cats like me"
print(sentence.replace("cats", "dogs"))          # replace all
print(sentence.replace("cats", "dogs", 1))      # replace first only

# ── SPLIT & JOIN ─────────────────────────────────────────────
csv_line = "Abhishek,20,CSE,Ludhiana"
parts = csv_line.split(",")
print(parts)               # ['Abhishek', '20', 'CSE', 'Ludhiana']
print(type(parts))         # <class 'list'>

# split with maxsplit
print("a-b-c-d".split("-", 2))   # ['a', 'b', 'c-d']

# splitlines
multi = "line1\nline2\nline3"
print(multi.splitlines())   # ['line1', 'line2', 'line3']

# join (opposite of split)
words = ["Python", "is", "awesome"]
print(" ".join(words))      # Python is awesome
print("-".join(words))      # Python-is-awesome
print("".join(words))       # Pythonisawesome

# ── IS... BOOLEAN METHODS ────────────────────────────────────
print("hello".isalpha())      # True  — only letters
print("hello123".isalpha())   # False
print("12345".isdigit())      # True  — only digits
print("12.5".isdigit())       # False (dot is not digit)
print("12345".isnumeric())    # True
print("hello123".isalnum())   # True  — letters + digits only
print("   ".isspace())        # True  — only whitespace
print("Hello".istitle())      # True  — title case
print("HELLO".isupper())      # True
print("hello".islower())      # True
print("abc123".isidentifier())# True  — valid Python variable name?

# ── ALIGNMENT / PADDING ──────────────────────────────────────
name = "Python"
print(name.center(20))          # "       Python       "
print(name.center(20, "*"))     # "*******Python*******"
print(name.ljust(20, "."))      # "Python.............."
print(name.rjust(20, "."))      # "..............Python"
print("42".zfill(6))            # "000042" (zero-fill)

# ── ENCODE ───────────────────────────────────────────────────
s = "Hello"
encoded = s.encode("utf-8")
print(encoded)                  # b'Hello'
print(encoded.decode("utf-8"))  # Hello

# ── PARTITION ────────────────────────────────────────────────
email = "abhishek@gmail.com"
print(email.partition("@"))    # ('abhishek', '@', 'gmail.com')
print(email.rpartition("."))   # ('abhishek@gmail', '.', 'com')

# ── FORMAT ───────────────────────────────────────────────────
template = "Name: {name}, Age: {age}"
print(template.format(name="Abhishek", age=20))

# ── MISC ─────────────────────────────────────────────────────
print("  hello  ".strip())               # hello
print("Python".expandtabs(4))            # expands \t to spaces
print(len("Python"))                     # 6
print(ord("A"))                          # 65  (char → ASCII)
print(chr(65))                           # A   (ASCII → char)
