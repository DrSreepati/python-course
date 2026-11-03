"""
Course 1, Chapter 8, Subtopic 8.4: Set operations
Notes: c1-ch08-8.4-set-operations-bangla.md and
       c1-ch08-8.4-set-operations-english.md
"""

sales = {"INV-2024-007", "INV-2024-008", "INV-2024-009"}
payments = {"INV-2024-008", "INV-2024-009", "INV-2024-010"}

print("Matched:", sorted(sales & payments))
print("Sales without payment:", sorted(sales - payments))
print("Payment register extra:", sorted(payments - sales))
print("All exceptions:", sorted(sales ^ payments))
# Expected:
# Matched: ['INV-2024-008', 'INV-2024-009']
# Sales without payment: ['INV-2024-007']
# Payment register extra: ['INV-2024-010']
# All exceptions: ['INV-2024-007', 'INV-2024-010']

branch_a = {"C-101", "C-102"}
branch_b = {"C-102", "C-103"}
print("All customers:", sorted(branch_a | branch_b))
print("Shared customers:", sorted(branch_a & branch_b))
# Expected:
# All customers: ['C-101', 'C-102', 'C-103']
# Shared customers: ['C-102']

# Task 1: Find all unique invoice IDs from two daily reports.
# Task 2: Find invoice IDs present in both a sales and a payment set.
# Task 3: Find sales IDs with no matching payment ID.
# Task 4: Find IDs belonging to exactly one of two branches.
# Task 5: Correct Sreepati's use of union when he needs matched invoices.

# ===== SOLUTIONS (try first, then compare) =====

# Task 1 solution
day_one = {"INV-01", "INV-02", "INV-03"}
day_two = {"INV-03", "INV-04"}
print(sorted(day_one | day_two))
# Expected: ['INV-01', 'INV-02', 'INV-03', 'INV-04']

# Task 2 solution
sales_report = {"INV-01", "INV-02", "INV-03"}
payment_report = {"INV-02", "INV-04"}
print(sorted(sales_report & payment_report))
# Expected: ['INV-02']

# Task 3 solution
print(sorted(sales_report - payment_report))
# Expected: ['INV-01', 'INV-03']

# Task 4 solution
dhaka = {"C-101", "C-102"}
chattogram = {"C-102", "C-104"}
print(sorted(dhaka ^ chattogram))
# Expected: ['C-101', 'C-104']

# Task 5 solution
sreepati_sales = {"INV-01", "INV-02"}
sreepati_payments = {"INV-02", "INV-03"}
print(sorted(sreepati_sales & sreepati_payments))
# Expected: ['INV-02']

# Change the data and rerun. Real skill grows in the variations, not the copies.
