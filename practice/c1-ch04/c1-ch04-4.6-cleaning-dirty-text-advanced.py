"""Subtopic 4.6: Cleaning dirty text.
Notes: notes/c1-ch04-4.6-cleaning-dirty-text-bangla.md
       notes/c1-ch04-4.6-cleaning-dirty-text-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Keep the raw name and create a lowercase comparison key.
# Problem 2: Clean whitespace and case before replacing the known separator.
# Problem 3: Print intermediate steps so the cleaning order is visible.
# Problem 4: Validate both separator counts and the expected boundaries.
# Problem 5: Use different rules for customer names and invoice references.

# Problem 1 (Easy, LeetCode-style)
# Statement: Given one customer name with outer spaces and mixed case,
# return its lowercase comparison key without changing the raw input.
# Formal Input: "  Rahim TRADERS  ".
# Output: "rahim traders".
# Constraints: keep the internal space between the two words.
raw_customer_1 = "  Rahim TRADERS  "

# Problem 2 (Easy, interview-style)
# An interviewer asks: "Standardise an invoice with outer spaces, lowercase
# letters and slash separators. Explain why the cleaning order matters."
# Follow-up: "Which step would you change if the standard separator were /?"
raw_invoice_2 = " inv/2024/007 "

# Problem 3 (Medium, real-world business)
# The boss wants an audit-friendly cleaning report. Show each stage for a raw
# customer field, then show the final comparison key and preserve the raw value.
raw_customer_3 = "  KARIM Store  "

# Problem 4 (Medium, LeetCode-style)
# Statement: Validate a cleaned invoice. It must contain no slash, exactly two
# hyphens, start with "INV-" and end with a three-digit serial provided here.
# Formal Input: one cleaned invoice. Output: each check as True or False.
# Example: "INV-2024-007" passes all checks.
clean_invoice_4 = "INV-2024-007"

# Problem 5 (Hard, real-world business)
# The boss gives one customer field and one invoice field. Clean each using
# field-specific rules, keep raw values, and print a final audit summary with
# both cleaned values and validation checks.
raw_customer_5 = "  jahid ENTERPRISE  "
raw_invoice_5 = " inv/2025/003 "

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# 1. Keep the raw customer value.
# 2. Remove outer spaces.
# 3. Lowercase the result for matching.
raw_customer_1 = "  Rahim TRADERS  "
customer_key_1 = raw_customer_1.strip().lower()
print(f"Raw: {raw_customer_1}")  # Expected: Raw:   Rahim TRADERS
print(f"Key: {customer_key_1}")  # Expected: Key: rahim traders
# The work grows with the name length, so this is O(n).

# Problem 2 solution
# 1. Strip outer whitespace.
# 2. Standardise letter case.
# 3. Replace the known wrong separator.
raw_invoice_2 = " inv/2024/007 "
step_1_2 = raw_invoice_2.strip()
step_2_2 = step_1_2.upper()
clean_invoice_2 = step_2_2.replace("/", "-")
print(f"After strip: {step_1_2}")  # Expected: After strip: inv/2024/007
print(f"After upper: {step_2_2}")  # Expected: After upper: INV/2024/007
print(f"Clean invoice: {clean_invoice_2}")
# Expected: Clean invoice: INV-2024-007
# The text is scanned by each method, so this is O(n).
# Interview talking point: the order creates clear, inspectable intermediate data.

# Problem 3 solution
# 1. Preserve the raw input.
# 2. Strip outer spaces.
# 3. Lowercase the display-clean value for comparison.
raw_customer_3 = "  KARIM Store  "
stripped_customer_3 = raw_customer_3.strip()
customer_key_3 = stripped_customer_3.lower()
print(f"Raw: {raw_customer_3}")  # Expected: Raw:   KARIM Store
print(f"Stripped: {stripped_customer_3}")
# Expected: Stripped: KARIM Store
print(f"Comparison key: {customer_key_3}")
# Expected: Comparison key: karim store
# This is O(n) in the length of the name.

# Problem 4 solution
# 1. Count slash and hyphen separators.
# 2. Check the expected prefix.
# 3. Check the expected serial ending.
clean_invoice_4 = "INV-2024-007"
no_slash_4 = clean_invoice_4.count("/") == 0
two_hyphens_4 = clean_invoice_4.count("-") == 2
has_prefix_4 = clean_invoice_4.startswith("INV-")
has_serial_4 = clean_invoice_4.endswith("007")
print(f"No slash: {no_slash_4}")  # Expected: No slash: True
print(f"Two hyphens: {two_hyphens_4}")  # Expected: Two hyphens: True
print(f"Correct prefix: {has_prefix_4}")  # Expected: Correct prefix: True
print(f"Correct serial: {has_serial_4}")  # Expected: Correct serial: True
# The fixed-format string makes this O(1); for length n, the checks are O(n).

# Problem 5 solution
# 1. Keep customer and invoice raw values.
# 2. Apply name-specific and invoice-specific cleaning rules.
# 3. Validate and print an audit summary.
raw_customer_5 = "  jahid ENTERPRISE  "
raw_invoice_5 = " inv/2025/003 "
customer_key_5 = raw_customer_5.strip().lower()
clean_invoice_5 = raw_invoice_5.strip().upper().replace("/", "-")

print(f"Customer raw: {raw_customer_5}")
# Expected: Customer raw:   jahid ENTERPRISE
print(f"Customer key: {customer_key_5}")
# Expected: Customer key: jahid enterprise
print(f"Invoice raw: {raw_invoice_5}")
# Expected: Invoice raw:  inv/2025/003
print(f"Invoice clean: {clean_invoice_5}")
# Expected: Invoice clean: INV-2025-003
print(f"Invoice valid: {clean_invoice_5.startswith('INV-') and clean_invoice_5.endswith('003')}")
# Expected: Invoice valid: True
# Each field is processed a constant number of times, so this is O(n).

# Interview talking point: field-specific rules prevent customer spaces from
# being destroyed while invoice separators are standardised.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
