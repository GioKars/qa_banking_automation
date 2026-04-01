import pytest
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
import logging

logger = logging.getLogger(__name__)


@pytest.mark.negative
@pytest.mark.parametrize("amount", ["-50", "abc", "", -100, 0, "0"])
def test_invalid_withdraw(driver, base_url, amount):
    logger.info(f"Starting negative withdraw test with amount: {amount}")

    driver.get(base_url)

    customer = CustomerPage(driver)
    login = LoginPage(driver)

    login.login_as_customer()

    initial_balance = int(customer.get_balance())

    customer.withdraw(amount)

    message = customer.get_message()
    logger.info(f"Message displayed: {message}")

    new_balance = int(customer.get_balance())

    assert new_balance == initial_balance

    assert message is not None, "No validation message displayed"
    assert any(word in message.lower()
               for word in ["fail", "invalid", "error"])
