"""
Course 1, Chapter 8, Subtopic 8.4: Set operations
Notes: c1-ch08-8.4-set-operations-bangla.md and
       c1-ch08-8.4-set-operations-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Use intersection, then sort the result.
# Problem 2: Use difference in the correct direction.
# Problem 3: Use union and intersection to build a small report.
# Problem 4: Compare the two branch sets in both directions.
# Problem 5: Symmetric difference gives the complete exception list.

# Problem 1 (Easy, LeetCode style)
# Given two invoice-ID sets, return the sorted IDs found in both sets.
# Input:
p1_sales = {"INV-101", "INV-102", "INV-103", "INV-104"}
p1_payments = {"INV-102", "INV-104", "INV-105"}
# Output: ['INV-102', 'INV-104']

# Problem 2 (Easy, business task)
# The boss wants sales invoices with no corresponding payment record.
# Input:
p2_sales = {"INV-201", "INV-202", "INV-203", "INV-204"}
p2_payments = {"INV-202", "INV-204"}
# Output: ['INV-201', 'INV-203']

# Problem 3 (Medium, interview style)
# Compare two branch customer registers. Return a report with all customers,
# shared customers, and customers unique to branch A.
# Follow-up: How would you keep the original registers unchanged?
p3_a = {"C-101", "C-102", "C-103", "C-105"}
p3_b = {"C-102", "C-104", "C-105"}

# Problem 4 (Medium, real business problem)
# Sales and payment systems contain invoice references. Prepare four lists:
# matched, sales-only, payment-only, and every exception.
p4_sales = {"INV-301", "INV-302", "INV-303", "INV-305"}
p4_payments = {"INV-302", "INV-304", "INV-305"}

# Problem 5 (Hard, real business problem)
# A weekly audit compares three registers. Find:
# 1. invoices present in every register,
# 2. invoices present in sales but absent from both other registers,
# 3. every invoice appearing in only one register.
p5_sales = {"INV-401", "INV-402", "INV-403", "INV-406"}
p5_collection = {"INV-402", "INV-403", "INV-404"}
p5_ledger = {"INV-402", "INV-405", "INV-406"}

# ===== SOLUTIONS (attempt first, then compare) =====

# Problem 1 solution
# Approach:
# 1. Treat both inputs as sets.
# 2. Use intersection for shared IDs.
# 3. Sort for stable report output.
p1_answer = sorted(p1_sales & p1_payments)
print("Problem 1:", p1_answer)
# Expected: Problem 1: ['INV-102', 'INV-104']
# Key line: & keeps only IDs in both sets.
# Complexity: set intersection scans the inputs, O(n + m).

# Problem 2 solution
# Approach:
# 1. Start with sales IDs.
# 2. Remove payment IDs with difference.
# 3. Sort the candidates for the boss.
p2_answer = sorted(p2_sales - p2_payments)
print("Problem 2:", p2_answer)
# Expected: Problem 2: ['INV-201', 'INV-203']
# Key line: sales - payments means sales-only IDs.
# Complexity: difference is O(n + m) on average.

# Problem 3 solution
# Approach:
# 1. Use union for every customer in either branch.
# 2. Use intersection for shared customers.
# 3. Use difference for branch-A-only customers.
p3_report = {
    "all": sorted(p3_a | p3_b),
    "shared": sorted(p3_a & p3_b),
    "branch_a_only": sorted(p3_a - p3_b),
}
print("Problem 3:", p3_report)
# Expected: Problem 3: {'all': ['C-101', 'C-102', 'C-103', 'C-104', 'C-105'],
# 'shared': ['C-102', 'C-105'], 'branch_a_only': ['C-101', 'C-103']}
# Key lines: each operation answers one business question.
# Complexity: the three comparisons together are O(n + m).
# Interview talking point: the source sets are not modified; each operation
# returns a new set, and sorting is only for presentation.

# Problem 4 solution
# Approach:
# 1. Find the intersection for matched invoices.
# 2. Find each directional difference.
# 3. Use symmetric difference for all exceptions.
p4_report = {
    "matched": sorted(p4_sales & p4_payments),
    "sales_only": sorted(p4_sales - p4_payments),
    "payment_only": sorted(p4_payments - p4_sales),
    "exceptions": sorted(p4_sales ^ p4_payments),
}
print("Problem 4:", p4_report)
# Expected: Problem 4: {'matched': ['INV-302', 'INV-305'],
# 'sales_only': ['INV-301', 'INV-303'],
# 'payment_only': ['INV-304'],
# 'exceptions': ['INV-301', 'INV-303', 'INV-304']}
# Key lines: difference direction identifies which register owns an exception.
# Complexity: four set operations are O(n + m) overall.

# Problem 5 solution
# Approach:
# 1. Intersect sales and collection.
# 2. Intersect that result with ledger for all-three matches.
# 3. Subtract both other registers from sales for sales-only records.
# 4. Count membership across the three registers with set operations.
all_three = p5_sales & p5_collection & p5_ledger
sales_only = p5_sales - p5_collection - p5_ledger
one_register = (
    (p5_sales ^ p5_collection ^ p5_ledger)
    - (p5_sales & p5_collection)
    - (p5_sales & p5_ledger)
    - (p5_collection & p5_ledger)
)
print("Problem 5 all three:", sorted(all_three))
print("Problem 5 sales only:", sorted(sales_only))
print("Problem 5 one register:", sorted(one_register))
# Expected:
# Problem 5 all three: ['INV-402']
# Problem 5 sales only: ['INV-401']
# Problem 5 one register: ['INV-401', 'INV-404', 'INV-405']
# Key lines: intersections identify repeated membership; differences remove
# records seen in another register.
# Complexity: fixed numbers of set operations, O(n + m + k).
# Interview talking point: for a large audit, I would define and test the
# membership rule clearly before presenting exceptions.

# Change the data and rerun. Real skill grows in the variations, not the copies.
