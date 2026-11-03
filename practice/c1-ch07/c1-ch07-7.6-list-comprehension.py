"""Subtopic 7.6: List comprehension.
Notes: notes/c1-ch07-7.6-list-comprehension-bangla.md
       notes/c1-ch07-7.6-list-comprehension-english.md
"""

# Program 1: transform every sale.
sales = [12000, 9500, 8800]
updated_sales = [sale * 1.10 for sale in sales]
print(updated_sales)  # Expected: [13200.000000000002, 10450.0, 9680.000000000002]

# Program 2: select large sales.
report = [12000, 9500, 8800, 13200, 7500]
large_sales = [sale for sale in report if sale > 10000]
print(large_sales)  # Expected: [12000, 13200]

# Program 3: label each sale.
labels = ["High" if sale >= 10000 else "Regular" for sale in sales]
print(labels)  # Expected: ['High', 'Regular', 'Regular']

# Program 4: create indexed business labels.
day_labels = [
    f"Day {day}: {sale}"
    for day, sale in enumerate(sales, start=1)
]
print(day_labels)  # Expected: ['Day 1: 12000', 'Day 2: 9500', 'Day 3: 8800']

# Task 1: Subtract 1000 from every value in report.
# Task 2: Keep only sales of 10000 or more.
# Task 3: Add "Tk " before every weekly taking.
# Task 4: Label balances as Review or Normal.
# Task 5: Fix Rafiq bhai's filtering bug so every amount appears.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
report = [12000, 9500, 8800, 13200, 7500]
reduced = [sale - 1000 for sale in report]
print(reduced)
# Expected: [11000, 8500, 7800, 12200, 6500]

# Task 2
selected = [sale for sale in report if sale >= 10000]
print(selected)
# Expected: [12000, 13200]

# Task 3
week = [5000, 4200, 6100]
labels = [f"Tk {amount}" for amount in week]
print(labels)
# Expected: ['Tk 5000', 'Tk 4200', 'Tk 6100']

# Task 4
balances = [50000, 32000, 71000]
labels = ["Review" if balance >= 50000 else "Normal" for balance in balances]
print(labels)
# Expected: ['Review', 'Normal', 'Review']

# Task 5
amounts = [12000, 9500, 8800]
full_report = [amount for amount in amounts]
print(full_report)
# Expected: [12000, 9500, 8800]
"""
# Change the values and rerun. Real skill grows in the variations, not the copies.
