"""Subtopic 2.6: Money as data, the float problem.
Notes: notes/c1-ch02-2.6-money-float-bangla.md
       notes/c1-ch02-2.6-money-float-english.md
"""

# Program 1: the float surprise and display rounding
result = 0.1 + 0.2
print(result)  # Expected: 0.30000000000000004
print(round(result, 2))  # Expected: 0.3

# Program 2: compare raw and rounded values
print(result == 0.3)  # Expected: False
print(round(result, 2) == 0.3)  # Expected: True

# Program 3: Decimal for a financial-style calculation
from decimal import Decimal

unit_price = Decimal("19.99")
quantity = 3
amount = unit_price * quantity
print(amount)  # Expected: 59.97

# Task 1: Print 0.1 + 0.2 and its value rounded to two places.

# Task 2: Calculate 19.99 * 3 and display the rounded amount.

# Task 3: Compare raw float equality with rounded equality.

# Task 4: Store 1999 paisa and calculate the amount for 3 items.

# Task 5: Fix Rafiq bhai's float equality bug.
# Broken idea: 0.1 + 0.2 == 0.3

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
result = 0.1 + 0.2
print(result)  # Expected: 0.30000000000000004
print(round(result, 2))  # Expected: 0.3

# Task 2 solution
amount = 19.99 * 3
print(amount)  # Expected: 59.97
print(round(amount, 2))  # Expected: 59.97

# Task 3 solution
calculated = 0.1 + 0.2
print(calculated == 0.3)  # Expected: False
print(round(calculated, 2) == 0.3)  # Expected: True

# Task 4 solution
price_paisa = 1999
quantity = 3
print(price_paisa * quantity)  # Expected: 5997

# Task 5 solution
calculated = 0.1 + 0.2
if round(calculated, 2) == 0.3:
    print("Amount matches")  # Expected: Amount matches
else:
    print("Amount does not match")
"""
# Change the values, save, and run this file again.
