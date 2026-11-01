# স্টার্টার PROGRESS.md


# Course Progress (maintained by the tutor, updated after every subtopic)

## Delivered subtopics

Course 1, Chapter 1 (Python Environment) is skipped: the learner already works inside VS Code with Python running. The series starts at Chapter 2.

- [x] 2.1 Variables: creation, naming rules, assignment (files: c1-ch02-2.1-variables-bangla.md, c1-ch02-2.1-variables-english.md, c1-ch02-2.1-variables.py)
- [x] 2.2 Core types: int, float, str, bool (files: c1-ch02-2.2-core-types-bangla.md, c1-ch02-2.2-core-types-english.md, c1-ch02-2.2-core-types.py)
- [x] 2.3 None: what it means and why it is not zero (files: c1-ch02-2.3-none-bangla.md, c1-ch02-2.3-none-english.md, c1-ch02-2.3-none.py)
- [x] 2.4 type() and input(); reading user data (files: c1-ch02-2.4-type-input-bangla.md, c1-ch02-2.4-type-input-english.md, c1-ch02-2.4-type-input.py)
- [x] 2.5 Type casting: int(), float(), str() (files: c1-ch02-2.5-type-casting-bangla.md, c1-ch02-2.5-type-casting-english.md, c1-ch02-2.5-type-casting.py)
- [x] 2.6 Money as data: the float problem (0.1 + 0.2 surprise) (files: c1-ch02-2.6-money-float-bangla.md, c1-ch02-2.6-money-float-english.md, c1-ch02-2.6-money-float.py)
- [x] 2.7 Business data examples: percentage, quantity, unit price, amount; dates (files: c1-ch02-2.7-business-data-bangla.md, c1-ch02-2.7-business-data-english.md, c1-ch02-2.7-business-data.py)

(Later chapters are appended here as the series reaches them, from SYLLABUS.md.)

- [x] 3.1 Arithmetic operators: +, -, *, /, //, %, ** (files: c1-ch03-3.1-arithmetic-operators-bangla.md, c1-ch03-3.1-arithmetic-operators-english.md, c1-ch03-3.1-arithmetic-operators.py)
- [x] 3.2 Comparison and logical operators: ==, !=, >, <, >=, <=, and, or, not (files: c1-ch03-3.2-comparison-logical-operators-bangla.md, c1-ch03-3.2-comparison-logical-operators-english.md, c1-ch03-3.2-comparison-logical-operators.py)

## Quiz keys used (never repeat the previous note's full answer pattern)

- 2.1: a c b c b c b
- 2.2: b a c b a c b
- 2.3: a b c b a c b
- 2.4: c a b c a b c
- 2.5: b c a b c a b
- 2.6: a c b a c b a
- 2.7: b a c b a c b
- 3.1: c b a c b a c
- 3.2: a b c b a c a

## Rafiq bhai bug log (one new bug species per note; no species repeats)

- 2.1: variable name contains a space, causing a syntax error
- 2.2: Boolean value written with incorrect capitalisation (`true` instead of `True`)
- 2.3: unknown balance replaced with zero using `balance or 0`
- 2.4: input value used as a number without conversion, causing a TypeError
- 2.5: word passed to int(), causing a ValueError
- 2.6: exact float equality used for money comparison
- 2.7: unit price divided by quantity instead of multiplying, producing a silent wrong amount
- 3.1: floor division used for an average, silently dropping decimal precision
- 3.2: strict greater-than used instead of greater-than-or-equal at a discount boundary

## Story state

- Business world: a small wholesale trading business in Dhaka. People: the boss (asks for reports), Rahim (sales assistant), Rafiq bhai (senior accountant, writes the bugs).
- Datasets agreed so far: report = [12000, 9500, 8800, 13200, 7500] (days 1-5); week = [5000, 4200, 6100, 3800, 5500, 4700, 5700]; customers: "Rahim Traders" 50000, "Karim Store" 32000, "Jahid Enterprise" 71000; codes: "C-1023", "INV-2024-007". New values are introduced only when a topic demands, and stay in the story afterwards.
- Story threads in play: mala (garland) = list, puti (bead) = element, doroan (doorkeeper) = loop/condition, dal-palla (scales) = accumulator, guntaraj (abacus) = counter, ghor-bari (house) = indentation, namfok (name plate) = variable name, ason (seat) = index.
- Open thread for the Next Step seed of 2.1: Are 12000, "Rahim Traders", and True the same type? This leads to 2.2.
- Open thread for the Next Step seed of 2.2: If a customer's balance is unknown, should it be written as 0? This leads to 2.3.
- Open thread for the Next Step seed of 2.3: If a user leaves a field blank, what type of value does Python read? This leads to 2.4.
- Open thread for the Next Step seed of 2.4: How can `"6"` become a real integer quantity? This leads to 2.5.
- Open thread for the Next Step seed of 2.5: Why can two small decimal values produce a surprising result? This leads to 2.6.
- Open thread for the Next Step seed of 2.6: Should quantity, price, percentage, and date all use the same type? This leads to 2.7.
- Open thread for the Next Step seed of 2.7: How can Python decide whether a sale made a profit? This leads to 3.1.
- Open thread for the Next Step seed of 3.1: How can Python decide whether a customer's order deserves a discount? This leads to 3.2.
- Open thread for the Next Step seed of 3.2: How can sales, cost and profit produce a margin percentage? This leads to 3.3.