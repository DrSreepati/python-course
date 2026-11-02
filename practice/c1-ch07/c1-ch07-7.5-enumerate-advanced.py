"""Subtopic 7.5: Loops and enumerate on lists.
Notes: notes/c1-ch07-7.5-enumerate-bangla.md
       notes/c1-ch07-7.5-enumerate-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: unpack index and value from enumerate.
# Problem 2: use start=1 for customer-facing labels.
# Problem 3: use the zero-based index to read the matching balance.
# Problem 4: enumerate each nested row with a row number.
# Problem 5: combine indexed daily, customer, and invoice reports.

# Problem 1 (Easy, LeetCode-style)
# Given sales, return labelled strings such as "Day 1: 12000".
# Formal Input: a list of integer sales.
# Output: one printed label per sale.
# Example: [10, 20] -> Day 1: 10, Day 2: 20.
sales_1 = [12000, 9500, 8800, 13200, 7500]

# Problem 2 (Easy, real-world business)
# The boss wants an indexed invoice review list starting at one.
references_2 = ["INV-2024-007", "INV-2024-008", "INV-2024-009"]

# Problem 3 (Medium, interview-style)
# Match customer names with balances using enumerate and parallel lists.
# Follow-up: why should the balance lookup use the zero-based index?
customers_3 = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
balances_3 = [50000, 32000, 71000]

# Problem 4 (Medium, real-world business)
# A table has one row per customer. Print row number, customer name,
# and each sale in that row.
customer_names_4 = ["Rahim Traders", "Karim Store"]
sales_table_4 = [[12000, 9500, 8800], [13200, 7500, 11000]]

# Problem 5 (Hard, real-world business)
# Build an indexed management report for daily sales, invoice reviews,
# and customer balances. Use business labels starting from one.
daily_sales_5 = [12000, 9500, 8800, 13200, 7500]
references_5 = ["INV-2024-007", "INV-2024-008", "INV-2024-009"]
customers_5 = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
balances_5 = [50000, 32000, 71000]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Enumerate the sales with a one-based label.
# 2. Pair each day with its value.
# 3. Print the labelled report.
for day_1, sale_1 in enumerate(sales_1, start=1):
    print(f"Day {day_1}: {sale_1}")
# Expected:
# Day 1: 12000
# Day 2: 9500
# Day 3: 8800
# Day 4: 13200
# Day 5: 7500
# One pass reads each sale, so this is O(n).

# Problem 2 solution
# Approach:
# 1. Start review labels at one.
# 2. Keep the invoice reference unchanged.
# 3. Print each audit line.
for review_number_2, reference_2 in enumerate(references_2, start=1):
    print(f"Review {review_number_2}: {reference_2}")
# Expected:
# Review 1: INV-2024-007
# Review 2: INV-2024-008
# Review 3: INV-2024-009
# The loop makes a clear customer-facing sequence, O(n).
# Business talking point: report labels are one-based, internal indexes are zero-based.

# Problem 3 solution
# Approach:
# 1. Enumerate customer names.
# 2. Use the zero-based index for the aligned balance.
# 3. Print the one-based customer number.
for index_3, customer_3 in enumerate(customers_3):
    balance_3 = balances_3[index_3]
    print(f"Customer {index_3 + 1}: {customer_3}, balance {balance_3}")
# Expected:
# Customer 1: Rahim Traders, balance 50000
# Customer 2: Karim Store, balance 32000
# Customer 3: Jahid Enterprise, balance 71000
# Enumeration is O(n), and each aligned lookup is O(1).
# Interview talking point: use the technical index for data access.

# Problem 4 solution
# Approach:
# 1. Enumerate customer names with one-based row labels.
# 2. Read the matching row by zero-based index.
# 3. Enumerate each sale in that row with a one-based day label.
for row_index_4, customer_4 in enumerate(customer_names_4):
    row_4 = sales_table_4[row_index_4]
    print(f"Customer {row_index_4 + 1}: {customer_4}")
    for day_4, sale_4 in enumerate(row_4, start=1):
        print(f"Day {day_4}: {sale_4}")
# Expected:
# Customer 1: Rahim Traders
# Day 1: 12000
# Day 2: 9500
# Day 3: 8800
# Customer 2: Karim Store
# Day 1: 13200
# Day 2: 7500
# Day 3: 11000
# Every cell is read once, O(n * m).
# Business talking point: row labels and day labels are separate counters.

# Problem 5 solution
# Approach:
# 1. Print daily sales with day numbers.
# 2. Print invoice references with review numbers.
# 3. Print customer balances using aligned indexes.
for day_5, sale_5 in enumerate(daily_sales_5, start=1):
    print(f"Day {day_5} sale: {sale_5}")
for review_5, reference_5 in enumerate(references_5, start=1):
    print(f"Review {review_5}: {reference_5}")
for customer_index_5, customer_5 in enumerate(customers_5):
    print(f"Customer {customer_index_5 + 1}: {customer_5}, balance {balances_5[customer_index_5]}")
# Expected:
# Day 1 sale: 12000
# Day 2 sale: 9500
# Day 3 sale: 8800
# Day 4 sale: 13200
# Day 5 sale: 7500
# Review 1: INV-2024-007
# Review 2: INV-2024-008
# Review 3: INV-2024-009
# Customer 1: Rahim Traders, balance 50000
# Customer 2: Karim Store, balance 32000
# Customer 3: Jahid Enterprise, balance 71000
# Each report scans its own list once. Total work is O(n + r + c).
# Business talking point: use one-based labels for people and zero-based indexes for storage.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
