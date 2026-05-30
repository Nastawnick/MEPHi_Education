from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class AlertsPage(BasePage):
    @property
    def js_alert_button(self):
        return (By.XPATH, "//button[text()='Click for JS Alert']")

    @property
    def result_message(self):
        return (By.ID, "result")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        return self

    def click_js_alert(self):
        self.click(self.js_alert_button)
        return self

    def accept_alert(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        return self

    def get_result_text(self) -> str:
        return self.get_text(self.result_message)