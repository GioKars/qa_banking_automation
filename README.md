# Banking App Test Automation (Selenium + Pytest)

## About this project

This project demonstrates a Selenium + Pytest automation framework for testing a banking web application, covering both positive and negative scenarios using best practices like Page Object Model (POM).

Tested application:  
https://www.globalsqa.com/angularJs-protractor/BankingProject/

---

## What I used

- Python
- Selenium WebDriver
- Pytest
- pytest-html (for reports)
- Python logging

---

## Key highlights

- Built a reusable Selenium + Pytest automation framework from scratch
- Implemented Page Object Model (POM) for maintainability
- Covered both positive and negative test scenarios
- Used parametrization for data-driven testing
- Added logging and automatic screenshots on test failure
- Supported cross-browser execution (Chrome & Firefox)
- Identified and documented UI validation issues (missing error messages, weak input validation)

---

## Project structure

```
qa_banking/
│
├── pages/
│   ├── login_page.py
│   └── customer_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_deposit.py
│   └── test_deposit_multiple_amounts.py
│   ├── test_deposit_negative.py
│   ├── test_withdraw.py
│   ├── test_withdraw_negative.py
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
```

---

## What’s implemented

- Page Object Model (separate page classes for login and customer actions)
- Parametrized tests for multiple inputs
- Positive and negative test scenarios
- Logging (console + file)
- Screenshot on failure
- Cross-browser support (Chrome & Firefox)

---

## How to run

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
- Try invalid deposit inputs (negative, text, empty)
- Try withdrawing more than the available balance

---

## Screenshots

Screenshots are automatically captured on test failures and saved in the `/screenshots` folder.

---

## Notes

This project focuses on demonstrating practical test automation skills and clean framework design using industry-standard tools.

---

## Author

QA Automation project created as part of my portfolio to demonstrate Selenium and Pytest skills.

---

## License

This project is licensed under the MIT License.

Thanks for checking it out 🙂
