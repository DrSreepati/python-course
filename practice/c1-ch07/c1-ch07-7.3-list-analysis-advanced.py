"""Subtopic 7.3: List analysis.
Notes: notes/c1-ch07-7.3-list-analysis-bangla.md
       notes/c1-ch07-7.3-list-analysis-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: use sorted with reverse=True.
# Problem 2: calculate total, count, average, minimum, and maximum.
# Problem 3: sort a copy before identifying collection priority.
# Problem 4: preserve the original list while making two report views.
# Problem 5: calculate each measure from the correct list.

# Problem 1 (Easy, LeetCode-style)
# Given sales, return them in descending order without changing the input.
# Formal Input: a list of integers.
# Output: a new descending list.
# Example: [3, 1, 2] -> [3, 2, 1].
sales_1 = [12000, 9500, 8800, 13200, 7500]

# Problem 2 (Easy, interview-style)
# Build a sales summary with total, number of days, average, best, and
# slowest values. Follow-up: why is len needed for average?
sales_2 = [12000, 9500, 8800, 13200, 7500]

# Problem 3 (Medium, real-world business)
# Rank customer balances from largest to smallest. Print the largest
# balance and the average balance.
balances_3 = [50000, 32000, 71000]

# Problem 4 (Medium, interview-style)
# Produce ascending and descending report views while preserving the
# original daily sales list. Follow-up: when would sorted be safer than sort?
sales_4 = [12000, 9500, 8800, 13200, 7500]

# Problem 5 (Hard, real-world business)
# Build the boss's weekly and daily management summary. Include totals,
# counts, averages, minimums, maximums, and descending views.
daily_sales_5 = [12000, 9500, 8800, 13200, 7500]
weekly_takings_5 = [5000, 4200, 6100, 3800, 5500, 4700, 5700]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Keep the input list unchanged.
# 2. Ask sorted for descending order.
# 3. Print the new report view.
descending_1 = sorted(sales_1, reverse=True)
print(descending_1)
print(sales_1)
# Expected:
# [13200, 12000, 9500, 8800, 7500]
# [12000, 9500, 8800, 13200, 7500]
# Complexity: sorting grows as O(n log n).

# Problem 2 solution
# Approach:
# 1. Calculate the total and count.
# 2. Divide total by count.
# 3. Add best and slowest values.
total_2 = sum(sales_2)
count_2 = len(sales_2)
print(f"Total: {total_2}")
print(f"Days: {count_2}")
print(f"Average: {total_2 / count_2}")
print(f"Best: {max(sales_2)}")
print(f"Slowest: {min(sales_2)}")
# Expected:
# Total: 51000
# Days: 5
# Average: 10200.0
# Best: 13200
# Slowest: 7500
# Each summary scan is linear, O(n).
# Interview talking point: length is the denominator for a mean.

# Problem 3 solution
# Approach:
# 1. Make a descending balance copy.
# 2. Read the first value as the largest.
# 3. Calculate the average from total and count.
ranked_balances_3 = sorted(balances_3, reverse=True)
average_balance_3 = sum(balances_3) / len(balances_3)
print(ranked_balances_3)
print(f"Largest: {ranked_balances_3[0]}")
print(f"Average: {average_balance_3}")
# Expected:
# [71000, 50000, 32000]
# Largest: 71000
# Average: 51000.0
# Sorting is O(n log n); summary calculations are O(n).
# Business talking point: ranking identifies collection priority.

# Problem 4 solution
# Approach:
# 1. Create ascending and descending copies.
# 2. Print both views.
# 3. Print the original list to prove it is unchanged.
ascending_4 = sorted(sales_4)
descending_4 = sorted(sales_4, reverse=True)
print(ascending_4)
print(descending_4)
print(sales_4)
# Expected:
# [7500, 8800, 9500, 12000, 13200]
# [13200, 12000, 9500, 8800, 7500]
# [12000, 9500, 8800, 13200, 7500]
# Interview talking point: sorted is safer when the input is also needed.
# Complexity: two sorts are still O(n log n).

# Problem 5 solution
# Approach:
# 1. Summarise daily sales.
# 2. Summarise weekly takings.
# 3. Print descending views for both.
print(f"Daily total: {sum(daily_sales_5)}")
print(f"Daily count: {len(daily_sales_5)}")
print(f"Daily average: {sum(daily_sales_5) / len(daily_sales_5)}")
print(f"Daily minimum: {min(daily_sales_5)}")
print(f"Daily maximum: {max(daily_sales_5)}")
print(f"Daily descending: {sorted(daily_sales_5, reverse=True)}")
print(f"Weekly total: {sum(weekly_takings_5)}")
print(f"Weekly count: {len(weekly_takings_5)}")
print(f"Weekly average: {sum(weekly_takings_5) / len(weekly_takings_5)}")
print(f"Weekly minimum: {min(weekly_takings_5)}")
print(f"Weekly maximum: {max(weekly_takings_5)}")
print(f"Weekly descending: {sorted(weekly_takings_5, reverse=True)}")
# Expected:
# Daily total: 51000
# Daily count: 5
# Daily average: 10200.0
# Daily minimum: 7500
# Daily maximum: 13200
# Daily descending: [13200, 12000, 9500, 8800, 7500]
# Weekly total: 35000
# Weekly count: 7
# Weekly average: 5000.0
# Weekly minimum: 3800
# Weekly maximum: 6100
# Weekly descending: [6100, 5700, 5500, 5000, 4700, 4200, 3800]
# The report uses constant-time access for each measure after linear scans.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
