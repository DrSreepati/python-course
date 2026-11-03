"""
Course 1, Chapter 8, Subtopic 8.5: Practical uses of sets
Notes: c1-ch08-8.5-practical-set-uses-bangla.md and
       c1-ch08-8.5-practical-set-uses-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Convert the invoice rows to a set.
# Problem 2: Keep a seen set and a duplicate list.
# Problem 3: Use intersection and directional differences.
# Problem 4: Keep unique values in source order with seen plus a list.
# Problem 5: Compare category sets and report all three useful groups.

# Problem 1 (Easy, LeetCode style)
# Given invoice rows, return the number of unique invoice references.
# Input:
p1_rows = ["INV-101", "INV-102", "INV-101", "INV-103", "INV-102"]
# Output: 3

# Problem 2 (Easy, real business problem)
# The boss wants each duplicate invoice reference once, in first-repeat order.
# Input:
p2_rows = ["INV-201", "INV-202", "INV-201", "INV-203", "INV-202", "INV-202"]

# Problem 3 (Medium, interview style)
# Compare two customer registers. Return all customers, shared customers,
# and customers belonging to only one branch.
# Follow-up: Why should the source registers remain unchanged?
p3_dhaka = {"C-101", "C-102", "C-103", "C-105"}
p3_chattogram = {"C-102", "C-104", "C-105"}

# Problem 4 (Medium, real business problem)
# Remove repeated invoice rows while preserving the original first-seen order.
# Also report how many rows were removed.
p4_rows = ["INV-301", "INV-302", "INV-301", "INV-303", "INV-302", "INV-304"]

# Problem 5 (Hard, real business problem)
# Compare product categories from three branch reports. Return:
# 1. categories sold by every branch,
# 2. categories only in Dhaka,
# 3. categories present in exactly one branch.
p5_dhaka = {"rice", "oil", "lentils", "sugar"}
p5_chattogram = {"oil", "sugar", "tea"}
p5_sylhet = {"oil", "tea", "spices"}

# ===== SOLUTIONS (attempt first, then compare) =====

# Problem 1 solution
# Approach:
# 1. Keep the input rows as a list.
# 2. Convert the rows to a set.
# 3. Count the set.
p1_answer = len(set(p1_rows))
print("Problem 1:", p1_answer)
# Expected: Problem 1: 3
# Key line: set(p1_rows) removes repeated invoice references.
# Complexity: building the set scans the rows once on average, O(n).

# Problem 2 solution
# Approach:
# 1. Start with an empty seen set.
# 2. A repeated invoice is one already in seen.
# 3. Append it only once to the duplicate report.
p2_seen = set()
p2_duplicates = []
for invoice in p2_rows:
    if invoice in p2_seen:
        if invoice not in p2_duplicates:
            p2_duplicates.append(invoice)
    else:
        p2_seen.add(invoice)
print("Problem 2:", p2_duplicates)
# Expected: Problem 2: ['INV-201', 'INV-202']
# Key lines: seen checks earlier rows; duplicates preserves report order.
# Complexity: membership checks are average O(1), so the scan is O(n).

# Problem 3 solution
# Approach:
# 1. Union gives every customer.
# 2. Intersection gives shared customers.
# 3. Symmetric difference gives customers in one branch only.
p3_report = {
    "all": sorted(p3_dhaka | p3_chattogram),
    "shared": sorted(p3_dhaka & p3_chattogram),
    "one_branch_only": sorted(p3_dhaka ^ p3_chattogram),
}
print("Problem 3:", p3_report)
# Expected: Problem 3: {'all': ['C-101', 'C-102', 'C-103', 'C-104', 'C-105'],
# 'shared': ['C-102', 'C-105'], 'one_branch_only': ['C-101', 'C-103', 'C-104']}
# Key lines: each set operation answers a separate management question.
# Complexity: the comparisons together are O(n + m).
# Interview talking point: the operations return new sets, so source registers
# stay unchanged.

# Problem 4 solution
# Approach:
# 1. Use seen to test each row.
# 2. Add only first occurrences to the ordered list.
# 3. Subtract the unique count from the original row count.
p4_seen = set()
p4_unique_in_order = []
for invoice in p4_rows:
    if invoice not in p4_seen:
        p4_seen.add(invoice)
        p4_unique_in_order.append(invoice)
p4_removed = len(p4_rows) - len(p4_unique_in_order)
print("Problem 4 unique:", p4_unique_in_order)
print("Problem 4 removed:", p4_removed)
# Expected: Problem 4 unique: ['INV-301', 'INV-302', 'INV-303', 'INV-304']
# Expected: Problem 4 removed: 2
# Key lines: the list preserves source order; the set prevents repeats.
# Complexity: one scan with average O(1) membership checks, O(n).

# Problem 5 solution
# Approach:
# 1. Intersect all three sets for categories shared by every branch.
# 2. Subtract both other branches from Dhaka for Dhaka-only categories.
# 3. Build the union and remove categories appearing in any pair.
p5_all = p5_dhaka | p5_chattogram | p5_sylhet
p5_every_branch = p5_dhaka & p5_chattogram & p5_sylhet
p5_dhaka_only = p5_dhaka - p5_chattogram - p5_sylhet
p5_two_or_more = (
    (p5_dhaka & p5_chattogram)
    | (p5_dhaka & p5_sylhet)
    | (p5_chattogram & p5_sylhet)
)
p5_exactly_one = p5_all - p5_two_or_more
print("Problem 5 every branch:", sorted(p5_every_branch))
print("Problem 5 Dhaka only:", sorted(p5_dhaka_only))
print("Problem 5 exactly one branch:", sorted(p5_exactly_one))
# Expected:
# Problem 5 every branch: ['oil']
# Problem 5 Dhaka only: ['lentils', 'rice']
# Problem 5 exactly one branch: ['lentils', 'rice', 'spices']
# Key lines: pairwise intersections identify categories in at least two
# branches; removing them leaves exactly-one categories.
# Complexity: a fixed number of set operations, O(n + m + k).
# Interview talking point: define “exactly one” explicitly, then remove all
# pairwise overlaps before presenting the final category list.

# Change the data and rerun. Real skill grows in the variations, not the copies.
