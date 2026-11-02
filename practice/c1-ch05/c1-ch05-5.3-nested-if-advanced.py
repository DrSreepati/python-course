"""Subtopic 5.3: Nested if.
Notes: notes/c1-ch05-5.3-nested-if-bangla.md
       notes/c1-ch05-5.3-nested-if-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Test the order gate before the balance gate.
# Problem 2: Give zero outstanding its own branch.
# Problem 3: Use the larger order threshold inside the eligible branch.
# Problem 4: Keep each business approval gate at its own indentation level.
# Problem 5: Write the decision tree before coding its three gates.

# Problem 1 (Easy, LeetCode-style)
# Given an order and balance, return the approval label.
# Formal Input: order_amount = 12000, balance = 32000.
# Output: "Approved".
# Constraints: use comparisons and nested if only.
order_amount_1 = 12000
balance_1 = 32000

# Problem 2 (Easy, interview-style)
# Classify a customer. First decide whether the order is large.
# Then classify zero outstanding as Paid, otherwise Payment pending.
# Follow-up: which values are boundary tests for order size?
order_amount_2 = 15000
outstanding_2 = 0

# Problem 3 (Medium, business report)
# The boss wants Gold review for order >= 15000, but only when balance
# >= 30000. Other eligible orders receive Standard review.
customer_name_3 = "Jahid Enterprise"
order_amount_3 = 13200
balance_3 = 71000

# Problem 4 (Medium, interview-style)
# Approve only when account balance is healthy, order is large, and profit
# is positive. Give a different message for each failed gate.
# Follow-up: how would you test exact thresholds 30000 and 10000?
balance_4 = 71000
order_amount_4 = 13200
profit_4 = 2500

# Problem 5 (Hard, business workflow)
# Review five named customer orders. For each record, first reject small orders,
# then hold weak balances, then separate profitable and loss-making orders.
# Use only the conditional tools taught so far.
orders_5 = [
    ["Rahim Traders", 12000, 50000, 2500],
    ["Karim Store", 8000, 32000, 1000],
    ["Jahid Enterprise", 15000, 71000, -500],
    ["Nila Market", 11000, 20000, 1800],
    ["Bashundhara Shop", 10000, 30000, 0],
]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Check the order threshold.
# 2. If eligible, check the balance threshold.
# 3. Select a clear result for every path.
if order_amount_1 >= 10000:
    if balance_1 >= 30000:
        result_1 = "Approved"
    else:
        result_1 = "Balance hold"
else:
    result_1 = "Order too small"
print(result_1)
# Expected: Approved
# Key lines: the outer if checks eligibility; the inner if checks credit.
# Complexity: fixed checks do not grow with input, O(1).

# Problem 2 solution
# Approach:
# 1. Check whether the order is large.
# 2. Check zero before the fallback payment state.
# 3. Print the selected label.
if order_amount_2 >= 10000:
    if outstanding_2 == 0:
        result_2 = "Paid"
    else:
        result_2 = "Payment pending"
else:
    result_2 = "Small order"
print(result_2)
# Expected: Paid
# Key lines: the outer branch protects the payment test.
# Complexity: constant work, O(1).
# Interview talking point: state why zero is a meaningful business case.

# Problem 3 solution
# Approach:
# 1. Reject orders below 10000.
# 2. Inside eligible orders, test 15000 first.
# 3. Keep the customer's name in the report.
if order_amount_3 >= 10000:
    if order_amount_3 >= 15000:
        result_3 = "Gold review"
    else:
        result_3 = "Standard review"
else:
    result_3 = "No review"
print(f"{customer_name_3}: {result_3}")
# Expected: Jahid Enterprise: Standard review
# Key lines: the inner threshold distinguishes the two eligible categories.
# Complexity: fixed comparisons, O(1).

# Problem 4 solution
# Approach:
# 1. Check the account gate.
# 2. Check order size only after the account passes.
# 3. Check profit only after both earlier gates pass.
if balance_4 >= 30000:
    if order_amount_4 >= 10000:
        if profit_4 > 0:
            result_4 = "Approved"
        else:
            result_4 = "Profit review"
    else:
        result_4 = "Order review"
else:
    result_4 = "Account hold"
print(result_4)
# Expected: Approved
# Key lines: each indentation level represents one business gate.
# Complexity: fixed checks, O(1).
# Interview talking point: explain why each failure has a separate message.

# Problem 5 solution
# Approach:
# 1. Visit each order record.
# 2. Reject a small order before checking credit.
# 3. Hold a weak balance before checking profit.
# 4. Label the remaining order by profit.
for customer, order_amount, balance, profit in orders_5:
    if order_amount < 10000:
        result = "Small order"
    else:
        if balance < 30000:
            result = "Account hold"
        else:
            if profit > 0:
                result = "Approve profitable order"
            elif profit < 0:
                result = "Profit review"
            else:
                result = "Break-even review"
    print(f"{customer}: {result}")
# Expected:
# Rahim Traders: Approve profitable order
# Karim Store: Small order
# Jahid Enterprise: Profit review
# Nila Market: Account hold
# Bashundhara Shop: Break-even review
# Key lines: the loop processes records; nested branches preserve gate order.
# Complexity: one decision tree per record, O(n).
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
