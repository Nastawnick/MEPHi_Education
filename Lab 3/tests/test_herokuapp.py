import os
import pytest
from models.user import User
from pages.login_page import LoginPage
from pages.iframe_page import IframePage
from pages.windows_page import WindowsPage
from pages.alerts_page import AlertsPage
from pages.upload_page import UploadPage
from selenium.webdriver.common.by import By


class TestHerokuApp:

    def test_1_login_with_explicit_wait(self, driver):
        login_page = LoginPage(driver)

        result = (login_page
                  .open()
                  .login(User.valid_user())
                  .is_logged_in())

        assert result, "Не удалось войти в систему"
        assert "You logged into a secure area" in login_page.get_success_message()

    def test_2_iframe_editor(self, driver):
        test_text = "Автоматизация тестирования iframe"
        iframe_page = IframePage(driver)

        (iframe_page
         .open()
         .switch_to_editor_frame()
         .clear_editor()
         .type_in_editor(test_text))

        actual_text = iframe_page.get_editor_text()
        iframe_page.exit_frame()

        assert test_text in actual_text, "Текст не введён в редактор"

    def test_3_windows_tabs(self, driver):
        windows_page = WindowsPage(driver)
        original_handle = driver.current_window_handle

        (windows_page
         .open()
         .click_new_window_link())

        import time
        time.sleep(1)

        handles = windows_page.get_window_handles()
        new_handle = [h for h in handles if h != original_handle][0]

        windows_page.switch_to_window(new_handle)
        assert windows_page.get_current_title() == "New Window"

        windows_page.close_current_window()
        windows_page.switch_to_window(original_handle)

        assert windows_page.get_current_title() == "The Internet"

    def test_4_javascript_alert(self, driver):
        alerts_page = AlertsPage(driver)

        (alerts_page
         .open()
         .click_js_alert()
         .accept_alert())

        result_text = alerts_page.get_result_text()
        assert "You successfully clicked an alert" in result_text

    def test_5_file_upload(self, driver):
        test_file_path = "test_file.txt"
        with open(test_file_path, "w") as f:
            f.write("Тестовый файл для загрузки")

        upload_page = UploadPage(driver)

        (upload_page
         .open()
         .upload_file(test_file_path)
         .submit_upload())

        uploaded_name = upload_page.get_uploaded_filename()
        assert "test_file.txt" in uploaded_name

        os.remove(test_file_path)