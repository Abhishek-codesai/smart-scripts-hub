# ============================================================
# 01 - Quick Reference: All Data Type Conversions
# ============================================================

print("=" * 55)
print("PYTHON DATA TYPES — QUICK REFERENCE")
print("=" * 55)

# ── 1. Everything → int ──────────────────────────────────────
print("\n--- To int ---")
print(int(3.9))          # 3      (truncates)
print(int("42"))         # 42
print(int(True))         # 1
print(int(False))        # 0
print(int("0xFF", 16))   # 255   (hex string)
print(int("1010", 2))    # 10    (binary string)

# ── 2. Everything → float ────────────────────────────────────
print("\n--- To float ---")
print(float(5))          # 5.0
print(float("3.14"))     # 3.14
print(float(True))       # 1.0
print(float("1e3"))      # 1000.0

# ── 3. Everything → str ──────────────────────────────────────
print("\n--- To str ---")
print(str(100))          # '100'
print(str(3.14))         # '3.14'
print(str([1,2,3]))      # '[1, 2, 3]'
print(str(True))         # 'True'
print(str(None))         # 'None'

# ── 4. Everything → list ─────────────────────────────────────
print("\n--- To list ---")
print(list("hello"))         # ['h','e','l','l','o']
print(list((1, 2, 3)))       # [1, 2, 3]
print(list({1, 2, 3}))       # [1, 2, 3] (order may vary)
print(list(range(5)))        # [0, 1, 2, 3, 4]
print(list({"a":1,"b":2}))   # ['a', 'b']  (just keys!)

# ── 5. Everything → tuple ────────────────────────────────────
print("\n--- To tuple ---")
print(tuple([1, 2, 3]))      # (1, 2, 3)
print(tuple("abc"))          # ('a', 'b', 'c')
print(tuple({10, 20}))       # (10, 20)

# ── 6. Everything → set ──────────────────────────────────────
print("\n--- To set ---")
print(set([1, 2, 2, 3]))     # {1, 2, 3}
print(set("banana"))         # {'b', 'a', 'n'}
print(set((1, 1, 2, 3)))     # {1, 2, 3}

# ── 7. Everything → dict ─────────────────────────────────────
print("\n--- To dict ---")
print(dict([("a", 1), ("b", 2)]))     # from list of tuples
print(dict(zip(["x","y"], [1, 2])))   # from zip

# ── 8. bool conversions ──────────────────────────────────────
print("\n--- Truthy / Falsy ---")
falsy_values = [0, 0.0, "", [], {}, set(), tuple(), None, False]
for v in falsy_values:
    print(f"bool({repr(v):12}) = {bool(v)}")

print()
truthy_values = [1, -1, "hi", [0], {"a": 1}, {0}, (0,), True]
for v in truthy_values:
    print(f"bool({repr(v):12}) = {bool(v)}")

# ── 9. Summary table ─────────────────────────────────────────
print("\n" + "=" * 55)
print("SUMMARY: Python Data Types")
print("=" * 55)
print(f"{'Type':<12} {'Mutable':<10} {'Ordered':<10} {'Duplicates'}")
print("-" * 55)
print(f"{'int':<12} {'No':<10} {'—':<10} {'—'}")
print(f"{'float':<12} {'No':<10} {'—':<10} {'—'}")
print(f"{'complex':<12} {'No':<10} {'—':<10} {'—'}")
print(f"{'bool':<12} {'No':<10} {'—':<10} {'—'}")
print(f"{'str':<12} {'No':<10} {'Yes':<10} {'Yes'}")
print(f"{'list':<12} {'Yes':<10} {'Yes':<10} {'Yes'}")
print(f"{'tuple':<12} {'No':<10} {'Yes':<10} {'Yes'}")
print(f"{'set':<12} {'Yes':<10} {'No':<10} {'No'}")
print(f"{'frozenset':<12} {'No':<10} {'No':<10} {'No'}")
print(f"{'dict':<12} {'Yes':<10} {'Yes':<10} {'Keys: No'}")
