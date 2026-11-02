"""Subtopic 4.1: Creating strings, indexing and negative indexing.
Notes: notes/c1-ch04-4.1-strings-indexing-bangla.md
       notes/c1-ch04-4.1-strings-indexing-english.md
"""

# Program 1: business strings
customer = "Rahim Traders"
invoice_no = "INV-2024-007"
print(customer)  # Expected: Rahim Traders
print(invoice_no)  # Expected: INV-2024-007

# Program 2: positive and negative indexing
customer_code = "C-1023"
print(customer_code[0])  # Expected: C
print(customer_code[-1])  # Expected: 3

# Program 3: invoice prefix and length
invoice_no = "INV-2024-007"
print(invoice_no[0], invoice_no[1], invoice_no[2])  # Expected: I N V
print(len(invoice_no))  # Expected: 12
print(invoice_no[-1])  # Expected: 7

# Task 1: Print the first three characters of "INV-2024-007".
# Task 2: Print the first and last characters of "C-1023".
# Task 3: Print the last two characters of "Rahim Traders".
# Task 4: Find the length and last positive index of "INV-2024-007".
# Task 5: Fix Rafiq bhai's indexing bug:
# invoice_no = "INV-2024-007"
# first_letter = invoice_no[1]

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
code = "INV-2024-007"
print(code[0], code[1], code[2])  # Expected: I N V

# Task 2 solution
code = "C-1023"
print(code[0], code[-1])  # Expected: C 3

# Task 3 solution
name = "Rahim Traders"
print(name[-2], name[-1])  # Expected: r s

# Task 4 solution
code = "INV-2024-007"
print(len(code))  # Expected: 12
print(len(code) - 1)  # Expected: 11

# Task 5 solution
invoice_no = "INV-2024-007"
first_letter = invoice_no[0]
print(first_letter)  # Expected: I
"""
# Change the values, save, and run this file again.
