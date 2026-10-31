"""Subtopic 2.1: Variables: creation, naming rules, assignment.
Notes: notes/c1-ch02-variables-business-data-types-bangla.md
       notes/c1-ch02-variables-business-data-types-english.md
"""

# Program 1: named business values
daily_sales = 12000
customer = "Rahim Traders"
print(daily_sales)  # Expected: 12000
print(customer)  # Expected: Rahim Traders

# Program 2: updating a value
pending_amount = 32000
print(pending_amount)  # Expected: 32000
pending_amount = 28000
print(pending_amount)  # Expected: 28000

# Program 3: a small business calculation
unit_price = 250
quantity = 4
amount = unit_price * quantity
print(amount)  # Expected: 1000

# Task 1: Store and print a product name and stock quantity.
# Data: product_name = "Rice", stock_quantity = 25


# Task 2: Find the total amount.
# Data: unit_price = 120, quantity = 6

# Task 3: Update a customer balance after a payment.
# Data: starting balance = 71000, payment = 5000

# Task 4: Find profit.
# Data: sales = 50000, cost = 38000

# Task 5: Fix Rafiq bhai's variable-name bug.
# Broken idea: invoice number = "INV-2024-007"

# ===== SOLUTIONS (try first, then compare) =====
'''

# Task 1 solution
product_name = "Rice"
stock_quantity = 25
print(product_name)  # Expected: Rice
print(stock_quantity)  # Expected: 25

# Task 2 solution
unit_price = 120
quantity = 6
total_amount = unit_price * quantity
print(total_amount)  # Expected: 720

# Task 3 solution
customer_balance = 71000
customer_balance = customer_balance - 5000
print(customer_balance)  # Expected: 66000

# Task 4 solution
sales = 50000
cost = 38000
profit = sales - cost
print(profit)  # Expected: 12000

# Task 5 solution
invoice_number = "INV-2024-007"
print(invoice_number)  # Expected: INV-2024-007
’’’
# Change the values, save, and run this file again.
