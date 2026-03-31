# Bug Reports – Banking Application

## Bug 1: No validation message for invalid deposit input

- **ID:** BUG_01

- **Severity:** Medium

- **Description:**
  When entering invalid values (e.g. text, negative number, empty input) in the deposit field, the system does not display any error message.

- **Steps to Reproduce:**
  1. Login as customer
  2. Click Deposit
  3. Enter invalid input (e.g. "abc")
  4. Press Enter

- **Expected Result:**
  User should see an error message indicating invalid input

- **Actual Result:**
  No message is displayed and no action occurs

---

## Bug 2: Input field accepts non-numeric values

- **ID:** BUG_02

- **Severity:** Low

- **Description:**
  The amount input field allows non-numeric values such as text.

- **Steps to Reproduce:**
  1. Login
  2. Click Deposit or Withdraw
  3. Enter text (e.g. "test")

- **Expected Result:**
  Input should be restricted to numeric values only

- **Actual Result:**
  Text input is accepted

---

## Bug 3: No clear feedback when transaction is blocked

- **ID:** BUG_03

- **Severity:** Low

- **Description:**
  When invalid actions are attempted (e.g. deposit with 0 or negative value), the system silently blocks the action without informing the user.

- **Expected Result:**
  User should receive feedback explaining why the action failed

- **Actual Result:**
  No feedback is shown

---

## Notes

These issues were identified during automated testing.
Since this is a demo application, some limitations are expected.
