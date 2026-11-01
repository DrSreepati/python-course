"""Subtopic 4.4: String methods 2.
Notes: notes/c1-ch04-4.4-string-methods-2-bangla.md
       notes/c1-ch04-4.4-string-methods-2-english.md
"""

# Program 1: split and join an invoice
invoice_no = "INV-2024-007"
parts = invoice_no.split("-")
print(parts)  # Expected: ['INV', '2024', '007']
print("-".join(parts))  # Expected: INV-2024-007

# Program 2: find and boundary checks
print(invoice_no.find("2024"))  # Expected: 4
print(invoice_no.startswith("INV"))  # Expected: True
print(invoice_no.endswith("007"))  # Expected: True

# Program 3: clean, parse and standardise an invoice
raw_invoice = " inv/2024/007 "
clean_invoice = raw_invoice.strip().upper()
invoice_parts = clean_invoice.split("/")
standard_invoice = "-".join(invoice_parts)
print(invoice_parts)  # Expected: ['INV', '2024', '007']
print(standard_invoice)  # Expected: INV-2024-007

# Task 1: Split "INV-2024-007" into three parts.
# Task 2: Join ["INV", "2024", "007"] with hyphens.
# Task 3: Find where "2024" starts in "INV-2024-007".
# Task 4: Check whether "C-1023" starts with "C-" and ends with "1023".
# Task 5: Fix Rafiq bhai's parsing bug:
# invoice_no = "INV/2024/007"
# parts = invoice_no.split("-")

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
invoice_no = "INV-2024-007"
print(invoice_no.split("-"))  # Expected: ['INV', '2024', '007']

# Task 2 solution
parts = ["INV", "2024", "007"]
print("-".join(parts))  # Expected: INV-2024-007

# Task 3 solution
invoice_no = "INV-2024-007"
print(invoice_no.find("2024"))  # Expected: 4

# Task 4 solution
code = "C-1023"
print(code.startswith("C-"))  # Expected: True
print(code.endswith("1023"))  # Expected: True

# Task 5 solution
invoice_no = "INV/2024/007"
parts = invoice_no.split("/")
print(parts)  # Expected: ['INV', '2024', '007']
"""
# Change the values, save, and run this file again.
