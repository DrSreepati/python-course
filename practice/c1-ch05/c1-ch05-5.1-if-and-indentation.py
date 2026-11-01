"""Subtopic 5.1: if, and and the indentation block.
Notes: notes/c1-ch05-5.1-if-and-indentation-bangla.md
       notes/c1-ch05-5.1-if-and-indentation-english.md
"""

# Program 1: a simple if condition
order_amount = 12000
if order_amount >= 10000:
    print("Discount eligible")  # Expected: Discount eligible

# Program 2: a false condition and code outside the block
profit = -500
if profit > 0:
    print("The sale made a profit")
print("Report checked")  # Expected: Report checked

# Program 3: store a comparison result in a Boolean variable
balance = 32000
is_large_balance = balance >= 30000
print(is_large_balance)  # Expected: True
if is_large_balance:
    print("Review customer balance")  # Expected: Review customer balance

# Program 4: multiple lines in an indentation block
order_amount = 12000
if order_amount >= 10000:
    discount_rate = 0.05
    print("Discount rate:", discount_rate)  # Expected: Discount rate: 0.05
print("Order processed")  # Expected: Order processed

# Program 5: two business conditions with and
order_amount = 12000
customer_balance = 50000
if order_amount >= 10000 and customer_balance >= 30000:
    print("Approve discount review")  # Expected: Approve discount review

# Program 6: a complete business decision
customer_name = "Jahid Enterprise"
order_amount = 13200
customer_balance = 71000
large_order = order_amount >= 10000
reliable_balance = customer_balance >= 30000

if large_order and reliable_balance:
    print(f"{customer_name}: approve discount review")
    # Expected: Jahid Enterprise: approve discount review
    print("Reason: large order and balance threshold passed")
    # Expected: Reason: large order and balance threshold passed
print("Decision recorded")  # Expected: Decision recorded

# Task 1: Print "Large order" when order_amount is at least 10000.
# Task 2: Print "Profit" when profit is greater than 0.
# Task 3: Approve when order_amount is at least 10000 and balance is at least 30000.
# Task 4: Print a payment follow-up message for outstanding >= 30000.
# Task 5: Fix Rafiq bhai's boundary bug:
# order_amount = 10000
# if order_amount > 10000:
#     print("Discount eligible")

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
order_amount = 12000
if order_amount >= 10000:
    print("Large order")  # Expected: Large order

# Task 2 solution
profit = 2500
if profit > 0:
    print("Profit")  # Expected: Profit

# Task 3 solution
order_amount = 12000
customer_balance = 50000
if order_amount >= 10000 and customer_balance >= 30000:
    print("Approve")  # Expected: Approve

# Task 4 solution
customer_name = "Karim Store"
outstanding = 32000
if outstanding >= 30000:
    print(f"{customer_name}: follow-up needed")
    # Expected: Karim Store: follow-up needed

# Task 5 solution
order_amount = 10000
if order_amount >= 10000:
    print("Discount eligible")  # Expected: Discount eligible
"""
# Change the values, save, and run this file again.
