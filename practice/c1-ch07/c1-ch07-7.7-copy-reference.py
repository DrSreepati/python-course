"""Subtopic 7.7: Copy vs reference, aliasing.
Notes: notes/c1-ch07-7.7-copy-reference-bangla.md
       notes/c1-ch07-7.7-copy-reference-english.md
"""

# Program 1: an alias shares changes.
sales = [12000, 9500, 8800]
alias = sales
alias[0] = 13000
print(sales)  # Expected: [13000, 9500, 8800]
print(alias)  # Expected: [13000, 9500, 8800]

# Program 2: a slice creates an independent flat list.
report = [12000, 9500, 8800]
working_report = report[:]
working_report[0] = 13000
print(report)  # Expected: [12000, 9500, 8800]
print(working_report)  # Expected: [13000, 9500, 8800]

# Program 3: .copy() creates an independent flat list.
balances = [50000, 32000, 71000]
audit_balances = balances.copy()
audit_balances.pop()
print(balances)  # Expected: [50000, 32000, 71000]
print(audit_balances)  # Expected: [50000, 32000]

# Program 4: shallow copies do not separate nested rows.
table = [[12000, 9500], [8800, 13200]]
table_copy = table[:]
table_copy[0][0] = 13000
print(table)  # Expected: [[13000, 9500], [8800, 13200]]

# Task 1: Show an alias changing the original report.
# Task 2: Make an independent report with a slice.
# Task 3: Make an audit balance copy with .copy().
# Task 4: Compare an alias, a slice copy, and a method copy.
# Task 5: Fix Sreepati's original-report aliasing bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
report = [12000, 9500, 8800]
alias = report
alias.append(13200)
print(report)
# Expected: [12000, 9500, 8800, 13200]

# Task 2
report = [12000, 9500, 8800]
working = report[:]
working[0] = 13000
print(report)
print(working)
# Expected:
# [12000, 9500, 8800]
# [13000, 9500, 8800]

# Task 3
balances = [50000, 32000, 71000]
audit = balances.copy()
audit.pop()
print(balances)
print(audit)
# Expected:
# [50000, 32000, 71000]
# [50000, 32000]

# Task 4
sales = [12000, 9500]
alias = sales
slice_copy = sales[:]
method_copy = sales.copy()
alias.append(8800)
slice_copy.append(13200)
method_copy.append(7500)
print(sales)
print(slice_copy)
print(method_copy)
# Expected:
# [12000, 9500, 8800]
# [12000, 9500, 13200]
# [12000, 9500, 7500]

# Task 5
original = [12000, 9500, 8800]
working = original.copy()
working.pop()
print(original)
print(working)
# Expected:
# [12000, 9500, 8800]
# [12000, 9500]
"""
# Change the values and rerun. Safe reporting grows from careful copying.
