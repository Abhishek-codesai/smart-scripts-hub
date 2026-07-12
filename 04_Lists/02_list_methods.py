# ============================================================
# 02 - List Methods (Complete Reference)
# ============================================================

# ── ADDING ELEMENTS ──────────────────────────────────────────
fruits = ["apple", "banana"]

# append() - adds ONE item at the END
fruits.append("cherry")
print(fruits)       # ['apple', 'banana', 'cherry']

# insert(index, item) - inserts at specific position
fruits.insert(1, "mango")
print(fruits)       # ['apple', 'mango', 'banana', 'cherry']

# extend() - adds ALL items from another iterable
fruits.extend(["kiwi", "grape"])
print(fruits)       # [..., 'kiwi', 'grape']

# difference: append vs extend
lst = [1, 2, 3]
lst.append([4, 5])    # adds list AS ONE item: [1,2,3,[4,5]]
print(lst)

lst2 = [1, 2, 3]
lst2.extend([4, 5])   # adds each item: [1,2,3,4,5]
print(lst2)

# ── REMOVING ELEMENTS ────────────────────────────────────────
nums = [10, 20, 30, 20, 40, 50]

# remove(value) - removes FIRST occurrence of value
nums.remove(20)
print(nums)   # [10, 30, 20, 40, 50]

# pop(index) - removes and RETURNS item at index
val = nums.pop()     # default: last item
print(val)           # 50
print(nums)          # [10, 30, 20, 40]

val = nums.pop(1)    # remove at index 1
print(val)           # 30
print(nums)          # [10, 20, 40]

# del - remove by index or slice
lst = [1, 2, 3, 4, 5]
del lst[0]           # removes index 0
print(lst)           # [2, 3, 4, 5]
del lst[1:3]         # removes slice
print(lst)           # [2, 5]

# clear() - removes ALL items
lst.clear()
print(lst)    # []

# ── SEARCHING ────────────────────────────────────────────────
items = ["a", "b", "c", "b", "d"]

print(items.index("b"))      # 1  (index of first occurrence)
print(items.count("b"))      # 2  (how many times b appears)
# items.index("z")           # ❌ ValueError if not found

# ── SORTING ──────────────────────────────────────────────────
nums = [5, 2, 8, 1, 9, 3]

nums.sort()                 # ascending (modifies in place)
print(nums)                 # [1, 2, 3, 5, 8, 9]

nums.sort(reverse=True)     # descending
print(nums)                 # [9, 8, 5, 3, 2, 1]

words = ["banana", "apple", "cherry", "date"]
words.sort()                # alphabetical
print(words)

words.sort(key=len)         # sort by string length
print(words)

# sorted() — returns NEW sorted list, does NOT modify original
original = [3, 1, 4, 1, 5, 9]
new_sorted = sorted(original)
print(original)    # unchanged
print(new_sorted)  # [1, 1, 3, 4, 5, 9]

# ── REVERSING ────────────────────────────────────────────────
lst = [1, 2, 3, 4, 5]
lst.reverse()               # modifies in place
print(lst)                  # [5, 4, 3, 2, 1]

# reversed() gives an iterator, not a list
rev = list(reversed([1, 2, 3]))
print(rev)

# ── COPYING ──────────────────────────────────────────────────
original = [1, 2, 3]

# WRONG - this creates a reference, not a copy!
wrong_copy = original
wrong_copy.append(99)
print(original)     # [1, 2, 3, 99] — original ALSO changed!

# RIGHT - use copy() for shallow copy
original = [1, 2, 3]
right_copy = original.copy()
right_copy.append(99)
print(original)     # [1, 2, 3]  — unchanged
print(right_copy)   # [1, 2, 3, 99]

# Also: list(original) or original[:]
copy2 = list(original)
copy3 = original[:]

# For nested lists, use deepcopy
import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)

# ── SUMMARY TABLE ────────────────────────────────────────────
# Method          Returns   Modifies original?
# append(x)       None      Yes
# insert(i, x)    None      Yes
# extend(iter)    None      Yes
# remove(x)       None      Yes
# pop([i])        item      Yes
# clear()         None      Yes
# index(x)        int       No
# count(x)        int       No
# sort()          None      Yes
# reverse()       None      Yes
# copy()          list      No
