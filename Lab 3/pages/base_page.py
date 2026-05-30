from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.long_wait = WebDriverWait(driver, 80)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self

    def type_text(self, locator, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator) -> str:
        return self.find(locator).text

    def switch_to_frame(self, locator):
        print('')
        frame = self.long_wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
        return self

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        return self