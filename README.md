# Tasks Overview

This folder contains two small tasks: one HTML/JavaScript formatting exercise and one Python URL status checker.

## Task 1 - HTML + JavaScript

**File:** `Task 1 - Intern.html`

**Goal:** Read the `data` array and print formatted article lines into the `#results` element.

**Output format:**
```
Article "ARTICLE TITLE" (Page ID PAGEID) was created at MONTH DAY, YEAR.
```

**Notes:**
- The `{# INPUT #}` and `{# YOUR CODE HERE #}` markers are commented so the script runs.
- Dates are parsed from `YYYY-MM-DD` and formatted in `Month Day, Year` style.

## Task 2 - Python URL Status Checker

**File:** `task2.py`

**Input CSV:** `Task 2 - Intern.csv`

**Goal:** Read URLs from the CSV and print their HTTP status code in this format:
```
(STATUS CODE) URL
```

**Run it:**
```powershell
python task2.py
```

- This assumes you are running the command from the `Tasks` directory.

**Assumption:**
- The script expects the CSV to be in the same directory as `task2.py` unless you pass a full path argument.

**Behavior:**
- Uses a browser-like `User-Agent`.
- Handles BOM issues with `utf-8-sig`.
- Logs detailed failures to `error_details.log` while printing `(ERROR)` in output.
