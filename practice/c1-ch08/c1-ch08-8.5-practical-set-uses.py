"""
Course 1, Chapter 8, Subtopic 8.5: Practical uses of sets
Notes: c1-ch08-8.5-practical-set-uses-bangla.md and
       c1-ch08-8.5-practical-set-uses-english.md
"""

invoices = ["INV-007", "INV-008", "INV-007", "INV-009", "INV-008"]
print("Rows:", len(invoices))
print("Unique:", len(set(invoices)))
# Expected:
# Rows: 5
# Unique: 3

seen = set()
duplicates = []
for invoice in invoices:
    if invoice in seen:
        if invoice not in duplicates:
            duplicates.append(invoice)
    else:
        seen.add(invoice)
print("Duplicates:", duplicates)
# Expected: Duplicates: ['INV-007', 'INV-008']

dhaka = {"rice", "oil", "lentils", "sugar"}
chattogram = {"oil", "sugar", "tea"}
print("Shared categories:", sorted(dhaka & chattogram))
print("Dhaka only:", sorted(dhaka - chattogram))
print("Chattogram only:", sorted(chattogram - dhaka))
# Expected:
# Shared categories: ['oil', 'sugar']
# Dhaka only: ['lentils', 'rice']
# Chattogram only: ['tea']

# Task 1: Find the unique count of a repeated invoice list.
# Task 2: Build a first-seen-order unique customer list.
# Task 3: Find shared and branch-specific product categories.
# Task 4: Report each duplicate invoice reference once.
# Task 5: Correct a unique-count program that uses len(rows).

# ===== SOLUTIONS (try first, then compare) =====

# Task 1 solution
task_one = ["A", "B", "A", "C"]
print(len(set(task_one)))
# Expected: 3

# Task 2 solution
customers = ["C-1", "C-2", "C-1", "C-3"]
seen = set()
unique_customers = []
for customer in customers:
    if customer not in seen:
        seen.add(customer)
        unique_customers.append(customer)
print(unique_customers)
# Expected: ['C-1', 'C-2', 'C-3']

# Task 3 solution
category_a = {"rice", "oil", "tea"}
category_b = {"oil", "sugar"}
print(sorted(category_a & category_b))
print(sorted(category_a - category_b))
print(sorted(category_b - category_a))
# Expected:
# ['oil']
# ['rice', 'tea']
# ['sugar']

# Task 4 solution
rows = ["INV-1", "INV-2", "INV-1", "INV-3", "INV-2", "INV-2"]
seen = set()
duplicates = []
for invoice in rows:
    if invoice in seen and invoice not in duplicates:
        duplicates.append(invoice)
    else:
        seen.add(invoice)
print(duplicates)
# Expected: ['INV-1', 'INV-2']

# Task 5 solution
sreepati_rows = ["INV-1", "INV-2", "INV-1", "INV-3"]
print(len(set(sreepati_rows)))
# Expected: 3

# Change the data and rerun. Real skill grows in the variations, not the copies.
