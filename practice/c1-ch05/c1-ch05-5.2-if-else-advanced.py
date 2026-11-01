"""Subtopic 5.2: if-else and if-elif-else.
Notes: notes/c1-ch05-5.2-if-else-bangla.md
       notes/c1-ch05-5.2-if-else-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Use if-else so exactly one message is selected.
# Problem 2: Put the zero case first, then the high threshold, then fallback.
# Problem 3: Test the larger threshold before the smaller threshold.
# Problem 4: Use positive, negative and zero as three mutually exclusive cases.
# Problem 5: Keep both discount categories and the fallback in one ordered chain.

# Problem 1 (Easy, LeetCode-style)
# Statement: Given one order amount, print "Discount" when it reaches 10000;
# otherwise print "No discount".
# Formal Input: 8000.
# Output: "No discount".
order_amount_1 = 8000

# Problem 2 (Easy, interview-style)
# Classify a customer's outstanding balance as Paid, High outstanding or Small
# outstanding. Explain why the zero case must be checked first.
outstanding_2 = 32000

# Problem 3 (Medium, real-world business)
# Classify an order as Gold (15000+), Silver (10000+) or Standard. Print the
# right category for the boundary value 15000.
order_amount_3 = 15000

# Problem 4 (Medium, LeetCode-style)
# Statement: Classify profit into Profit, Loss or Break-even.
# Formal Input: 0.
# Output: "Break-even".
profit_4 = 0

# Problem 5 (Hard, real-world business)
# The boss wants a discount review category. Gold requires order >= 15000 and
# balance >= 30000. Standard requires order >= 10000 and balance >= 30000.
# Every other case receives no review.
customer_name_5 = "Jahid Enterprise"
order_amount_5 = 13200
customer_balance_5 = 71000

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
order_amount_1 = 8000
if order_amount_1 >= 10000:
    print("Discount")
else:
    print("No discount")  # Expected: No discount
# Exactly one branch runs, so the decision is mutually exclusive.
# This numeric comparison is O(1) time and O(1) extra space.

# Problem 2 solution
outstanding_2 = 32000
if outstanding_2 == 0:
    print("Paid")
elif outstanding_2 >= 30000:
    print("High outstanding")  # Expected: High outstanding
else:
    print("Small outstanding")
# The zero rule comes first because paid is a separate business meaning.
# Interview talking point: explicit zero handling prevents ambiguous reports.

# Problem 3 solution
order_amount_3 = 15000
if order_amount_3 >= 15000:
    print("Gold")  # Expected: Gold
elif order_amount_3 >= 10000:
    print("Silver")
else:
    print("Standard")
# The larger threshold must come first; otherwise 15000 would match Silver.

# Problem 4 solution
profit_4 = 0
if profit_4 > 0:
    print("Profit")
elif profit_4 < 0:
    print("Loss")
else:
    print("Break-even")  # Expected: Break-even
# The three comparisons are constant-time and mutually exclusive.

# Problem 5 solution
customer_name_5 = "Jahid Enterprise"
order_amount_5 = 13200
customer_balance_5 = 71000

if order_amount_5 >= 15000 and customer_balance_5 >= 30000:
    decision_5 = "Gold discount review"
elif order_amount_5 >= 10000 and customer_balance_5 >= 30000:
    decision_5 = "Standard discount review"
else:
    decision_5 = "No discount review"

print(f"{customer_name_5}: {decision_5}")
# Expected: Jahid Enterprise: Standard discount review
# Each branch uses a constant number of comparisons, so the workflow is O(1)
# in time and O(1) in extra space.
# Interview talking point: order branches from most specific to least specific.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
