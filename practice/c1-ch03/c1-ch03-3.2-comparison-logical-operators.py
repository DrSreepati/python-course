"""Subtopic 3.2: Comparison and logical operators.
Notes: notes/c1-ch03-3.2-comparison-logical-operators-bangla.md
       notes/c1-ch03-3.2-comparison-logical-operators-english.md
"""

# Program 1: target comparison
sales = 12000
target = 10000
print(sales > target)  # Expected: True

# Program 2: discount eligibility
order_amount = 71000
minimum_order = 50000
paid = True
discount_eligible = order_amount >= minimum_order and paid
print(discount_eligible)  # Expected: True

# Program 3: boundary testing
minimum_order = 50000
print(49999 >= minimum_order)  # Expected: False
print(50000 >= minimum_order)  # Expected: True
print(50001 >= minimum_order)  # Expected: True

# Task 1: Check whether report total is greater than 50000.
# Task 2: Check whether a balance of 71000 is at least 50000.
# Task 3: Use False or True to calculate payment_received.
# Task 4: Check discount eligibility for amount 32000, minimum 30000 and paid True.
# Task 5: Fix Rafiq bhai's boundary bug:
# order_amount = 50000
# minimum_order = 50000
# eligible = order_amount > minimum_order

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
report = [12000, 9500, 8800, 13200, 7500]
print(sum(report) > 50000)  # Expected: True

# Task 2 solution
print(71000 >= 50000)  # Expected: True

# Task 3 solution
cash_received = False
bank_received = True
print(cash_received or bank_received)  # Expected: True

# Task 4 solution
print(32000 >= 30000 and True)  # Expected: True

# Task 5 solution
order_amount = 50000
minimum_order = 50000
eligible = order_amount >= minimum_order
print(eligible)  # Expected: True
"""
# Change the values, save, and run this file again.
