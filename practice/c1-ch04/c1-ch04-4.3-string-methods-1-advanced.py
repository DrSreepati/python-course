"""Subtopic 4.3: String methods 1.
Notes: notes/c1-ch04-4.3-string-methods-1-bangla.md
       notes/c1-ch04-4.3-string-methods-1-english.md
Solutions are at the bottom. Attempt each problem before reading them.
"""

# HINTS (read only if stuck)
# Problem 1: Standardise case first, then count the cleaned separator.
# Problem 2: strip() removes outer whitespace, while replace() changes text.
# Problem 3: Keep a comparison key and a display name as separate values.
# Problem 4: Apply the methods in the order that matches the desired format.
# Problem 5: Preserve the readable name while creating a separate report key.

# Problem 1 (Easy, LeetCode-style)
# Statement: Given one invoice reference with slashes and outer spaces,
# return its standard form using uppercase, strip and replace.
# Formal Input: " inv/2024/007 ".
# Output: "INV-2024-007".
# Constraints: the two separators are slashes.
invoice_1 = " inv/2024/007 "

# Problem 2 (Easy, interview-style)
# An interviewer asks: "Clean a customer name for display and count how many
# spaces it has before cleaning. Do not remove the internal word separator."
# Follow-up: "What changes if the name contains three words?"
customer_name_2 = "  Rahim Traders  "

# Problem 3 (Medium, real-world business)
# The boss receives two spellings of the same customer from separate forms.
# Create comparison keys and decide whether the records refer to one customer.
form_name_a = " Rahim TRADERS "
form_name_b = "rahim traders"

# Problem 4 (Medium, LeetCode-style)
# Statement: Given a payment note, change only its first "paid" label to
# "checked", then count the remaining word "paid".
# Formal Input: "paid paid pending".
# Output: "checked paid pending" and count 1.
# Constraints: replace only the first matching word.
payment_note_4 = "paid paid pending"

# Problem 5 (Hard, real-world business)
# The boss wants a small customer master summary. Keep readable display names,
# create comparison keys, count the letter "a" in each key, and print results.
# Use only the string methods taught in this subtopic.
customer_a = "  Rahim Traders  "
customer_b = "KARIM store"
customer_c = "  Jahid Enterprise "

# ===== SOLUTIONS (attempt first, then compare) =====
"""
# Problem 1 solution
# 1. Remove outer whitespace.
# 2. Make letters uppercase.
# 3. Replace every slash with a hyphen.
invoice_1 = " inv/2024/007 "
standard_invoice_1 = invoice_1.strip().upper().replace("/", "-")
print(standard_invoice_1)  # Expected: INV-2024-007
# The input has a fixed format, so this is O(1).

# Problem 2 solution
# 1. Count spaces in the raw name.
# 2. Remove only outer spaces for a readable display name.
# 3. Print both results.
customer_name_2 = "  Rahim Traders  "
raw_space_count_2 = customer_name_2.count(" ")
display_name_2 = customer_name_2.strip()
print(f"Raw spaces: {raw_space_count_2}")  # Expected: Raw spaces: 4
print(f"Display name: {display_name_2}")  # Expected: Display name: Rahim Traders
# The fixed string is scanned a constant number of times, so this is O(1).
# Interview talking point: I preserve the internal separator because it has
# meaning in a readable customer name.

# Problem 3 solution
# 1. Strip outer whitespace.
# 2. Lowercase both names.
# 3. Compare their standard keys.
form_name_a = " Rahim TRADERS "
form_name_b = "rahim traders"
key_a = form_name_a.strip().lower()
key_b = form_name_b.strip().lower()
print(f"Key A: {key_a}")  # Expected: Key A: rahim traders
print(f"Key B: {key_b}")  # Expected: Key B: rahim traders
print(f"Same customer: {key_a == key_b}")  # Expected: Same customer: True
# The work grows with the length of the two names, which is O(n).

# Problem 4 solution
# 1. Replace only the first "paid".
# 2. Count the word in the resulting note.
# 3. Print the updated note and count.
payment_note_4 = "paid paid pending"
checked_note_4 = payment_note_4.replace("paid", "checked", 1)
remaining_paid_4 = checked_note_4.count("paid")
print(checked_note_4)  # Expected: checked paid pending
print(remaining_paid_4)  # Expected: 1
# Both operations scan the note, so the work is O(n).

# Problem 5 solution
# 1. Keep each original name for readable reporting.
# 2. Build lowercase comparison keys after stripping outer spaces.
# 3. Count "a" in each key and print a compact summary.
customer_a = "  Rahim Traders  "
customer_b = "KARIM store"
customer_c = "  Jahid Enterprise "

display_a = customer_a.strip()
display_b = customer_b.strip()
display_c = customer_c.strip()
key_a = display_a.lower()
key_b = display_b.lower()
key_c = display_c.lower()

print(f"{display_a} | key: {key_a} | a-count: {key_a.count('a')}")
# Expected: Rahim Traders | key: rahim traders | a-count: 2
print(f"{display_b} | key: {key_b} | a-count: {key_b.count('a')}")
# Expected: KARIM store | key: karim store | a-count: 1
print(f"{display_c} | key: {key_c} | a-count: {key_c.count('a')}")
# Expected: Jahid Enterprise | key: jahid enterprise | a-count: 2
# Each name is processed a fixed number of times, so this is O(n).

# Interview talking point: I keep display text and comparison keys separate.
# This avoids losing readable business spelling while standardising searches.
"""
# Change the data and rerun. Real skill grows in the variations, not the copies.
