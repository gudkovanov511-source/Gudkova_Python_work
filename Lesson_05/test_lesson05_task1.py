from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")

    button_htmlForm = driver.find_element(
        By.CSS_SELECTOR, 'a[href="/forms/post"]')
    sleep(2)
    button_htmlForm.click()
    assert driver.current_url == (
        'https://httpbin.qa-territory.online/forms/post')
    sleep(2)

    driver.execute_script("window.history.back();")
    expected_url = "https://httpbin.qa-territory.online/"
    assert driver.current_url == expected_url

    driver.quit()
