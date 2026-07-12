# ============================================================
# 02 - Variables & Assignment
# ============================================================

# Variable naming rules:
# - Start with a letter or underscore
# - No spaces (use _ instead)
# - Case-sensitive

name = "Abhishek"
age = 20
gpa = 8.5
is_student = True

print(name, age, gpa, is_student)
print(type(name), type(age), type(gpa), type(is_student))

# Multiple assignment
x, y, z = 10, 20, 30
print(x, y, z)

# Same value to multiple variables
a = b = c = 100
print(a, b, c)

# Reassignment - Python is dynamically typed
var = 10
print(var, type(var))
var = "Now I'm a string"
print(var, type(var))

# Swapping variables (Pythonic way)
p, q = 5, 99
p, q = q, p
print("After swap:", p, q)

# Constants (by convention, use ALL_CAPS)
PI = 3.14159
MAX_SIZE = 100
print(PI, MAX_SIZE)
