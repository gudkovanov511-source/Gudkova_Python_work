from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    SUMMARUTOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_info(self, name, surname, postal_code):
        fields = {
            "first-name": name,
            "last-name": surname,
            "postal-code": postal_code
        }
        for field_id, value in fields.items():
            element = self.wait.until(EC.visibility_of_element_located(
                (By.ID, field_id)))
            element.clear()
            element.send_keys(value)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "continue"))).click()

    def get_total(self):
        total_element = self.wait.until(EC.visibility_of_element_located(
            self.SUMMARUTOTAL))
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", total_element)
        return total_element.text
