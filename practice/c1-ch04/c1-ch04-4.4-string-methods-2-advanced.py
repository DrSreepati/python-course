"""Subtopic 4.4: String methods 2.
Notes: notes/c1-ch04-4.4-string-methods-2-bangla.md
       notes/c1-ch04-4.4-string-methods-2-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Split at the hyphens, then join with a different separator.
# Problem 2: Use find() for a position and boundary methods for validation.
# Problem 3: Clean first, then split and join the invoice reference.
# Problem 4: A tuple can hold several acceptable endings.
# Problem 5: Keep parsed parts, validation results and a display code separate.

# Problem 1 (Easy, LeetCode-style)
# Statement: Given an invoice code in the form "INV-YYYY-NNN", return the
# same parts joined with slashes. Formal input: one invoice string.
# Output: "INV/YYYY/NNN".
# Example: "INV-2024-007" -> "INV/2024/007".
# Constraints: the input contains two hyphens.
invoice_1 = "INV-2024-007"

# Problem 2 (Easy, interview-style)
# An interviewer asks: "Validate a customer code such as C-1023. Report the
# separator position, whether it starts with C-, and whether it ends in digits."
# Follow-up: "What check would you add if the code could use S- for suppliers?"
customer_code_2 = "C-1023"

# Problem 3 (Medium, real-world business)
# The boss receives a raw invoice. Clean it, split its parts, rebuild a
# standard invoice, and report whether it has the expected prefix and serial.
raw_invoice_3 = " inv/2024/007 "

# Problem 4 (Medium, LeetCode-style)
# Statement: Given a report filename, decide whether it ends with an accepted
# spreadsheet extension. Formal input: one filename and two accepted suffixes.
# Output: True or False.
# Example: "sales_report.csv" -> True.
# Constraints: accept only .csv and .xlsx.
file_name_4 = "sales_report.csv"

# Problem 5 (Hard, real-world business)
# The boss wants a compact parser for two customer codes and two invoices.
# For each invoice, show its parts and rebuilt standard form. For each
# customer, show its parts and whether it has the expected C- prefix.
customer_a = "C-1023"
customer_b = "C-2048"
invoice_a = "INV-2024-007"
invoice_b = "INV-2025-003"

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# 1. Split the invoice at hyphens.
# 2. Join the parts with slashes.
# 3. Print the converted reference.
invoice_1 = "INV-2024-007"
parts_1 = invoice_1.split("-")
slash_invoice_1 = "/".join(parts_1)
print(slash_invoice_1)  # Expected: INV/2024/007
# The fixed-format input needs constant work, so this is O(1).

# Problem 2 solution
# 1. Find the separator position.
# 2. Check the expected prefix.
# 3. Check that the code ends with the expected numeric part.
customer_code_2 = "C-1023"
separator_position_2 = customer_code_2.find("-")
has_prefix_2 = customer_code_2.startswith("C-")
has_numeric_suffix_2 = customer_code_2.endswith("1023")
print(f"Separator position: {separator_position_2}")
# Expected: Separator position: 1
print(f"Has C- prefix: {has_prefix_2}")
# Expected: Has C- prefix: True
print(f"Has 1023 suffix: {has_numeric_suffix_2}")
# Expected: Has 1023 suffix: True
# Each check scans a short fixed string, so this is O(1).
# Interview talking point: I would add an allowed-prefix check for C- and S-.

# Problem 3 solution
# 1. Remove outer spaces and standardise case.
# 2. Split the slash-separated parts.
# 3. Rebuild the invoice with hyphens and validate its boundaries.
raw_invoice_3 = " inv/2024/007 "
clean_invoice_3 = raw_invoice_3.strip().upper()
parts_3 = clean_invoice_3.split("/")
standard_invoice_3 = "-".join(parts_3)
print(parts_3)  # Expected: ['INV', '2024', '007']
print(standard_invoice_3)  # Expected: INV-2024-007
print(standard_invoice_3.startswith("INV"))
# Expected: True
print(standard_invoice_3.endswith("007"))
# Expected: True
# Work grows with the invoice text length, so this is O(n).

# Problem 4 solution
# 1. Store the accepted extensions in a tuple.
# 2. Pass the tuple to endswith().
# 3. Print the Boolean validation result.
file_name_4 = "sales_report.csv"
accepted_extensions_4 = (".csv", ".xlsx")
is_spreadsheet_4 = file_name_4.endswith(accepted_extensions_4)
print(is_spreadsheet_4)  # Expected: True
# The tuple has a fixed number of suffixes, so this is O(n).

# Problem 5 solution
# 1. Split each customer code and invoice.
# 2. Rebuild each invoice with hyphens.
# 3. Validate each customer prefix and print a clear report.
customer_a = "C-1023"
customer_b = "C-2048"
invoice_a = "INV-2024-007"
invoice_b = "INV-2025-003"

customer_a_parts = customer_a.split("-")
customer_b_parts = customer_b.split("-")
invoice_a_parts = invoice_a.split("-")
invoice_b_parts = invoice_b.split("-")

print(f"Customer A parts: {customer_a_parts}")
# Expected: Customer A parts: ['C', '1023']
print(f"Customer A valid: {customer_a.startswith('C-')}")
# Expected: Customer A valid: True
print(f"Customer B parts: {customer_b_parts}")
# Expected: Customer B parts: ['C', '2048']
print(f"Customer B valid: {customer_b.startswith('C-')}")
# Expected: Customer B valid: True
print(f"Invoice A: {'-'.join(invoice_a_parts)}")
# Expected: Invoice A: INV-2024-007
print(f"Invoice B: {'-'.join(invoice_b_parts)}")
# Expected: Invoice B: INV-2025-003
# With these four fixed records, this is O(1); with n records, it is O(n).

# Interview talking point: I separate parsing, rebuilding and validation so
# each business rule can be checked independently.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
