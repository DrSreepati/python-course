"""Subtopic 6.4: break, continue, pass.
Notes: notes/c1-ch06-6.4-break-continue-pass-bangla.md
       notes/c1-ch06-6.4-break-continue-pass-english.md
"""

# Program 1: stop at an urgent invoice
for invoice in ["INV-001", "INV-002", "INV-URGENT", "INV-004"]:
    print(f"Checking {invoice}")
    if invoice == "INV-URGENT":
        print("Urgent invoice found")
        break

# Program 2: skip zero payments
payments = [10000, 0, 12000]
for payment in payments:
    if payment == 0:
        continue
    print(f"Record payment: {payment}")  # Expected: 10000 and 12000

# Program 3: skip day 2, stop at day 3
for day in range(1, 5):
    if day == 2:
        continue
    print(f"Report day {day}")  # Expected: days 1 and 3
    if day == 3:
        break

# Task 1: Stop at INV-URGENT.
# Task 2: Skip zero payment.
# Task 3: Use pass in a future review block.
# Task 4: Skip day 2 and stop at day 3.
# Task 5: Fix Rafiq bhai's break used for a single bad payment.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
for reference in ["INV-001", "INV-URGENT", "INV-003"]:
    print(reference)
    if reference == "INV-URGENT":
        break

# Task 2
for payment in [10000, 0, 12000]:
    if payment == 0:
        continue
    print(payment)

# Task 3
review_required = True
if review_required:
    pass
print("Continue")

# Task 4
for day in range(1, 5):
    if day == 2:
        continue
    print(day)
    if day == 3:
        break

# Task 5
for payment in [10000, 0, 12000]:
    if payment == 0:
        continue
    print(payment)
"""
# Change the values, save, and run this file again.
