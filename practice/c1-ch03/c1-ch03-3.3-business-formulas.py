"""Subtopic 3.3: Business formulas as code.
Notes: notes/c1-ch03-3.3-business-formulas-bangla.md
       notes/c1-ch03-3.3-business-formulas-english.md
"""

# Program 1: sales, cost and profit
quantity = 8
unit_price = 500
unit_cost = 350
sales = quantity * unit_price
cost = quantity * unit_cost
profit = sales - cost
print(sales)  # Expected: 4000
print(cost)  # Expected: 2800
print(profit)  # Expected: 1200

# Program 2: margin percentage
margin = profit / sales * 100
print(f"{margin:.2f}%")  # Expected: 30.00%

# Program 3: zero-sales guard
sales = 0
profit = 0
if sales == 0:
    print("Margin is not available")  # Expected: Margin is not available
else:
    print(profit / sales * 100)

# Task 1: Find sales from quantity 10 and unit price 300.
# Task 2: Find profit when sales are 5000 and cost is 3500.
# Task 3: Find margin when profit is 1500 and sales are 5000.
# Task 4: Find sales, cost, profit and margin for quantity 8, price 500, cost 350.
# Task 5: Fix Rafiq bhai's denominator bug:
# sales = 5000
# cost = 3500
# profit = sales - cost
# margin = profit / cost * 100

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
print(10 * 300)  # Expected: 3000

# Task 2 solution
print(5000 - 3500)  # Expected: 1500

# Task 3 solution
print(1500 / 5000 * 100)  # Expected: 30.0

# Task 4 solution
quantity = 8
unit_price = 500
unit_cost = 350
sales = quantity * unit_price
cost = quantity * unit_cost
profit = sales - cost
margin = profit / sales * 100
print(sales, cost, profit, margin)  # Expected: 4000 2800 1200 30.0

# Task 5 solution
sales = 5000
cost = 3500
profit = sales - cost
margin = profit / sales * 100
print(margin)  # Expected: 30.0
"""
# Change the values, save, and run this file again.
