"""Subtopic 6.6: Business practice.
Notes: notes/c1-ch06-6.6-business-practice-bangla.md
       notes/c1-ch06-6.6-business-practice-english.md
"""

# Program 1: transaction processing
transactions = [5000, 4200, 6100, 3800]
transaction_total = 0
for amount in transactions:
    if amount <= 0:
        continue
    transaction_total += amount
print(f"Transaction total: {transaction_total}")  # Expected: 19100

# Program 2: invoice total
invoice_items = [12000, 8000, 5000]
invoice_total = 0
for item_amount in invoice_items:
    invoice_total += item_amount
print(f"Invoice total: {invoice_total}")  # Expected: 25000

# Program 3: running balance
balance = 50000
for payment in [10000, 15000, 5000]:
    balance -= payment
print(f"Final balance: {balance}")  # Expected: 20000

# Program 4: monthly expense summary
monthly_expenses = [[12000, 8000], [9500, 7000], [11000, 6000]]
overall_expense = 0
month_number = 1
for expenses in monthly_expenses:
    month_total = 0
    for expense in expenses:
        month_total += expense
        overall_expense += expense
    print(f"Month {month_number}: {month_total}")
    month_number += 1
print(f"Overall expense: {overall_expense}")  # Expected: 53500

# Task 1: Process transactions and total them.
# Task 2: Calculate an invoice total.
# Task 3: Update a running balance.
# Task 4: Summarise monthly expenses.
# Task 5: Fix Rafiq bhai's balance = payment bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
total = 0
for amount in [5000, 4200, 6100]:
    total += amount
print(total)  # Expected: 15300

# Task 2
invoice_total = 0
for amount in [12000, 8000]:
    invoice_total += amount
print(invoice_total)  # Expected: 20000

# Task 3
balance = 50000
for payment in [10000, 5000]:
    balance -= payment
print(balance)  # Expected: 35000

# Task 4
months = [[12000, 8000], [9500, 7000]]
overall = 0
for expenses in months:
    month_total = 0
    for expense in expenses:
        month_total += expense
        overall += expense
    print(month_total)
print(overall)  # Expected: 20000, 16500, 36500

# Task 5
balance = 50000
for payment in [10000, 5000]:
    balance -= payment
print(balance)  # Expected: 35000
"""
# Change the values, save, and run this file again.
