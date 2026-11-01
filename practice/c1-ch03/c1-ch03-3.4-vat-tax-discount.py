"""Subtopic 3.4: VAT, tax and discount calculations.
Notes: notes/c1-ch03-3.4-vat-tax-discount-bangla.md
       notes/c1-ch03-3.4-vat-tax-discount-english.md
"""

# Program 1: discount, VAT and final total
gross_amount = 10000
discount_rate = 0.10
vat_rate = 0.15
discount = gross_amount * discount_rate
subtotal = gross_amount - discount
vat = subtotal * vat_rate
total = subtotal + vat
print(discount)  # Expected: 1000.0
print(subtotal)  # Expected: 9000.0
print(vat)  # Expected: 1350.0
print(total)  # Expected: 10350.0

# Program 2: full invoice summary
quantity = 4
unit_price = 2500
discount_percentage = 10
vat_percentage = 15
gross = quantity * unit_price
discount = gross * discount_percentage / 100
subtotal = gross - discount
vat = subtotal * vat_percentage / 100
total = subtotal + vat
print(f"Gross: {gross:.2f}")  # Expected: Gross: 10000.00
print(f"Discount: {discount:.2f}")  # Expected: Discount: 1000.00
print(f"Subtotal: {subtotal:.2f}")  # Expected: Subtotal: 9000.00
print(f"VAT: {vat:.2f}")  # Expected: VAT: 1350.00
print(f"Total: {total:.2f}")  # Expected: Total: 10350.00

# Program 3: zero-value guard
gross_amount = 0
if gross_amount <= 0:
    print("Check the gross amount")  # Expected: Check the gross amount

# Task 1: Find discount and subtotal for gross 10000 and discount 10%.
# Task 2: Find VAT on subtotal 9000 at 15%.
# Task 3: Find final total for subtotal 9000 and VAT 1350.
# Task 4: Calculate the full invoice for quantity 4, price 2500, discount 10%, VAT 15%.
# Task 5: Fix Rafiq bhai's VAT-base bug:
# gross = 10000
# discount = 1000
# vat_rate = 0.15
# subtotal = gross - discount
# vat = gross * vat_rate

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1 solution
gross = 10000
discount = gross * 10 / 100
subtotal = gross - discount
print(discount, subtotal)  # Expected: 1000.0 9000.0

# Task 2 solution
print(9000 * 15 / 100)  # Expected: 1350.0

# Task 3 solution
print(9000 + 1350)  # Expected: 10350

# Task 4 solution
quantity = 4
price = 2500
gross = quantity * price
discount = gross * 10 / 100
subtotal = gross - discount
vat = subtotal * 15 / 100
total = subtotal + vat
print(gross, discount, subtotal, vat, total)
# Expected: 10000 1000.0 9000.0 1350.0 10350.0

# Task 5 solution
gross = 10000
discount = 1000
vat_rate = 0.15
subtotal = gross - discount
vat = subtotal * vat_rate
print(subtotal + vat)  # Expected: 10350.0
"""
# Change the values, save, and run this file again.
