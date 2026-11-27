import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .cart_page_refined import CartPage


@allure.epic("Каталог товаров")
class ProductCatalogPage:

    CART = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Метод, с помощью которого мы кладём товары в корзину
    @allure.step("Выбираем товары и кладём в корзину")
    def add_to_cart(self, name: str) -> None:
        # id кнопки = "add-to-cart-" + имя товара в нижнем регистре,
        # пробелы → дефисы
        slug = name.lower().replace(" ", "-")
        locator = (By.ID, f"add-to-cart-{slug}")
        self.wait.until(EC.presence_of_element_located(locator)).click()

    # Метод, с помощью которого мы переходим в корзину
    @allure.step("Нажимаем на кнопку и переходим в корзину")
    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART)).click()
        return CartPage(self.driver)
