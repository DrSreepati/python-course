"""Subtopic 7.8: Shallow copy and mutable versus immutable.
Notes: notes/c1-ch07-7.8-shallow-copy-bangla.md
       notes/c1-ch07-7.8-shallow-copy-english.md
"""

# Program 1: a mutable list changes in place.
sales = [12000, 9500, 8800]
sales[1] = 10000
print(sales)  # Expected: [12000, 10000, 8800]

# Program 2: a string creates a new value.
code = "C-1023"
updated_code = code.replace("1023", "2048")
print(code)  # Expected: C-1023
print(updated_code)  # Expected: C-2048

# Program 3: an outer copy protects a new row.
table = [[12000, 9500], [8800, 13200]]
outer_copy = table[:]
outer_copy.append([7500, 6100])
print(table)  # Expected: [[12000, 9500], [8800, 13200]]
print(outer_copy)  # Expected: [[12000, 9500], [8800, 13200], [7500, 6100]]

# Program 4: copy every row before changing a cell.
safe_table = [row[:] for row in table]
safe_table[0][0] = 13000
print(table)  # Expected: [[12000, 9500], [8800, 13200]]
print(safe_table)  # Expected: [[13000, 9500], [8800, 13200]]

# Task 1: Copy a flat sales list and change its first item.
# Task 2: Make an outer copy and append a new table row.
# Task 3: Copy every row and change one cell.
# Task 4: Build a corrected invoice code without changing the old code.
# Task 5: Fix Sreepati's shared-inner-row bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
sales = [12000, 9500, 8800]
working = sales.copy()
working[0] = 13000
print(sales)
print(working)
# Expected:
# [12000, 9500, 8800]
# [13000, 9500, 8800]

# Task 2
table = [[12000, 9500], [8800, 13200]]
working = table[:]
working.append([7500, 6100])
print(table)
print(working)
# Expected:
# [[12000, 9500], [8800, 13200]]
# [[12000, 9500], [8800, 13200], [7500, 6100]]

# Task 3
table = [[12000, 9500], [8800, 13200]]
working = [row.copy() for row in table]
working[1][0] = 9000
print(table)
print(working)
# Expected:
# [[12000, 9500], [8800, 13200]]
# [[12000, 9500], [9000, 13200]]

# Task 4
code = "INV-2024-007"
corrected = code.replace("007", "008")
print(code)
print(corrected)
# Expected:
# INV-2024-007
# INV-2024-008

# Task 5
original = [[12000, 9500], [8800, 13200]]
working = [row[:] for row in original]
working[0][0] = 13000
print(original)
print(working)
# Expected:
# [[12000, 9500], [8800, 13200]]
# [[13000, 9500], [8800, 13200]]
"""
# Change the values and rerun. Safe table work grows from careful copies.
