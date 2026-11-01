"""Subtopic 4.7: Invoice/reference number parsing and code extraction.
Notes: notes/c1-ch04-4.7-invoice-code-parsing-bangla.md
       notes/c1-ch04-4.7-invoice-code-parsing-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Split the customer code and keep the two parts named.
# Problem 2: Clean the invoice before splitting; keep the serial as text.
# Problem 3: Validate the prefix and part count before unpacking.
# Problem 4: Use the fixed positions only after confirming the fixed format.
# Problem 5: Keep raw records, then build a report from validated parsed fields.

# Problem 1 (Easy, LeetCode-style)
# Statement: Given one customer code, return its type and ID as named fields.
# Formal Input: "C-1023".
# Output: "Type: C" and "Customer ID: 1023".
customer_code_1 = "C-1023"

# Problem 2 (Easy, interview-style)
# Standardise an invoice with outer spaces, lowercase letters and slash
# separators, then print its prefix, year and serial.
# Formal Input: " inv/2024/007 ".
raw_invoice_2 = " inv/2024/007 "

# Problem 3 (Medium, real-world business)
# Validate one invoice before unpacking it. It must start with "INV-", contain
# exactly two hyphens and have three parts. Print each check and the fields only
# when the structure is valid.
invoice_3 = "INV-2024-007"

# Problem 4 (Medium, LeetCode-style)
# Statement: Extract fields from a fixed-format invoice using slicing.
# Formal Input: "INV-2025-003".
# Output: prefix "INV", year "2025", serial "003".
invoice_4 = "INV-2025-003"

# Problem 5 (Hard, real-world business)
# The boss gives raw customer, product and invoice records. Clean each record
# using field-specific rules, parse the parts, validate the invoice, and print
# an audit-ready summary without losing the raw values.
raw_customer_5 = "  jahid ENTERPRISE  "
raw_product_5 = " p/rice/025 "
raw_invoice_5 = " inv/2025/003 "

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
customer_code_1 = "C-1023"
customer_type_1, customer_id_1 = customer_code_1.split("-")
print(f"Type: {customer_type_1}")  # Expected: Type: C
print(f"Customer ID: {customer_id_1}")  # Expected: Customer ID: 1023
# Splitting a string of length n takes O(n) time and O(n) space.

# Problem 2 solution
raw_invoice_2 = " inv/2024/007 "
clean_invoice_2 = raw_invoice_2.strip().upper().replace("/", "-")
prefix_2, year_2, serial_2 = clean_invoice_2.split("-")
print(f"Prefix: {prefix_2}")  # Expected: Prefix: INV
print(f"Year: {year_2}")  # Expected: Year: 2024
print(f"Serial: {serial_2}")  # Expected: Serial: 007
# Interview talking point: keep serial as text so its leading zero survives.
# The string is scanned a constant number of times, so this is O(n).

# Problem 3 solution
invoice_3 = "INV-2024-007"
parts_3 = invoice_3.split("-")
is_valid_3 = (
    invoice_3.startswith("INV-")
    and invoice_3.count("-") == 2
    and len(parts_3) == 3
)
print(f"Starts with INV-: {invoice_3.startswith('INV-')}")
# Expected: Starts with INV-: True
print(f"Two hyphens: {invoice_3.count('-') == 2}")
# Expected: Two hyphens: True
print(f"Three parts: {len(parts_3) == 3}")
# Expected: Three parts: True
print(f"Valid invoice: {is_valid_3}")  # Expected: Valid invoice: True
if is_valid_3:
    prefix_3, year_3, serial_3 = parts_3
    print(prefix_3, year_3, serial_3)  # Expected: INV 2024 007
# Checking before unpacking avoids ValueError for incomplete input.

# Problem 4 solution
invoice_4 = "INV-2025-003"
prefix_4 = invoice_4[:3]
year_4 = invoice_4[4:8]
serial_4 = invoice_4[9:]
print(prefix_4)  # Expected: INV
print(year_4)  # Expected: 2025
print(serial_4)  # Expected: 003
# With a fixed-width code, the number of positions is constant; the scan is O(n).
# Interview talking point: split() is safer when the separator position can vary.

# Problem 5 solution
raw_customer_5 = "  jahid ENTERPRISE  "
raw_product_5 = " p/rice/025 "
raw_invoice_5 = " inv/2025/003 "

clean_customer_5 = raw_customer_5.strip()
customer_key_5 = clean_customer_5.lower()
clean_product_5 = raw_product_5.strip().upper().replace("/", "-")
clean_invoice_5 = raw_invoice_5.strip().upper().replace("/", "-")

customer_parts_5 = clean_customer_5.split()
product_parts_5 = clean_product_5.split("-")
invoice_parts_5 = clean_invoice_5.split("-")
invoice_valid_5 = (
    clean_invoice_5.startswith("INV-")
    and clean_invoice_5.count("-") == 2
    and len(invoice_parts_5) == 3
)

print(f"Customer raw: {raw_customer_5}")
# Expected: Customer raw:   jahid ENTERPRISE
print(f"Customer key: {customer_key_5}")
# Expected: Customer key: jahid enterprise
print(f"Product: {product_parts_5[1]}")
# Expected: Product: RICE
print(f"Item number: {product_parts_5[2]}")
# Expected: Item number: 025
print(f"Invoice clean: {clean_invoice_5}")
# Expected: Invoice clean: INV-2025-003
print(f"Invoice valid: {invoice_valid_5}")
# Expected: Invoice valid: True
if invoice_valid_5:
    print(f"Invoice year: {invoice_parts_5[1]}")
    # Expected: Invoice year: 2025
    print(f"Invoice serial: {invoice_parts_5[2]}")
    # Expected: Invoice serial: 003
# Each record is processed a constant number of times, so total work is O(n)
# for the combined input length. Raw values use O(n) audit space.
# Interview talking point: field-specific rules preserve names while
# standardising code separators.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
