# ============================================================
# 03 - f-Strings & String Formatting (Deep Dive)
# ============================================================

name = "Abhishek"
score = 95.678
rank = 1

# ── Basic f-string ───────────────────────────────────────────
print(f"Name: {name}")
print(f"Score: {score}")
print(f"Rank: {rank}")

# ── Expressions inside f-strings ─────────────────────────────
a, b = 10, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} ** {b} = {a ** b}")
print(f"Is even? {a % 2 == 0}")

# ── Formatting numbers ───────────────────────────────────────
pi = 3.14159265358979

print(f"{pi:.2f}")        # 3.14       (2 decimal places)
print(f"{pi:.5f}")        # 3.14159    (5 decimal places)
print(f"{pi:10.3f}")      # right-aligned in 10 chars
print(f"{pi:<10.3f}|")    # left-aligned
print(f"{pi:^10.3f}|")    # center-aligned

# Large numbers
big = 1234567.89
print(f"{big:,.2f}")      # 1,234,567.89  (comma separator)
print(f"{big:e}")         # 1.234568e+06  (scientific notation)

# Percentage
ratio = 0.875
print(f"{ratio:.1%}")     # 87.5%

# ── Padding strings ──────────────────────────────────────────
print(f"{name:>20}")      # right align
print(f"{name:<20}|")     # left align (default)
print(f"{name:^20}")      # center
print(f"{name:*^20}")     # center with * padding

# ── Integers in different bases ──────────────────────────────
n = 255
print(f"Decimal : {n:d}")
print(f"Binary  : {n:b}")
print(f"Octal   : {n:o}")
print(f"Hex     : {n:x}")    # lowercase
print(f"Hex     : {n:X}")    # uppercase
print(f"Hex     : {n:#x}")   # with 0x prefix

# ── Debug format (Python 3.8+) ───────────────────────────────
x = 42
print(f"{x = }")         # x = 42  (shows variable name + value)
print(f"{x * 2 = }")     # x * 2 = 84

# ── Multi-line f-strings ─────────────────────────────────────
student = {
    "name": "Abhishek",
    "branch": "CSE AI/ML",
    "college": "PCTE"
}
report = (
    f"Student: {student['name']}\n"
    f"Branch : {student['branch']}\n"
    f"College: {student['college']}"
)
print(report)

# ── .format() method (older but still used) ──────────────────
print("Hello, {}!".format("World"))
print("{0} + {1} = {2}".format(5, 3, 8))
print("{name} scored {score:.1f}".format(name="Abhishek", score=95.6))

# ── % formatting (legacy, good to know) ──────────────────────
print("Name: %s, Age: %d, GPA: %.1f" % ("Abhishek", 20, 8.9))
