from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCalculator:

    FIELDTIME = (By.ID, "delay")
    FIELDRESULT = (By.CSS_SELECTOR, "div[class='screen']")
    BUTTONS = {
        'C': (By.XPATH, "//span[normalize-space()='C']"),
        '1': (By.XPATH, "//span[normalize-space()='1']"),
        '2': (By.XPATH, "//span[normalize-space()='2']"),
        '3': (By.XPATH, "//span[normalize-space()='3']"),
        '4': (By.XPATH, "//span[normalize-space()='4']"),
        '5': (By.XPATH, "//span[normalize-space()='5']"),
        '6': (By.XPATH, "//span[normalize-space()='6']"),
        '7': (By.XPATH, "//span[normalize-space()='7']"),
        '8': (By.XPATH, "//span[normalize-space()='8']"),
        '9': (By.XPATH, "//span[normalize-space()='9']"),
        '0': (By.XPATH, "//span[normalize-space()='7']"),
        '+': (By.XPATH, "//span[normalize-space()='+']"),
        '-': (By.XPATH, "//span[normalize-space()='-']"),
        '÷': (By.XPATH, "//span[normalize-space()='÷']"),
        'x': (By.XPATH, "//span[normalize-space()='x']"),
        '=': (By.XPATH, "//span[normalize-space()='=']"),
        '.': (By.XPATH, "//span[normalize-space()='.']")
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def timeout(self, seconds):
        time_field = self.wait.until(
            EC.element_to_be_clickable(self.FIELDTIME))
        time_field.clear()
        time_field.send_keys(seconds)

    def press_button(self, symbol):
        locator = self.BUTTONS[symbol]
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()

    def wait_for_result(self, expected):
        self.wait.until(EC.text_to_be_present_in_element
                        (self.FIELDRESULT, expected))
        result = self.driver.find_element(*self.FIELDRESULT).text
        return result
