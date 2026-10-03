from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    # Откройте страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")
    # Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESSION",
        "value": "NzE3NjA0ZmItYjVmYi00NTkzLTlkMWQtZjIxOWE3NDY5YTcz",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    # Обновите страницу.
    driver.refresh()
    # Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/project?sort=updated_at&direction=ASC")
    profile_ola = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, 'profile-page__profile-name')
    ))
    profile_ola.click()
    # Сохраните текущий URL. https://gitflic.ru/user/ola.
    current_url1 = driver.current_url
    saved_url1 = current_url1
    expected_url1 = "https://gitflic.ru/user/ola"
    assert expected_url1 == saved_url1, "URL не совпадают: ожидалось "
    f"{expected_url1}, а получилось {saved_url1}"
    # Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    # Установите cookie пользователя 2.
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "MzA0ZjBmOGYtNTExMS00OGRiLTkxYmEtMzRhMzRjNzE5YzM0",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    # Обновите страницу.
    driver.refresh()
    # Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/project?sort=updated_at&direction=ASC")
    profile_ola2 = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'profile-page__profile-name')
        ))
    profile_ola2.click()
    # Сохраните текущий URL. https://gitflic.ru/user/ola2
    current_url2 = driver.current_url
    saved_url2 = current_url2
    expected_url2 = "https://gitflic.ru/user/ola2"
    assert saved_url2 == expected_url2, "URL не совпадают, ожидалось "
    f"{expected_url2}, получилось {saved_url2}"
    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert saved_url1 != saved_url2, "URL совпадают"

    driver.quit()
