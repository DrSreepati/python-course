"""Subtopic 6.2: for loop and range().
Notes: notes/c1-ch06-6.2-for-range-bangla.md
       notes/c1-ch06-6.2-for-range-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: use an inclusive-looking end by passing one larger stop value.
# Problem 2: use a step of two.
# Problem 3: keep the accumulator before the loop.
# Problem 4: use a negative step.
# Problem 5: use separate fixed-count reports and one running total.

# Problem 1 (Easy, LeetCode-style)
# Print invoice numbers from 1 through 7.
# Formal Input: first = 1, last = 7.
# Output: 1, 2, 3, 4, 5, 6, 7.
first_1 = 1
last_1 = 7

# Problem 2 (Easy, interview-style)
# Print even review months from 2 through 12.
# Follow-up: why is the stop value 14?
first_month_2 = 2
last_month_2 = 12

# Problem 3 (Medium, real-world business)
# Add daily sales for days 1 through 5.
# Each day's value is day number multiplied by 1000.
total_sales_3 = 0

# Problem 4 (Medium, interview-style)
# Print priority levels from 5 down to 1.
# Follow-up: what happens if the step is positive?
highest_priority_4 = 5

# Problem 5 (Hard, real-world business)
# Produce a fixed business summary: print five report days, calculate their
# sales total, then print three review months in steps of two.
report_days_5 = 5
sales_total_5 = 0
first_review_month_5 = 2
last_review_month_5 = 6

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Start at the first invoice.
# 2. Use last plus one as the stop boundary.
# 3. Let for receive every invoice number.
for invoice in range(first_1, last_1 + 1):
    print(invoice)
# Expected:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# Complexity: work grows with the invoice count, O(n).

# Problem 2 solution
# Approach:
# 1. Start at month 2.
# 2. Move by two months.
# 3. Stop after month 12.
for month in range(first_month_2, last_month_2 + 1, 2):
    print(month)
# Expected:
# 2
# 4
# 6
# 8
# 10
# 12
# Complexity: half as many passes as months, still O(n).
# Interview talking point: the stop must be 13 or greater to include 12.

# Problem 3 solution
# Approach:
# 1. Start the total at zero.
# 2. Calculate each daily sale.
# 3. Add it to the total.
for day in range(1, 6):
    daily_sale = day * 1000
    total_sales_3 += daily_sale
print(total_sales_3)
# Expected: 15000
# Complexity: one pass per day, O(n).

# Problem 4 solution
# Approach:
# 1. Start at the highest priority.
# 2. Stop before zero.
# 3. Decrease by one.
for priority in range(highest_priority_4, 0, -1):
    print(priority)
# Expected:
# 5
# 4
# 3
# 2
# 1
# Complexity: one pass per priority level, O(n).
# Interview talking point: a positive step would move away from the stop.

# Problem 5 solution
# Approach:
# 1. Print each report day.
# 2. Add day times 1000 to the total.
# 3. Print review months using a step of two.
for day in range(1, report_days_5 + 1):
    print(f"Report day {day}")
    sales_total_5 += day * 1000
print(f"Sales total: {sales_total_5}")
for month in range(first_review_month_5, last_review_month_5 + 1, 2):
    print(f"Review month {month}")
# Expected:
# Report day 1
# Report day 2
# Report day 3
# Report day 4
# Report day 5
# Sales total: 15000
# Review month 2
# Review month 4
# Review month 6
# Complexity: each fixed range adds linear work, O(n).
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
