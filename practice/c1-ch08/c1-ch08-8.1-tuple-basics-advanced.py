"""Subtopic 8.1: Tuple, creation, indexing, slicing, immutability.
Notes: notes/c1-ch08-8.1-tuple-basics-bangla.md
       notes/c1-ch08-8.1-tuple-basics-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Use indexes to read the fixed invoice fields.
# Problem 2: Slice the tuple before building the approved snapshot.
# Problem 3: Use a new tuple instead of item assignment.
# Problem 4: Keep each customer's fixed pair inside a tuple.
# Problem 5: Build a complete immutable management snapshot.

# Problem 1 (Easy, LeetCode-style)
# Given one invoice tuple, return a tuple containing its invoice number
# and amount. Input: (reference, customer, amount). Output: (reference, amount).
invoice_1 = ("INV-2024-007", "Rahim Traders", 50000)

# Problem 2 (Easy, real-world business)
# The boss wants the first three approved entries from a weekly summary.
weekly_summary_2 = ("Mon", 5000, "Tue", 4200, "Wed", 6100, "Thu", 3800)

# Problem 3 (Medium, interview-style)
# Replace the amount in an immutable invoice tuple without changing the
# original. Follow-up: why is a new tuple safer for an approved record?
approved_invoice_3 = ("INV-2024-007", "Rahim Traders", 50000)

# Problem 4 (Medium, real-world business)
# Store each customer's name and balance as a tuple. Print a fixed audit
# line for every customer using the existing loop and tuple skills.
customer_records_4 = (
    ("Rahim Traders", 50000),
    ("Karim Store", 32000),
    ("Jahid Enterprise", 71000),
)

# Problem 5 (Hard, real-world business)
# Build an immutable five-day management snapshot. Report the total,
# best day, and the first two days without changing the snapshot.
management_sales_5 = (12000, 9500, 8800, 13200, 7500)

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Read the invoice reference at index 0.
# 2. Read the amount at index 2.
# 3. Build the requested two-item tuple.
short_invoice_1 = (invoice_1[0], invoice_1[2])
print(short_invoice_1)
# Expected: ('INV-2024-007', 50000)
# Key lines: indexes select fixed fields without changing the source.
# Complexity: each lookup is constant work, O(1).

# Problem 2 solution
# Approach:
# 1. Use a stop boundary of three.
# 2. Keep the start at zero.
# 3. Print the new tuple slice.
approved_entries_2 = weekly_summary_2[:3]
print(approved_entries_2)
# Expected: ('Mon', 5000, 'Tue')
# Key line: the stop boundary is excluded.
# Complexity: the slice copies three references, O(k).

# Problem 3 solution
# Approach:
# 1. Read the unchanged reference and customer.
# 2. Put the corrected amount in a new tuple.
# 3. Print both records.
corrected_invoice_3 = (
    approved_invoice_3[0],
    approved_invoice_3[1],
    55000,
)
print(approved_invoice_3)
print(corrected_invoice_3)
# Expected:
# ('INV-2024-007', 'Rahim Traders', 50000)
# ('INV-2024-007', 'Rahim Traders', 55000)
# Key line: immutable data is replaced by a new tuple.
# Complexity: the fixed three-field record takes O(1) work.
# Interview talking point: retaining the old record supports audit comparison.

# Problem 4 solution
# Approach:
# 1. Read each two-item customer tuple.
# 2. Select the name and balance by index.
# 3. Print a fixed audit line.
for number_4, record_4 in enumerate(customer_records_4, start=1):
    print(f"Customer {number_4}: {record_4[0]}, balance {record_4[1]}")
# Expected:
# Customer 1: Rahim Traders, balance 50000
# Customer 2: Karim Store, balance 32000
# Customer 3: Jahid Enterprise, balance 71000
# Key line: each record stays fixed while the report reads it.
# Complexity: each record is read once, O(n).

# Problem 5 solution
# Approach:
# 1. Sum the immutable snapshot.
# 2. Find its largest value.
# 3. Take the first two values by slicing.
# 4. Print the management measures.
total_5 = sum(management_sales_5)
best_5 = max(management_sales_5)
opening_days_5 = management_sales_5[:2]
print(total_5)
print(best_5)
print(opening_days_5)
# Expected:
# 51000
# 13200
# (12000, 9500)
# Key lines: all operations read the tuple without mutating it.
# Complexity: sum and max scan the five values, O(n).
# Business talking point: an immutable snapshot keeps the reported source stable.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
