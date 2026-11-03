"""Subtopic 8.2: Tuple unpacking, tuple versus list.
Notes: notes/c1-ch08-8.2-tuple-unpacking-bangla.md
       notes/c1-ch08-8.2-tuple-unpacking-english.md
"""

# Program 1: unpack a fixed invoice record.
invoice = ("INV-2024-007", "Rahim Traders", 50000)
invoice_no, customer, amount = invoice
print(invoice_no, customer, amount)  # Expected: INV-2024-007 Rahim Traders 50000

# Program 2: star unpacking.
sales = ("Rahim Traders", 12000, 9500, 8800, 13200)
customer, *daily_sales = sales
print(customer)  # Expected: Rahim Traders
print(daily_sales)  # Expected: [12000, 9500, 8800, 13200]

# Program 3: tuple versus changing list.
approved_status = ("INV-2024-007", "Approved")
daily_report = [12000, 9500, 8800]
daily_report.append(13200)
print(approved_status)  # Expected: ('INV-2024-007', 'Approved')
print(daily_report)  # Expected: [12000, 9500, 8800, 13200]

# Program 4: unpack a customer record.
record = ("Karim Store", 32000, "Active")
name, balance, status = record
print(f"{name}: {balance}, {status}")  # Expected: Karim Store: 32000, Active

# Task 1: Unpack an invoice tuple.
# Task 2: Separate a customer and the remaining sales.
# Task 3: Use a tuple for fixed status and a list for changing sales.
# Task 4: Unpack and print a customer record.
# Task 5: Fix Sreepati's count-mismatch bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
invoice = ("INV-2024-007", "Rahim Traders", 50000)
invoice_no, customer, amount = invoice
print(invoice_no, customer, amount)
# Expected: INV-2024-007 Rahim Traders 50000

# Task 2
sales = ("Rahim Traders", 12000, 9500, 8800)
customer, *amounts = sales
print(customer)
print(amounts)
# Expected:
# Rahim Traders
# [12000, 9500, 8800]

# Task 3
invoice_status = ("INV-2024-007", "Approved")
daily_sales = [12000, 9500]
daily_sales.append(8800)
print(invoice_status)
print(daily_sales)
# Expected:
# ('INV-2024-007', 'Approved')
# [12000, 9500, 8800]

# Task 4
record = ("Karim Store", 32000, "Active")
name, balance, status = record
print(f"{name} has {balance}, status {status}")
# Expected: Karim Store has 32000, status Active

# Task 5
record = ("Rahim Traders", 50000, "Review")
customer, balance, status = record
print(customer, balance, status)
# Expected: Rahim Traders 50000 Review
"""
# Change the values and rerun. Clear fields make reliable reports.
