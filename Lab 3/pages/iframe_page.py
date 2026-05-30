from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class IframePage(BasePage):

    @property
    def textarea_body(self):
        return (By.ID, "tinymce")

    @property
    def textarea_tag(self):
        return (By.TAG_NAME, "body")

    def open(self):
        print('1 - Открываем страницу')
        self.driver.get("https://the-internet.herokuapp.com/iframe")
        print('2 - Страница загружена, ждём загрузки TinyMCE...')
        return self

    def wait_for_tinymce(self):
        self.long_wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        print('3 - Iframe появился на странице')
        return self

    def switch_to_editor_frame(self):
        self.wait_for_tinymce()

        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        print(f'4 - Найдено iframe: {len(iframes)}')

        if len(iframes) > 0:
            self.driver.switch_to.frame(0)
            print('5 - Переключились на iframe редактора')
        else:
            raise Exception("Iframe не найден!")

        self.long_wait.until(EC.visibility_of_element_located(self.textarea_body))
        print('6 - Редактор готов к работе')
        return self

    def exit_frame(self):
        self.driver.switch_to.default_content()
        print('Вернулись на главную страницу')
        return self

    def clear_editor(self):
        element = self.long_wait.until(EC.element_to_be_clickable(self.textarea_body))
        element.clear()
        return self

    def type_in_editor(self, text: str):
        element = self.long_wait.until(EC.element_to_be_clickable(self.textarea_body))
        element.clear()
        element.send_keys(text)
        print(f'7 - Введён текст: {text[:50]}...')
        return self

    def get_editor_text(self) -> str:
        return self.get_text(self.textarea_body)
