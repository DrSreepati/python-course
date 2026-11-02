"""Subtopic 5.5: Business decision classification.
Notes: notes/c1-ch05-5.5-business-classification-bangla.md
       notes/c1-ch05-5.5-business-classification-english.md
"""

# Program 1: discount eligibility
order_amount = 12000
balance = 32000
if order_amount >= 10000 and balance >= 30000:
    print("Eligible")  # Expected: Eligible
else:
    print("Not eligible")

# Program 2: overdue status
outstanding = 50000
days_overdue = 12
payment_received = False
if outstanding > 0 and days_overdue > 0 and not payment_received:
    print("Overdue")  # Expected: Overdue
elif outstanding == 0 or payment_received:
    print("Clear")
else:
    print("Review")

# Program 3: one report with four classifications
budget = 40000
actual_cost = 38000
profit = 2500
paid_amount = 20000
invoice_amount = 20000

if actual_cost > budget:
    budget_status = "Over budget"
elif actual_cost < budget:
    budget_status = "Under budget"
else:
    budget_status = "On budget"

if profit > 0:
    profit_status = "Profit"
elif profit < 0:
    profit_status = "Loss"
else:
    profit_status = "Break-even"

if paid_amount == 0:
    payment_status = "Unpaid"
elif paid_amount < invoice_amount:
    payment_status = "Partly paid"
elif paid_amount == invoice_amount:
    payment_status = "Paid"
else:
    payment_status = "Overpaid"

print(budget_status)  # Expected: Under budget
print(profit_status)  # Expected: Profit
print(payment_status)  # Expected: Paid

# Task 1: classify discount eligibility.
# Task 2: classify an overdue account.
# Task 3: classify actual cost against budget.
# Task 4: classify profit and payment status.
# Task 5: fix Rafiq bhai's zero-profit bug:
# profit = 0
# if profit >= 0:
#     print("Profit")

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
order_amount = 12000
balance = 32000
if order_amount >= 10000 and balance >= 30000:
    print("Eligible")  # Expected: Eligible
else:
    print("Not eligible")

# Task 2 solution
outstanding = 50000
days_overdue = 12
payment_received = False
if outstanding > 0 and days_overdue > 0 and not payment_received:
    print("Overdue")  # Expected: Overdue
elif outstanding == 0 or payment_received:
    print("Clear")
else:
    print("Review")

# Task 3 solution
budget = 40000
actual_cost = 40000
if actual_cost > budget:
    print("Over budget")
elif actual_cost < budget:
    print("Under budget")
else:
    print("On budget")  # Expected: On budget

# Task 4 solution
profit = 0
paid_amount = 12000
invoice_amount = 20000
if profit > 0:
    print("Profit")
elif profit < 0:
    print("Loss")
else:
    print("Break-even")  # Expected: Break-even
if paid_amount == 0:
    print("Unpaid")
elif paid_amount < invoice_amount:
    print("Partly paid")  # Expected: Partly paid
elif paid_amount == invoice_amount:
    print("Paid")
else:
    print("Overpaid")

# Task 5 solution
profit = 0
if profit > 0:
    print("Profit")
elif profit < 0:
    print("Loss")
else:
    print("Break-even")  # Expected: Break-even
"""
# Change the values, save, and run this file again.
