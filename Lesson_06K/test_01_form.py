from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 15)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    for name, value in fields.items():
        driver.find_element(By.NAME, name).send_keys(value)

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")
    )).click()

    red_field = "zip-code"
    for field_id in [
        "first-name",
        "last-name",
        "address",
        "zip-code",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company"
    ]:
        element = driver.find_element(By.ID, field_id)
        class_attr = element.get_attribute("class")
        if field_id == red_field:
            assert "alert-danger" in class_attr, f"{field_id} "
            "должен быть красным"
        else:
            assert "alert-success" in class_attr, f"{field_id} "
            "должен быть зелёным"

    driver.quit()
