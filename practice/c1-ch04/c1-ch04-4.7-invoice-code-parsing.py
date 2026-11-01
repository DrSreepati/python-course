"""Subtopic 4.7: Invoice/reference number parsing and code extraction.
Notes: notes/c1-ch04-4.7-invoice-code-parsing-bangla.md
       notes/c1-ch04-4.7-invoice-code-parsing-english.md
"""

# Program 1: parse an invoice into business fields
invoice_no = "INV-2024-007"
parts = invoice_no.split("-")
print(parts)  # Expected: ['INV', '2024', '007']
print(f"Prefix: {parts[0]}")  # Expected: Prefix: INV
print(f"Year: {parts[1]}")  # Expected: Year: 2024
print(f"Serial: {parts[2]}")  # Expected: Serial: 007

# Program 2: parse a customer code
customer_code = "C-1023"
customer_parts = customer_code.split("-")
print(f"Type: {customer_parts[0]}")  # Expected: Type: C
print(f"Customer ID: {customer_parts[1]}")  # Expected: Customer ID: 1023

# Program 3: parse a product code
product_code = "P-RICE-025"
product_parts = product_code.split("-")
print(f"Product: {product_parts[1]}")  # Expected: Product: RICE
print(f"Item number: {product_parts[2]}")  # Expected: Item number: 025

# Program 4: clean and parse raw codes
raw_customer = " c-1023 "
raw_product = " p/rice/025 "
raw_invoice = " inv/2024/007 "

clean_customer = raw_customer.strip().upper()
clean_product = raw_product.strip().upper().replace("/", "-")
clean_invoice = raw_invoice.strip().upper().replace("/", "-")

print(clean_customer)  # Expected: C-1023
print(clean_product)  # Expected: P-RICE-025
print(clean_invoice)  # Expected: INV-2024-007

clean_invoice_parts = clean_invoice.split("-")
print(f"Invoice year: {clean_invoice_parts[1]}")  # Expected: Invoice year: 2024
print(f"Invoice serial: {clean_invoice_parts[2]}")  # Expected: Invoice serial: 007

# Program 5: basic invoice validation
is_invoice = invoice_no.startswith("INV-")
has_two_separators = invoice_no.count("-") == 2
has_three_parts = len(invoice_no.split("-")) == 3
print(is_invoice)  # Expected: True
print(has_two_separators)  # Expected: True
print(has_three_parts)  # Expected: True

# Program 6: fixed-format slicing
invoice_prefix = invoice_no[:3]
invoice_year = invoice_no[4:8]
invoice_serial = invoice_no[9:]
print(invoice_prefix)  # Expected: INV
print(invoice_year)  # Expected: 2024
print(invoice_serial)  # Expected: 007

# Task 1: Extract the customer type and customer ID from "C-1023".
# Task 2: Extract the product name and item number from "P-RICE-025".
# Task 3: Unpack "INV-2024-007" into prefix, year and serial.
# Task 4: Clean " inv/2024/007 " and print its year and serial.
# Task 5: Fix Rafiq bhai's bug:
# invoice_no = "INV-2024-007"
# prefix, serial, year = invoice_no.split("-")

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
customer_parts = "C-1023".split("-")
print(customer_parts[0])  # Expected: C
print(customer_parts[1])  # Expected: 1023

# Task 2 solution
product_parts = "P-RICE-025".split("-")
print(product_parts[1])  # Expected: RICE
print(product_parts[2])  # Expected: 025

# Task 3 solution
prefix, year, serial = "INV-2024-007".split("-")
print(prefix, year, serial)  # Expected: INV 2024 007

# Task 4 solution
code = " inv/2024/007 ".strip().upper().replace("/", "-")
parts = code.split("-")
print(parts[1])  # Expected: 2024
print(parts[2])  # Expected: 007

# Task 5 solution
invoice_no = "INV-2024-007"
prefix, year, serial = invoice_no.split("-")
print(f"Year: {year}")  # Expected: Year: 2024
"""
# Change the values, save, and run this file again.
