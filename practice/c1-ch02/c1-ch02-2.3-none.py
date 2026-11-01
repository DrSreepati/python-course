"""Subtopic 2.3: None, what it means and why it is not zero.
Notes: notes/c1-ch02-2.3-none-bangla.md
       notes/c1-ch02-2.3-none-english.md
"""

# Program 1: an unknown balance is None
pending_balance = None
print(pending_balance)  # Expected: None

# Program 2: known zero and unknown value are different
closed_shop_sales = 0
unreported_sales = None
print(closed_shop_sales)  # Expected: 0
print(unreported_sales)  # Expected: None

# Program 3: check before calculating
balance = None
payment = 5000
if balance is None:
    print("Cannot calculate: balance is unknown")
else:
    print(balance - payment)

# Task 1: Store and print pending_balance = None.

# Task 2: Store closed_shop_sales = 0 and unreported_sales = None.

# Task 3: Check whether balance = None is missing.

# Task 4: Show a pending message when payment_date = None.

# Task 5: Fix Rafiq bhai's bug.
# Broken idea: remaining = balance or 0

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
pending_balance = None
print(pending_balance)  # Expected: None

# Task 2 solution
closed_shop_sales = 0
unreported_sales = None
print(closed_shop_sales is None)  # Expected: False
print(unreported_sales is None)  # Expected: True

# Task 3 solution
balance = None
if balance is None:
    print("Balance is unknown")  # Expected: Balance is unknown

# Task 4 solution
invoice_number = "INV-2024-007"
payment_date = None
if payment_date is None:
    print(invoice_number, "payment date is pending")
    # Expected: INV-2024-007 payment date is pending

# Task 5 solution
balance = None
payment = 5000
if balance is None:
    print("Cannot calculate: balance is unknown")
else:
    print(balance - payment)
    # Expected: Cannot calculate: balance is unknown
"""
# Change the values, save, and run this file again.
