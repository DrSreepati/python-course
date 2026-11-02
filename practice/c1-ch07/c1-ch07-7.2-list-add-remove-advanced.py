"""Subtopic 7.2: Adding and removing list items.
Notes: notes/c1-ch07-7.2-list-add-remove-bangla.md
       notes/c1-ch07-7.2-list-add-remove-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: append the new invoice reference.
# Problem 2: insert at index zero and extend with the second batch.
# Problem 3: check membership before remove, then pop the final item.
# Problem 4: use the returned value from pop for the audit message.
# Problem 5: keep active and closed customer lists separate.

# Problem 1 (Easy, LeetCode-style)
# Given invoice references and one new reference, add the new reference.
# Formal Input: a list and a string.
# Output: the updated list.
# Example: ["INV-001"], "INV-002" -> ["INV-001", "INV-002"].
invoice_refs_1 = ["INV-2024-007", "INV-2024-008"]
new_ref_1 = "INV-2024-009"

# Problem 2 (Easy, real-world business)
# The boss wants Rahim Traders first, then a second branch batch added.
# Use insert and extend.
customers_2 = ["Karim Store", "Jahid Enterprise"]
branch_batch_2 = ["New Market Ltd", "Dhaka Wholesale"]

# Problem 3 (Medium, interview-style)
# Remove a closed customer only if present. Then pop the last follow-up
# customer and print both the removed name and the remaining list.
# Follow-up: why is membership checking important before remove?
customers_3 = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
closed_customer_3 = "Karim Store"

# Problem 4 (Medium, real-world business)
# A payment queue contains customer names. The first customer is ready
# for review. Pop that customer, then insert an urgent customer at front.
# Follow-up: what does pop return, and how does the queue change?
payment_queue_4 = ["Karim Store", "Jahid Enterprise"]
urgent_customer_4 = "Rahim Traders"

# Problem 5 (Hard, real-world business)
# Maintain an active customer register. Add a new customer batch, move
# Rahim Traders to the front, close Karim Store if present, and delete
# the final temporary entry. Print each final register.
active_customers_5 = ["Karim Store", "Jahid Enterprise", "Temporary Account"]
new_batch_5 = ["Rahim Traders", "New Market Ltd"]
closed_customer_5 = "Karim Store"

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Keep the existing invoice references.
# 2. Append the new reference.
# 3. Print the updated register.
invoice_refs_1.append(new_ref_1)
print(invoice_refs_1)
# Expected: ['INV-2024-007', 'INV-2024-008', 'INV-2024-009']
# `append` adds one reference at the end.
# Complexity: append is amortised O(1).

# Problem 2 solution
# Approach:
# 1. Insert the priority customer at index zero.
# 2. Extend with the second branch batch.
# 3. Print the complete register.
customers_2.insert(0, "Rahim Traders")
customers_2.extend(branch_batch_2)
print(customers_2)
# Expected:
# ['Rahim Traders', 'Karim Store', 'Jahid Enterprise', 'New Market Ltd', 'Dhaka Wholesale']
# `insert` preserves all old entries and shifts them right.
# Complexity: insert and extend are O(n) in the list size.

# Problem 3 solution
# Approach:
# 1. Check that the closed customer exists.
# 2. Remove the matching value.
# 3. Pop the final follow-up customer.
if closed_customer_3 in customers_3:
    customers_3.remove(closed_customer_3)
removed_follow_up_3 = customers_3.pop()
print(f"Closed: {closed_customer_3}")
print(f"Follow-up removed: {removed_follow_up_3}")
print(customers_3)
# Expected:
# Closed: Karim Store
# Follow-up removed: Jahid Enterprise
# ['Rahim Traders']
# Membership avoids ValueError. `pop()` uses the final position.
# Complexity: membership and remove are O(n), pop at the end is O(1).
# Interview talking point: validate external values before mutation.

# Problem 4 solution
# Approach:
# 1. Pop the first ready customer.
# 2. Insert the urgent customer at the front.
# 3. Print the action and queue.
ready_customer_4 = payment_queue_4.pop(0)
payment_queue_4.insert(0, urgent_customer_4)
print(f"Ready for review: {ready_customer_4}")
print(payment_queue_4)
# Expected:
# Ready for review: Karim Store
# ['Rahim Traders', 'Jahid Enterprise']
# `pop(0)` returns the first item. `insert(0, ...)` restores priority order.
# Complexity: front removal and insertion are O(n).
# Interview talking point: say why the returned value is needed for the audit.

# Problem 5 solution
# Approach:
# 1. Add the new batch as separate entries.
# 2. Move Rahim Traders to the front without duplicating it.
# 3. Remove the closed customer safely.
# 4. Delete the final temporary entry.
active_customers_5.extend(new_batch_5)
active_customers_5.remove("Rahim Traders")
active_customers_5.insert(0, "Rahim Traders")
if closed_customer_5 in active_customers_5:
    active_customers_5.remove(closed_customer_5)
del active_customers_5[-1]
print(active_customers_5)
# Expected: ['Rahim Traders', 'Jahid Enterprise', 'Temporary Account']
# The final `del` removes New Market Ltd, the final temporary entry after earlier updates.
# Complexity: each mutation scans or shifts the list, so the complete report is O(n).
# Business talking point: perform updates in a clear order and print the final register.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
