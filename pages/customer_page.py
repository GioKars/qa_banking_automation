from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class CustomerPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.MESSAGE_LOCATOR = (
            By.XPATH,
            "//span[contains(@class,'error') or contains(@class,'success')]"
        )

    def click_deposit(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Deposit')]"))
        ).click()

    def click_withdraw(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Withdrawl')]"))
        ).click()

    def add_amount(self, amount):
        field = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[ng-model='amount']"))
        )
        field.clear()
        field.send_keys(str(amount))
        field.send_keys(Keys.ENTER)

    def get_balance(self):
        balance_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//strong[2]"))
        )
        return int(balance_element.text)

    def deposit(self, amount):
        self.click_deposit()
        self.add_amount(amount)

    def withdraw(self, amount):
        self.click_withdraw()
        self.add_amount(amount)

    def get_message(self):
        try:
            elements = self.driver.find_elements(*self.MESSAGE_LOCATOR)

            if not elements:
                return None

            text = elements[0].text.strip()
            return text if text else None

        except Exception:
            return None

        except TimeoutException:
            return None
