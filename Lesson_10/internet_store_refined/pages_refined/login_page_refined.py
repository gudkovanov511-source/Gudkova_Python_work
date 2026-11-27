import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .product_catalog_page_refined import ProductCatalogPage


@allure.epic("Страница авторизации")
class LoginPage:

    LOGIN = (By.ID, "user-name")
    PAROL = (By.ID, "password")
    LOGBTN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Вводит логин пользователя
    @allure.step("Вводим логин пользователя")
    def enter_username(self, username: str) -> None:
        user = self.wait.until(EC.element_to_be_clickable(
            self.LOGIN))
        user.clear()
        user.send_keys(username)

    # Метод вводит пароль пользователя
    @allure.step("Вводим пароль")
    def enter_password(self, passwrd: str) -> None:
        password_field = self.wait.until(EC.element_to_be_clickable(
            self.PAROL))
        password_field.clear()
        password_field.send_keys(passwrd)

    # Метод нажимает на кнопку и переходит на страницу с каталогом товаров
    @allure.step("Нажимаем на кнопку и переходим в каталог товаров")
    def click_button(self):
        log_btn = self.wait.until(EC.element_to_be_clickable(
            self.LOGBTN))
        log_btn.click()
        return ProductCatalogPage(self.driver)
