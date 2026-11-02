"""Subtopic 7.4: Nested lists, tables and matrices.
Notes: notes/c1-ch07-7.4-nested-lists-bangla.md
       notes/c1-ch07-7.4-nested-lists-english.md
"""

# Program 1: access rows and cells.
sales_table = [[12000, 9500, 8800], [13200, 7500, 11000]]
print(sales_table[0])  # Expected: [12000, 9500, 8800]
print(sales_table[1][2])  # Expected: 11000

# Program 2: calculate row totals.
for row in sales_table:
    print(sum(row))  # Expected: 30300, then 31700

# Program 3: calculate a grand total.
grand_total = 0
for row in sales_table:
    for sale in row:
        grand_total += sale
print(grand_total)  # Expected: 62000

# Program 4: a balance table.
customer_balances = [[50000, 12000], [32000, 8000], [71000, 15000]]
for balance_row in customer_balances:
    print(f"Opening: {balance_row[0]}, Payment: {balance_row[1]}")

# Task 1: Create a two-row sales table and print the first row.
# Task 2: Print the second row's second cell.
# Task 3: Calculate each row total.
# Task 4: Calculate the table grand total.
# Task 5: Fix Rafiq bhai's grand-total reset bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
table = [[12000, 9500], [8800, 13200]]
print(table[0])

# Task 2
print(table[1][1])

# Task 3
for row in table:
    print(sum(row))

# Task 4
grand_total = 0
for row in table:
    for value in row:
        grand_total += value
print(grand_total)

# Task 5
grand_total = 0
for row in table:
    for value in row:
        grand_total += value
print(grand_total)
"""
# Change the values and rerun. Tables become clearer through practice.
