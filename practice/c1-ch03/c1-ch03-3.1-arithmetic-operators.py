"""Subtopic 3.1: Arithmetic operators.
Notes: notes/c1-ch03-3.1-arithmetic-operators-bangla.md
       notes/c1-ch03-3.1-arithmetic-operators-english.md
"""

# Program 1: profit and sales gap
sales = 12000
cost = 8500
profit = sales - cost
print(profit)  # Expected: 3500

# Program 2: amount and average
quantity = 8
unit_price = 175
amount = quantity * unit_price
average_daily_sales = amount / 4
print(amount)  # Expected: 1400
print(average_daily_sales)  # Expected: 350.0

# Program 3: cartons and loose items
stock = 47
carton_size = 12
print(stock // carton_size)  # Expected: 3
print(stock % carton_size)  # Expected: 11

# Task 1: Add 12000 and 9500, then find their difference.
# Task 2: Calculate amount for quantity 9 and unit price 275.
# Task 3: Find full cartons and loose items for 47 items and size 12.
# Task 4: Find total and average for the weekly sales list.
# Task 5: Fix Rafiq bhai's average bug:
# total_sales = 35001
# days = 7
# average_sales = total_sales // days

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
print(12000 + 9500)  # Expected: 21500
print(12000 - 9500)  # Expected: 2500

# Task 2 solution
print(9 * 275)  # Expected: 2475

# Task 3 solution
print(47 // 12)  # Expected: 3
print(47 % 12)  # Expected: 11

# Task 4 solution
week = [5000, 4200, 6100, 3800, 5500, 4700, 5700]
total = sum(week)
average = total / len(week)
print(total)  # Expected: 35000
print(average)  # Expected: 5000.0

# Task 5 solution
total_sales = 35001
days = 7
average_sales = total_sales / days
print(average_sales)  # Expected: 5000.142857142857
"""
# Change the values, save, and run this file again.
