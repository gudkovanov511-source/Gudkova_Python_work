from selenium import webdriver
from page_calculator import PageCalculator
import time


def test_result_15_within_45_seconds():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    page = PageCalculator(driver)

    page.timeout("45")

    page.press_button("7")
    page.press_button("+")
    page.press_button("8")
    page.press_button("=")

    start = time.time()
    result = page.wait_for_result("15")
    elapsed = time.time() - start

    assert result == "15"
    assert elapsed >= 45

    driver.quit()
