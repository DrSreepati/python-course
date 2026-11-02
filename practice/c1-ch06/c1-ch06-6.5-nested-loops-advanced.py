"""Subtopic 6.5: Nested loops.
Notes: notes/c1-ch06-6.5-nested-loops-bangla.md
       notes/c1-ch06-6.5-nested-loops-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: the inner range runs for every outer range value.
# Problem 2: reset the customer total before its inner loop.
# Problem 3: use break inside the inner invoice loop.
# Problem 4: keep group and overall totals separate.
# Problem 5: print each customer report after its inner invoice loop.

# Problem 1 (Easy, LeetCode-style)
# Print every pair of customer numbers and invoice numbers.
# Formal Input: customers 1 to 3, invoices 1 to 2.
# Output: six pairs.
customer_count_1 = 3
invoice_count_1 = 2

# Problem 2 (Easy, interview-style)
# Calculate invoice totals for three customers.
# Follow-up: where should the customer total be reset?
customer_names_2 = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
invoice_groups_2 = [[12000, 8000], [7000, 5000], [30000, 20000]]

# Problem 3 (Medium, real-world business)
# Check invoices for each customer. Stop that customer's checking at
# INV-URGENT, then continue with the next customer.
customers_3 = ["Rahim Traders", "Karim Store"]
invoices_3 = ["INV-001", "INV-URGENT", "INV-003"]

# Problem 4 (Medium, interview-style)
# Calculate each group total and one overall total.
# Follow-up: what bug appears if overall_total is reset inside the outer loop?
groups_4 = [[5000, 4000], [7000, 3000], [6000, 2000]]

# Problem 5 (Hard, real-world business)
# Produce a customer invoice report. Each customer has invoice amounts.
# Print each invoice, each customer total, and the overall total.
customers_5 = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
invoice_groups_5 = [[12000, 8000], [7000, 5000], [30000, 41000]]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Loop through each customer number.
# 2. Loop through each invoice number.
# 3. Print every pair.
for customer_number in range(1, customer_count_1 + 1):
    for invoice_number in range(1, invoice_count_1 + 1):
        print(f"Customer {customer_number}, invoice {invoice_number}")
# Expected:
# Customer 1, invoice 1
# Customer 1, invoice 2
# Customer 2, invoice 1
# Customer 2, invoice 2
# Customer 3, invoice 1
# Customer 3, invoice 2
# Complexity: outer times inner work, O(n * m).

# Problem 2 solution
# Approach:
# 1. Visit names in order.
# 2. Reset one total for that customer.
# 3. Add every invoice amount.
# 4. Print the result.
position_2 = 0
for name in customer_names_2:
    customer_total = 0
    for amount in invoice_groups_2[position_2]:
        customer_total += amount
    print(f"{name}: {customer_total}")
    position_2 += 1
# Expected:
# Rahim Traders: 20000
# Karim Store: 12000
# Jahid Enterprise: 50000
# Complexity: each invoice is read once, O(n * m) in the rectangular case.
# Interview talking point: reset the group total, not the overall total.

# Problem 3 solution
# Approach:
# 1. Take one customer.
# 2. Read its invoice sequence.
# 3. Stop only that inner loop at urgent.
for customer in customers_3:
    for invoice in invoices_3:
        print(f"{customer}: {invoice}")
        if invoice == "INV-URGENT":
            break
# Expected:
# Rahim Traders: INV-001
# Rahim Traders: INV-URGENT
# Karim Store: INV-001
# Karim Store: INV-URGENT
# Complexity: O(n * m) worst case.

# Problem 4 solution
# Approach:
# 1. Start overall total once.
# 2. Reset group total for each group.
# 3. Add each amount to both relevant totals.
overall_total_4 = 0
for amounts in groups_4:
    group_total_4 = 0
    for amount in amounts:
        group_total_4 += amount
        overall_total_4 += amount
    print(f"Group total: {group_total_4}")
print(f"Overall total: {overall_total_4}")
# Expected:
# Group total: 9000
# Group total: 10000
# Group total: 8000
# Overall total: 27000
# Complexity: one pass per amount, O(n * m).
# Interview talking point: explain the different lifetimes of the two totals.

# Problem 5 solution
# Approach:
# 1. Use one customer position.
# 2. Print and total each invoice group.
# 3. Print the customer total.
# 4. Keep an overall total across all groups.
overall_5 = 0
position_5 = 0
for customer in customers_5:
    customer_total_5 = 0
    for amount in invoice_groups_5[position_5]:
        print(f"{customer} invoice: {amount}")
        customer_total_5 += amount
        overall_5 += amount
    print(f"{customer} total: {customer_total_5}")
    position_5 += 1
print(f"Overall total: {overall_5}")
# Expected:
# Rahim Traders invoice: 12000
# Rahim Traders invoice: 8000
# Rahim Traders total: 20000
# Karim Store invoice: 7000
# Karim Store invoice: 5000
# Karim Store total: 12000
# Jahid Enterprise invoice: 30000
# Jahid Enterprise invoice: 41000
# Jahid Enterprise total: 71000
# Overall total: 103000
# Complexity: one pass per invoice, O(n * m).
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
