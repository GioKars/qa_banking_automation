import pytest
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
import logging

logger = logging.getLogger(__name__)


@pytest.mark.negative
@pytest.mark.parametrize("amount", ["-50", "abc", "", -100, 0, "0"])
def test_invalid_deposit(driver, amount, base_url):
    logger.info(f"Starting negative deposit test with amount: {amount}")

    customer = CustomerPage(driver)
    login = LoginPage(driver)

    driver.get(base_url)

    login.login_as_customer()

    initial_balance = int(customer.get_balance())
    logger.info(f"Initial balance: {initial_balance}")

    customer.deposit(amount)

    try:
        message = customer.get_message()
    except:
        message = None
    logger.info(f"Message displayed: {message}")

    new_balance = int(customer.get_balance())
    logger.info(f"New balance: {new_balance}")

    assert new_balance == initial_balance

    if message:
        assert any(word in message.lower()
                   for word in ["fail", "invalid", "error"])
