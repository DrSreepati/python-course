
---

# Python Course Plan v2 — Basic, Intermediate & Advanced

Purpose of this document: The complete, updated syllabus for three courses. Every chapter is divided into numbered subtopics. Each subtopic becomes one lecture sheet later (same format as the List and Slicing lectures).

What changed in v2 (based on Rajpati's approved proposal):

- The whole track now points toward Business Intelligence, Accounting, Automation & Data Analytics.
- SQL starts in Intermediate and becomes a major chapter in Advanced.
- Excel Automation, Accounting Analytics, AR/AP Analytics, Reconciliation, Financial Reporting, BI Fundamentals, Power BI + DAX, ETL Pipelines, KPI Analytics are new major modules.
- ML is reduced to a foundation — this is not an ML Engineer course.
- Metaprogramming/descriptors/concurrency are minimized; Flask becomes an optional track.
- Progression: Python Fundamentals → Professional Python → Excel/CSV/Pandas → Cleaning & Transformation → SQL → Accounting Data Analysis → Excel Automation → Reconciliation & Financial Reporting → ETL → BI & Data Modeling → Power BI → KPI Analytics → Streamlit/Reporting → Portfolio.

## Course Map

| Course | Chapters | Lecture Sheets | Duration | Target Skill |
| --- | --- | --- | --- | --- |
| 1. Basic Python | 12 | ~55 | 3 months | Programming foundations + business-flavored practice |
| 2. Intermediate Python (Data + Business Automation Track) | 14 | ~60 | 4 months | Professional Python, files/Excel/CSV, Pandas, SQL foundations |
| 3. Advanced Python for BI, Accounting, Automation & Analytics | 18 | ~90 | 6 months | Industry-grade BI/accounting/automation work + 3-project portfolio |

Every chapter ends with exercises + quiz. Every course ends with a capstone (Course 3 ends with three portfolio projects).

## Course 1: Basic Python

Goal: From zero to writing small real programs, with business-flavored examples from day one.

### Chapter 1: Python Environment [7 lecture sheets]

- 1.1 What is programming and why it matters — primary concepts
- 1.2 Python: history, features, and where it is used
- 1.3 Installing Python on Windows — click-by-click (PATH setup)
- 1.4 VS Code: install, extensions, running the first script
- 1.5 Jupyter Notebook / JupyterLab — what it is, when to use it
- 1.6 .py vs .ipynb — script vs notebook mindset
- 1.7 pip and the basic idea of a virtual environment (why real projects need one)

### Chapter 2: Variables & Business Data Types [7 lecture sheets]

- 2.1 Variables: creation, naming rules, assignment
- 2.2 Core types: int, float, str, bool
- 2.3 None — what it means and why it is not zero
- 2.4 type() and input(); reading user data
- 2.5 Type casting: int(), float(), str()
- 2.6 Money as data: why monetary values deserve care; intro to the float problem (0.1 + 0.2 surprise)
- 2.7 Business data examples: percentage, quantity, unit price, amount — and why a date is not just a string

### Chapter 3: Operators with Business Math [5 lecture sheets]

- 3.1 Arithmetic operators (+, -, *, /, //, %, **)
- 3.2 Comparison and logical operators
- 3.3 Business formulas as code: Sales = Quantity × Unit Price; Profit = Sales – Cost; Margin % = Profit / Sales × 100
- 3.4 VAT/tax calculations and discount calculations
- 3.5 Assignment & bitwise (brief) + operator precedence in business formulas

### Chapter 4: Strings [7 lecture sheets]

- 4.1 Creating strings, indexing, negative indexing
- 4.2 Slicing [start:stop:step] — the full lecture
- 4.3 String methods 1: lower/upper/strip/replace/count
- 4.4 String methods 2: split, join, find, startswith/endswith
- 4.5 Immutability — building new strings
- 4.6 Cleaning dirty text: extra spaces, mixed case, stray symbols
- 4.7 Practice: invoice/reference number parsing; customer & product code extraction (e.g., "C-1023", "INV-2024-007")

### Chapter 5: Conditional Logic — Business Decisions [5 lecture sheets]

- 5.1 if, and the indentation block
- 5.2 if-else and if-elif-else
- 5.3 Nested if
- 5.4 Compound conditions in real rules
- 5.5 Practice: discount eligibility, overdue status, budget variance, profit/loss classification, payment-status classification

### Chapter 6: Loops — Processing Many Records [6 lecture sheets]

- 6.1 while loop and the loop variable
- 6.2 for loop and range()
- 6.3 for over sequences (string/list)
- 6.4 break, continue, pass
- 6.5 Nested loops
- 6.6 Practice: transaction processing, invoice total, running balance, monthly expense summary

### Chapter 7: Lists [8 lecture sheets]

- 7.1 Creating, indexing, slicing (the List lecture is the base)
- 7.2 Adding/removing: append, insert, extend, remove, pop, del
- 7.3 sort, reverse, sorted, min/max/sum/len
- 7.4 Nested lists (tables/matrices)
- 7.5 Loops and enumerate on lists
- 7.6 List comprehension (basic)
- 7.7 Copy vs reference — aliasing, b = a, why one change hits both
- 7.8 Shallow copy (a[:], a.copy()), copying nested lists, mutable vs immutable summary

### Chapter 8: Tuple & Set [5 lecture sheets]

- 8.1 Tuple: creation, indexing, slicing, immutability
- 8.2 Tuple unpacking; tuple vs list — when to use which
- 8.3 Set: creation, uniqueness, add/remove
- 8.4 Set operations: union, intersection, difference
- 8.5 Practical uses: duplicate invoice detection concept, unique customer/product IDs, category comparison

### Chapter 9: Dictionary — Business Records [6 lecture sheets]

- 9.1 Key-value idea with a real analogy
- 9.2 Creating, accessing, adding, changing, deleting
- 9.3 keys(), values(), items() and looping
- 9.4 get(), in, nested dictionaries
- 9.5 Dictionary comprehension (basic)
- 9.6 Business records as dictionaries:

```python
invoice = {
    "invoice_no": "INV-001",
    "customer": "ABC Ltd",
    "sales": 50000,
    "vat": 7500
}
```

Plus practice: phone book, result sheet, word counter.

### Chapter 10: Functions [7 lecture sheets]

- 10.1 What a function is and why — code reuse
- 10.2 def, calling, return
- 10.3 Parameters vs arguments
- 10.4 Default values and keyword arguments
- 10.5 Local vs global scope
- 10.6 Reusable business functions: validation functions (is_valid_invoice_no), calculation functions (vat_amount, net_payable), reporting functions (print_invoice_summary)
- 10.7 Practice: grade function, tax calculator, prime checker

### Chapter 11: Modules [5 lecture sheets]

- 11.1 import and the idea of the standard library
- 11.2 math and random
- 11.3 datetime and date arithmetic
- 11.4 decimal — Decimal for money: why 0.1 + 0.2 ≠ 0.3 and how Decimal fixes financial math
- 11.5 statistics module + pathlib introduction; making your own module; pip recap

### Chapter 12: Files & Basic Capstone [7 lecture sheets]

- 12.1 Reading/writing text files ('r', 'w', 'a')
- 12.2 The with statement
- 12.3 Line-by-line processing
- 12.4 CSV introduction + the encoding idea (utf-8) + file paths (absolute vs relative)
- 12.5 try-except (introduction only)
- 12.6 Capstone: Student Result Manager (names, marks, grades, file save, report)
- 12.7 Optional second project: Personal Expense & Budget Tracker (category totals, monthly summary, CSV storage)

## Course 2: Intermediate Python — Data + Business Automation Track

Goal: Professional Python with a clear direction: files, CSV/JSON/Excel, Pandas, cleaning, transformation, dates, visualization, and SQL foundations. This course is the direct foundation for Advanced BI.

### Chapter 1: Professional Functions [6 lecture sheets]

- 1.1 *args and **kwargs
- 1.2 Lambda, map, filter
- 1.3 Scope deep-dive; closures introduction
- 1.4 Type hints and docstrings — professional style
- 1.5 Reusable calculation functions (margin, vat, discount — as a small business toolkit)
- 1.6 Modular programming: splitting a program into modules

### Chapter 2: Data Validation & Text Processing [6 lecture sheets]

- 2.1 Advanced string formatting (%, .format(), full f-string power)
- 2.2 Project-style string methods (word counting, CSV-line parsing)
- 2.3 Regex 1: re module, findall, search, basic patterns
- 2.4 Regex 2: groups, quantifiers, real patterns (phone, email, dates, invoice IDs)
- 2.5 Unicode & Bangla text processing (practical notes)
- 2.6 Validation in practice: ID/invoice/date parsing, messy accounting text cleaning

### Chapter 3: Professional Data Structures [6 lecture sheets]

- 3.1 Comprehension mastery (list/dict/set + conditions + nesting)
- 3.2 Generator expressions and memory efficiency
- 3.3 collections: Counter, defaultdict, deque
- 3.4 namedtuple and nested business records (order → line items)
- 3.5 Choosing the right structure — a decision guide
- 3.6 Mutable/immutable, hashability, and the cost of each structure

### Chapter 4: Exception Handling & Logging Foundations [5 lecture sheets]

- 4.1 try/except/else/finally — the full picture
- 4.2 Knowing the common exception types
- 4.3 raise and custom exceptions
- 4.4 Practical validation loops, missing files, data import errors
- 4.5 Logging introduction: logging module basics (levels, basicConfig) — print's professional replacement

### Chapter 5: OOP for Business Applications [6 lecture sheets]

- 5.1 Class/object concept — less theory, more modeling
- 5.2 __init__, self, attributes
- 5.3 Methods; instance vs class variables; __str__
- 5.4 Modeling practice: Customer, Product
- 5.5 Modeling practice: Invoice, Transaction (with line items)
- 5.6 Modeling practice: Account, Employee; inheritance where it genuinely helps

### Chapter 6: File & Folder Automation [5 lecture sheets]

- 6.1 pathlib — modern path handling
- 6.2 os and shutil — copy, move, delete safely
- 6.3 glob — finding files by pattern
- 6.4 Bulk operations: batch rename, folder structures
- 6.5 Archive workflow (zip) + safety rules (never delete without checking)

### Chapter 7: CSV, JSON & Excel [7 lecture sheets]

- 7.1 CSV deep-dive with the csv module (reader/writer, DictReader)
- 7.2 JSON: json module, data ↔ Python objects, nested JSON
- 7.3 Excel concepts: workbooks, worksheets, cells/ranges
- 7.4 openpyxl 1: reading and writing cells and sheets
- 7.5 openpyxl 2: formulas and multiple sheets
- 7.6 Number formats and basic formatting
- 7.7 Business reporting: building a small Excel report from Python; CSV ↔ Excel ↔ JSON conversion

### Chapter 8: NumPy for Analysis [4 lecture sheets]

- 8.1 Why NumPy: limits of lists, power of arrays
- 8.2 ndarray creation: array, arange, zeros, ones, linspace
- 8.3 Indexing, slicing, broadcasting (connecting to the Slicing lecture)
- 8.4 Vector operations and statistics functions on business data (mean, std, sum, max) — only the NumPy that analysis needs, no heavy math

### Chapter 9: Pandas Fundamentals [6 lecture sheets]

- 9.1 Why Pandas; Series and DataFrame
- 9.2 Reading CSV and Excel (read_csv, read_excel) + common read options
- 9.3 Inspecting: head, tail, info, describe, shape, dtypes
- 9.4 Selecting columns, filtering rows, sorting
- 9.5 Calculated columns and datatype conversion
- 9.6 Practice: a small sales dataset — ten analysis questions

### Chapter 10: Data Cleaning [5 lecture sheets]

- 10.1 Missing values: isnull, fillna, dropna
- 10.2 Duplicates: finding and removing them
- 10.3 Text cleaning in columns (strip, replace, title)
- 10.4 Dates and numeric conversion (to_datetime, astype) + validation
- 10.5 Inconsistent categories: standardizing "Dhaka", "dhaka ", "DHAKA"; practice on a deliberately messy dataset

### Chapter 11: Data Transformation [6 lecture sheets]

- 11.1 groupby and agg
- 11.2 pivot_table and crosstab
- 11.3 merge (joins in Pandas) — with join validation
- 11.4 concat
- 11.5 Reshape: melt; wide vs long formats
- 11.6 Practice: one dataset, five transformation tasks

### Chapter 12: Date & Time Analysis [5 lecture sheets]

- 12.1 datetime objects; parsing real date strings
- 12.2 year/month/quarter extraction; month-end dates
- 12.3 Date differences and aging (invoice age in days)
- 12.4 Resampling time series (monthly/quarterly summaries)
- 12.5 Rolling calculations (moving averages) — on sales data

### Chapter 13: Visualization [4 lecture sheets]

- 13.1 Matplotlib: line, bar, scatter, histogram
- 13.2 Labels, titles, legends, saving charts
- 13.3 Seaborn essentials + Pandas built-in plots
- 13.4 Chart selection and business storytelling: which chart answers which question; KPI visualization basics

### Chapter 14: SQL Foundations [6 lecture sheets]

- 14.1 What a database/table is; primary & foreign keys
- 14.2 SELECT and WHERE
- 14.3 ORDER BY and LIMIT
- 14.4 GROUP BY, HAVING, aggregate functions
- 14.5 JOINs (inner/left) — joining customer and sales tables
- 14.6 SQL from Python: sqlite3, and SQL ↔ Pandas (read_sql, to_sql) — one workflow

### Intermediate Capstone [2 lecture sheets]

- C.1 Project: Sales & Profit Analysis — Excel/CSV → Pandas → Clean → Transform → Analyze → Charts → Excel Report
- C.2 Presentation of findings + code review walkthrough (this project is the direct foundation of Advanced BI)

## Course 3: Advanced Python for BI, Accounting, Automation & Analytics

Goal: Not a general "advanced Python" course. The identity of this course is Python for Business Intelligence, Accounting, Automation & Data Analytics, ending with a three-project portfolio.

### Chapter 1: Advanced Pandas for Business Data [7 lecture sheets]

- 1.1 merge/join/concat — multi-key joins + validation during joins
- 1.2 pivot/melt for report-shaped data
- 1.3 groupby().agg() — professional aggregation patterns
- 1.4 Window-style calculations 1: cumulative totals, expanding windows
- 1.5 Window-style calculations 2: percentage contribution, rankings (rank, pct_change)
- 1.6 Time-series in Pandas: resample, rolling, shifting
- 1.7 Performance: dtypes, chunked reading, memory-conscious analysis

### Chapter 2: SQL for Data Analysis [10 lecture sheets]

- 2.1 SELECT/WHERE recap for analysis (from Intermediate)
- 2.2 CASE WHEN — business logic in SQL
- 2.3 GROUP BY/HAVING for reporting
- 2.4 JOINs: inner/left/right/full — multi-table business joins
- 2.5 Subqueries
- 2.6 CTEs (WITH clauses)
- 2.7 Window functions 1: ROW_NUMBER, RANK, DENSE_RANK
- 2.8 Window functions 2: LAG/LEAD, running totals, period-over-period
- 2.9 Date analysis in SQL + views + indexing concept
- 2.10 SQL → Pandas workflow; Project: Customer + Sales + Product relational database analysis

### Chapter 3: Excel Automation with Python [7 lecture sheets]

- 3.1 openpyxl professional: workbook/sheet manipulation
- 3.2 Writing formulas from Python
- 3.3 Formatting: fonts, borders, fills, number formats
- 3.4 Conditional formatting
- 3.5 Charts inside Excel
- 3.6 Multiple worksheets and Excel templates
- 3.7 Batch workbook processing; Project: Monthly Management Report Generator

### Chapter 4: Accounting Analytics with Python [6 lecture sheets]

- 4.1 Accounting data structure: Chart of Accounts, Journal, General Ledger
- 4.2 Trial Balance: Debit/Credit structure, transaction IDs
- 4.3 Building a journal in Pandas; ledger summarization
- 4.4 Account-wise balances; trial balance preparation (and checking it balances!)
- 4.5 Revenue/expense classification; account movement analysis (period comparison)
- 4.6 Practice: a small accounting dataset from journal to trial balance

### Chapter 5: Accounts Receivable & Payable Analytics [5 lecture sheets]

- 5.1 AR basics: customer outstanding, invoice aging, overdue invoices
- 5.2 Days Sales Outstanding (DSO) concept
- 5.3 AP: supplier balances, due-date analysis, overdue liabilities
- 5.4 Aging buckets: Current, 1–30, 31–60, 61–90, 90+
- 5.5 Project: AR Aging Dashboard (Pandas + charts + Excel output)

### Chapter 6: Reconciliation Automation [5 lecture sheets]

- 6.1 The reconciliation problem: two lists that should match
- 6.2 Exact matching and one-to-one matching
- 6.3 Duplicate transactions and unmatched records
- 6.4 Tolerance-based matching (small differences), date-based matching, reference matching
- 6.5 Projects: Bank Reconciliation Automation + Ledger vs Bank Matching Tool

### Chapter 7: Financial & Management Reporting [6 lecture sheets]

- 7.1 Revenue, COGS, Gross Profit, Operating Expenses, Operating Profit — the structure of a P&L in code
- 7.2 Margins: gross margin %, operating margin %
- 7.3 Actual vs Budget and variance analysis
- 7.4 Growth: MoM, YoY, YTD calculations
- 7.5 Budget utilization
- 7.6 Project: Automated Monthly MIS Report

### Chapter 8: Business Intelligence Fundamentals [5 lecture sheets]

- 8.1 The BI pipeline: Source → Extract → Clean → Transform → Model → Measure → Visualize → Decision
- 8.2 Facts and dimensions; grain; keys
- 8.3 Star schema design
- 8.4 Date dimension — the most important table in BI
- 8.5 KPIs and measures: turning business questions into measurable numbers

### Chapter 9: Power BI Integration [8 lecture sheets]

- 9.1 Python/Pandas → Power BI-ready dataset (the handover mindset)
- 9.2 Power BI interface and data modeling (relationships, star schema in practice)
- 9.3 Power Query concepts — cleaning that survives refresh
- 9.4 DAX foundations: SUM, CALCULATE, DIVIDE, DISTINCTCOUNT
- 9.5 Filter context — the key mental model
- 9.6 Calculated column vs measure — when each
- 9.7 Basic time intelligence in DAX
- 9.8 KPI cards, slicers, drill-down, dashboard/report design; Project: Sales BI Dashboard (Python-prepared data + Power BI model)

### Chapter 10: ETL & Data Pipeline Automation [6 lecture sheets]

- 10.1 ETL thinking: Extract → Transform → Load
- 10.2 Extract: CSV, Excel, JSON, API, SQL sources
- 10.3 Transform: clean, validate, standardize, merge, calculate
- 10.4 Load: Excel, CSV, SQL, BI-ready tables
- 10.5 Orchestration basics: one script, clear steps, logging at each stage
- 10.6 Project: Automated Monthly ETL Pipeline (multi-source → validated → loaded)

### Chapter 11: API & Business Automation [5 lecture sheets]

- 11.1 REST APIs, GET/POST, authentication concepts
- 11.2 JSON handling and pagination
- 11.3 Error handling and retry concepts
- 11.4 API → Pandas and API → SQL
- 11.5 Scheduled extraction (task scheduler concept + code structure)

### Chapter 12: Office & Reporting Automation [6 lecture sheets]

- 12.1 Batch processing monthly files; report folder structures
- 12.2 CSV consolidation workflows
- 12.3 Automated Excel reports and charts
- 12.4 PDF/report generation
- 12.5 Email report workflow (smtplib concept + safety) and scheduling concepts
- 12.6 Logging + error reports; Project: Monthly Office Automation Suite — Read monthly files → Validate → Combine → Analyze → Generate Excel report → Generate charts → Produce management summary

### Chapter 13: Statistics & Forecasting for Business [6 lecture sheets]

- 13.1 Descriptive statistics: mean, median, percentile, variance, standard deviation
- 13.2 Distributions and outliers in business data
- 13.3 Correlation, trend, and seasonality
- 13.4 Moving averages for smoothing
- 13.5 Simple forecasting: basic linear regression, sales trend, demand/revenue forecasting
- 13.6 Honest limits of forecasting + practice on real sales data

### Chapter 14: KPI & Business Performance Analytics [5 lecture sheets]

- 14.1 Sales KPIs: Revenue, Quantity, Average Order Value, Growth %, Customer contribution
- 14.2 Financial KPIs: Gross Margin %, Expense Ratio, Budget Variance %, AR Outstanding, Collection performance
- 14.3 Inventory KPIs: stock movement, inventory aging, slow-moving products, turnover concepts
- 14.4 KPI design: definitions, targets, and benchmark discipline
- 14.5 Practice: a KPI sheet computed entirely in Pandas from raw data

### Chapter 15: Interactive Analytics Applications [5 lecture sheets]

- 15.1 Plotly — interactive charts
- 15.2 Streamlit basics: layout, filters, KPI cards
- 15.3 Tables, file upload, and downloadable reports in Streamlit
- 15.4 Combining filters + charts for exploration
- 15.5 Project: Finance/Sales Management Dashboard (upload CSV → filter → KPIs → charts → download)

### Chapter 16: Testing, Logging & Production-Ready Automation [5 lecture sheets]

- 16.1 pytest fundamentals; assertions for business rules
- 16.2 Data validation tests (does the reconciliation still match? does the trial balance balance?)
- 16.3 Logging configuration for scheduled jobs
- 16.4 Secrets and environment variables (never hardcode credentials)
- 16.5 Reproducible scripts: dependency management (requirements.txt), folder structure, error handling standards

### Chapter 17: ML for Business Analytics — Foundation Only [4 lecture sheets]

- 17.1 What ML is (and is not); supervised vs unsupervised in business words
- 17.2 Regression for business (sales/demand), train/test split
- 17.3 Classification basics + clustering concept; evaluation in plain terms
- 17.4 Business use cases, limitations, and responsible use — this is deliberately not an ML Engineer track

### Chapter 18: Final Capstone Portfolio [4 lecture sheets]

Three portfolio-grade projects (the learner builds all three):

- 18.1 Project 1 — Accounting Automation: Bank Reconciliation & AR Aging System (Python + Pandas + Excel)
- 18.2 Project 2 — Business Intelligence: Sales & Profit BI System (SQL → Python/Pandas → Data Model → Power BI → Management Dashboard)
- 18.3 Project 3 — Automation: Automated Monthly Management Reporting System (Multiple Excel/CSV files → Python → validation/cleaning → accounting logic → analysis → Excel management report → Power BI-ready output)
- 18.4 Portfolio packaging: GitHub, project READMEs, and presenting results to management (interview Q&A practice)

### The Overall Progression

Python Fundamentals → Professional Python → Excel + CSV + Pandas → Data Cleaning & Transformation → SQL → Accounting Data Analysis → Excel Automation → Reconciliation & Financial Reporting → ETL & Automation → Business Intelligence & Data Modeling → Power BI + DAX → KPI & Management Analytics → Streamlit / Automated Reporting → Business Portfolio Projects

## Lecture Sheet Production Workflow (for every subtopic)

1. Pick the subtopic → 2. Read the matching book section(s) if available → 3. Select the best material → 4. Bangla lecture sheet (List/Slicing lecture format) → 5. After approval, simple-English version → 6. Exercises with solutions + quiz

Fixed lecture-sheet structure: Title & objective → simple definition → formal definition → code → output → line-by-line explanation → common mistakes → exercises (solutions) → quiz → key idea → next-step connection.