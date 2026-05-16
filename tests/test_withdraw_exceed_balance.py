from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
import logging

logger = logging.getLogger(__name__)


def test_withdraw_exceed_balance(driver, base_url):
    driver.get(base_url)

    login = LoginPage(driver)
    customer = CustomerPage(driver)

    logger.info("Logging in as customer")
    login.login_as_customer()

    initial_balance = int(customer.get_balance())

    amount = initial_balance + 500
    logger.info(f"Attempting to withdraw more than balance: {amount}")

    customer.withdraw(amount)

    error_message = customer.get_message()
    logger.info(f"Error msg: {error_message}")

    assert error_message is not None
    assert "fail" in error_message.lower()
