"""Subtopic 7.4: Nested lists, tables and matrices.
Notes: notes/c1-ch07-7.4-nested-lists-bangla.md
       notes/c1-ch07-7.4-nested-lists-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: use two indexes, row first and column second.
# Problem 2: use sum on each row.
# Problem 3: keep the grand total outside the outer loop.
# Problem 4: add matching positions across rows.
# Problem 5: produce row totals, column totals, and the grand total.

# Problem 1 (Easy, LeetCode-style)
# Given a table and a valid row and column, return one cell.
# Formal Input: a nested list, row_index, and column_index.
# Output: the selected numeric cell.
# Example: [[10, 20], [30, 40]], 1, 0 -> 30.
table_1 = [[12000, 9500], [8800, 13200]]
row_index_1 = 1
column_index_1 = 0

# Problem 2 (Easy, interview-style)
# Print every customer row total from a two-dimensional sales table.
# Follow-up: why can sum(row) replace the inner loop for row totals?
customer_sales_2 = [[12000, 9500], [8800, 13200], [5000, 6100]]

# Problem 3 (Medium, real-world business)
# The boss wants the grand total across all customer and day cells.
# Follow-up: where must the accumulator be initialised?
customer_sales_3 = [[12000, 9500], [8800, 13200], [5000, 6100]]

# Problem 4 (Medium, interview-style)
# Calculate day-one and day-two totals across customer rows.
# Follow-up: what does each index mean in table[row][column]?
customer_sales_4 = [[12000, 9500], [8800, 13200], [5000, 6100]]

# Problem 5 (Hard, real-world business)
# Build a complete management matrix report. Print each customer total,
# each day total, and the grand total.
customer_sales_5 = [
    [12000, 9500, 8800],
    [13200, 7500, 11000],
    [5000, 4200, 6100],
]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Read the selected row.
# 2. Read the selected column from that row.
# 3. Print the cell.
selected_cell_1 = table_1[row_index_1][column_index_1]
print(selected_cell_1)
# Expected: 8800
# The first index selects the row. The second selects its cell.
# Complexity: direct nested indexing is constant work, O(1).

# Problem 2 solution
# Approach:
# 1. Visit each customer row.
# 2. Add the row values.
# 3. Print each customer total.
for row in customer_sales_2:
    print(sum(row))
# Expected:
# 21500
# 22000
# 11100
# `sum(row)` reads every cell in one row.
# Complexity: all cells are read once, O(n * m) for n rows and m columns.
# Interview talking point: sum is clear when no extra cell-level logic is needed.

# Problem 3 solution
# Approach:
# 1. Start one accumulator before the rows.
# 2. Visit every row and every sale.
# 3. Add each sale to the grand total.
grand_total_3 = 0
for row in customer_sales_3:
    for sale in row:
        grand_total_3 += sale
print(grand_total_3)
# Expected: 54600
# The accumulator is outside the outer loop, so earlier rows remain included.
# Complexity: every cell is visited once, O(n * m).
# Business talking point: this is the total for all customers and days.

# Problem 4 solution
# Approach:
# 1. Add column zero from every row.
# 2. Add column one from every row.
# 3. Print both day totals.
day_one_4 = customer_sales_4[0][0] + customer_sales_4[1][0] + customer_sales_4[2][0]
day_two_4 = customer_sales_4[0][1] + customer_sales_4[1][1] + customer_sales_4[2][1]
print(day_one_4)
print(day_two_4)
# Expected:
# 25800
# 28800
# The first index changes rows. The second stays on the chosen column.
# Complexity: fixed three-row access is O(1); for a general table it is O(n).
# Interview talking point: explain row first, column second.

# Problem 5 solution
# Approach:
# 1. Print each row total.
# 2. Add each column across all rows.
# 3. Add every cell for the grand total.
grand_total_5 = 0
for row in customer_sales_5:
    row_total_5 = sum(row)
    print(f"Customer total: {row_total_5}")
    for sale in row:
        grand_total_5 += sale

day_totals_5 = []
for column_index_5 in range(3):
    column_total_5 = 0
    for row in customer_sales_5:
        column_total_5 += row[column_index_5]
    day_totals_5.append(column_total_5)

print(f"Day totals: {day_totals_5}")
print(f"Grand total: {grand_total_5}")
# Expected:
# Customer total: 30300
# Customer total: 31700
# Customer total: 15300
# Day totals: [30200, 21200, 25900]
# Grand total: 77300
# Row totals and column totals inspect the same matrix from different directions.
# Complexity: each cell is read a small constant number of times, O(n * m).
# Business talking point: explain why both views help management.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
