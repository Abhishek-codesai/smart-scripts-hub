# ============================================================
# 04 - Input & Output in Python
# ============================================================

# ── input() always returns a string ──────────────────────────
name = input("Enter your name: ")
print("Hello,", name)

# Convert input to int or float
age = int(input("Enter your age: "))
print("Next year you'll be:", age + 1)

price = float(input("Enter price: "))
print("With 18% GST:", price * 1.18)

# ── Output formatting ────────────────────────────────────────

# 1. Concatenation (old way - only works with strings)
lang = "Python"
print("I love " + lang + "!")

# 2. , separator (adds space automatically)
version = 3.11
print("Version:", version)

# 3. f-strings (RECOMMENDED - modern & clean)
student = "Abhishek"
score = 95.5
print(f"Student: {student} | Score: {score}")
print(f"Score out of 100: {score:.2f}")   # 2 decimal places
print(f"10 + 5 = {10 + 5}")               # expression inside

# 4. .format() method
print("Name: {} | Age: {}".format("Abhishek", 20))
print("Name: {0} | Branch: {1}".format("Abhishek", "CSE AI/ML"))

# 5. % formatting (old style, rarely used)
print("Name: %s | Age: %d | GPA: %.2f" % ("Abhishek", 20, 8.5))

# ── Formatting numbers ───────────────────────────────────────
pi = 3.14159265
print(f"Pi = {pi:.4f}")          # 3.1416 (4 decimal places)
print(f"Pi = {pi:10.2f}")        # right-aligned in 10 chars
print(f"Pi = {pi:<10.2f}|")      # left-aligned
print(f"Large: {1000000:,}")     # 1,000,000 with comma separator
print(f"Binary of 10: {10:b}")   # 1010
print(f"Hex of 255: {255:x}")    # ff
