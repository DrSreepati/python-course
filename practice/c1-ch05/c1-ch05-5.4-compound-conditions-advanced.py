"""Subtopic 5.4: Compound conditions in real rules.
Notes: notes/c1-ch05-5.4-compound-conditions-bangla.md
       notes/c1-ch05-5.4-compound-conditions-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: all three tests must be true.
# Problem 2: zero payment is a separate business case.
# Problem 3: use parentheses around the two valid priority routes.
# Problem 4: name each Boolean before combining it.
# Problem 5: write each customer's rule with the same business wording.

# Problem 1 (Easy, LeetCode-style)
# Given an order, balance, and payment flag, return Release or Hold.
# Formal Input: 12000, 32000, True.
# Output: "Release".
# Constraints: use and, not, and comparisons.
order_amount_1 = 12000
balance_1 = 32000
payment_received_1 = True

# Problem 2 (Easy, interview-style)
# Classify an account as Overdue follow-up when money is outstanding,
# days are overdue, and payment has not arrived.
# Follow-up: which exact values should test the zero boundaries?
outstanding_2 = 50000
days_overdue_2 = 12
payment_received_2 = False

# Problem 3 (Medium, business request)
# A manager wants priority when either a large order has a safe balance,
# or the customer has a serious outstanding balance.
customer_name_3 = "Karim Store"
order_amount_3 = 12000
balance_3 = 32000
outstanding_3 = 32000

# Problem 4 (Medium, interview-style)
# Build readable Boolean rules for a profitable, paid credit order.
# Follow-up: how would named Booleans help a code review?
order_amount_4 = 13200
balance_4 = 71000
profit_4 = 2500
payment_received_4 = True

# Problem 5 (Hard, real-world business)
# The boss has five named review facts. Write one compound condition for
# each record, without loops, functions, or later topics.
rahim_order_5 = 12000
rahim_balance_5 = 50000
rahim_payment_5 = False

karim_order_5 = 8000
karim_balance_5 = 32000
karim_payment_5 = True

jahid_order_5 = 15000
jahid_balance_5 = 71000
jahid_payment_5 = True

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Check the order threshold.
# 2. Check the balance threshold.
# 3. Require payment to have arrived.
if order_amount_1 >= 10000 and balance_1 >= 30000 and payment_received_1:
    result_1 = "Release"
else:
    result_1 = "Hold"
print(result_1)
# Expected: Release
# Key line: and requires every business gate to pass.
# Complexity: a fixed number of checks, O(1).

# Problem 2 solution
# Approach:
# 1. Require a positive outstanding balance.
# 2. Require positive overdue days.
# 3. Reverse the payment flag.
if outstanding_2 > 0 and days_overdue_2 > 0 and not payment_received_2:
    result_2 = "Overdue follow-up"
else:
    result_2 = "Review account"
print(result_2)
# Expected: Overdue follow-up
# Key line: not payment_received_2 means payment is still missing.
# Complexity: fixed checks, O(1).
# Interview talking point: mention zero and exact boundary tests.

# Problem 3 solution
# Approach:
# 1. Group the large-order route.
# 2. Add the serious-outstanding alternative.
# 3. Print the customer's result.
if (order_amount_3 >= 10000 and balance_3 >= 30000) or outstanding_3 >= 30000:
    result_3 = "Manager priority"
else:
    result_3 = "Normal queue"
print(f"{customer_name_3}: {result_3}")
# Expected: Karim Store: Manager priority
# Key line: parentheses keep the first route together.
# Complexity: fixed comparisons, O(1).

# Problem 4 solution
# Approach:
# 1. Name the order, balance, profit, and payment rules.
# 2. Join all required rules with and.
# 3. Select the business result.
large_order_4 = order_amount_4 >= 10000
safe_balance_4 = balance_4 >= 30000
profitable_4 = profit_4 > 0
paid_4 = payment_received_4
if large_order_4 and safe_balance_4 and profitable_4 and paid_4:
    result_4 = "Release profitable order"
else:
    result_4 = "Hold for review"
print(result_4)
# Expected: Release profitable order
# Key lines: each Boolean names one auditable rule.
# Complexity: fixed checks, O(1).
# Interview talking point: named conditions make failures easier to isolate.

# Problem 5 solution
# Approach:
# 1. Check every named customer's order, balance, and payment.
# 2. Use the same rule for each customer.
# 3. Print separate results for this small fixed report.
rahim_release = rahim_order_5 >= 10000 and rahim_balance_5 >= 30000 and rahim_payment_5
karim_release = karim_order_5 >= 10000 and karim_balance_5 >= 30000 and karim_payment_5
jahid_release = jahid_order_5 >= 10000 and jahid_balance_5 >= 30000 and jahid_payment_5
if rahim_release:
    print("Rahim Traders: Release")
else:
    print("Rahim Traders: Hold")
if karim_release:
    print("Karim Store: Release")
else:
    print("Karim Store: Hold")
if jahid_release:
    print("Jahid Enterprise: Release")
else:
    print("Jahid Enterprise: Hold")
# Expected:
# Rahim Traders: Hold
# Karim Store: Hold
# Jahid Enterprise: Release
# Key lines: each record uses the same compound business rule.
# Complexity: fixed three-record report, O(1) for this fixed input.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
