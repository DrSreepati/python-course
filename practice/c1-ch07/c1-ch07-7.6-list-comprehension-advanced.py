"""Subtopic 7.6: List comprehension.
Notes: notes/c1-ch07-7.6-list-comprehension-bangla.md
       notes/c1-ch07-7.6-list-comprehension-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Put the transformation before the for part.
# Problem 2: Put the selection condition at the end.
# Problem 3: Build a formatted string for each indexed sale.
# Problem 4: Use an if-else expression to label every balance.
# Problem 5: Use two comprehensions, one for each business report.

# Problem 1 (Easy, LeetCode-style)
# Given a list of invoice amounts, return each amount after a fixed 5% service charge.
# Input: a list of numbers. Output: a new list of adjusted amounts.
invoice_amounts_1 = [1000, 2500, 4000]

# Problem 2 (Easy, real-world business)
# The boss wants only daily sales that reached the target of 10,000.
daily_sales_2 = [12000, 9500, 8800, 13200, 7500]

# Problem 3 (Medium, interview-style)
# Create one-based day labels for every weekly taking.
# Follow-up: how would you keep only labels above 5,000?
weekly_takings_3 = [5000, 4200, 6100, 3800, 5500, 4700, 5700]

# Problem 4 (Medium, real-world business)
# Label each customer balance as "Review" at 50,000 or above, otherwise "Normal".
customer_names_4 = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
customer_balances_4 = [50000, 32000, 71000]

# Problem 5 (Hard, real-world business)
# Build two management lists from the same sales report:
# one list of high-sale day labels and one list of low-sale follow-up labels.
management_sales_5 = [12000, 9500, 8800, 13200, 7500]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Read each invoice amount.
# 2. Multiply by 1.05.
# 3. Store the adjusted amount in a new list.
adjusted_1 = [amount * 1.05 for amount in invoice_amounts_1]
print(adjusted_1)
# Expected: [1050.0, 2625.0, 4200.0]
# The expression changes each item. One pass is O(n).
# Key line: the expression is evaluated once for every amount.
# Complexity: work grows with the number of invoices, O(n).

# Problem 2 solution
# Approach:
# 1. Check every daily sale.
# 2. Keep values at or above the target.
# 3. Print the selected report.
target_sales_2 = [sale for sale in daily_sales_2 if sale >= 10000]
print(target_sales_2)
# Expected: [12000, 13200]
# Key line: the final if is a filter, not a transformation.
# Complexity: every sale is checked once, O(n).

# Problem 3 solution
# Approach:
# 1. Enumerate weekly takings from one.
# 2. Build a readable string for each pair.
# 3. Keep the strings in a new list.
labels_3 = [
    f"Day {day}: Tk {amount}"
    for day, amount in enumerate(weekly_takings_3, start=1)
]
print(labels_3)
# Expected:
# ['Day 1: Tk 5000', 'Day 2: Tk 4200', 'Day 3: Tk 6100',
#  'Day 4: Tk 3800', 'Day 5: Tk 5500', 'Day 6: Tk 4700',
#  'Day 7: Tk 5700']
# Key line: enumerate supplies the report label and the value.
# Complexity: one scan of the week, O(n).
# Interview talking point: keep display numbering one-based and storage access zero-based.

# Problem 4 solution
# Approach:
# 1. Pair names and balances by index.
# 2. Select the correct label with if-else.
# 3. Build a complete customer status line.
status_4 = [
    f"{customer}: {'Review' if balance >= 50000 else 'Normal'}"
    for customer, balance in zip(customer_names_4, customer_balances_4)
]
print(status_4)
# Expected: ['Rahim Traders: Review', 'Karim Store: Normal',
# 'Jahid Enterprise: Review']
# Key line: the if-else expression labels every pair.
# Complexity: one pass through the aligned data, O(n).

# Problem 5 solution
# Approach:
# 1. Enumerate every sale with a business day number.
# 2. Build a high-sale label only when the target is met.
# 3. Build a separate follow-up label for smaller sales.
# 4. Print both management lists.
high_days_5 = [
    f"Day {day}: high sale {sale}"
    for day, sale in enumerate(management_sales_5, start=1)
    if sale >= 10000
]
follow_up_5 = [
    f"Day {day}: follow up {sale}"
    for day, sale in enumerate(management_sales_5, start=1)
    if sale < 10000
]
print(high_days_5)
print(follow_up_5)
# Expected:
# ['Day 1: high sale 12000', 'Day 4: high sale 13200']
# ['Day 2: follow up 9500', 'Day 3: follow up 8800',
#  'Day 5: follow up 7500']
# Key lines: each comprehension has one clear business purpose.
# Complexity: the report is scanned twice, so it is O(n), with two passes.
# Business talking point: separate outputs are clearer than one complicated expression.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
