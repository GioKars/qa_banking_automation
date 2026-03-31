# Test Cases: Banking Application

## 1. Login Test

- **ID:** TC_01

- **Description:** Verify that a customer can log in successfully

- **Steps:**
  1. Open application
  2. Click "Customer Login"
  3. Select user
  4. Click Login

- **Expected Result:**
  User is redirected to dashboard

---

## 2. Deposit Valid Amount

- **ID:** TC_02

- **Description:** Verify deposit with a single valid amount

- **Steps:**
  1. Login as customer
  2. Click Deposit
  3. Enter amount (e.g. 100)

- **Expected Result:**
  - Deposit is successful
  - Balance increases correctly

---

## 3. Deposit Multiple Amounts

- **ID:** TC_03

- **Description:** Verify deposit using multiple valid inputs

- **Test Data:** 50, 100, 200

- **Steps:**
  1. Login
  2. Perform deposit with different amounts

- **Expected Result:**
  - Each deposit is successful
  - Balance updates correctly for each amount

---

## 4. Withdraw Valid Amount

- **ID:** TC_04

- **Description:** Verify withdraw with valid amount

- **Steps:**
  1. Login
  2. Click Withdraw
  3. Enter amount

- **Expected Result:**
  - Transaction successful
  - Balance decreases correctly

---

## 5. Withdraw Exceeding Balance

- **ID:** TC_05

- **Description:** Verify withdrawing more than available balance

- **Steps:**
  1. Login
  2. Attempt to withdraw amount greater than balance

- **Expected Result:**
  - Transaction fails
  - Error message is shown
  - Balance remains unchanged

---

## 6. Deposit Invalid Input

- **ID:** TC_06

- **Description:** Verify system behavior for invalid deposit inputs

- **Test Data:** -50, "abc", empty, 0

- **Steps:**
  1. Login
  2. Attempt deposit with invalid input

- **Expected Result:**
  - Deposit is not performed
  - Balance remains unchanged
  - (Optional) Error message may be displayed

---

## 7. Withdraw Invalid Input

- **ID:** TC_07

- **Description:** Verify system behavior for invalid withdraw inputs

- **Test Data:** -50, "abc", empty, 0

- **Steps:**
  1. Login
  2. Attempt withdraw with invalid input

- **Expected Result:**
  - Withdraw is not performed
  - Balance remains unchanged
  - (Optional) Error message may be displayed

---

## Notes

These test cases are implemented using Pytest and Selenium with parametrized inputs where applicable.
