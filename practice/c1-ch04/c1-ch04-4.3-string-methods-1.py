"""Subtopic 4.3: String methods 1.
Notes: notes/c1-ch04-4.3-string-methods-1-bangla.md
       notes/c1-ch04-4.3-string-methods-1-english.md
"""

# Program 1: case conversion
customer = "Rahim Traders"
print(customer.upper())  # Expected: RAHIM TRADERS
print(customer.lower())  # Expected: rahim traders

# Program 2: cleaning and standardising customer text
raw_customer = "  RAHIM traders  "
clean_customer = raw_customer.strip().lower()
print(clean_customer)  # Expected: rahim traders
print(clean_customer.upper())  # Expected: RAHIM TRADERS

# Program 3: standardising and counting an invoice reference
raw_invoice = " inv/2024/007 "
clean_invoice = raw_invoice.strip().upper().replace("/", "-")
print(clean_invoice)  # Expected: INV-2024-007
print(clean_invoice.count("-"))  # Expected: 2

# Task 1: Clean the outer spaces from "  Rahim Traders  ".
# Task 2: Print "karim store" in uppercase.
# Task 3: Change "INV/2024/007" into "INV-2024-007".
# Task 4: Count the hyphens and zeroes in "INV-2024-007".
# Task 5: Fix Rafiq bhai's bug:
# customer = "  Rahim Traders  "
# report_name = customer.replace(" ", "")

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
name = "  Rahim Traders  "
print(name.strip())  # Expected: Rahim Traders

# Task 2 solution
name = "karim store"
print(name.upper())  # Expected: KARIM STORE

# Task 3 solution
code = "INV/2024/007"
print(code.replace("/", "-"))  # Expected: INV-2024-007

# Task 4 solution
code = "INV-2024-007"
print(code.count("-"))  # Expected: 2
print(code.count("0"))  # Expected: 3

# Task 5 solution
customer = "  Rahim Traders  "
report_name = customer.strip()
print(report_name)  # Expected: Rahim Traders
"""
# Change the values, save, and run this file again.
