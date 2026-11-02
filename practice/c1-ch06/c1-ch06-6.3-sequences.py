"""Subtopic 6.3: for over sequences.
Notes: notes/c1-ch06-6.3-sequences-bangla.md
       notes/c1-ch06-6.3-sequences-english.md
"""

# Program 1: characters
invoice_code = "INV"
for character in invoice_code:
    print(character)  # Expected: I, N, V

# Program 2: customers
customers = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
for customer in customers:
    print(customer)  # Expected: three customer names

# Program 3: daily sales total and filter
report = [12000, 9500, 8800, 13200, 7500]
total_sales = 0
for sale in report:
    total_sales += sale
    if sale >= 10000:
        print(f"Large sale: {sale}")  # Expected: 12000 and 13200
print(total_sales)  # Expected: 51000

# Task 1: Print each character in INV.
# Task 2: Print three customer names.
# Task 3: Calculate the daily sales total.
# Task 4: Print sales of 10000 or more.
# Task 5: Fix Rafiq bhai's total = sale bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
for character in "INV":
    print(character)

# Task 2
customers = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
for customer in customers:
    print(customer)

# Task 3
report = [12000, 9500, 8800, 13200, 7500]
total = 0
for sale in report:
    total += sale
print(total)  # Expected: 51000

# Task 4
for sale in [12000, 9500, 8800, 13200, 7500]:
    if sale >= 10000:
        print(sale)

# Task 5
report = [12000, 9500, 8800]
total = 0
for sale in report:
    total += sale
print(total)  # Expected: 30300
"""
# Change the values, save, and run this file again.
