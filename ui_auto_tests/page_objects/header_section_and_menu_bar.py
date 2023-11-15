from selenium.webdriver.common.by import By
from ui_auto_tests.helper import BaseMethods
from ui_auto_tests.locators import MenuBarLocators, HeaderLocators


class HeaderSectionAndMenuBar(BaseMethods):
    """хедер сайту і панель меню"""

    def get_title(self) -> str:
        return self.get_text(By.CSS_SELECTOR, HeaderLocators.HEADER)

    def click_on_btn_text_box(self) -> None:
        self.click_on(By.XPATH, MenuBarLocators.BTN_TEXT_BOX)

    def click_on_btn_check_box(self) -> None:
        self.click_on(By.XPATH, MenuBarLocators.BTN_CHECK_BOX)

    def click_on_btn_radio_button(self) -> None:
        self.click_on(By.XPATH, MenuBarLocators.BTN_RADIO_BUTTON)

    def click_on_btn_web_tables(self) -> None:
        self.click_on(By.XPATH, MenuBarLocators.BTN_WEB_TABLES)

    def click_on_btn_practice_form(self) -> None:
        self.click_on(By.XPATH, MenuBarLocators.BTN_PRACTICE_FORM)

