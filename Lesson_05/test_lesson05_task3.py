from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    all_links = driver.find_elements(By.CSS_SELECTOR, 'a[href]')
    assert len(all_links) == 9

    link1 = driver.find_element(
        By.CSS_SELECTOR, 'a[href="/links/10/1"]')
    assert link1.is_displayed()
    assert link1.text.strip() == "1"

    link2 = driver.find_element(
        By.CSS_SELECTOR, 'a[href="/links/10/2"]')
    assert link2.is_displayed()

    link3 = driver.find_element(
        By.CSS_SELECTOR, 'a[href="/links/10/3"]')
    assert link3.is_displayed()

    link4 = driver.find_element(
        By.CSS_SELECTOR, 'a[href="/links/10/4"]')
    assert link4.is_displayed()

    link5 = driver.find_element(
        By.CSS_SELECTOR, 'a[href="/links/10/5"]')
    assert link5.is_displayed()

    link6 = driver.find_element(
        By.CSS_SELECTOR, 'a[href="/links/10/6"]')
    assert link6.is_displayed()

    link7 = driver.find_element(
        By.CSS_SELECTOR, 'a[href="/links/10/7"]')
    assert link7.is_displayed()

    link8 = driver.find_element(
        By.CSS_SELECTOR, 'a[href="/links/10/8"]')
    assert link8.is_displayed()

    link9 = driver.find_element(
        By.CSS_SELECTOR, 'a[href="/links/10/9"]')
    assert link9.is_displayed()

    driver.quit()
