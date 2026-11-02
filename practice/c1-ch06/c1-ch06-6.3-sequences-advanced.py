"""Subtopic 6.3: for over sequences.
Notes: notes/c1-ch06-6.3-sequences-bangla.md
       notes/c1-ch06-6.3-sequences-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: loop directly over the reference string.
# Problem 2: add each list amount to an accumulator.
# Problem 3: test each customer balance inside the loop.
# Problem 4: use a second accumulator for qualifying sales.
# Problem 5: process the fixed sequences in their original order.

# Problem 1 (Easy, LeetCode-style)
# Print each character in the invoice code "INV-2024-007".
# Formal Input: one string.
# Output: one character per line.
invoice_code_1 = "INV-2024-007"

# Problem 2 (Easy, interview-style)
# Calculate total weekly takings from the fixed business sequence.
# Follow-up: how would you verify the total without code?
weekly_takings_2 = [5000, 4200, 6100, 3800, 5500, 4700, 5700]

# Problem 3 (Medium, real-world business)
# Classify three customer balances as High or Regular.
customer_balances_3 = [50000, 32000, 71000]

# Problem 4 (Medium, interview-style)
# Add only sales of 10000 or more from the daily report.
# Follow-up: why must the accumulator start before the loop?
sales_4 = [12000, 9500, 8800, 13200, 7500]

# Problem 5 (Hard, real-world business)
# Produce a small report from customer names and balances. Print each name,
# classify its balance, and calculate the combined balance.
customer_names_5 = ["Rahim Traders", "Karim Store", "Jahid Enterprise"]
customer_balances_5 = [50000, 32000, 71000]

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# Approach:
# 1. Take one character from the invoice code.
# 2. Print the current character.
# 3. Continue in string order.
for character in invoice_code_1:
    print(character)
# Expected:
# I
# N
# V
# -
# 2
# 0
# 2
# 4
# -
# 0
# 0
# 7
# Complexity: one pass per character, O(n).

# Problem 2 solution
# Approach:
# 1. Start the total at zero.
# 2. Add each taking.
# 3. Print the final total.
total_2 = 0
for taking in weekly_takings_2:
    total_2 += taking
print(total_2)
# Expected: 35000
# Complexity: one pass per item, O(n).
# Interview talking point: the accumulator preserves all earlier values.

# Problem 3 solution
# Approach:
# 1. Read each balance.
# 2. Compare it with the 50000 threshold.
# 3. Print the matching label.
for balance in customer_balances_3:
    if balance >= 50000:
        print(f"High balance: {balance}")
    else:
        print(f"Regular balance: {balance}")
# Expected:
# High balance: 50000
# Regular balance: 32000
# High balance: 71000
# Complexity: one decision per balance, O(n).

# Problem 4 solution
# Approach:
# 1. Start a qualifying total at zero.
# 2. Test each daily sale.
# 3. Add only values at least 10000.
qualifying_total_4 = 0
for sale in sales_4:
    if sale >= 10000:
        qualifying_total_4 += sale
print(qualifying_total_4)
# Expected: 25200
# Complexity: one pass through sales, O(n).
# Interview talking point: filter first, then accumulate.

# Problem 5 solution
# Approach:
# 1. Use the same position in both fixed sequences.
# 2. Classify each balance.
# 3. Add every balance to the combined total.
combined_balance_5 = 0
position_5 = 0
for name in customer_names_5:
    balance = customer_balances_5[position_5]
    if balance >= 50000:
        label = "High"
    else:
        label = "Regular"
    print(f"{name}: {label}, {balance}")
    combined_balance_5 += balance
    position_5 += 1
print(f"Combined balance: {combined_balance_5}")
# Expected:
# Rahim Traders: High, 50000
# Karim Store: Regular, 32000
# Jahid Enterprise: High, 71000
# Combined balance: 153000
# Complexity: one pass through names, O(n).
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
