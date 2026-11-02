"""Subtopic 5.5: Business decision classification.
Notes: notes/c1-ch05-5.5-business-classification-bangla.md
       notes/c1-ch05-5.5-business-classification-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: test both discount gates with and.
# Problem 2: test zero outstanding before the overdue rule.
# Problem 3: compare actual cost in both directions.
# Problem 4: handle profit zero and payment boundaries separately.
# Problem 5: give each report question its own status variable.

# Problem 1 (Easy, LeetCode-style)
# Classify one order as Eligible or Not eligible.
# Formal Input: order = 12000, balance = 32000.
# Output: "Eligible".
order_1 = 12000
balance_1 = 32000

# Problem 2 (Easy, interview-style)
# Classify an account as Overdue, Clear, or Review.
# Follow-up: why must zero outstanding be checked explicitly?
outstanding_2 = 50000
days_overdue_2 = 12
payment_received_2 = False

# Problem 3 (Medium, business report)
# Classify a budget as Over budget, Under budget, or On budget.
budget_3 = 40000
actual_cost_3 = 42500

# Problem 4 (Medium, interview-style)
# Classify profit and payment independently.
# Follow-up: which boundary cases would you test?
profit_4 = -500
invoice_4 = 20000
paid_4 = 12000

# Problem 5 (Hard, real-world business)
# The boss wants one fixed report containing five named business decisions.
# Use only conditions taught so far, without loops or functions.
customer_name_5 = "Jahid Enterprise"
order_5 = 13200
balance_5 = 71000
outstanding_5 = 0
days_overdue_5 = 0
payment_received_5 = True
budget_5 = 40000
actual_cost_5 = 38000
profit_5 = 2500
invoice_5 = 20000
paid_5 = 20000

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Check the order threshold.
# 2. Check the balance threshold.
# 3. Select one status.
if order_1 >= 10000 and balance_1 >= 30000:
    result_1 = "Eligible"
else:
    result_1 = "Not eligible"
print(result_1)
# Expected: Eligible
# Complexity: fixed checks, O(1).

# Problem 2 solution
# Approach:
# 1. Detect a genuinely overdue account.
# 2. Detect a clear account.
# 3. Keep the remaining case for review.
if outstanding_2 > 0 and days_overdue_2 > 0 and not payment_received_2:
    result_2 = "Overdue"
elif outstanding_2 == 0 or payment_received_2:
    result_2 = "Clear"
else:
    result_2 = "Review"
print(result_2)
# Expected: Overdue
# Complexity: fixed checks, O(1).
# Interview talking point: zero outstanding means a separate business state.

# Problem 3 solution
# Approach:
# 1. Compare actual cost above budget.
# 2. Compare it below budget.
# 3. Use equality as the final category.
if actual_cost_3 > budget_3:
    result_3 = "Over budget"
elif actual_cost_3 < budget_3:
    result_3 = "Under budget"
else:
    result_3 = "On budget"
print(result_3)
# Expected: Over budget
# Complexity: fixed comparisons, O(1).

# Problem 4 solution
# Approach:
# 1. Classify positive, negative, and zero profit.
# 2. Classify paid amount against the invoice.
# 3. Print both statuses.
if profit_4 > 0:
    profit_result_4 = "Profit"
elif profit_4 < 0:
    profit_result_4 = "Loss"
else:
    profit_result_4 = "Break-even"
if paid_4 == 0:
    payment_result_4 = "Unpaid"
elif paid_4 < invoice_4:
    payment_result_4 = "Partly paid"
elif paid_4 == invoice_4:
    payment_result_4 = "Paid"
else:
    payment_result_4 = "Overpaid"
print(profit_result_4)
print(payment_result_4)
# Expected:
# Loss
# Partly paid
# Complexity: fixed comparisons, O(1).
# Interview talking point: explain why profit and payment are independent rules.

# Problem 5 solution
# Approach:
# 1. Classify discount eligibility.
# 2. Classify overdue status.
# 3. Classify budget, profit, and payment.
# 4. Print the complete report.
if order_5 >= 10000 and balance_5 >= 30000:
    discount_5 = "Eligible"
else:
    discount_5 = "Not eligible"
if outstanding_5 > 0 and days_overdue_5 > 0 and not payment_received_5:
    overdue_5 = "Overdue"
elif outstanding_5 == 0 or payment_received_5:
    overdue_5 = "Clear"
else:
    overdue_5 = "Review"
if actual_cost_5 > budget_5:
    budget_status_5 = "Over budget"
elif actual_cost_5 < budget_5:
    budget_status_5 = "Under budget"
else:
    budget_status_5 = "On budget"
if profit_5 > 0:
    profit_status_5 = "Profit"
elif profit_5 < 0:
    profit_status_5 = "Loss"
else:
    profit_status_5 = "Break-even"
if paid_5 == 0:
    payment_status_5 = "Unpaid"
elif paid_5 < invoice_5:
    payment_status_5 = "Partly paid"
elif paid_5 == invoice_5:
    payment_status_5 = "Paid"
else:
    payment_status_5 = "Overpaid"
print(customer_name_5)
print(discount_5)
print(overdue_5)
print(budget_status_5)
print(profit_status_5)
print(payment_status_5)
# Expected:
# Jahid Enterprise
# Eligible
# Clear
# Under budget
# Profit
# Paid
# Complexity: a fixed five-question report, O(1).
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
