"""Subtopic 7.1: List creation, indexing and slicing.
Notes: notes/c1-ch07-7.1-list-basics-bangla.md
       notes/c1-ch07-7.1-list-basics-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: use an index to read the requested day.
# Problem 2: use one slice for the first section and one for the final section.
# Problem 3: use negative indexes and a step to select positions from the end.
# Problem 4: keep names and balances in matching positions.
# Problem 5: build each report section from the fixed business lists.

# Problem 1 (Easy, LeetCode-style)
# Given daily sales, return the sale for the requested zero-based day index.
# Formal Input: sales list and day_index.
# Output: the value at that index.
# Example: [12000, 9500, 8800], 1 -> 9500.
# Constraints: day_index is valid.
sales_1 = [12000, 9500, 8800, 13200, 7500]
day_index_1 = 3

# Problem 2 (Easy, interview-style)
# The boss wants an opening report containing the first three days and
# the last two days. Use slices, not a loop.
# Follow-up: why is the stop value four for the first four days?
sales_2 = [12000, 9500, 8800, 13200, 7500]

# Problem 3 (Medium, real-world business)
# Rahim wants a reverse review of the final three daily sales and an
# every-second-day sample from the full report.
# Follow-up: which negative index identifies the final item?
sales_3 = [12000, 9500, 8800, 13200, 7500]

# Problem 4 (Medium, interview-style)
# Match each customer with its balance using the same index positions.
# Then print the first two customer names as a morning call list.
# Follow-up: what mistake occurs if the two lists have different lengths?
customers_4 = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
balances_4 = [50000, 32000, 71000]

# Problem 5 (Hard, real-world business)
# Build a fixed management report with the daily sales, first three days,
# final two days, best-day candidate at index 3, and reversed review.
# Use only list creation, indexes, and slicing.
sales_5 = [12000, 9500, 8800, 13200, 7500]
customers_5 = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
balances_5 = [50000, 32000, 71000]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Keep the report in a list.
# 2. Use the supplied zero-based index.
# 3. Print the selected sale.
selected_sale_1 = sales_1[day_index_1]
print(selected_sale_1)
# Expected: 13200
# The index selects one seat in the list.
# Complexity: direct index access is constant work, O(1).

# Problem 2 solution
# Approach:
# 1. Slice the first four positions.
# 2. Slice the final two positions.
# 3. Print both report sections.
opening_days_2 = sales_2[:4]
closing_days_2 = sales_2[-2:]
print(opening_days_2)
print(closing_days_2)
# Expected:
# [12000, 9500, 8800, 13200]
# [13200, 7500]
# `:4` stops before index 4. `-2:` starts two seats from the end.
# Complexity: each slice copies its selected section, O(n) in the section size.
# Interview talking point: explain that slice stops are exclusive.

# Problem 3 solution
# Approach:
# 1. Take the final three items.
# 2. Reverse that selected slice.
# 3. Take every second item from the full report.
final_three_3 = sales_3[-3:]
reverse_final_three_3 = final_three_3[::-1]
alternate_3 = sales_3[::2]
print(reverse_final_three_3)
print(alternate_3)
# Expected:
# [7500, 13200, 8800]
# [12000, 8800, 7500]
# Negative slicing selects the tail. A step of -1 reverses it.
# Complexity: the selected slices require linear work, O(n).
# Interview talking point: say which operation creates each new list.

# Problem 4 solution
# Approach:
# 1. Read each matching position directly.
# 2. Print the customer and balance together.
# 3. Slice the first two names for the call list.
print(customers_4[0], balances_4[0])
print(customers_4[1], balances_4[1])
print(customers_4[2], balances_4[2])
morning_call_list_4 = customers_4[:2]
print(morning_call_list_4)
# Expected:
# Rahim Traders 50000
# Karim Store 32000
# Jahid Enterprise 71000
# ['Rahim Traders', 'Karim Store']
# Matching indexes preserve the relationship between names and balances.
# Complexity: the fixed accesses are O(1), while the slice is O(k).
# Interview talking point: state that parallel lists must stay aligned.

# Problem 5 solution
# Approach:
# 1. Print the complete sales report.
# 2. Select the first and final report sections.
# 3. Read the day-four candidate directly.
# 4. Print the reversed review and aligned customer balances.
print(f"Sales report: {sales_5}")
print(f"First three: {sales_5[:3]}")
print(f"Final two: {sales_5[-2:]}")
print(f"Day four candidate: {sales_5[3]}")
print(f"Reversed review: {sales_5[::-1]}")
print(f"Customer 1: {customers_5[0]}, balance {balances_5[0]}")
print(f"Customer 2: {customers_5[1]}, balance {balances_5[1]}")
print(f"Customer 3: {customers_5[2]}, balance {balances_5[2]}")
# Expected:
# Sales report: [12000, 9500, 8800, 13200, 7500]
# First three: [12000, 9500, 8800]
# Final two: [13200, 7500]
# Day four candidate: 13200
# Reversed review: [7500, 13200, 8800, 9500, 12000]
# Customer 1: Rahim Traders, balance 50000
# Customer 2: Karim Store, balance 32000
# Customer 3: Jahid Enterprise, balance 71000
# Direct indexes and slices keep this report within today’s topic.
# Complexity: the report copies selected list sections, O(n).
# Business talking point: explain why the day-four value uses index 3.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
