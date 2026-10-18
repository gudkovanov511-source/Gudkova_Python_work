from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    login = wait.until(EC.visibility_of_element_located(
        (By.ID, "user-name")))
    login.clear()
    login.send_keys("standard_user")
    parol = wait.until(EC.visibility_of_element_located(
        (By.ID, "password")))
    parol.clear()
    parol.send_keys("secret_sauce")
    log_btn = wait.until(EC.element_to_be_clickable(
        (By.ID, "login-button")))
    log_btn.click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".shopping_cart_link"))).click()

    check_btn = wait.until(EC.element_to_be_clickable(
        (By.ID, "checkout")))
    check_btn.click()

    fields = {
        "first-name": "Vasja",
        "last-name": "Petrov",
        "postal-code": "100100"
    }

    for field_id, value in fields.items():
        element = driver.find_element(By.ID, field_id)
        element.clear()
        element.send_keys(value)

    wait.until(EC.element_to_be_clickable(
        (By.ID, "continue"))).click()

    total_element = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".summary_total_label")))
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", total_element)
    wait.until(EC.visibility_of(total_element))
    assert total_element.text == "Total: $58.29"

    text = total_element.text
    amount_text = text.replace("Total: ", "")
    driver.quit()

    expected_text = "$58.29"
    assert amount_text == expected_text, "Сумма не совпадает: ожидалось "
    f"{expected_text}, а получен {amount_text}"
