import pytest
from selenium import webdriver

BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)

    yield driver
    # согласно ТЗ проверку в тесте надо делать после закрытия
    # браузера, поэтому driver.quit() перенесён в тест
