# ============================================================
# 01 - Sets: Creation, Methods & Set Operations
# ============================================================

# A Set is:
#   - Unordered   (no guaranteed order)
#   - Unique items (no duplicates)
#   - Mutable     (you can add/remove)
#   - NOT subscriptable (no indexing or slicing)

# ── Creating Sets ────────────────────────────────────────────
empty  = set()          # ← MUST use set(), NOT {} (that's a dict!)
nums   = {1, 2, 3, 4, 5}
mixed  = {1, "hello", 3.14, True}

# Duplicates are automatically removed
dupes  = {1, 2, 2, 3, 3, 3, 4}
print(dupes)   # {1, 2, 3, 4}

# From other iterables
from_list   = set([1, 2, 2, 3])
from_string = set("banana")      # unique chars only
from_tuple  = set((1, 2, 3))

print(from_list)    # {1, 2, 3}
print(from_string)  # {'b', 'a', 'n'} — order not guaranteed

print(type(nums))   # <class 'set'>

# ── ADDING ELEMENTS ──────────────────────────────────────────
s = {1, 2, 3}

s.add(4)           # add ONE item
print(s)           # {1, 2, 3, 4}

s.add(2)           # already exists — silently ignored
print(s)           # {1, 2, 3, 4}

s.update([5, 6, 7])     # add multiple items from iterable
print(s)                # {1, 2, 3, 4, 5, 6, 7}

s.update({10, 11}, [8, 9])   # can pass multiple iterables
print(s)

# ── REMOVING ELEMENTS ────────────────────────────────────────
s = {1, 2, 3, 4, 5}

s.remove(3)        # removes 3
print(s)           # {1, 2, 4, 5}
# s.remove(99)     # ❌ KeyError if not found

s.discard(4)       # removes 4 — NO error if not found
s.discard(99)      # silently does nothing
print(s)           # {1, 2, 5}

val = s.pop()      # removes and returns a RANDOM element
print(val)         # unpredictable which one
print(s)

s.clear()          # removes ALL items
print(s)           # set()

# ── SEARCHING ────────────────────────────────────────────────
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)       # True
print("grape" not in fruits)   # True
print(len(fruits))             # 3

# ── COPY ─────────────────────────────────────────────────────
original = {1, 2, 3}
copy     = original.copy()
copy.add(99)
print(original)   # {1, 2, 3}  — unchanged

# ── FROZEN SET (immutable version of set) ────────────────────
fs = frozenset([1, 2, 3, 4])
print(fs)                  # frozenset({1, 2, 3, 4})
# fs.add(5)                # ❌ AttributeError — can't modify
print(2 in fs)             # True

# ── SET MATHEMATICAL OPERATIONS ──────────────────────────────
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union (all items from both)
print(A | B)              # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))         # same result

# Intersection (common items)
print(A & B)              # {4, 5}
print(A.intersection(B))  # same

# Difference (in A but NOT in B)
print(A - B)              # {1, 2, 3}
print(A.difference(B))    # same

# Difference (in B but NOT in A)
print(B - A)              # {6, 7, 8}

# Symmetric Difference (in A or B but NOT both)
print(A ^ B)                          # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))      # same

# ── UPDATE VERSIONS (modify the set in place) ────────────────
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.intersection_update(B)         # A = A ∩ B
print(A)    # {3, 4}

A = {1, 2, 3, 4}
A.difference_update(B)           # A = A - B
print(A)    # {1, 2}

A = {1, 2, 3, 4}
A.symmetric_difference_update(B) # A = A △ B
print(A)    # {1, 2, 5, 6}

# ── COMPARISON OPERATIONS ────────────────────────────────────
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}

print(A.issubset(B))      # True  — A ⊆ B (all of A in B)
print(B.issuperset(A))    # True  — B ⊇ A (B contains all of A)
print(A == C)             # True  — same elements
print(A.isdisjoint({6, 7})) # True — no common elements

# ── PRACTICAL USE CASES ──────────────────────────────────────

# 1. Remove duplicates from a list
lst = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(lst))
print(unique)   # [1, 2, 3, 4] (order may vary)

# 2. Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = set(list1) & set(list2)
print(common)   # {3, 4, 5}

# 3. Find unique elements across two lists
all_unique = set(list1) | set(list2)
print(all_unique)

# ── SUMMARY ──────────────────────────────────────────────────
# Method              Description
# add(x)              Add single element
# update(iter)        Add multiple elements
# remove(x)           Remove (KeyError if absent)
# discard(x)          Remove (no error if absent)
# pop()               Remove & return random element
# clear()             Remove all
# copy()              Shallow copy
# union(B)            A | B
# intersection(B)     A & B
# difference(B)       A - B
# symmetric_difference(B) A ^ B
# issubset(B)         A ⊆ B
# issuperset(B)       A ⊇ B
# isdisjoint(B)       No common elements
