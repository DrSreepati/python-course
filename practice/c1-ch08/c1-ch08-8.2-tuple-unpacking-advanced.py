"""Subtopic 8.2: Tuple unpacking, tuple versus list.
Notes: notes/c1-ch08-8.2-tuple-unpacking-bangla.md
       notes/c1-ch08-8.2-tuple-unpacking-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Unpack the three fields, then rebuild the requested tuple.
# Problem 2: Use a star target for all remaining daily values.
# Problem 3: Match every customer record with three variables.
# Problem 4: Use tuple records for fixed data and a list for new entries.
# Problem 5: Unpack each record, then build a readable management line.

# Problem 1 (Easy, LeetCode-style)
# Given an invoice tuple (reference, customer, amount), return
# (customer, amount). Input: one fixed tuple. Output: a two-item tuple.
invoice_1 = ("INV-2024-007", "Rahim Traders", 50000)

# Problem 2 (Easy, real-world business)
# The boss wants the customer name separated from all daily sales.
customer_sales_2 = ("Rahim Traders", 12000, 9500, 8800, 13200, 7500)

# Problem 3 (Medium, interview-style)
# Print each fixed customer record as a numbered audit line.
# Follow-up: why is a tuple suitable for a record whose fields should not change?
customer_records_3 = (
    ("Rahim Traders", 50000, "Review"),
    ("Karim Store", 32000, "Active"),
    ("Jahid Enterprise", 71000, "Review"),
)

# Problem 4 (Medium, real-world business)
# Keep an approved invoice status as a tuple, but add daily sales to a list.
approved_status_4 = ("INV-2024-007", "Approved")
daily_sales_4 = [12000, 9500, 8800]

# Problem 5 (Hard, real-world business)
# Build a complete management report from fixed customer records.
# Each output line must include the customer, balance, and status.
management_records_5 = (
    ("Rahim Traders", 50000, "Review"),
    ("Karim Store", 32000, "Active"),
    ("Jahid Enterprise", 71000, "Review"),
)

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Unpack the invoice fields.
# 2. Keep the customer and amount.
# 3. Return them in a new tuple.
reference_1, customer_1, amount_1 = invoice_1
short_invoice_1 = (customer_1, amount_1)
print(short_invoice_1)
# Expected: ('Rahim Traders', 50000)
# Key lines: unpacking gives meaningful names before rebuilding.
# Complexity: fixed fields require O(1) work.

# Problem 2 solution
# Approach:
# 1. Separate the customer name.
# 2. Capture every remaining amount with a star target.
# 3. Calculate the total of the resulting list.
customer_2, *sales_2 = customer_sales_2
print(customer_2)
print(sales_2)
print(sum(sales_2))
# Expected:
# Rahim Traders
# [12000, 9500, 8800, 13200, 7500]
# 48000
# Key line: star unpacking is useful when the remaining count is variable.
# Complexity: reading and summing the values is O(n).

# Problem 3 solution
# Approach:
# 1. Enumerate the fixed records.
# 2. Unpack each three-field tuple.
# 3. Print one audit line per customer.
for number_3, record_3 in enumerate(customer_records_3, start=1):
    customer_3, balance_3, status_3 = record_3
    print(f"{number_3}. {customer_3}: {balance_3}, {status_3}")
# Expected:
# 1. Rahim Traders: 50000, Review
# 2. Karim Store: 32000, Active
# 3. Jahid Enterprise: 71000, Review
# Key line: each tuple remains fixed while its fields receive names.
# Complexity: one pass through the records, O(n).
# Interview talking point: tuple fields make a fixed record contract visible.

# Problem 4 solution
# Approach:
# 1. Keep the approved status as a fixed tuple.
# 2. Append a new sale to the changing list.
# 3. Print both structures.
daily_sales_4.append(13200)
print(approved_status_4)
print(daily_sales_4)
# Expected:
# ('INV-2024-007', 'Approved')
# [12000, 9500, 8800, 13200]
# Key line: structure choice follows whether the data changes.
# Complexity: list append at the end is amortised O(1).

# Problem 5 solution
# Approach:
# 1. Read each customer tuple.
# 2. Unpack its three fields.
# 3. Build a numbered management line.
for number_5, record_5 in enumerate(management_records_5, start=1):
    customer_5, balance_5, status_5 = record_5
    print(
        f"Customer {number_5}: {customer_5}, "
        f"balance {balance_5}, status {status_5}"
    )
# Expected:
# Customer 1: Rahim Traders, balance 50000, status Review
# Customer 2: Karim Store, balance 32000, status Active
# Customer 3: Jahid Enterprise, balance 71000, status Review
# Key lines: unpacking keeps the report readable and ordered.
# Complexity: each record is read once, O(n).
# Business talking point: fixed field order is clear for an audit report.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
