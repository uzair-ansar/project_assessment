from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ITEMS = (By.CLASS_NAME, "inventory_item")
    LOGOUT_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")

    def extract_items(self):
        items = self.driver.find_elements(*self.ITEMS)
        data = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            data.append({"name": name, "price": price})
        return data

    def logout(self):
        self.driver.find_element(*self.LOGOUT_MENU).click()
        self.driver.find_element(*self.LOGOUT_BTN).click()