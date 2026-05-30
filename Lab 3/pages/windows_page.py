from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WindowsPage(BasePage):
    @property
    def click_here_link(self):
        return (By.LINK_TEXT, "Click Here")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/windows")
        return self

    def click_new_window_link(self):
        self.click(self.click_here_link)
        return self

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)
        return self

    def get_current_title(self) -> str:
        return self.driver.title

    def close_current_window(self):
        self.driver.close()
        return self