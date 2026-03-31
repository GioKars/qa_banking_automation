from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_customer_login(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Customer Login')]"))
        ).click()

    def select_user(self, user_index=2):
        self.wait.until(
            EC.presence_of_element_located((By.ID, "userSelect"))
        ).click()

        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//option[{user_index}]"))
        ).click()

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
        ).click()

    def wait_for_dashboard(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Deposit')]"))
        )

    def login_as_customer(self):
        logger.info("Logging in as customer")

        self.click_customer_login()
        logger.debug("Clicked Customer Login")

        self.select_user()
        logger.debug("User selected")

        self.click_login()
        logger.debug("Login button clicked")

        self.wait_for_dashboard()
        logger.info("Login successful - dashboard loaded")
