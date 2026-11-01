"""Subtopic 2.2: Core types: int, float, str, bool.
Notes: notes/c1-ch02-2.2-core-types-bangla.md
       notes/c1-ch02-2.2-core-types-english.md
"""

# Program 1: the four core types
daily_sales = 12000
unit_price = 250.50
customer = "Rahim Traders"
credit_approved = True
print(daily_sales)  # Expected: 12000
print(unit_price)  # Expected: 250.5
print(customer)  # Expected: Rahim Traders
print(credit_approved)  # Expected: True

# Program 2: codes are strings, even when they contain digits
customer_code = "C-1023"
invoice_number = "INV-2024-007"
print(customer_code)  # Expected: C-1023
print(invoice_number)  # Expected: INV-2024-007

# Program 3: mixed types in one business record
quantity = 6
vat_rate = 7.5
paid = False
print(quantity, vat_rate, paid)  # Expected: 6 7.5 False

# Task 1: Store and print daily_sales = 12000 and customer = "Rahim Traders".

# Task 2: Store and print unit_price = 250.50 and vat_rate = 7.5.

# Task 3: Store and print invoice_number = "INV-2024-007" and payment_received = False.

# Task 4: Store customer_code = "C-1023", items = 24, and stock_available = True.

# Task 5: Fix Rafiq bhai's Boolean capitalisation bug.
# Broken idea: paid = true

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
daily_sales = 12000
customer = "Rahim Traders"
print(daily_sales)  # Expected: 12000
print(customer)  # Expected: Rahim Traders

# Task 2 solution
unit_price = 250.50
vat_rate = 7.5
print(unit_price)  # Expected: 250.5
print(vat_rate)  # Expected: 7.5

# Task 3 solution
invoice_number = "INV-2024-007"
payment_received = False
print(invoice_number)  # Expected: INV-2024-007
print(payment_received)  # Expected: False

# Task 4 solution
customer_code = "C-1023"
items = 24
stock_available = True
print(customer_code, items, stock_available)  # Expected: C-1023 24 True

# Task 5 solution
paid = True
print(paid)  # Expected: True
"""
# Change the values, save, and run this file again.
