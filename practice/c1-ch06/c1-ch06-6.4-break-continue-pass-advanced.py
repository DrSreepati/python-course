"""Subtopic 6.4: break, continue, pass.
Notes: notes/c1-ch06-6.4-break-continue-pass-bangla.md
       notes/c1-ch06-6.4-break-continue-pass-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: print first, then stop when the urgent code appears.
# Problem 2: continue for zero, otherwise accumulate.
# Problem 3: skip empty references, then stop at the urgent one.
# Problem 4: place pass inside the future review condition.
# Problem 5: use the same flow for every payment reference.

# Problem 1 (Easy, LeetCode-style)
# Search invoice references until "INV-URGENT" appears.
# Formal Input: a sequence of invoice strings.
# Output: print checked references through the urgent one.
references_1 = ["INV-001", "INV-002", "INV-URGENT", "INV-004"]

# Problem 2 (Easy, interview-style)
# Add non-zero payments. Skip zero payments.
# Follow-up: why is break incorrect here?
payments_2 = [10000, 0, 12000, 0, 5000]

# Problem 3 (Medium, real-world business)
# Validate invoice references. Skip empty strings. Stop at the urgent reference.
invoice_references_3 = ["INV-001", "", "INV-002", "INV-URGENT", "INV-005"]

# Problem 4 (Medium, interview-style)
# Leave a future audit rule as a valid placeholder with pass.
# Follow-up: what would you replace pass with later?
audit_required_4 = True

# Problem 5 (Hard, real-world business)
# Process a payment queue. Skip zero payments, stop at an urgent reference,
# and total the payments processed before the stop.
queue_5 = [
    ["INV-001", 10000],
    ["INV-002", 0],
    ["INV-URGENT", 12000],
    ["INV-004", 5000],
]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Read each reference.
# 2. Print the current reference.
# 3. Break at the urgent reference.
for reference in references_1:
    print(f"Checked: {reference}")
    if reference == "INV-URGENT":
        break
# Expected:
# Checked: INV-001
# Checked: INV-002
# Checked: INV-URGENT
# Complexity: one pass until the stop, O(n) worst case.

# Problem 2 solution
# Approach:
# 1. Test for zero.
# 2. Continue when zero appears.
# 3. Add every non-zero payment.
total_2 = 0
for payment in payments_2:
    if payment == 0:
        continue
    total_2 += payment
print(total_2)
# Expected: 27000
# Complexity: one pass through payments, O(n).
# Interview talking point: break would lose valid payments after zero.

# Problem 3 solution
# Approach:
# 1. Skip empty references.
# 2. Print valid references.
# 3. Stop after the urgent reference.
for reference in invoice_references_3:
    if reference == "":
        continue
    print(reference)
    if reference == "INV-URGENT":
        break
# Expected:
# INV-001
# INV-002
# INV-URGENT
# Complexity: O(n) worst case.

# Problem 4 solution
# Approach:
# 1. Check whether an audit is required.
# 2. Keep the block valid while its future action is undecided.
# 3. Continue the report.
if audit_required_4:
    pass
print("Report continues")
# Expected: Report continues
# Complexity: constant work, O(1).
# Interview talking point: pass is temporary structure, not business logic.

# Problem 5 solution
# Approach:
# 1. Read the reference and payment.
# 2. Skip zero payments.
# 3. Add valid payments.
# 4. Stop at the urgent reference.
processed_total_5 = 0
for reference, payment in queue_5:
    if payment == 0:
        continue
    processed_total_5 += payment
    print(f"Processed {reference}: {payment}")
    if reference == "INV-URGENT":
        print("Urgent stop")
        break
print(f"Processed total: {processed_total_5}")
# Expected:
# Processed INV-001: 10000
# Processed INV-URGENT: 12000
# Urgent stop
# Processed total: 22000
# Complexity: O(n) worst case, with early stopping in this input.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
