from pages.login_page import LoginPage


def test_buyer_scenario(driver):
    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    catalog = login.click_button()

    catalog.add_to_cart("Sauce Labs Backpack")
    catalog.add_to_cart("Sauce Labs Bolt T-Shirt")
    catalog.add_to_cart("Sauce Labs Onesie")
    cart = catalog.go_to_cart()
    items = cart.get_cart_items()

    checkout = cart.click_checkout()

    checkout.fill_info("Вася", "Иванов", "100000")
    checkout.click_continue()
    total = checkout.get_total()

    driver.quit()
    assert items == [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    assert total == "Total: $58.29"
