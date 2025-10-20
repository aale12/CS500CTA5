```markdown
# CSC500 – Critical Thinking Assignment 5
## Rainfall Collector & Bookstore Points

### 📌 Overview
This project implements two small interactive utilities as part of **Critical Thinking Assignment 5** for **CSC500 – Principles of Programming**. The behavior and prompts below follow the implementation found in `CSC500CTA5.py`.

- `collect_rainfall_data()` — Uses nested loops to collect monthly rainfall data across a user-specified number of years, validates inputs, accumulates total rainfall, and reports total months, total inches, and average monthly rainfall.
- `bookstore_points()` — Calculates reward points based on the number of books purchased using the following scale (implemented with explicit ranges):
	- 0–1 books: 0 points
	- 2–3 books: 5 points
	- 4–5 books: 15 points
	- 6–7 books: 30 points
	- 8 or more books: 60 points

Both functions are interactive command-line routines accessible from a simple menu when running the script directly.

---

### 🖥️ Program Features

- Input validation for integer and numeric inputs (ensures positive integers for years/books and non-negative rainfall values).
- Monthly prompts for rainfall collection (January–December) for each year.
- Aggregation and reporting of total and average rainfall.
- Points calculation with explicit ranges and formatted output.

---

### 📋 Example Runs (from the program prompts)

Rainfall collection example:

```
Enter the number of years: 1

Year 1:
	Enter the rainfall for month January (in inches): 0.2
	Enter the rainfall for month February (in inches): 0
	Enter the rainfall for month March (in inches): 0.35
	...

Total months: 12
Total inches of rainfall: 0.65
Average monthly rainfall: 0.05 inches
```

Bookstore points example:

```
Enter the number of books purchased: 4
Points earned: 15
```

---

### ▶️ How to Run
1. Ensure you have **Python 3.x** installed.
2. From the project directory, run:

```powershell
python CSC500CTA5.py
```

3. Choose an option from the menu:
	- Enter `1` to run rainfall collection.
	- Enter `2` to run bookstore points calculator.
	- Enter `Q` to quit.

---

### Notes & Suggestions

- The rainfall function expects non-negative floating-point values. Negative values are rejected and reprompted.
- The points table is implemented with explicit ranges in the source; modify the `bookstore_points()` function to change the reward policy.
- The module is structured so you can import the functions for unit testing or reuse in other scripts:


```

