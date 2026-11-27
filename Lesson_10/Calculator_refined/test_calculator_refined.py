from page_calculator_refined import PageCalculator
import time
import allure


@allure.title("Проверка сложения 7 + 8 с задержкой 45 секунд")
@allure.description(
    "Тест проверяет, что калькулятор корректно выполняет"
    " сложение и соблюдает заданную задержку в 45 секунд."
                    )
@allure.feature("Арифметическое действие")
@allure.severity(allure.severity_level.BLOCKER)
def test_result_15_within_45_seconds(chrome_driver):
    chrome_driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    page = PageCalculator(chrome_driver)

    page.timeout("45")

    page.press_button("7")
    page.press_button("+")
    page.press_button("8")
    page.press_button("=")

    start = time.time()
    result = page.wait_for_result("15")
    elapsed = time.time() - start

    with allure.step(
        f"Проверяем результат арифметического действия: {result}"
                     ):
        assert result == "15"
    # В проверке сделана поправка на возможную погрешность работы Selenium
    with allure.step(
        f"Проверяем фактическое время задержки: {elapsed:.2f} "
                    ):
        assert elapsed >= 44.7
