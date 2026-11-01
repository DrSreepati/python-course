"""Subtopic 4.5: Immutability, building new strings.
Notes: notes/c1-ch04-4.5-immutability-bangla.md
       notes/c1-ch04-4.5-immutability-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Keep the old prefix out of the result by joining a new prefix
# with a slice of the old code.
# Problem 2: Replace the known year instead of assigning to a slice.
# Problem 3: Split into a list, update the list item, then join.
# Problem 4: Keep original and new display values in separate variables.
# Problem 5: Use the format's fixed boundaries and preserve the source code.

# Problem 1 (Easy, LeetCode-style)
# Statement: Given a customer code "C-NNNN", build a supplier code
# "S-NNNN" without changing the original string.
# Formal Input: one customer code.
# Output: the original code and the new supplier code.
# Example: "C-1023" -> "S-1023".
# Constraints: the hyphen and numeric ID remain unchanged.
customer_code_1 = "C-1023"

# Problem 2 (Easy, interview-style)
# An interviewer asks: "Update the year in an invoice without direct character
# assignment. Which approach is clearer, slicing or replace()?"
# Follow-up: "When would fixed slicing become risky?"
invoice_2 = "INV-2024-007"

# Problem 3 (Medium, real-world business)
# The boss receives an invoice in parts. Update its serial number while keeping
# the prefix and year. The original invoice must remain available for audit.
original_parts_3 = ["INV", "2024", "007"]

# Problem 4 (Medium, LeetCode-style)
# Statement: Given a customer name, return a formal display name by adding
# "Mr. " without modifying the input. Formal input: one customer name.
# Output: original and new display names.
# Example: "Rahim Traders" -> "Mr. Rahim Traders".
# Constraints: the original name must be printed unchanged.
customer_name_4 = "Rahim Traders"

# Problem 5 (Hard, real-world business)
# The boss wants an audit-safe correction report. A raw invoice has a wrong
# year and slash separators. Create a standard invoice with a new year, while
# printing the raw input, old standard form and corrected standard form.
raw_invoice_5 = " inv/2024/007 "

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# 1. Keep the original customer code.
# 2. Keep everything after the first character with slicing.
# 3. Add the supplier prefix to create a new string.
customer_code_1 = "C-1023"
supplier_code_1 = "S" + customer_code_1[1:]
print(f"Original: {customer_code_1}")  # Expected: Original: C-1023
print(f"Supplier: {supplier_code_1}")  # Expected: Supplier: S-1023
# The fixed code has constant length, so this is O(1).

# Problem 2 solution
# 1. Preserve the original invoice.
# 2. Replace the known year with a new year.
# 3. Print both versions.
invoice_2 = "INV-2024-007"
updated_invoice_2 = invoice_2.replace("2024", "2025")
print(f"Original: {invoice_2}")  # Expected: Original: INV-2024-007
print(f"Updated: {updated_invoice_2}")  # Expected: Updated: INV-2025-007
# replace() scans the text, so this is O(n).
# Interview talking point: fixed slicing is risky when the code format changes;
# replace() is clearer when the target year is known.

# Problem 3 solution
# 1. Copy the parts into a new list so the source list stays available.
# 2. Change only the serial item.
# 3. Join the new list into a corrected invoice.
original_parts_3 = ["INV", "2024", "007"]
corrected_parts_3 = original_parts_3.copy()
corrected_parts_3[2] = "008"
original_invoice_3 = "-".join(original_parts_3)
corrected_invoice_3 = "-".join(corrected_parts_3)
print(f"Original: {original_invoice_3}")  # Expected: Original: INV-2024-007
print(f"Corrected: {corrected_invoice_3}")  # Expected: Corrected: INV-2024-008
# The list has three fixed items, so this is O(1).

# Problem 4 solution
# 1. Keep the input name unchanged.
# 2. Concatenate a title with the original name.
# 3. Print both values.
customer_name_4 = "Rahim Traders"
formal_name_4 = "Mr. " + customer_name_4
print(f"Original: {customer_name_4}")  # Expected: Original: Rahim Traders
print(f"Formal: {formal_name_4}")  # Expected: Formal: Mr. Rahim Traders
# Work grows with the name length, so this is O(n).

# Problem 5 solution
# 1. Preserve the raw invoice for the audit record.
# 2. Clean and standardise its separators.
# 3. Replace the old year by building a new string.
raw_invoice_5 = " inv/2024/007 "
old_standard_5 = raw_invoice_5.strip().upper().replace("/", "-")
corrected_standard_5 = old_standard_5.replace("2024", "2025")
print(f"Raw: {raw_invoice_5}")  # Expected: Raw:  inv/2024/007 
print(f"Old standard: {old_standard_5}")
# Expected: Old standard: INV-2024-007
print(f"Corrected standard: {corrected_standard_5}")
# Expected: Corrected standard: INV-2025-007
# Each method scans the text, so the work is O(n).

# Interview talking point: keeping raw, old and corrected values makes an
# audit trail possible and avoids pretending that immutable text was edited.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
