"""Subtopic 3.5: Assignment, bitwise and operator precedence.
Notes: notes/c1-ch03-3.5-assignment-bitwise-precedence-bangla.md
       notes/c1-ch03-3.5-assignment-bitwise-precedence-english.md
"""

# Program 1: running sales total
total_sales = 12000
total_sales += 9500
print(total_sales)  # Expected: 21500

# Program 2: balance update
balance = 50000
balance -= 12000
print(balance)  # Expected: 38000

# Program 3: precedence and parentheses
print(100 + 20 * 3)  # Expected: 160
print((100 + 20) * 3)  # Expected: 360

# Program 4: invoice formula with clear order
gross = 10000
discount_rate = 0.10
vat_rate = 0.15
total = (gross - gross * discount_rate) * (1 + vat_rate)
print(total)  # Expected: 10350.0

# Task 1: Add 9500 to total 12000 with +=.
# Task 2: Subtract payment 12000 from balance 50000 with -=.
# Task 3: Compare 100 + 20 * 3 with (100 + 20) * 3.
# Task 4: Calculate the invoice total with gross 10000, discount 10%, VAT 15%.
# Task 5: Fix Rafiq bhai's update bug:
# total_sales = 12000
# total_sales =+ 9500

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
total = 12000
total += 9500
print(total)  # Expected: 21500

# Task 2 solution
balance = 50000
balance -= 12000
print(balance)  # Expected: 38000

# Task 3 solution
print(100 + 20 * 3)  # Expected: 160
print((100 + 20) * 3)  # Expected: 360

# Task 4 solution
gross = 10000
total = (gross - gross * 0.10) * (1 + 0.15)
print(total)  # Expected: 10350.0

# Task 5 solution
total_sales = 12000
total_sales += 9500
print(total_sales)  # Expected: 21500
"""
# Change the values, save, and run this file again.
