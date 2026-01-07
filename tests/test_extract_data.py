import pytest
import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.extract
def test_extract_inventory_data(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    data = inventory.extract_items()

    with open("data/inventory_data.json", "w") as f:
        json.dump(data, f, indent=4)

    inventory.logout()
    assert "saucedemo.com" in driver.current_url