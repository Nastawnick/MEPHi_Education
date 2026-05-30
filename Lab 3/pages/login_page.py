from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from models.user import User


class LoginPage(BasePage):
    @property
    def username_input(self):
        return (By.ID, "username")

    @property
    def password_input(self):
        return (By.ID, "password")

    @property
    def login_button(self):
        return (By.CSS_SELECTOR, "button[type='submit']")

    @property
    def success_message(self):
        return (By.CSS_SELECTOR, ".flash.success")

    @property
    def error_message(self):
        return (By.CSS_SELECTOR, ".flash.error")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
        return self

    def login(self, user: User):
        self.type_text(self.username_input, user.username)
        self.type_text(self.password_input, user.password)
        self.click(self.login_button)
        return self

    def get_success_message(self) -> str:
        return self.get_text(self.success_message)

    def is_logged_in(self) -> bool:
        try:
            return "You logged into a secure area" in self.get_success_message()
        except:
            return False