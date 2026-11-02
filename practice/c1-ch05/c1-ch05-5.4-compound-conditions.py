"""Subtopic 5.4: Compound conditions in real rules.
Notes: notes/c1-ch05-5.4-compound-conditions-bangla.md
       notes/c1-ch05-5.4-compound-conditions-english.md
"""

# Program 1: all required conditions
order_amount = 12000
customer_balance = 32000
if order_amount >= 10000 and customer_balance >= 30000:
    print("Discount review approved")  # Expected: Discount review approved
else:
    print("Discount review held")

# Program 2: one alternative condition
outstanding = 32000
order_amount = 8000
if outstanding >= 30000 or order_amount >= 15000:
    print("Manager review")  # Expected: Manager review
else:
    print("Normal review")

# Program 3: named rules
order_amount = 13200
customer_balance = 71000
payment_received = True
large_order = order_amount >= 10000
safe_balance = customer_balance >= 30000
if large_order and safe_balance and payment_received:
    print("Release order")  # Expected: Release order
else:
    print("Hold order")

# Task 1: Approve order 12000 with balance 32000 using and.
# Task 2: Use or for outstanding 32000 or order 15000.
# Task 3: Use not when payment_received is False.
# Task 4: Release an order only when it is large, safe, and paid.
# Task 5: Fix Rafiq bhai's or bug:
# if order_amount >= 10000 or balance >= 30000:
#     print("Discount approved")

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
order_amount = 12000
balance = 32000
if order_amount >= 10000 and balance >= 30000:
    print("Approve")  # Expected: Approve
else:
    print("Hold")

# Task 2 solution
outstanding = 32000
order_amount = 8000
if outstanding >= 30000 or order_amount >= 15000:
    print("Manager review")  # Expected: Manager review
else:
    print("Normal review")

# Task 3 solution
payment_received = False
if not payment_received:
    print("Follow-up")  # Expected: Follow-up
else:
    print("Clear")

# Task 4 solution
order_amount = 13200
balance = 71000
payment_received = True
large_order = order_amount >= 10000
safe_balance = balance >= 30000
if large_order and safe_balance and payment_received:
    print("Release")  # Expected: Release
else:
    print("Hold")

# Task 5 solution
order_amount = 8000
balance = 50000
if order_amount >= 10000 and balance >= 30000:
    print("Discount approved")
else:
    print("Hold")  # Expected: Hold
"""
# Change the values, save, and run this file again.
