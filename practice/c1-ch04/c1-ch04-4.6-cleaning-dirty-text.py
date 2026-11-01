"""Subtopic 4.6: Cleaning dirty text.
Notes: notes/c1-ch04-4.6-cleaning-dirty-text-bangla.md
       notes/c1-ch04-4.6-cleaning-dirty-text-english.md
"""

# Program 1: customer comparison key
raw_customer = "  RAHIM traders  "
customer_key = raw_customer.strip().lower()
print(raw_customer)  # Expected:   RAHIM traders
print(customer_key)  # Expected: rahim traders

# Program 2: invoice cleaning
raw_invoice = " inv/2024/007 "
clean_invoice = raw_invoice.strip().upper().replace("/", "-")
print(clean_invoice)  # Expected: INV-2024-007
print(clean_invoice.startswith("INV-"))  # Expected: True
print(clean_invoice.endswith("007"))  # Expected: True

# Program 3: cleaning checks
print(clean_invoice.count("/"))  # Expected: 0
print(clean_invoice.count("-"))  # Expected: 2

# Task 1: Create a comparison key from "  RAHIM traders  ".
# Task 2: Clean " inv/2024/007 " into "INV-2024-007".
# Task 3: Check that "INV-2024-007" has no slash and two hyphens.
# Task 4: Print raw and cleaned values for "  Karim STORE  ".
# Task 5: Fix Rafiq bhai's cleaning bug:
# raw_invoice = " inv/2024/007 "
# clean_invoice = raw_invoice.replace("/", "")

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
raw_name = "  RAHIM traders  "
customer_key = raw_name.strip().lower()
print(customer_key)  # Expected: rahim traders

# Task 2 solution
raw_invoice = " inv/2024/007 "
clean_invoice = raw_invoice.strip().upper().replace("/", "-")
print(clean_invoice)  # Expected: INV-2024-007

# Task 3 solution
invoice = "INV-2024-007"
print(invoice.count("/"))  # Expected: 0
print(invoice.count("-"))  # Expected: 2

# Task 4 solution
raw_name = "  Karim STORE  "
clean_name = raw_name.strip().lower()
print(f"Raw: {raw_name}")  # Expected: Raw:   Karim STORE
print(f"Clean key: {clean_name}")  # Expected: Clean key: karim store

# Task 5 solution
raw_invoice = " inv/2024/007 "
clean_invoice = raw_invoice.strip().upper().replace("/", "-")
print(clean_invoice)  # Expected: INV-2024-007
"""
# Change the values, save, and run this file again.
