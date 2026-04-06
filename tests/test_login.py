# tests/test_login.py
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.is_loaded()