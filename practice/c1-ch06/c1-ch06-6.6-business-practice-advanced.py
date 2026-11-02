"""Subtopic 6.6: Business practice.
Notes: notes/c1-ch06-6.6-business-practice-bangla.md
       notes/c1-ch06-6.6-business-practice-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: skip non-positive transactions and accumulate the rest.
# Problem 2: add every invoice line to one total.
# Problem 3: subtract every payment from the opening balance.
# Problem 4: reset the month total, but not the overall total.
# Problem 5: combine all four report patterns in separate sections.

# Problem 1 (Easy, LeetCode-style)
# Process transaction amounts. Ignore zero or negative values.
# Formal Input: [5000, 0, 4200, -100].
# Output: total 9200.
transactions_1 = [5000, 0, 4200, -100]

# Problem 2 (Easy, interview-style)
# Calculate an invoice total from line amounts.
# Follow-up: why must the accumulator start before the loop?
invoice_lines_2 = [12000, 8000, 5000]

# Problem 3 (Medium, real-world business)
# Track a customer balance of 71000 after payments of 20000, 15000,
# and 6000. Print each remaining balance.
opening_balance_3 = 71000
payments_3 = [20000, 15000, 6000]

# Problem 4 (Medium, interview-style)
# Summarise monthly expenses and print the overall expense.
# Follow-up: which accumulator resets for each month?
monthly_expenses_4 = [[12000, 8000], [9500, 7000], [11000, 6000]]

# Problem 5 (Hard, real-world business)
# Build one fixed management report with transaction total, invoice total,
# final balance, and monthly expense totals.
transactions_5 = [5000, 4200, 6100, 3800]
invoice_lines_5 = [12000, 8000, 5000]
opening_balance_5 = 50000
payments_5 = [10000, 15000, 5000]
monthly_expenses_5 = [[12000, 8000], [9500, 7000], [11000, 6000]]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Start a transaction total.
# 2. Skip non-positive values.
# 3. Add valid values.
transaction_total_1 = 0
for amount in transactions_1:
    if amount <= 0:
        continue
    transaction_total_1 += amount
print(transaction_total_1)
# Expected: 9200
# Complexity: one pass, O(n).

# Problem 2 solution
# Approach:
# 1. Start at zero.
# 2. Add each invoice line.
# 3. Print the total.
invoice_total_2 = 0
for line in invoice_lines_2:
    invoice_total_2 += line
print(invoice_total_2)
# Expected: 25000
# Complexity: one pass, O(n).
# Interview talking point: initialise before the loop to preserve earlier lines.

# Problem 3 solution
# Approach:
# 1. Start with the opening balance.
# 2. Subtract each payment.
# 3. Print the state after every payment.
balance_3 = opening_balance_3
for payment in payments_3:
    balance_3 -= payment
    print(f"After {payment}: {balance_3}")
# Expected:
# After 20000: 51000
# After 15000: 36000
# After 6000: 30000
# Complexity: one pass, O(n).

# Problem 4 solution
# Approach:
# 1. Start the overall total once.
# 2. Reset a month total for each month.
# 3. Add each expense to both needed totals.
overall_4 = 0
month_number_4 = 1
for expenses in monthly_expenses_4:
    month_total_4 = 0
    for expense in expenses:
        month_total_4 += expense
        overall_4 += expense
    print(f"Month {month_number_4}: {month_total_4}")
    month_number_4 += 1
print(f"Overall: {overall_4}")
# Expected:
# Month 1: 20000
# Month 2: 16500
# Month 3: 17000
# Overall: 53500
# Complexity: one pass per expense, O(n * m) for grouped data.
# Interview talking point: month total resets, overall total does not.

# Problem 5 solution
# Approach:
# 1. Process valid transactions.
# 2. Add invoice lines.
# 3. Track payments.
# 4. Summarise each expense month.
transaction_total_5 = 0
for amount in transactions_5:
    if amount > 0:
        transaction_total_5 += amount
invoice_total_5 = 0
for line in invoice_lines_5:
    invoice_total_5 += line
balance_5 = opening_balance_5
for payment in payments_5:
    balance_5 -= payment
overall_expense_5 = 0
month_number_5 = 1
for expenses in monthly_expenses_5:
    month_total_5 = 0
    for expense in expenses:
        month_total_5 += expense
        overall_expense_5 += expense
    print(f"Month {month_number_5}: {month_total_5}")
    month_number_5 += 1
print(f"Transaction total: {transaction_total_5}")
print(f"Invoice total: {invoice_total_5}")
print(f"Final balance: {balance_5}")
print(f"Overall expense: {overall_expense_5}")
# Expected:
# Month 1: 20000
# Month 2: 16500
# Month 3: 17000
# Transaction total: 19100
# Invoice total: 25000
# Final balance: 20000
# Overall expense: 53500
# Complexity: linear in all transaction, invoice, payment, and expense items.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
