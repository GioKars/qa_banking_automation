# QA Banking Automation Framework (Selenium + Pytest)

![Tests](https://github.com/GioKars/qa_banking_automation/actions/workflows/selenium-tests.yml/badge.svg)

## About this project

This project demonstrates a Selenium + Pytest automation framework for testing a banking web application, covering both positive and negative scenarios using industry-standard automation practices such as the Page Object Model (POM).

Tested application:  
https://www.globalsqa.com/angularJs-protractor/BankingProject/

---

## Tech Stack

- Python 3.11
- Selenium WebDriver
- Pytest
- Pytest HTML Reports
- GitHub Actions
- Logging
- Page Object Model (POM)

---

## Key Highlights

- Built a reusable Selenium + Pytest automation framework from scratch
- Implemented Page Object Model (POM) for maintainability and scalability
- Covered both positive and negative test scenarios
- Used parametrization for data-driven testing
- Added logging and automatic screenshots on test failure
- Supported cross-browser execution (Chrome & Firefox)
- Integrated CI/CD using GitHub Actions
- Identified and documented UI validation issues (missing error messages, weak input validation)

---

## Project Structure

```text
qa_banking_automation/
│
├── .github/
│   └── workflows/
│       └── selenium-tests.yml
│
├── pages/
│   ├── login_page.py
│   └── customer_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_deposit.py
│   ├── test_deposit_multiple_amounts.py
│   ├── test_invalid_deposit.py
│   ├── test_withdraw.py
│   ├── test_invalid_withdraw.py
│   └── test_withdraw_exceed_balance.py
│
├── manual_testing/
│   ├── test_plan.md
│   ├── test_cases.md
│   └── bug_reports.md
│
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## What’s implemented

- Page Object Model (separate page classes for login and customer actions)
- Parametrized tests for multiple inputs
- Positive and negative test scenarios
- Logging (console + file)
- Screenshot on failure
- Cross-browser support (Chrome & Firefox)
- HTML report generation
- GitHub Actions CI/CD pipeline

---

## How to run

Clone repository:

```
git clone https://github.com/GioKars/qa_banking_automation.git
cd qa_banking_automation
```

Install dependencies:

```
pip install -r requirements.txt
```

Run all tests:

```
pytest
```

Run only negative tests:

```
pytest -m negative
```

Run with a specific browser:

```
pytest --browser=chrome
pytest --browser=firefox
```

Generate HTML report:

```
pytest --html=report.html --self-contained-html --capture=tee-sys
```

---

## Example scenarios covered

- Login as customer
- Deposit valid amounts and verify balance
- Withdraw valid amounts
- Deposit multiple amounts using parametrized tests
- Try invalid deposit inputs (negative, text, empty)
- Try invalid withdraw inputs
- Try withdrawing more than the available balance

---

## Reports & Screenshots

- HTML reports can be generated using pytest-html
- Screenshots are automatically captured on test failures and saved in the `/screenshots` folder.
- Logs are saved to test.log

---

## CI/CD

This project uses GitHub Actions for Continuous Integration (CI).

Tests automatically run on:

- push to main branch
- pull requests

CI artifacts:

- logs
- screenshots on failure

## Notes

This project focuses on demonstrating practical test automation skills and clean framework design using industry-standard tools.

---

## Author

QA Automation project created as part of my portfolio to demonstrate Selenium and Pytest skills.

---

## License

This project is licensed under the MIT License.

Thanks for checking it out 🙂
