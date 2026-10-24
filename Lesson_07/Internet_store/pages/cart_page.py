from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .checkout_page import CheckoutPage


class CartPage:

    CHECKOUT = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return [item.text for item in items]

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT)).click()
        return CheckoutPage(self.driver)
