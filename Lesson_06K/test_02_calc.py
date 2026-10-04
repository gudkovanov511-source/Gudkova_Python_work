from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 45)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    field = driver.find_element(By.ID, "delay")
    field.clear()
    field.send_keys('45')

    driver.find_element(By.XPATH, "//span[normalize-space()='7']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='+']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='8']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='=']").click()

    result_field = (By.CSS_SELECTOR, "div[class='screen']")
    assert wait.until(
        EC.text_to_be_present_in_element(result_field, "15")
    )

    driver.quit()
