from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    custname = driver.find_element(
        By.CSS_SELECTOR, '[name="custname"]')
    custname.send_keys('Гудкова Ольга')
    sleep(2)

    Submit = driver.find_element(
        By.CSS_SELECTOR, '[type="submit"]')
    Submit.click()

    expected_url = "https://httpbin.qa-territory.online/post"
    assert driver.current_url == expected_url

    driver.quit()
