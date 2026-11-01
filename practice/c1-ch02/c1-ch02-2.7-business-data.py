"""Subtopic 2.7: Business data examples.
Notes: notes/c1-ch02-2.7-business-data-bangla.md
       notes/c1-ch02-2.7-business-data-english.md
"""

# Program 1: amount from quantity and unit price
quantity = 6
unit_price = 250
amount = quantity * unit_price
print(amount)  # Expected: 1500

# Program 2: percentage and net amount
discount_percentage = 15
discount = amount * discount_percentage / 100
net_amount = amount - discount
print(discount)  # Expected: 225.0
print(net_amount)  # Expected: 1275.0

# Program 3: a small sales record
invoice_no = "INV-2024-007"
customer = "Rahim Traders"
report_date = "2026-11-01"
print(invoice_no, customer, report_date)  # Expected: INV-2024-007 Rahim Traders 2026-11-01
print(type(report_date))  # Expected: <class 'str'>

# Task 1: Calculate amount for quantity 12 and unit price 85.
# Task 2: Calculate an 8% discount on 5000 and the net amount.
# Task 3: Cast quantity "7" and price "120.50", then calculate amount.
# Task 4: Print invoice code, customer, quantity, price and date.
# Task 5: Fix Rafiq bhai's division bug:
# quantity = 6
# unit_price = 250
# wrong_amount = unit_price / quantity

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
quantity = 12
unit_price = 85
print(quantity * unit_price)  # Expected: 1020

# Task 2 solution
amount = 5000
discount = amount * 8 / 100
print(discount, amount - discount)  # Expected: 400.0 4600.0

# Task 3 solution
quantity = "7"
unit_price = "120.50"
print(int(quantity) * float(unit_price))  # Expected: 843.5

# Task 4 solution
print("INV-2024-007", "Rahim Traders", 3, 450.0, "2026-11-01")
# Expected: INV-2024-007 Rahim Traders 3 450.0 2026-11-01

# Task 5 solution
quantity = 6
unit_price = 250
amount = quantity * unit_price
print(amount)  # Expected: 1500
"""
# Change the values, save, and run this file again.
