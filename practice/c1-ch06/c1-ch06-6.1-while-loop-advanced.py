"""Subtopic 6.1: while loop and the loop variable.
Notes: notes/c1-ch06-6.1-while-loop-bangla.md
       notes/c1-ch06-6.1-while-loop-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: start at one and increase the invoice number.
# Problem 2: update the balance and the month on every pass.
# Problem 3: use the outstanding amount as the stopping state.
# Problem 4: count attempts and stop after the third attempt.
# Problem 5: make each payment reduce the remaining balance.

# Problem 1 (Easy, LeetCode-style)
# Print invoice numbers from 1 through 5.
# Formal Input: first_invoice = 1, last_invoice = 5.
# Output: 1, 2, 3, 4, 5.
first_invoice_1 = 1
last_invoice_1 = 5

# Problem 2 (Easy, interview-style)
# A customer pays 10000 each month from a balance of 50000.
# Print each month and its remaining balance.
# Follow-up: what changes when the payment is 12500?
balance_2 = 50000
monthly_payment_2 = 10000
month_2 = 1

# Problem 3 (Medium, real-world business)
# The boss wants to follow up until outstanding reaches zero.
# Start with 30000 and collect 10000 each round.
outstanding_3 = 30000
collection_3 = 10000
follow_up_3 = 1

# Problem 4 (Medium, interview-style)
# Print attempts while an account review has fewer than three attempts.
# Follow-up: why must attempts change inside the loop?
attempt_4 = 1
max_attempts_4 = 3

# Problem 5 (Hard, real-world business)
# Process a fixed payment plan. Start with 60000 and collect 15000 each pass.
# Print the payment number and remaining balance. Stop at zero.
remaining_5 = 60000
payment_5 = 15000
payment_number_5 = 1

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Start at the first invoice.
# 2. Print the current invoice.
# 3. Increase it until the final invoice is printed.
invoice_1 = first_invoice_1
while invoice_1 <= last_invoice_1:
    print(invoice_1)
    invoice_1 += 1
# Expected:
# 1
# 2
# 3
# 4
# 5
# Complexity: work grows with the invoice count, O(n).

# Problem 2 solution
# Approach:
# 1. Continue while three months remain.
# 2. Subtract the payment.
# 3. Print the new balance and advance the month.
while month_2 <= 3:
    balance_2 -= monthly_payment_2
    print(f"Month {month_2}: balance {balance_2}")
    month_2 += 1
# Expected:
# Month 1: balance 40000
# Month 2: balance 30000
# Month 3: balance 20000
# Complexity: three fixed passes, O(1) for this input.
# Interview talking point: put every state update inside the loop.

# Problem 3 solution
# Approach:
# 1. Continue while money remains.
# 2. Collect one fixed amount.
# 3. Print the follow-up and remaining amount.
while outstanding_3 > 0:
    outstanding_3 -= collection_3
    print(f"Follow-up {follow_up_3}: outstanding {outstanding_3}")
    follow_up_3 += 1
# Expected:
# Follow-up 1: outstanding 20000
# Follow-up 2: outstanding 10000
# Follow-up 3: outstanding 0
# Complexity: one pass per collection, O(n).

# Problem 4 solution
# Approach:
# 1. Check whether the attempt limit is reached.
# 2. Print the current attempt.
# 3. Increase the attempt number.
while attempt_4 <= max_attempts_4:
    print(f"Review attempt {attempt_4}")
    attempt_4 += 1
# Expected:
# Review attempt 1
# Review attempt 2
# Review attempt 3
# Complexity: O(n), where n is the attempt limit.
# Interview talking point: without the increment, the loop never reaches its stop state.

# Problem 5 solution
# Approach:
# 1. Continue while a balance remains.
# 2. Subtract one payment.
# 3. Print the payment number and new balance.
# 4. Advance the payment number.
while remaining_5 > 0:
    remaining_5 -= payment_5
    print(f"Payment {payment_number_5}: remaining {remaining_5}")
    payment_number_5 += 1
# Expected:
# Payment 1: remaining 45000
# Payment 2: remaining 30000
# Payment 3: remaining 15000
# Payment 4: remaining 0
# Complexity: one pass per payment, O(n).
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
