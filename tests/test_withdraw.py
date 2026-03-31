from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
import logging

logger = logging.getLogger(__name__)


def test_withdraw(driver, base_url):
    driver.get(base_url)

    login = LoginPage(driver)
    customer = CustomerPage(driver)

    logger.info("Logging in as customer")
    login.login_as_customer()

    initial_balance = int(customer.get_balance())
    logger.info(f"Initial balance: {initial_balance}")
    # customer.click_withdraw()
    logger.info("Performing withdraw of 100")
    customer.withdraw("100")

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(),'Transaction successful')]")
        )
    )

    logger.info("Checking success message")

    assert success_message.is_displayed()

    new_balance = int(customer.get_balance())
    logger.info(f"New balance: {new_balance}")

    assert new_balance == initial_balance - 100
    logger.info("Withdraw test passed")
