from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .product_catalog_page import ProductCatalogPage


class LoginPage:

    LOGIN = (By.ID, "user-name")
    PAROL = (By.ID, "password")
    LOGBTN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        user = self.wait.until(EC.element_to_be_clickable(
            self.LOGIN))
        user.clear()
        user.send_keys(username)

    def enter_password(self, passwrd):
        password_field = self.wait.until(EC.element_to_be_clickable(
            self.PAROL))
        password_field.clear()
        password_field.send_keys(passwrd)

    def click_button(self):
        log_btn = self.wait.until(EC.element_to_be_clickable(
            self.LOGBTN))
        log_btn.click()
        return ProductCatalogPage(self.driver)
