"""Subtopic 8.3: Set, creation, uniqueness, add, remove.
Notes: notes/c1-ch08-8.3-set-basics-bangla.md
       notes/c1-ch08-8.3-set-basics-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Convert the invoice list to a set.
# Problem 2: Add IDs one at a time and inspect the unique result.
# Problem 3: Use membership tests rather than indexes.
# Problem 4: Remove a known product and discard an uncertain one.
# Problem 5: Build a unique, sorted management list for display.

# Problem 1 (Easy, LeetCode-style)
# Given invoice references, return the unique references in sorted order.
references_1 = [
    "INV-2024-007", "INV-2024-008", "INV-2024-007",
    "INV-2024-009", "INV-2024-008",
]

# Problem 2 (Easy, real-world business)
# Maintain the unique customer-code register as new codes arrive.
existing_codes_2 = {"C-1023", "C-2048"}
new_codes_2 = ["C-3099", "C-1023", "C-4010"]

# Problem 3 (Medium, interview-style)
# Check which invoice references have already appeared in an audit batch.
# Follow-up: why is a set better than scanning a list for every reference?
registered_invoices_3 = {"INV-2024-007", "INV-2024-008"}
audit_batch_3 = ["INV-2024-008", "INV-2024-009", "INV-2024-007"]

# Problem 4 (Medium, real-world business)
# Maintain an active product set. Remove a discontinued product and safely
# ignore a product that may already be absent.
active_products_4 = {"Rice", "Oil", "Lentil", "Sugar"}

# Problem 5 (Hard, real-world business)
# Build a unique sorted management register from three daily invoice batches.
# Report the count and every unique reference.
batch_one_5 = ["INV-2024-007", "INV-2024-008", "INV-2024-007"]
batch_two_5 = ["INV-2024-009", "INV-2024-008"]
batch_three_5 = ["INV-2024-010", "INV-2024-007"]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Convert the batch to a set.
# 2. Remove duplicates automatically.
# 3. Sort the unique references for display.
unique_1 = sorted(set(references_1))
print(unique_1)
# Expected:
# ['INV-2024-007', 'INV-2024-008', 'INV-2024-009']
# Key line: set() keeps one copy of each reference.
# Complexity: building and sorting takes O(n log n) for display.

# Problem 2 solution
# Approach:
# 1. Start with the existing set.
# 2. Add every incoming code.
# 3. Display the unique register.
for code_2 in new_codes_2:
    existing_codes_2.add(code_2)
print(sorted(existing_codes_2))
# Expected: ['C-1023', 'C-2048', 'C-3099', 'C-4010']
# Key line: add() ignores a code already present.
# Complexity: each membership insertion is average O(1), so the batch is O(n).

# Problem 3 solution
# Approach:
# 1. Test every audit reference with `in`.
# 2. Label it as Seen or New.
# 3. Print the audit decision.
for reference_3 in audit_batch_3:
    state_3 = "Seen" if reference_3 in registered_invoices_3 else "New"
    print(f"{reference_3}: {state_3}")
# Expected:
# INV-2024-008: Seen
# INV-2024-009: New
# INV-2024-007: Seen
# Key line: the set membership test avoids position assumptions.
# Complexity: average O(n) for the batch.
# Interview talking point: a set gives fast membership checks.

# Problem 4 solution
# Approach:
# 1. Remove the discontinued product.
# 2. Discard a possibly absent product safely.
# 3. Print the active products.
active_products_4.remove("Oil")
active_products_4.discard("Tea")
print(sorted(active_products_4))
# Expected: ['Lentil', 'Rice', 'Sugar']
# Key line: discard() is safe when absence is acceptable.
# Complexity: average constant-time updates, O(1) per operation.

# Problem 5 solution
# Approach:
# 1. Start with an empty register.
# 2. Add each batch reference.
# 3. Sort the unique register.
# 4. Print its count and values.
register_5 = set()
for batch_5 in (batch_one_5, batch_two_5, batch_three_5):
    for reference_5 in batch_5:
        register_5.add(reference_5)
ordered_register_5 = sorted(register_5)
print(len(ordered_register_5))
print(ordered_register_5)
# Expected:
# 4
# ['INV-2024-007', 'INV-2024-008', 'INV-2024-009', 'INV-2024-010']
# Key lines: the set removes cross-batch duplicates.
# Complexity: all references are inserted once, then sorted, O(n log n).
# Business talking point: count unique invoices, not raw rows.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
