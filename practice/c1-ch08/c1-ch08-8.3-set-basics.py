"""Subtopic 8.3: Set, creation, uniqueness, add, remove.
Notes: notes/c1-ch08-8.3-set-basics-bangla.md
       notes/c1-ch08-8.3-set-basics-english.md
"""

# Program 1: duplicate references become unique.
references = {"INV-2024-007", "INV-2024-008", "INV-2024-007"}
print(sorted(references))  # Expected: ['INV-2024-007', 'INV-2024-008']

# Program 2: add unique customer IDs.
customer_ids = {"C-1023", "C-2048"}
customer_ids.add("C-3099")
customer_ids.add("C-1023")
print(sorted(customer_ids))  # Expected: ['C-1023', 'C-2048', 'C-3099']

# Program 3: remove and discard.
products = {"Rice", "Oil", "Lentil"}
products.remove("Oil")
products.discard("Sugar")
print(sorted(products))  # Expected: ['Lentil', 'Rice']

# Program 4: membership checks.
invoice_ids = {"INV-2024-007", "INV-2024-008"}
print("INV-2024-007" in invoice_ids)  # Expected: True
print("INV-2024-009" in invoice_ids)  # Expected: False

# Task 1: Remove duplicate invoice references.
# Task 2: Add a new customer code.
# Task 3: Remove a product and discard a missing product.
# Task 4: Check whether two invoice IDs are present.
# Task 5: Fix Sreepati's set-indexing bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
references = ["INV-2024-007", "INV-2024-007", "INV-2024-008"]
unique = set(references)
print(sorted(unique))
# Expected: ['INV-2024-007', 'INV-2024-008']

# Task 2
codes = {"C-1023", "C-2048"}
codes.add("C-3099")
print(sorted(codes))
# Expected: ['C-1023', 'C-2048', 'C-3099']

# Task 3
products = {"Rice", "Oil", "Lentil"}
products.remove("Oil")
products.discard("Sugar")
print(sorted(products))
# Expected: ['Lentil', 'Rice']

# Task 4
invoice_ids = {"INV-2024-007", "INV-2024-008"}
print("INV-2024-007" in invoice_ids)
print("INV-2024-009" in invoice_ids)
# Expected:
# True
# False

# Task 5
invoice_ids = {"INV-2024-007", "INV-2024-008"}
ordered_ids = sorted(invoice_ids)
print(ordered_ids[0])
# Expected: INV-2024-007
"""
# Change the values and rerun. Unique records grow from careful checking.
