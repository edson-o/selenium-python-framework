# pages/inventory_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")

    def is_loaded(self):
        return self.get_text(self.TITLE) == "Products"