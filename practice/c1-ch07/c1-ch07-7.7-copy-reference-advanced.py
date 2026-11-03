"""Subtopic 7.7: Copy vs reference, aliasing.
Notes: notes/c1-ch07-7.7-copy-reference-bangla.md
       notes/c1-ch07-7.7-copy-reference-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Assigning a second name does not copy the list.
# Problem 2: Use a slice before changing the working report.
# Problem 3: Keep the original balance list and copy it before removing items.
# Problem 4: Compare a reference with two flat-list copies.
# Problem 5: A shallow outer copy does not protect inner rows.

# Problem 1 (Easy, LeetCode-style)
# Given a list of daily sales, demonstrate what happens when a second
# name changes the first item. Input: a list. Output: both visible reports.
sales_1 = [12000, 9500, 8800, 13200, 7500]

# Problem 2 (Easy, real-world business)
# The boss wants an adjusted working report, but the original report must
# remain unchanged. Apply a 1000 correction to day one.
original_report_2 = [12000, 9500, 8800, 13200, 7500]

# Problem 3 (Medium, interview-style)
# Explain and demonstrate the difference between a reference and a copy
# for an audit list. Follow-up: why is a copy safer for audit evidence?
balances_3 = [50000, 32000, 71000]

# Problem 4 (Medium, real-world business)
# Prepare three versions of a weekly report: a shared review version,
# a slice copy, and a .copy() version. Add a different note to each.
weekly_report_4 = [5000, 4200, 6100, 3800]

# Problem 5 (Hard, real-world business)
# A sales table has customer rows. Produce an outer copy, then show why
# changing one inner cell still affects the original table.
sales_table_5 = [[12000, 9500, 8800], [13200, 7500, 11000]]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Give the sales list a second name.
# 2. Change one item through the second name.
# 3. Print both names.
review_1 = sales_1
review_1[0] = 13000
print(sales_1)
print(review_1)
# Expected:
# [13000, 9500, 8800, 13200, 7500]
# [13000, 9500, 8800, 13200, 7500]
# Key line: review_1 = sales_1 creates an alias.
# Complexity: one item change is constant work, O(1).

# Problem 2 solution
# Approach:
# 1. Make a slice copy.
# 2. Change only the working copy.
# 3. Print both reports.
working_2 = original_report_2[:]
working_2[0] -= 1000
print(original_report_2)
print(working_2)
# Expected:
# [12000, 9500, 8800, 13200, 7500]
# [11000, 9500, 8800, 13200, 7500]
# Key line: [:] creates a separate flat list.
# Complexity: copying five items grows with list size, O(n).

# Problem 3 solution
# Approach:
# 1. Keep one reference and one copy.
# 2. Remove an item from each working version.
# 3. Compare the original balance list.
reference_3 = balances_3
copy_3 = balances_3.copy()
reference_3.pop()
copy_3.pop()
print(balances_3)
print(copy_3)
# Expected:
# [50000, 32000]
# [50000, 32000]
# Key line: the reference removal also changes balances_3.
# Complexity: copying is O(n), while pop() from the end is O(1).
# Interview talking point: audit evidence needs an independent copy.

# Problem 4 solution
# Approach:
# 1. Create an alias and two independent copies.
# 2. Append a different report marker to each.
# 3. Print all three results.
shared_4 = weekly_report_4
slice_4 = weekly_report_4[:]
method_4 = weekly_report_4.copy()
shared_4.append(9999)
slice_4.append(8888)
method_4.append(7777)
print(weekly_report_4)
print(slice_4)
print(method_4)
# Expected:
# [5000, 4200, 6100, 3800, 9999]
# [5000, 4200, 6100, 3800, 8888]
# [5000, 4200, 6100, 3800, 7777]
# Key line: only the shared version changes the source.
# Complexity: each copy scans the list, O(n).

# Problem 5 solution
# Approach:
# 1. Copy the outer table with a slice.
# 2. Change one cell in the copied table.
# 3. Print both tables.
outer_copy_5 = sales_table_5[:]
outer_copy_5[0][0] = 13000
print(sales_table_5)
print(outer_copy_5)
# Expected:
# [[13000, 9500, 8800], [13200, 7500, 11000]]
# [[13000, 9500, 8800], [13200, 7500, 11000]]
# Key line: the inner customer row is still shared.
# Complexity: the outer copy is O(n), but it does not copy inner cells.
# Business talking point: a nested table needs a deeper copying strategy.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
