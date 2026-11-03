"""Subtopic 8.1: Tuple, creation, indexing, slicing, immutability.
Notes: notes/c1-ch08-8.1-tuple-basics-bangla.md
       notes/c1-ch08-8.1-tuple-basics-english.md
"""

# Program 1: a fixed invoice record.
invoice = ("INV-2024-007", "Rahim Traders", 50000)
print(invoice)  # Expected: ('INV-2024-007', 'Rahim Traders', 50000)

# Program 2: tuple indexes and a slice.
weekly_summary = ("Mon", 5000, "Tue", 4200, "Wed", 6100)
print(weekly_summary[0])  # Expected: Mon
print(weekly_summary[-1])  # Expected: 6100
print(weekly_summary[:3])  # Expected: ('Mon', 5000, 'Tue')

# Program 3: tuple calculations.
daily_sales = (12000, 9500, 8800, 13200, 7500)
print(sum(daily_sales))  # Expected: 51000
print(max(daily_sales))  # Expected: 13200

# Program 4: an approved snapshot from a mutable list.
report = [12000, 9500, 8800]
approved_report = tuple(report)
report[0] = 13000
print(report)  # Expected: [13000, 9500, 8800]
print(approved_report)  # Expected: (12000, 9500, 8800)

# Task 1: Create an invoice tuple and print its first and last items.
# Task 2: Slice the first three items from a weekly tuple.
# Task 3: Make an approved tuple snapshot from a list.
# Task 4: Show the difference between a one-item tuple and a string.
# Task 5: Fix Sreepati's tuple item-assignment bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
invoice = ("INV-2024-007", "Rahim Traders", 50000)
print(invoice[0])
print(invoice[-1])
# Expected:
# INV-2024-007
# 50000

# Task 2
summary = ("Mon", 5000, "Tue", 4200, "Wed", 6100)
print(summary[:3])
# Expected: ('Mon', 5000, 'Tue')

# Task 3
report = [12000, 9500, 8800]
approved = tuple(report)
report.append(13200)
print(report)
print(approved)
# Expected:
# [12000, 9500, 8800, 13200]
# (12000, 9500, 8800)

# Task 4
single_tuple = ("INV-2024-007",)
single_text = ("INV-2024-007")
print(type(single_tuple).__name__)
print(type(single_text).__name__)
# Expected:
# tuple
# str

# Task 5
approved = ("INV-2024-007", 50000)
corrected = (approved[0], 55000)
print(corrected)
# Expected: ('INV-2024-007', 55000)
"""
# Change the values and rerun. Fixed records grow from careful reading.
