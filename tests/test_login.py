import logging
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def test_login(driver, base_url):
    logger.info("Starting login test")

    driver.get(base_url)
    logger.info("Opened banking application")

    login = LoginPage(driver)

    logger.info("Logging in as customer")
    login.login_as_customer()

    logger.info("Verifying login was successful")

    assert "Account" in driver.page_source

    logger.info("Login test passed successfully")
