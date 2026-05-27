from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)

    def is_item_in_cart(self, item_name: str) -> bool:
        for item in self.get_cart_items():
            if item_name in item.text:
                return True
        return False

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
