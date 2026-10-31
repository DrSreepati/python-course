# Course 1 -> Chapter 2 -> Subtopic 2.1: Variables

## Objective

By the end of this lecture the student will be able to:

1. Explain a variable in simple words.
2. Create a variable.
3. Explain how assignment works.
4. State the valid naming rules.
5. Choose clear names for business data.
6. Replace an old value with a new value.

## Requirements

- Chapter 1: Python Environment, running Python files in VS Code.

## How to read

Today’s new idea is a variable, a named place for a value. Watch this trap: `=` stores a value here. It does not test equality. Keep VS Code and a working Python setup nearby.

## Topic List

1. What a variable is
2. The name-plate analogy
3. Assignment
4. Creating variables
5. Clear names
6. Valid naming rules
7. Invalid names
8. Replacing a value
9. Multiple assignments
10. Using names in a business report

## 1. What a variable is

A variable is a name that lets us use a value later. A shop ledger has a space called “today’s sales”. In Python, that space can be called `daily_sales`.

```python
daily_sales = 12000
print(daily_sales)
```

**Output**

```text
12000
```

`daily_sales` is the name. `12000` is the stored value. `print()` displays it.

## 2. The name-plate analogy

The name plate is the variable name. The value is behind it. In our business, a name lets us reuse a figure without typing it again.

```python
customer = "Rahim Traders"
balance = 50000
print(customer)
print(balance)
```

**Output**

```text
Rahim Traders
50000
```

`customer` points to the text. `balance` points to 50000.

## 3. What assignment means

Assignment stores the right-hand value under the left-hand name. Read `balance = 50000` as, “put 50000 into balance”. It is not a mathematical equation.

```python
unit_price = 250
quantity = 4
amount = unit_price * quantity
print(amount)
```

**Output**

```text
1000
```

Python stores the price and quantity first. It then stores their product in `amount`.

## 4. Replacing a value

A new assignment under the same name replaces the current value. This is like updating a business record.

```python
pending_amount = 32000
print(pending_amount)

pending_amount = 28000
print(pending_amount)
```

**Output**

```text
32000
28000
```

The first `print()` shows the old value. The second assignment gives the name a new value.

## 5. Choosing clear names

A name should show its job. `weekly_sales` is clearer than `x`. Use lowercase words joined by underscores.

```python
weekly_sales = 35000
invoice_number = "INV-2024-007"
print(weekly_sales)
print(invoice_number)
```

**Output**

```text
35000
INV-2024-007
```

`weekly_sales` explains the figure. `invoice_number` explains the text.

## 6. Valid naming rules

A variable name starts with a letter or underscore. It may then contain letters, numbers, and underscores. It cannot contain spaces or be a Python keyword.

```python
customer_1 = "Rahim Traders"
_internal_note = "Check later"
print(customer_1)
print(_internal_note)
```

**Output**

```text
Rahim Traders
Check later
```

`customer_1` contains a number after its first character. `_internal_note` starts with an underscore. Both are valid.

## 7. Recognising invalid names

`2nd_customer`, `customer name`, and `class` are not valid variable names. Python will report a syntax error. Check the rules before writing a name.

```python
customer_name = "Karim Store"
print(customer_name)
```

**Output**

```text
Karim Store
```

The space has become an underscore. Therefore, `customer_name` is valid.

## 8. Several assignments on one line

Small related values can share one line. Separate lines are often clearer for beginners.

```python
sales, cost = 50000, 38000
profit = sales - cost
print(profit)
```

**Output**

```text
12000
```

Python stores 50000 in `sales` and 38000 in `cost`. It then stores the difference in `profit`.

## 9. Names in a business report

Naming report values avoids repeated typing. If the boss requests a change, one assignment is easier to update.

```python
report_total = 51000
best_day_sales = 13200
slowest_day_sales = 7500

print("Total:", report_total)
print("Best day:", best_day_sales)
print("Slowest day:", slowest_day_sales)
```

**Output**

```text
Total: 51000
Best day: 13200
Slowest day: 7500
```

Each name stores one useful business fact.

Run the practice file to confirm every output.

## Synthesis table

| Job | Python method | Example |
|---|---|---|
| Store a value | assignment | `sales = 50000` |
| See a value | `print()` | `print(sales)` |
| Replace a value | new assignment | `sales = 51000` |
| Name several words | underscore | `daily_sales` |
| Store a result | expression assignment | `profit = sales - cost` |

## Troubleshooting

### Problem 1: `SyntaxError`

- What is happening: Python cannot understand the statement.
- Most likely cause: the name contains a space or invalid symbol.
- Step-by-step fix: inspect the name, remove the space, add an underscore, and run again.
- Prevent it next time: use snake_case, such as `daily_sales`.

### Problem 2: `NameError`

- What is happening: Python cannot find a name.
- Most likely cause: the name was not assigned first, or its spelling changed.
- Step-by-step fix: compare the spelling, assign the name first, and run again.
- Prevent it next time: create a name before using it.

### Problem 3: The old value appears

- What is happening: the report does not show the expected new figure.
- Most likely cause: `print()` runs before the new assignment.
- Step-by-step fix: put the new assignment first, then print the value.
- Prevent it next time: keep the order store, calculate, output.

### Problem 4: The names are hard to understand

- What is happening: the code runs, but its purpose is unclear.
- Most likely cause: names such as `a`, `b`, or `x`.
- Step-by-step fix: choose a name that describes the data, such as `invoice_number`.
- Prevent it next time: read the name and check whether it explains the data.

## Common Misconceptions

1. Wrong claim: `=` tests equality. -> Truth: `=` stores a value here.
2. Wrong claim: a variable name may start with a number. -> Truth: it may not.
3. Wrong claim: a name may contain spaces. -> Truth: use underscores instead.
4. Wrong claim: both old and new values remain under one name. -> Truth: the new assignment becomes the current value.
5. Wrong claim: a short name is always best. -> Truth: a clear name is usually safer and easier to read.

## Exercises

### Exercise 1

Store `"Rice"` in `product_name` and `25` in `stock_quantity`. Print both.

**Solution**

```python
product_name = "Rice"
stock_quantity = 25
print(product_name)
print(stock_quantity)
```

**Output**

```text
Rice
25
```

### Exercise 2

Use `unit_price = 120` and `quantity = 6` to find `total_amount`.

**Solution**

```python
unit_price = 120
quantity = 6
total_amount = unit_price * quantity
print(total_amount)
```

**Output**

```text
720
```

### Exercise 3

Store `customer_balance = 71000`. After a payment of 5000, store and print the new balance.

**Solution**

```python
customer_balance = 71000
customer_balance = customer_balance - 5000
print(customer_balance)
```

**Output**

```text
66000
```

### Exercise 4

Store `sales = 50000` and `cost = 38000`. Print `profit`.

**Solution**

```python
sales = 50000
cost = 38000
profit = sales - cost
print(profit)
```

**Output**

```text
12000
```

### Exercise 5: Rafiq bhai’s debugging bug

Rafiq bhai wrote:

```python
invoice number = "INV-2024-007"
print(invoice number)
```

**Solution**

```python
invoice_number = "INV-2024-007"
print(invoice_number)
```

**Output**

```text
INV-2024-007
```

The bug species is a space inside a variable name. Python cannot read it as one name. An underscore makes it valid.

## Quiz

1. What does a variable do?  
   a) It stores a value under a name  
   b) It only shows errors  
   c) It deletes files  
   **Answer: a.** A variable lets us use a value through its name.

2. Which is a valid name?  
   a) `2sales`  
   b) `sales total`  
   c) `sales_total`  
   **Answer: c.** It starts correctly and uses an underscore.

3. What does `=` do in `balance = 50000`?  
   a) It compares values  
   b) It stores a value  
   c) It prints a value  
   **Answer: b.** The right-hand value is stored under the left-hand name.

4. After `sales = 10` and `sales = 15`, what is current?  
   a) 10  
   b) 25  
   c) 15  
   **Answer: c.** The later assignment replaces the current value.

5. Which name is clearest for business data?  
   a) `x`  
   b) `invoice_number`  
   c) `q`  
   **Answer: b.** It explains the data.

6. Which is invalid?  
   a) `_note`  
   b) `customer_1`  
   c) `1_customer`  
   **Answer: c.** A variable name cannot start with a number.

7. Where does `profit = sales - cost` store its result?  
   a) `cost`  
   b) `profit`  
   c) `sales`  
   **Answer: b.** The result is stored in `profit`.

## Key Idea

A variable is a clear name plate for business data. Assignment stores a value. A later assignment replaces the current value.

**Rhyme 1:** A name plate names, a box holds the store,  
Python keeps the figures ready at the door.

**Rhyme 2:** Use underscores, never spaces in sight,  
Clear names keep the ledger right.

## Next Step

Subtopic 2.2 covers `int`, `float`, `str`, and `bool`. Today we gave values names. Next, we will identify their types. Seed question: are `12000`, `"Rahim Traders"`, and `True` the same type?

Next: 2.2 Core types: int, float, str, bool. Type next (or এগো) for the next step.
