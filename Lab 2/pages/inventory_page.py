from selenium.webdriver.common.by import By
class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_container = (By.CLASS_NAME, "inventory_list")

    def is_loaded(self):
        return len(self.driver.find_elements(*self.inventory_container)) > 0

    def add_item_to_cart(self, item_name: str):
        # Находим товар по названию и кликаем на кнопку добавления
        item = self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']")
        item.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
