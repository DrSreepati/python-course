# কোর্স 1 → অধ্যায় 2 → উপবিষয় 2.1: ভেরিয়েবল

## Objective

এই পাঠের শেষে শিক্ষার্থী পারবে:

1. ভেরিয়েবলকে সহজ ভাষায় ব্যাখ্যা করতে।
2. একটি ভেরিয়েবল তৈরি করতে।
3. assignment কীভাবে কাজ করে তা বুঝতে।
4. ভেরিয়েবলের নামের বৈধ নিয়ম বলতে।
5. ব্যবসায়িক ডেটার জন্য অর্থপূর্ণ নাম বেছে নিতে।
6. পুরনো মান বদলে নতুন মান সংরক্ষণ করতে।

## Requirements

- Chapter 1: Python Environment, VS Code-এ Python ফাইল চালানো।

## How to read

আজকের নতুন ধারণা হলো ভেরিয়েবল, অর্থাৎ একটি নামফলকের অধীনে রাখা মান। সতর্কতা: `=` চিহ্ন এখানে “সমান” যাচাই করে না, এটি মান সংরক্ষণ করে। পাশে VS Code এবং Python চালানোর ব্যবস্থা রাখুন।

## Topic List

1. ভেরিয়েবল কী
2. নামফলকের উপমা
3. assignment
4. ভেরিয়েবল তৈরি
5. অর্থপূর্ণ নাম
6. বৈধ নামের নিয়ম
7. অবৈধ নাম
8. মান বদলানো
9. একাধিক assignment
10. ব্যবসায়িক রিপোর্টে প্রয়োগ

## 1. ভেরিয়েবল কী

ভেরিয়েবল হলো এমন একটি নাম, যার মাধ্যমে আমরা একটি মানকে পরে ব্যবহার করতে পারি। দোকানের হিসাবের খাতায় “আজকের বিক্রি” নামে একটি ঘর থাকে। Python-এ সেই ঘরটির নাম হতে পারে `daily_sales`।

```python
daily_sales = 12000
print(daily_sales)
```

**Output**

```text
12000
```

`daily_sales` হলো নাম। `12000` হলো রাখা মান। `print()` সেই মানটি দেখায়।

## 2. নামফলকের উপমা

নামফলকটি হলো ভেরিয়েবলের নাম, আর তার পেছনে রাখা বাক্সে থাকে মান। Python-এ নামফলকটি মানের সঙ্গে যুক্ত হয়। আমাদের ব্যবসার `report` তালিকার প্রতিটি হিসাবও পরে একটি নামের মাধ্যমে ব্যবহার করা যাবে।

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

`customer` নামটি লেখাটির দিকে ইঙ্গিত করছে। `balance` নামটি 50000-এর দিকে ইঙ্গিত করছে।

## 3. Assignment কী

Assignment মানে ডান পাশের মানটি বাম পাশের নামে সংরক্ষণ করা। পড়ার সুবিধার জন্য `balance = 50000`-কে বলা যায়, “balance-এ 50000 রাখো।” এটি গাণিতিক সমীকরণ নয়।

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

প্রথমে `unit_price` এবং `quantity` রাখা হয়েছে। পরে Python তাদের গুণ করে `amount`-এ রেখেছে।

## 4. একটি মান বদলানো

একই নামের সঙ্গে নতুন assignment করলে পুরনো মানটি বদলে যায়। এটি ব্যবসায়িক হিসাব আপডেট করার মতো।

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

প্রথম `print()` পুরনো মান দেখায়। দ্বিতীয় assignment-এর পরে একই নাম নতুন মান ধরে।

## 5. অর্থপূর্ণ নাম বাছাই

নামের মধ্যে কাজটি বোঝা উচিত। `x` চললেও `weekly_sales` অনেক পরিষ্কার। নাম সাধারণত ছোট হাতের অক্ষরে এবং একাধিক শব্দে underscore দিয়ে লেখা হয়।

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

`weekly_sales` দেখে বোঝা যায় এটি সপ্তাহের বিক্রির মান। `invoice_number` দেখে বোঝা যায় এটি চালান নম্বর।

## 6. নামের বৈধ নিয়ম

ভেরিয়েবলের নাম অক্ষর বা underscore দিয়ে শুরু হবে। পরে অক্ষর, সংখ্যা বা underscore থাকতে পারে। ফাঁকা স্থান চলবে না, এবং Python-এর reserved keyword ব্যবহার করা যাবে না।

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

`customer_1` সংখ্যাযুক্ত বৈধ নাম। `_internal_note` underscore দিয়ে শুরু হওয়ায় বৈধ।

## 7. অবৈধ নাম চিনে রাখা

`2nd_customer`, `customer name`, এবং `class` বৈধ ভেরিয়েবল নাম নয়। এগুলো ব্যবহার করলে Python syntax error দেখাবে। তাই নাম বানানোর আগে নিয়ম যাচাই করুন।

```python
customer_name = "Karim Store"
print(customer_name)
```

**Output**

```text
Karim Store
```

এখানে ফাঁকা স্থানের বদলে underscore ব্যবহার করা হয়েছে। `customer_name` তাই নিরাপদ নাম।

## 8. একই লাইনে একাধিক assignment

ছোট, একই ধরনের মান এক লাইনে রাখা যায়। তবে শিক্ষানবিশ অবস্থায় আলাদা লাইন বেশি পরিষ্কার।

```python
sales, cost = 50000, 38000
profit = sales - cost
print(profit)
```

**Output**

```text
12000
```

`sales`-এ 50000 এবং `cost`-এ 38000 রাখা হয়েছে। তারপর তাদের পার্থক্য `profit`-এ রাখা হয়েছে।

## 9. ব্যবসায়িক রিপোর্টে নাম ব্যবহার

একটি রিপোর্টের মানকে নাম দিলে একই মান বারবার লিখতে হয় না। পরে বসের রিপোর্টে পরিবর্তন দরকার হলে এক জায়গা বদলানো সহজ হয়।

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

প্রতিটি নাম রিপোর্টের একটি আলাদা ব্যবসায়িক তথ্য ধরে রেখেছে।

Run the practice file to confirm every output.

## Synthesis table

| কাজ | Python পদ্ধতি | উদাহরণ |
|---|---|---|
| মান রাখা | assignment | `sales = 50000` |
| মান দেখা | `print()` | `print(sales)` |
| মান বদলানো | নতুন assignment | `sales = 51000` |
| একাধিক শব্দের নাম | underscore | `daily_sales` |
| হিসাবের ফল রাখা | expression assignment | `profit = sales - cost` |

## Troubleshooting

### সমস্যা 1: `SyntaxError`

- কী হচ্ছে: Python বাক্যটি বুঝতে পারছে না।
- সম্ভাব্য কারণ: নামের মধ্যে ফাঁকা স্থান বা ভুল চিহ্ন আছে।
- ধাপে ধাপে সমাধান: নামটি দেখুন, ফাঁকা স্থান সরান, underscore দিন, আবার চালান।
- পরের বার প্রতিরোধ: `daily_sales`-এর মতো snake_case ব্যবহার করুন।

### সমস্যা 2: `NameError`

- কী হচ্ছে: Python এমন একটি নাম খুঁজছে যা তৈরি করা হয়নি।
- সম্ভাব্য কারণ: নামটি আগে assignment করা হয়নি বা বানান বদলে গেছে।
- ধাপে ধাপে সমাধান: নামের বানান মিলান, তার আগেই assignment দিন, আবার চালান।
- পরের বার প্রতিরোধ: নাম তৈরি করার পরে ব্যবহার করুন।

### সমস্যা 3: পুরনো মান দেখা যাচ্ছে

- কী হচ্ছে: রিপোর্টে প্রত্যাশিত নতুন সংখ্যা নেই।
- সম্ভাব্য কারণ: নতুন assignment-এর আগে `print()` করা হয়েছে।
- ধাপে ধাপে সমাধান: নতুন মানের assignment আগে আনুন, তারপর `print()` করুন।
- পরের বার প্রতিরোধ: সংরক্ষণ, হিসাব, তারপর output এই ক্রম রাখুন।

### সমস্যা 4: নাম বুঝতে অসুবিধা হচ্ছে

- কী হচ্ছে: কোড চলে, কিন্তু কাজ বোঝা কঠিন।
- সম্ভাব্য কারণ: `a`, `b`, `x`-এর মতো অস্পষ্ট নাম।
- ধাপে ধাপে সমাধান: কাজ বোঝায় এমন নাম দিন, যেমন `invoice_number`।
- পরের বার প্রতিরোধ: নামটি পড়ে ডেটার অর্থ অনুমান করা যায় কি না দেখুন।

## Common Misconceptions

1. ভুল দাবি: `=` মানে সমান যাচাই করা। → সত্য: `=` মান রাখে; তুলনা পরে আসবে।
2. ভুল দাবি: ভেরিয়েবলের নাম সংখ্যা দিয়ে শুরু করা যায়। → সত্য: সংখ্যা দিয়ে শুরু করা যায় না।
3. ভুল দাবি: নামের মধ্যে space ব্যবহার করা যায়। → সত্য: space-এর বদলে underscore ব্যবহার করুন।
4. ভুল দাবি: assignment করলে পুরনো মান দুটিই একই নামে থাকে। → সত্য: নতুন assignment নামটির বর্তমান মান বদলে দেয়।
5. ভুল দাবি: ছোট নাম সবসময় ভালো। → সত্য: অর্থপূর্ণ নাম সাধারণত বেশি নিরাপদ ও পাঠযোগ্য।

## Exercises

### Exercise 1

`product_name`-এ `"Rice"` এবং `stock_quantity`-তে `25` রাখুন, দুটো print করুন।

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

`unit_price = 120` এবং `quantity = 6` দিয়ে `total_amount` বের করুন।

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

`customer_balance = 71000` রাখুন। পরে 5000 জমা হলে নতুন balance রাখুন এবং print করুন।

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

`sales = 50000`, `cost = 38000` রেখে `profit` print করুন।

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

### Exercise 5: Rafiq bhai-এর debugging bug

Rafiq bhai লিখেছেন:

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

Bug species হলো variable name-এ space। Python সেটিকে একটি নাম হিসেবে পড়তে পারে না। underscore ব্যবহার করলে নামটি বৈধ হয়।

## Quiz

1. ভেরিয়েবল কী কাজ করে?  
   a) মানকে একটি নামে রাখে  
   b) শুধু error দেখায়  
   c) ফাইল মুছে দেয়  
   **উত্তর: a।** ভেরিয়েবল নামের মাধ্যমে মান ব্যবহার করা যায়।

2. কোনটি বৈধ নাম?  
   a) `2sales`  
   b) `sales total`  
   c) `sales_total`  
   **উত্তর: c।** এটি অক্ষর দিয়ে শুরু এবং underscore ব্যবহার করেছে।

3. `balance = 50000`-এ `=` কী করে?  
   a) তুলনা করে  
   b) মান সংরক্ষণ করে  
   c) মান print করে  
   **উত্তর: b।** ডান পাশের মান বাম পাশের নামে রাখা হয়।

4. `sales = 10`-এর পরে `sales = 15` হলে বর্তমান মান কত?  
   a) 10  
   b) 25  
   c) 15  
   **উত্তর: c।** নতুন assignment বর্তমান মান বদলে দেয়।

5. কোনটি ব্যবসায়িকভাবে পরিষ্কার নাম?  
   a) `x`  
   b) `invoice_number`  
   c) `q`  
   **উত্তর: b।** নামটি ডেটার অর্থ স্পষ্ট করে।

6. কোনটি ভুল?  
   a) `_note`  
   b) `customer_1`  
   c) `1_customer`  
   **উত্তর: c।** ভেরিয়েবলের নাম সংখ্যা দিয়ে শুরু করা যায় না।

7. `profit = sales - cost`-এর ফল কোথায় থাকে?  
   a) `cost`-এ  
   b) `profit`-এ  
   c) `sales`-এ  
   **উত্তর: b।** হিসাবের ফল `profit` নামের সঙ্গে রাখা হয়।

## Key Idea

ভেরিয়েবল হলো ব্যবসায়িক ডেটার জন্য অর্থপূর্ণ নামফলক। Assignment দিয়ে মান রাখি, আর নতুন assignment দিয়ে বর্তমান মান বদলাই।

**ছড়া 1:** নামফলকে নাম, বাক্সে মান,  
হিসাব রাখে Python প্রাণ।

**ছড়া 2:** underscore দাও, space নয়,  
পরিষ্কার নামেই ভুল কম হয়।

## Next Step

পরের উপবিষয় 2.2-এ `int`, `float`, `str`, এবং `bool` দেখব। আজ আমরা মানকে নামে রেখেছি, পরের ধাপে জানব সেই মানের ধরন কী। Seed question: `12000`, `"Rahim Traders"`, এবং `True` কি একই ধরনের মান?

Next: 2.2 Core types: int, float, str, bool. Type next (or এগো) for the next step.
