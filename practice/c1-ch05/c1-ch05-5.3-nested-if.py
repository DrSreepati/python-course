"""Subtopic 5.3: Nested if.
Notes: notes/c1-ch05-5.3-nested-if-bangla.md
       notes/c1-ch05-5.3-nested-if-english.md
"""

# Program 1: eligibility followed by balance
order_amount = 12000
customer_balance = 32000
if order_amount >= 10000:
    if customer_balance >= 30000:
        print("Discount review approved")  # Expected: Discount review approved
    else:
        print("Hold for balance review")
else:
    print("Order too small")

# Program 2: three outcomes
order_amount = 15000
outstanding = 0
if order_amount >= 10000:
    if outstanding == 0:
        label = "Large order, paid"
    else:
        label = "Large order, payment pending"
else:
    label = "Small order"
print(label)  # Expected: Large order, paid

# Program 3: three-level decision
balance = 71000
order_amount = 13200
profit = 2500
if balance >= 30000:
    if order_amount >= 10000:
        if profit > 0:
            print("Approve profitable credit order")
        else:
            print("Review profit before approval")
    else:
        print("Review order size")
else:
    print("Hold customer account")
# Expected: Approve profitable credit order

# Task 1: Approve order 12000 when balance is 32000.
# Task 2: Print Small order for order_amount = 9500.
# Task 3: Classify a large order as Paid or Payment pending.
# Task 4: Check balance, order size, and profit in nested levels.
# Task 5: Fix the missing order gate in Rafiq bhai's code:
# order_amount = 8000
# balance = 50000
# if balance >= 30000:
#     print("Approve")

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
order_amount = 12000
balance = 32000
if order_amount >= 10000:
    if balance >= 30000:
        print("Approve")  # Expected: Approve

# Task 2
order_amount = 9500
if order_amount >= 10000:
    print("Large order")
else:
    print("Small order")  # Expected: Small order

# Task 3
order_amount = 15000
outstanding = 32000
if order_amount >= 10000:
    if outstanding == 0:
        print("Paid")
    else:
        print("Payment pending")  # Expected: Payment pending
else:
    print("Small order")

# Task 4
balance = 71000
order_amount = 13200
profit = 2500
if balance >= 30000:
    if order_amount >= 10000:
        if profit > 0:
            print("Approve")  # Expected: Approve
        else:
            print("Review profit")
    else:
        print("Review order")
else:
    print("Hold account")

# Task 5
order_amount = 8000
balance = 50000
if order_amount >= 10000:
    if balance >= 30000:
        print("Approve")
    else:
        print("Hold")
else:
    print("Small order")  # Expected: Small order
"""
# Change the values, save, and run this file again.
