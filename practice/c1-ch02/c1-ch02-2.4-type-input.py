"""Subtopic 2.4: type() and input(), reading user data.
Notes: notes/c1-ch02-2.4-type-input-bangla.md
       notes/c1-ch02-2.4-type-input-english.md
"""

# Program 1: inspect known business values
daily_sales = 12000
customer = "Rahim Traders"
print(type(daily_sales))  # Expected: <class 'int'>
print(type(customer))  # Expected: <class 'str'>

# Program 2: unattended input with a default value
invoice_number = input("Invoice [INV-2024-007]: ") or "INV-2024-007"
print(invoice_number)  # Expected when Enter is pressed: INV-2024-007

# Program 3: input is text, even when it looks like a number
quantity = input("Quantity [6]: ") or "6"
print(quantity)  # Expected when Enter is pressed: 6
print(type(quantity))  # Expected: <class 'str'>

# Task 1: Print the types of daily_sales = 12000 and customer = "Rahim Traders".

# Task 2: Read an invoice number and use "INV-2024-007" when it is blank.

# Task 3: Read a quantity and print its value and type.

# Task 4: Read an optional payment note and store None when it is blank.

# Task 5: Fix Rafiq bhai's bug.
# Broken idea: total_items = quantity + 100 after input()

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
daily_sales = 12000
customer = "Rahim Traders"
print(type(daily_sales))  # Expected: <class 'int'>
print(type(customer))  # Expected: <class 'str'>

# Task 2 solution
invoice_number = input("Invoice [INV-2024-007]: ")
if invoice_number == "":
    invoice_number = "INV-2024-007"
print(invoice_number)

# Task 3 solution
quantity = input("Quantity [6]: ") or "6"
print(quantity)  # Expected: 6
print(type(quantity))  # Expected: <class 'str'>

# Task 4 solution
payment_note = input("Payment note [optional]: ")
if payment_note == "":
    payment_note = None
print(payment_note)  # Expected when Enter is pressed: None

# Task 5 solution
quantity = input("Quantity [6]: ") or "6"
print(type(quantity))  # Expected: <class 'str'>
"""
# Change the values, save, and run this file again.
