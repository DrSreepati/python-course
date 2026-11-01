"""Subtopic 2.5: Type casting, int(), float(), str().
Notes: notes/c1-ch02-2.5-type-casting-bangla.md
       notes/c1-ch02-2.5-type-casting-english.md
"""

# Program 1: convert text to an integer
quantity_text = "6"
quantity = int(quantity_text)
print(quantity)  # Expected: 6
print(type(quantity))  # Expected: <class 'int'>

# Program 2: convert decimal text and calculate an amount
price_text = "250.50"
unit_price = float(price_text)
amount = unit_price * 4
print(amount)  # Expected: 1002.0

# Program 3: convert a number to report text
invoice_number = "INV-2024-007"
report_line = str(invoice_number) + ": " + str(1002)
print(report_line)  # Expected: INV-2024-007: 1002

# Task 1: Convert "24" to an integer and add 6.

# Task 2: Convert "250.50" to a float and multiply it by 4.

# Task 3: Convert amount = 1002 to text in a report line.

# Task 4: Store None for a blank balance, otherwise convert it to int.

# Task 5: Fix Rafiq bhai's invalid integer conversion.
# Broken idea: quantity = int("six")

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
items = int("24")
print(items + 6)  # Expected: 30

# Task 2 solution
unit_price = float("250.50")
print(unit_price * 4)  # Expected: 1002.0

# Task 3 solution
invoice_number = "INV-2024-007"
amount = 1002
print(str(invoice_number) + ": " + str(amount))
# Expected: INV-2024-007: 1002

# Task 4 solution
balance_text = ""
if balance_text == "":
    balance = None
else:
    balance = int(balance_text)
print(balance)  # Expected: None

# Task 5 solution
quantity_text = "6"
quantity = int(quantity_text)
print(quantity)  # Expected: 6
"""
# Change the values, save, and run this file again.
