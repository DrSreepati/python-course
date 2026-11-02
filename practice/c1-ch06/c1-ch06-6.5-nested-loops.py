"""Subtopic 6.5: Nested loops.
Notes: notes/c1-ch06-6.5-nested-loops-bangla.md
       notes/c1-ch06-6.5-nested-loops-english.md
"""

# Program 1: every customer and invoice
customers = ["Rahim Traders", "Karim Store"]
invoice_numbers = [1, 2]
for customer in customers:
    for invoice_number in invoice_numbers:
        print(f"{customer}: invoice {invoice_number}")

# Program 2: customer invoice totals
invoice_groups = [[12000, 8000], [7000, 5000]]
for amounts in invoice_groups:
    total = 0
    for amount in amounts:
        total += amount
    print(f"Group total: {total}")  # Expected: 20000 and 12000

# Program 3: overall total
overall_total = 0
for amounts in invoice_groups:
    for amount in amounts:
        overall_total += amount
print(f"Overall total: {overall_total}")  # Expected: 32000

# Task 1: Print two invoices for two customers.
# Task 2: Find each customer's invoice total.
# Task 3: Print two rows and three columns.
# Task 4: Show group totals and overall total.
# Task 5: Fix Rafiq bhai's total = amount bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
for customer in ["Rahim Traders", "Karim Store"]:
    for invoice in [1, 2]:
        print(customer, invoice)

# Task 2
groups = [[12000, 8000], [7000, 5000]]
for amounts in groups:
    total = 0
    for amount in amounts:
        total += amount
    print(total)

# Task 3
for row in range(1, 3):
    for column in range(1, 4):
        print(row, column)

# Task 4
groups = [[10000, 5000], [7000, 3000]]
overall = 0
for amounts in groups:
    group_total = 0
    for amount in amounts:
        group_total += amount
        overall += amount
    print(group_total)
print(overall)  # Expected: 15000, 10000, 25000

# Task 5
groups = [[12000, 8000], [7000, 5000]]
for amounts in groups:
    total = 0
    for amount in amounts:
        total += amount
    print(total)  # Expected: 20000, 12000
"""
# Change the values, save, and run this file again.
