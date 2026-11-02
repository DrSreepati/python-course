"""Subtopic 7.5: Loops and enumerate on lists.
Notes: notes/c1-ch07-7.5-enumerate-bangla.md
       notes/c1-ch07-7.5-enumerate-english.md
"""

# Program 1: enumerate with the technical zero-based index.
sales = [12000, 9500, 8800]
for index, sale in enumerate(sales):
    print(f"Index {index}: {sale}")

# Program 2: enumerate with a business day label.
for day, sale in enumerate(sales, start=1):
    print(f"Day {day}: {sale}")  # Expected: Day 1, Day 2, Day 3

# Program 3: aligned customer and balance report.
customers = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
balances = [50000, 32000, 71000]
for index, customer in enumerate(customers):
    print(f"{customer}: {balances[index]}")

# Program 4: invoice audit labels.
references = ["INV-2024-007", "INV-2024-008", "INV-2024-009"]
for review_number, reference in enumerate(references, start=1):
    print(f"Review {review_number}: {reference}")

# Task 1: Print sales with their zero-based indexes.
# Task 2: Print sales with day numbers starting at one.
# Task 3: Print customers with matching balances.
# Task 4: Print invoice references with review numbers.
# Task 5: Fix Rafiq bhai's zero-based business-day bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
for index, sale in enumerate([12000, 9500, 8800]):
    print(index, sale)

# Task 2
for day, sale in enumerate([12000, 9500, 8800], start=1):
    print(f"Day {day}: {sale}")

# Task 3
customers = ["Rahim Traders", "Karim Store"]
balances = [50000, 32000]
for index, customer in enumerate(customers):
    print(customer, balances[index])

# Task 4
references = ["INV-2024-007", "INV-2024-008"]
for number, reference in enumerate(references, start=1):
    print(f"Review {number}: {reference}")

# Task 5
sales = [12000, 9500, 8800]
for day, sale in enumerate(sales, start=1):
    print(f"Day {day}: {sale}")
"""
# Change the values and rerun. Position-aware reports grow from practice.
