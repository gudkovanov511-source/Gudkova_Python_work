import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Оформление заказа")
class CheckoutPage:

    SUMMARUTOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Вводит данные, необходимые для оформления заказа
    @allure.step(
            "Вводим {name}, {surname}, {postal_code} для оформления заказа"
            )
    def fill_info(self, name: str, surname: str, postal_code: str) -> None:
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

    # Нажимает кнопку "continue" для сохранения данных и
    # продолжения оформления покупки
    @allure.step("Нажимаем на кнопку 'continue' для сохранения данных")
    def click_continue(self) -> None:
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "continue"))).click()

    # Получает итоговую сумму для оплаты товаров в корзине
    @allure.step("Получаем итоговую сумму покупки")
    def get_total(self) -> str:
        total_element = self.wait.until(EC.visibility_of_element_located(
            self.SUMMARUTOTAL))
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", total_element)
        return total_element.text
