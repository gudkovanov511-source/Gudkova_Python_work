from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    # 2. Найдите и нажмите на кнопку "Start"
    start_btn = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//button[normalize-space()='Start']")
    ))
    start_btn.click()
    # 3. Дождитесь появления текста "Hello World!"
    fin_text = wait.until(EC.visibility_of_element_located(
        (By.ID, "finish")
    ))
    # 4. Сделайте скриншот страницы
    fin_text.screenshot("screenshots/fin_text.png")
    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert fin_text.text == "Hello World!", "Нет такого текста"

    driver.quit()
