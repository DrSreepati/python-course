"""Subtopic 4.2: String slicing [start:stop:step].
Notes: notes/c1-ch04-4.2-slicing-bangla.md
       notes/c1-ch04-4.2-slicing-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Use the hyphens as boundaries. The year has four characters.
# Problem 2: Count positions from the left before writing each slice.
# Problem 3: Process each fixed invoice explicitly. No loop is needed yet.
# Problem 4: A reverse slice can read the final three characters backwards.
# Problem 5: Keep each report field separate, then print one management line.

# Problem 1 (Easy, LeetCode-style)
# Statement: Given one invoice code in the form "INV-YYYY-NNN", extract its
# prefix, year and serial. Formal input: one fixed-format invoice string.
# Output: print the three fields in separate labelled lines.
# Example: "INV-2024-007" -> INV, 2024, 007.
# Constraints: the prefix has three characters and the serial has three.
invoice_1 = "INV-2024-007"

# Problem 2 (Easy, interview-style)
# An interviewer asks: "The warehouse uses codes like C-1023. Extract the
# type marker, numeric part, and reversed numeric part without using methods."
# Follow-up: "Which boundary changes if the numeric part gains one digit?"
customer_code_2 = "C-1023"

# Problem 3 (Medium, real-world business)
# The boss gives Rahim three invoice references. Produce a compact report for
# each one containing prefix, year and serial. The references share one format.
invoice_a = "INV-2024-007"
invoice_b = "INV-2024-018"
invoice_c = "INV-2025-003"

# Problem 4 (Medium, LeetCode-style)
# Given an invoice code "INV-2024-007", return the serial digits in reverse
# order. Formal input: one invoice string. Output: the reversed serial.
# Example: "INV-2024-007" -> "700".
# Constraints: the serial always occupies the final three characters.
invoice_4 = "INV-2024-007"

# Problem 5 (Hard, real-world business)
# The boss wants a management summary from three customer references and two
# invoice references. For each code, report the useful business identity
# pieces. Use only indexing, slicing, variables and print statements.
customer_a = "C-1023"
customer_b = "C-2048"
invoice_x = "INV-2024-007"
invoice_y = "INV-2025-003"

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# 1. Store the invoice reference.
# 2. Slice the three fixed fields.
# 3. Print each field with a clear label.
invoice_1 = "INV-2024-007"
prefix_1 = invoice_1[:3]
year_1 = invoice_1[4:8]
serial_1 = invoice_1[9:]
print(f"Prefix: {prefix_1}")  # Expected: Prefix: INV
print(f"Year: {year_1}")  # Expected: Year: 2024
print(f"Serial: {serial_1}")  # Expected: Serial: 007
# Work grows with the number of fields, not records, so this is O(1).

# Problem 2 solution
# 1. Take the marker before the hyphen.
# 2. Take the numeric part after the hyphen.
# 3. Reverse only that numeric part.
customer_code_2 = "C-1023"
marker_2 = customer_code_2[:1]
number_2 = customer_code_2[2:]
reversed_number_2 = number_2[::-1]
print(f"Marker: {marker_2}")  # Expected: Marker: C
print(f"Number: {number_2}")  # Expected: Number: 1023
print(f"Reversed number: {reversed_number_2}")  # Expected: Reversed number: 3201
# Slicing reads fixed positions, so the work is O(1).
# Interview talking point: I would update the boundary if the code format changed.

# Problem 3 solution
# 1. Slice the same three fields from each invoice.
# 2. Print one compact report line per invoice.
# 3. Keep the repeated boundaries consistent.
invoice_a = "INV-2024-007"
invoice_b = "INV-2024-018"
invoice_c = "INV-2025-003"

print(
    f"{invoice_a[:3]} | {invoice_a[4:8]} | {invoice_a[9:]}"
)  # Expected: INV | 2024 | 007
print(
    f"{invoice_b[:3]} | {invoice_b[4:8]} | {invoice_b[9:]}"
)  # Expected: INV | 2024 | 018
print(
    f"{invoice_c[:3]} | {invoice_c[4:8]} | {invoice_c[9:]}"
)  # Expected: INV | 2025 | 003
# With a fixed number of records, this is O(1). A later loop would reduce repetition.

# Problem 4 solution
# 1. Select the final three serial digits.
# 2. Reverse that new string.
# 3. Print the result.
invoice_4 = "INV-2024-007"
serial_4 = invoice_4[-3:]
reversed_serial_4 = serial_4[::-1]
print(reversed_serial_4)  # Expected: 700
# The serial length is fixed, so the work is O(1).

# Problem 5 solution
# 1. Extract numeric customer IDs after the customer marker.
# 2. Extract invoice years and serials.
# 3. Print a compact management summary for each reference.
customer_a = "C-1023"
customer_b = "C-2048"
invoice_x = "INV-2024-007"
invoice_y = "INV-2025-003"

customer_a_id = customer_a[2:]
customer_b_id = customer_b[2:]
invoice_x_year = invoice_x[4:8]
invoice_x_serial = invoice_x[9:]
invoice_y_year = invoice_y[4:8]
invoice_y_serial = invoice_y[9:]

print(f"Customer {customer_a_id}: {customer_a[:1]}")  # Expected: Customer 1023: C
print(f"Customer {customer_b_id}: {customer_b[:1]}")  # Expected: Customer 2048: C
print(
    f"Invoice {invoice_x_year}-{invoice_x_serial}"
)  # Expected: Invoice 2024-007
print(
    f"Invoice {invoice_y_year}-{invoice_y_serial}"
)  # Expected: Invoice 2025-003
# This uses constant work for the four fixed references, so it is O(1).

# Interview talking point: fixed-format codes are easy to slice, but a changing
# format needs validation before trusting fixed boundaries.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
