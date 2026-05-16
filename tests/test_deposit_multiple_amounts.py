import pytest
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
import logging

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("amount", ["50", "100", "200"])
def test_deposit_multiple_amounts(driver, amount, base_url):
    logger.info(f"Starting deposit test with amount: {amount}")

    driver.get(base_url)

    customer = CustomerPage(driver)
    login = LoginPage(driver)

    logger.info("Logging in as customer")
    login.login_as_customer()

    initial_balance = int(customer.get_balance())
    logger.info(f"Initial balance: {initial_balance}")

    logger.info(f"Depositing amount: {amount}")
    customer.deposit(amount)

    new_balance = int(customer.get_balance())
    logger.info(f"New balance: {new_balance}")

    assert new_balance == initial_balance + int(amount)
    logger.info(f"Deposit test passed for amount: {amount}")
