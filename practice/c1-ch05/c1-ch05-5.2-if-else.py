"""Subtopic 5.2: if-else and if-elif-else.
Notes: notes/c1-ch05-5.2-if-else-bangla.md
       notes/c1-ch05-5.2-if-else-english.md
"""

# Program 1: a two-path discount decision
order_amount = 8000
if order_amount >= 10000:
    print("Discount eligible")  # Expected: not printed
else:
    print("No discount")  # Expected: No discount

# Program 2: profit or loss/break-even
profit = 2500
if profit > 0:
    print("Profit")  # Expected: Profit
else:
    print("Loss or break-even")

# Program 3: assign one common message from either branch
order_amount = 12000
if order_amount >= 10000:
    message = "Discount approved"
else:
    message = "No discount"
print(message)  # Expected: Discount approved

# Program 4: payment-status classification
customer_name = "Karim Store"
outstanding = 32000
if outstanding == 0:
    status = "Paid"
elif outstanding >= 30000:
    status = "High outstanding"
else:
    status = "Small outstanding"
print(f"{customer_name}: {status}")  # Expected: Karim Store: High outstanding

# Program 5: profit/loss/break-even classification
profit = 0
if profit > 0:
    label = "Profit"
elif profit < 0:
    label = "Loss"
else:
    label = "Break-even"
print(label)  # Expected: Break-even

# Program 6: threshold order and a fallback
order_amount = 15000
if order_amount >= 15000:
    print("Gold order")  # Expected: Gold order
elif order_amount >= 10000:
    print("Silver order")
else:
    print("Standard order")

# Program 7: complete discount category workflow
customer_name = "Jahid Enterprise"
order_amount = 13200
customer_balance = 71000

if order_amount >= 15000 and customer_balance >= 30000:
    decision = "Gold discount review"
elif order_amount >= 10000 and customer_balance >= 30000:
    decision = "Standard discount review"
else:
    decision = "No discount review"

print(f"{customer_name}: {decision}")
# Expected: Jahid Enterprise: Standard discount review

# Task 1: Print "No discount" for order_amount = 8000, otherwise "Discount".
# Task 2: Print "Profit" for a positive profit, otherwise "Loss or break-even".
# Task 3: Classify outstanding as Paid, High outstanding or Small outstanding.
# Task 4: Classify 15000+ as Gold, 10000+ as Standard, and the rest as Basic.
# Task 5: Fix Rafiq bhai's threshold-order bug:
# order_amount = 15000
# if order_amount >= 10000:
#     print("Standard")
# elif order_amount >= 15000:
#     print("Gold")

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
order_amount = 8000
if order_amount >= 10000:
    print("Discount")  # Expected: not printed
else:
    print("No discount")  # Expected: No discount

# Task 2 solution
profit = -500
if profit > 0:
    print("Profit")
else:
    print("Loss or break-even")  # Expected: Loss or break-even

# Task 3 solution
outstanding = 32000
if outstanding == 0:
    print("Paid")
elif outstanding >= 30000:
    print("High outstanding")  # Expected: High outstanding
else:
    print("Small outstanding")

# Task 4 solution
order_amount = 15000
if order_amount >= 15000:
    print("Gold")  # Expected: Gold
elif order_amount >= 10000:
    print("Standard")
else:
    print("Basic")

# Task 5 solution
order_amount = 15000
if order_amount >= 15000:
    print("Gold")  # Expected: Gold
elif order_amount >= 10000:
    print("Standard")
else:
    print("Basic")
"""
# Change the values, save, and run this file again.
