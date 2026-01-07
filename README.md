# project_assessment
For Aristocrat Assessment

# Python Automation – QA Coding Assessment

This repository contains my solution for the QA Automation coding assessment.  
The project is implemented using **Python, Selenium, and Pytest** and covers login validation scenarios along with inventory data extraction from the SauceDemo application.

The focus of this solution is clarity, maintainability, and adherence to standard automation practices.

---

## Tools & Technologies

- Python 3.8+
- Selenium WebDriver
- Pytest
- Pytest-HTML (for reporting)
- WebDriver Manager

---

## Project Structure

```
project_assessment/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
│
├── tests/
│   ├── test_login_success.py
│   ├── test_login_failure.py
│   └── test_extract_data.py
│
├── data/
│   └── inventory_data.json
│
├── reports/
│
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── run_tests.sh
├── run_tests.bat
```

---

## Test Coverage

### 1. Successful Login
- Logs in with a valid user
- Confirms successful access to the inventory page

### 2. Failed Login
- Attempts login with a locked-out user
- Verifies that the appropriate error message is displayed

### 3. Inventory Data Extraction
- Logs in with a valid user
- Extracts product names and prices from the inventory page
- Stores the extracted data in a JSON file
- Logs out of the application

---

## How to Run the Tests

### Step 1: (Optional) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate --> for Linux
.venv\Scripts\activate --> for Windows
```

---

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Execute the test suite

**Linux**
```bash
./run_tests.sh
```

## Test Report

An HTML execution report is generated automatically after the test run.

Location:
```
reports/report.html
```

## Test Data Output

Inventory details extracted during execution are saved to:

```
data/inventory_data.json
```

Sample structure:
```json
[
    {
        "name": "Sauce Labs Backpack",
        "price": "$29.99"
    }
]
```

---

## Framework Design Notes

- Page Object Model is used to separate test logic from UI interactions
- Common setup and teardown logic is handled via Pytest fixtures
- Custom Pytest markers are defined for better test categorization
- Configuration values such as credentials and base URL are centralized
- The framework supports execution on any system with Python 3.8+

---

## Notes

- Browser drivers are managed automatically using webdriver-manager
- Generated files, caches, and virtual environments are excluded using `.gitignore`
- No environment-specific paths are hardcoded

---

## Summary

This project demonstrates a practical and maintainable approach to UI automation testing using Python and Pytest, following commonly used industry patterns.
