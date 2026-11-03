"""Subtopic 7.8: Shallow copy and mutable versus immutable.
Notes: notes/c1-ch07-7.8-shallow-copy-bangla.md
       notes/c1-ch07-7.8-shallow-copy-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Copy the outer list, then copy each row.
# Problem 2: A new row and an inner-cell edit test different levels.
# Problem 3: Strings return new values instead of changing in place.
# Problem 4: Copy each customer's sales row before applying a correction.
# Problem 5: Make a row-by-row working table and compare totals.

# Problem 1 (Easy, LeetCode-style)
# Given a matrix of daily sales, return a copy whose first cell is corrected.
# The original matrix must remain unchanged.
sales_matrix_1 = [[12000, 9500], [8800, 13200]]

# Problem 2 (Easy, real-world business)
# The boss wants a working customer-day table. Add a new customer row and
# correct one existing cell without changing the audit table.
audit_table_2 = [[12000, 9500], [8800, 13200]]

# Problem 3 (Medium, interview-style)
# Explain mutable and immutable business values. Create a corrected invoice
# reference while preserving the original.
# Follow-up: why is a string replacement safer than character assignment?
invoice_reference_3 = "INV-2024-007"

# Problem 4 (Medium, real-world business)
# Apply a 500 correction to day two for each customer's copied sales row.
# The original customer table must remain available for audit.
customer_sales_4 = [[12000, 9500, 8800], [13200, 7500, 11000]]

# Problem 5 (Hard, real-world business)
# Prepare an adjusted management table. Copy every row, change day one for
# the first customer, add a new customer, and report both grand totals.
management_table_5 = [[12000, 9500], [8800, 13200], [7500, 6100]]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Copy every row.
# 2. Correct the first cell in the working matrix.
# 3. Print original and working matrices.
working_1 = [row[:] for row in sales_matrix_1]
working_1[0][0] = 13000
print(sales_matrix_1)
print(working_1)
# Expected:
# [[12000, 9500], [8800, 13200]]
# [[13000, 9500], [8800, 13200]]
# Key line: each row gets its own slice.
# Complexity: every cell row reference is copied across the table, O(n * m).

# Problem 2 solution
# Approach:
# 1. Copy every existing row.
# 2. Correct one inner cell.
# 3. Append a new row to the working table.
# 4. Print both tables.
working_2 = [row.copy() for row in audit_table_2]
working_2[1][1] = 14000
working_2.append([7500, 6100])
print(audit_table_2)
print(working_2)
# Expected:
# [[12000, 9500], [8800, 13200]]
# [[12000, 9500], [8800, 14000], [7500, 6100]]
# Key line: row copies protect the original inner lists.
# Complexity: copying the table is O(n * m), then edits are constant work.

# Problem 3 solution
# Approach:
# 1. Keep the old immutable string.
# 2. Build a new corrected string.
# 3. Print both values.
corrected_3 = invoice_reference_3.replace("007", "008")
print(invoice_reference_3)
print(corrected_3)
# Expected:
# INV-2024-007
# INV-2024-008
# Key line: replace returns a new string.
# Complexity: the work grows with the reference length, O(n).
# Interview talking point: immutable values make the original reference safe.

# Problem 4 solution
# Approach:
# 1. Copy every customer row.
# 2. Correct day two in each copied row.
# 3. Print original and adjusted tables.
adjusted_4 = [
    [day_one, day_two - 500, day_three]
    for day_one, day_two, day_three in customer_sales_4
]
print(customer_sales_4)
print(adjusted_4)
# Expected:
# [[12000, 9500, 8800], [13200, 7500, 11000]]
# [[12000, 9000, 8800], [13200, 7000, 11000]]
# Key line: each new row contains new values, so no inner row is shared.
# Complexity: every cell is read once, O(n * m).

# Problem 5 solution
# Approach:
# 1. Copy every row into a working table.
# 2. Correct the first customer’s first day.
# 3. Add a new customer row.
# 4. Calculate both grand totals.
working_5 = [row[:] for row in management_table_5]
working_5[0][0] = 13000
working_5.append([5000, 4200])
original_total_5 = sum(sum(row) for row in management_table_5)
working_total_5 = sum(sum(row) for row in working_5)
print(management_table_5)
print(working_5)
print(original_total_5)
print(working_total_5)
# Expected:
# [[12000, 9500], [8800, 13200], [7500, 6100]]
# [[13000, 9500], [8800, 13200], [7500, 6100], [5000, 4200]]
# 57100
# 67300
# Key lines: row copies protect the original, and nested sum totals rows.
# Complexity: copying and summing scan the table, O(n * m).
# Business talking point: report the audit total and working total separately.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
