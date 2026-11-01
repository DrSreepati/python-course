"""Subtopic 4.5: Immutability, building new strings.
Notes: notes/c1-ch04-4.5-immutability-bangla.md
       notes/c1-ch04-4.5-immutability-english.md
"""

# Program 1: strings cannot be changed by item assignment
customer_code = "C-1023"
try:
    customer_code[0] = "S"
except TypeError as error:
    print(type(error).__name__)  # Expected: TypeError
    print(error)  # Expected: 'str' object does not support item assignment

# Program 2: build a new string with slicing and concatenation
invoice_no = "INV-2024-007"
updated_invoice = invoice_no[:4] + "2025" + invoice_no[8:]
print(invoice_no)  # Expected: INV-2024-007
print(updated_invoice)  # Expected: INV-2025-007

# Program 3: update a list of parts, then join a new string
parts = "INV-2024-007".split("-")
parts[1] = "2025"
new_invoice = "-".join(parts)
print(parts)  # Expected: ['INV', '2025', '007']
print(new_invoice)  # Expected: INV-2025-007

# Task 1: Change "C-1023" into "S-1023" without item assignment.
# Task 2: Change "INV-2024-007" into "INV-2025-007" with replace().
# Task 3: Split "INV-2024-007", change the year, and join it again.
# Task 4: Add "Mr. " before "Rahim Traders" and print both values.
# Task 5: Fix Rafiq bhai's immutability bug:
# invoice_no = "INV-2024-007"
# invoice_no[4:8] = "2025"

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
code = "C-1023"
new_code = "S" + code[1:]
print(new_code)  # Expected: S-1023

# Task 2 solution
invoice_no = "INV-2024-007"
new_invoice = invoice_no.replace("2024", "2025")
print(new_invoice)  # Expected: INV-2025-007

# Task 3 solution
parts = "INV-2024-007".split("-")
parts[1] = "2025"
print("-".join(parts))  # Expected: INV-2025-007

# Task 4 solution
name = "Rahim Traders"
new_name = "Mr. " + name
print(name)  # Expected: Rahim Traders
print(new_name)  # Expected: Mr. Rahim Traders

# Task 5 solution
invoice_no = "INV-2024-007"
updated_invoice = invoice_no[:4] + "2025" + invoice_no[8:]
print(updated_invoice)  # Expected: INV-2025-007
"""
# Change the values, save, and run this file again.
