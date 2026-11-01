"""Subtopic 5.1: if, and and the indentation block.
Notes: notes/c1-ch05-5.1-if-and-indentation-bangla.md
       notes/c1-ch05-5.1-if-and-indentation-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Compare the order amount with the inclusive threshold.
# Problem 2: Store each comparison as a Boolean before joining with and.
# Problem 3: Test the exact boundary and the customer balance separately.
# Problem 4: Keep every action that belongs to the rule at the same indentation.
# Problem 5: Preserve the report action outside the conditional approval block.

# Problem 1 (Easy, LeetCode-style)
# Statement: Given one order amount, print whether it reaches the inclusive
# discount threshold of 10000.
# Formal Input: 10000.
# Output: "Discount eligible".
order_amount_1 = 10000

# Problem 2 (Easy, interview-style)
# The boss approves a discount review only when an order is at least 10000 and
# the customer's balance is at least 30000. Print each named rule and the final
# decision.
order_amount_2 = 12000
customer_balance_2 = 50000

# Problem 3 (Medium, real-world business)
# A boundary-order audit checks an order amount and balance. Print the result of
# each comparison and approve only when both rules pass.
order_amount_3 = 10000
customer_balance_3 = 32000

# Problem 4 (Medium, LeetCode-style)
# Statement: Given profit and an outstanding balance, print the applicable
# actions. Profit greater than zero prints "Profit found"; an outstanding
# balance of at least 30000 prints "Payment follow-up needed".
profit_4 = 2500
outstanding_4 = 32000

# Problem 5 (Hard, real-world business)
# The boss wants an audit-friendly discount decision. Use customer name, order
# amount and balance. Print approval details only when both rules pass, then
# always print "Decision recorded" outside the conditional block.
customer_name_5 = "Jahid Enterprise"
order_amount_5 = 13200
customer_balance_5 = 71000

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
order_amount_1 = 10000
discount_eligible_1 = order_amount_1 >= 10000
if discount_eligible_1:
    print("Discount eligible")  # Expected: Discount eligible
# The comparison is O(1) for one numeric value and uses O(1) extra space.

# Problem 2 solution
order_amount_2 = 12000
customer_balance_2 = 50000
large_order_2 = order_amount_2 >= 10000
reliable_balance_2 = customer_balance_2 >= 30000
print(f"Large order: {large_order_2}")
# Expected: Large order: True
print(f"Reliable balance: {reliable_balance_2}")
# Expected: Reliable balance: True
if large_order_2 and reliable_balance_2:
    print("Discount review approved")
    # Expected: Discount review approved
# Interview talking point: named Boolean rules make policy changes easier.
# The work and extra space are O(1).

# Problem 3 solution
order_amount_3 = 10000
customer_balance_3 = 32000
large_order_3 = order_amount_3 >= 10000
reliable_balance_3 = customer_balance_3 >= 30000
print(f"Order threshold passed: {large_order_3}")
# Expected: Order threshold passed: True
print(f"Balance threshold passed: {reliable_balance_3}")
# Expected: Balance threshold passed: True
if large_order_3 and reliable_balance_3:
    print("Boundary order approved")
    # Expected: Boundary order approved
# Testing the exact threshold prevents a > versus >= regression.

# Problem 4 solution
profit_4 = 2500
outstanding_4 = 32000
if profit_4 > 0:
    print("Profit found")  # Expected: Profit found
if outstanding_4 >= 30000:
    print("Payment follow-up needed")
    # Expected: Payment follow-up needed
# Each independent rule gets its own if block; both actions can apply.

# Problem 5 solution
customer_name_5 = "Jahid Enterprise"
order_amount_5 = 13200
customer_balance_5 = 71000
large_order_5 = order_amount_5 >= 10000
reliable_balance_5 = customer_balance_5 >= 30000

if large_order_5 and reliable_balance_5:
    print(f"{customer_name_5}: approve discount review")
    # Expected: Jahid Enterprise: approve discount review
    print("Reason: large order and balance threshold passed")
    # Expected: Reason: large order and balance threshold passed
print("Decision recorded")
# Expected: Decision recorded
# Each rule uses constant-time numeric comparisons, so the workflow is O(1)
# in time and O(1) in extra space. The outside report action is unconditional.
# Interview talking point: keep audit logging outside the decision block when
# every attempt must be recorded.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
