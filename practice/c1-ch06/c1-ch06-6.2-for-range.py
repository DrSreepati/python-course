"""Subtopic 6.2: for loop and range().
Notes: notes/c1-ch06-6.2-for-range-bangla.md
       notes/c1-ch06-6.2-for-range-english.md
"""

# Program 1: report days
for day in range(1, 4):
    print(f"Preparing report for day {day}")  # Expected: days 1, 2, 3

# Program 2: stepped months
for month in range(2, 8, 2):
    print(f"Reviewing month {month}")  # Expected: months 2, 4, 6

# Program 3: running total
total = 0
for day in range(1, 4):
    sale = day * 1000
    total += sale
print(total)  # Expected: 6000

# Task 1: Check invoices 1 through 5.
# Task 2: Review months 2, 4, and 6.
# Task 3: Add sales 1000, 2000, and 3000.
# Task 4: Print priorities from 3 down to 1.
# Task 5: Fix Rafiq bhai's unnecessary manual update.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
for invoice in range(1, 6):
    print(invoice)

# Task 2
for month in range(2, 8, 2):
    print(month)

# Task 3
total = 0
for day in range(1, 4):
    total += day * 1000
print(total)  # Expected: 6000

# Task 4
for priority in range(3, 0, -1):
    print(priority)

# Task 5
for day in range(1, 4):
    print(f"Day {day}")
"""
# Change the values, save, and run this file again.
