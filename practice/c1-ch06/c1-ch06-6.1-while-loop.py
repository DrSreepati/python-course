"""Subtopic 6.1: while loop and the loop variable.
Notes: notes/c1-ch06-6.1-while-loop-bangla.md
       notes/c1-ch06-6.1-while-loop-english.md
"""

# Program 1: report days
day = 1
while day <= 3:
    print(f"Preparing report for day {day}")  # Expected: days 1, 2, 3
    day += 1

# Program 2: running balance
balance = 50000
payment = 10000
month = 1
while month <= 3:
    balance -= payment
    print(f"Month {month}: balance {balance}")  # Expected: 40000, 30000, 20000
    month += 1

# Program 3: stop at zero
remaining_invoices = 3
while remaining_invoices > 0:
    print(f"Invoices left: {remaining_invoices}")  # Expected: 3, 2, 1
    remaining_invoices -= 1
print("Invoice check complete")  # Expected: Invoice check complete

# Task 1: Print days 1 to 3.
# Task 2: Check invoices 1 to 3.
# Task 3: Subtract 10000 three times from 50000.
# Task 4: Dispatch two stock units.
# Task 5: Fix the missing counter update in Rafiq bhai's loop.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
day = 1
while day <= 3:
    print(day)  # Expected: 1, 2, 3
    day += 1

# Task 2
invoice = 1
while invoice <= 3:
    print(f"Checking invoice {invoice}")
    invoice += 1

# Task 3
balance = 50000
count = 1
while count <= 3:
    balance -= 10000
    count += 1
print(balance)  # Expected: 20000

# Task 4
stock = 2
while stock > 0:
    print("Dispatch one unit")
    stock -= 1

# Task 5
invoice = 1
while invoice <= 3:
    print(f"Checking invoice {invoice}")
    invoice += 1
"""
# Change the values, save, and run this file again.
