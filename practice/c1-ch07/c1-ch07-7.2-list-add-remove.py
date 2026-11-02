"""Subtopic 7.2: Adding and removing list items.
Notes: notes/c1-ch07-7.2-list-add-remove-bangla.md
       notes/c1-ch07-7.2-list-add-remove-english.md
"""

# Program 1: add one item at the end and at a position.
customers = ["Karim Store", "Jahid Enterprise"]
customers.insert(0, "Rahim Traders")
customers.append("New Market Ltd")
print(customers)  # Expected: ['Rahim Traders', 'Karim Store', 'Jahid Enterprise', 'New Market Ltd']

# Program 2: add several items.
branch_customers = ["Rahim Traders"]
branch_customers.extend(["Karim Store", "Jahid Enterprise"])
print(branch_customers)  # Expected: ['Rahim Traders', 'Karim Store', 'Jahid Enterprise']

# Program 3: remove by value, then by position.
customers = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
customers.remove("Karim Store")
removed_customer = customers.pop(0)
print(removed_customer)  # Expected: Rahim Traders
print(customers)  # Expected: ['Jahid Enterprise']

# Program 4: safe removal and del.
customers = ["Rahim Traders", "Karim Store"]
if "Jahid Enterprise" in customers:
    customers.remove("Jahid Enterprise")
else:
    print("Customer not found")  # Expected: Customer not found
del customers[0]
print(customers)  # Expected: ['Karim Store']

# Task 1: Append a new customer.
# Task 2: Insert Rahim Traders at position zero.
# Task 3: Extend a list with two customers.
# Task 4: Remove Karim Store and pop the remaining first customer.
# Task 5: Fix Rafiq bhai's nested-list bug.

# ===== SOLUTIONS (try first, then compare) =====
"""
# Task 1
customers = ["Rahim Traders", "Karim Store"]
customers.append("Jahid Enterprise")
print(customers)

# Task 2
customers = ["Karim Store", "Jahid Enterprise"]
customers.insert(0, "Rahim Traders")
print(customers)

# Task 3
customers = ["Rahim Traders"]
customers.extend(["Karim Store", "Jahid Enterprise"])
print(customers)

# Task 4
customers = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
customers.remove("Karim Store")
removed = customers.pop(0)
print(removed)
print(customers)

# Task 5
customers = ["Rahim Traders"]
new_customers = ["Karim Store", "Jahid Enterprise"]
customers.extend(new_customers)
print(customers)
"""
# Change the values and rerun. Lists become useful through safe updates.
