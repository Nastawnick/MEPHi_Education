import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UploadPage(BasePage):
    @property
    def file_input(self):
        return (By.ID, "file-upload")

    @property
    def upload_button(self):
        return (By.ID, "file-submit")

    @property
    def uploaded_files(self):
        return (By.ID, "uploaded-files")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/upload")
        return self

    def upload_file(self, file_path: str):
        abs_path = os.path.abspath(file_path)
        self.find(self.file_input).send_keys(abs_path)
        return self

    def submit_upload(self):
        self.click(self.upload_button)
        return self

    def get_uploaded_filename(self) -> str:
        return self.get_text(self.uploaded_files)