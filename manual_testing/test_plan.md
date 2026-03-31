# Test Plan – Banking Application

## Overview

This project tests a demo banking web application using Selenium and Pytest.
The goal is to validate core user actions and ensure the application behaves correctly under both normal and invalid conditions.

---

## Scope

### Features covered:

- Customer login
- Deposit functionality
- Withdraw functionality
- Balance validation

### Out of scope:

- Admin features
- Backend/API testing
- Performance testing

---

## Test Approach

Testing is mainly automated using Selenium with Pytest.

Types of testing included:

- Functional testing
- Negative testing (invalid inputs)
- Basic UI validation

---

## Test Environment

- Browser: Chrome, Firefox
- OS: Windows
- Tool: Selenium WebDriver
- Framework: Pytest

---

## Test Data

Test data is passed using Pytest parametrization (e.g. different deposit/withdraw amounts).

---

## Risks / Limitations

- Application is a demo app with limited validation
- Some UI behaviors (like missing error messages) may not reflect real production systems

---

## Conclusion

The test suite covers the main user flows and basic edge cases.
It is designed to be simple, maintainable, and easy to extend.
