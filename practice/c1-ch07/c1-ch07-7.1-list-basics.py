"""Subtopic 7.1: List creation, indexing and slicing.
Notes: notes/c1-ch07-7.1-list-basics-bangla.md
       notes/c1-ch07-7.1-list-basics-english.md
"""

# Program 1: create a business list and read its length.
daily_sales = [12000, 9500, 8800, 13200, 7500]
print(daily_sales)
print(len(daily_sales))  # Expected: 5

# Program 2: use positive and negative indexes.
print(daily_sales[0])  # Expected: 12000
print(daily_sales[3])  # Expected: 13200
print(daily_sales[-1])  # Expected: 7500
print(daily_sales[-2])  # Expected: 13200

# Program 3: select report sections with slices.
print(daily_sales[:3])  # Expected: [12000, 9500, 8800]
print(daily_sales[-2:])  # Expected: [13200, 7500]
print(daily_sales[::2])  # Expected: [12000, 8800, 7500]
print(daily_sales[::-1])  # Expected: [7500, 13200, 8800, 9500, 12000]

# Program 4: a customer record list.
customers = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
print(customers[1])  # Expected: Karim Store
print(customers[:2])  # Expected: ['Rahim Traders', 'Karim Store']

# Task 1: Create the weekly takings list and print its length.
# Task 2: Read Rahim Traders and the matching balance by index.
# Task 3: Print the first three and final two daily sales.
# Task 4: Print alternate sales and reversed sales.
# Task 5: Fix Rafiq bhai's first-sale indexing bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
week = [5000, 4200, 6100, 3800, 5500, 4700, 5700]
print(week)
print(len(week))  # Expected: 7

# Task 2
customers = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
balances = [50000, 32000, 71000]
print(customers[0], balances[0])  # Expected: Rahim Traders 50000

# Task 3
sales = [12000, 9500, 8800, 13200, 7500]
print(sales[:3])  # Expected: [12000, 9500, 8800]
print(sales[-2:])  # Expected: [13200, 7500]

# Task 4
print(sales[::2])  # Expected: [12000, 8800, 7500]
print(sales[::-1])  # Expected: [7500, 13200, 8800, 9500, 12000]

# Task 5
first_sale = sales[0]
print(first_sale)  # Expected: 12000
"""
# Change the values and rerun. Lists become clearer through variations.
