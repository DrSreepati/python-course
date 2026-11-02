"""Subtopic 7.3: List analysis.
Notes: notes/c1-ch07-7.3-list-analysis-bangla.md
       notes/c1-ch07-7.3-list-analysis-english.md
"""

# Program 1: sort, reverse, and sorted.
sales = [12000, 9500, 8800, 13200, 7500]
ordered_sales = sorted(sales)
print(ordered_sales)  # Expected: [7500, 8800, 9500, 12000, 13200]
print(sorted(sales, reverse=True))  # Expected: [13200, 12000, 9500, 8800, 7500]
print(sales)  # Expected: original order

# Program 2: basic summary.
print(min(sales))  # Expected: 7500
print(max(sales))  # Expected: 13200
print(sum(sales))  # Expected: 51000
print(len(sales))  # Expected: 5

# Program 3: business report.
average = sum(sales) / len(sales)
print(f"Total: {sum(sales)}")  # Expected: Total: 51000
print(f"Average: {average}")  # Expected: Average: 10200.0
print(f"Best: {max(sales)}")  # Expected: Best: 13200
print(f"Slowest: {min(sales)}")  # Expected: Slowest: 7500

# Task 1: Sort sales in ascending order.
# Task 2: Sort sales in descending order without changing the original.
# Task 3: Find weekly total, count, and average.
# Task 4: Find lowest and highest customer balances.
# Task 5: Fix Rafiq bhai's sort return-value bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
print(sorted([12000, 9500, 8800, 13200, 7500]))

# Task 2
sales = [12000, 9500, 8800, 13200, 7500]
print(sorted(sales, reverse=True))
print(sales)

# Task 3
week = [5000, 4200, 6100, 3800, 5500, 4700, 5700]
print(sum(week))
print(len(week))
print(sum(week) / len(week))

# Task 4
balances = [50000, 32000, 71000]
print(min(balances))
print(max(balances))

# Task 5
sales = [12000, 9500, 8800, 13200, 7500]
sorted_sales = sorted(sales)
print(sorted_sales)
"""
# Change the values and rerun. Useful reports begin with careful summaries.
