"""Subtopic 4.2: String slicing [start:stop:step].
Notes: notes/c1-ch04-4.2-slicing-bangla.md
       notes/c1-ch04-4.2-slicing-english.md
"""

# Program 1: invoice parts
invoice_no = "INV-2024-007"
print(invoice_no[:3])  # Expected: INV
print(invoice_no[4:8])  # Expected: 2024
print(invoice_no[9:])  # Expected: 007

# Program 2: step and reverse slicing
customer_code = "C-1023"
print(customer_code[::2])  # Expected: C12
print(customer_code[::-1])  # Expected: 3201-C

# Program 3: negative slicing
invoice_no = "INV-2024-007"
print(invoice_no[-3:])  # Expected: 007
print(invoice_no[-8:-4])  # Expected: 2024

# Task 1: Slice the prefix "INV" from "INV-2024-007".
# Task 2: Slice the year "2024" from "INV-2024-007".
# Task 3: Print the final three characters of "C-1023".
# Task 4: Print every second character of "Rahim Traders".
# Task 5: Fix Rafiq bhai's slicing bug:
# invoice_no = "INV-2024-007"
# year = invoice_no[4:9]

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
code = "INV-2024-007"
print(code[:3])  # Expected: INV

# Task 2 solution
code = "INV-2024-007"
print(code[4:8])  # Expected: 2024

# Task 3 solution
code = "C-1023"
print(code[-3:])  # Expected: 023

# Task 4 solution
name = "Rahim Traders"
print(name[::2])  # Expected: RhmTaes

# Task 5 solution
invoice_no = "INV-2024-007"
year = invoice_no[4:8]
print(year)  # Expected: 2024
"""
# Change the values, save, and run this file again.
