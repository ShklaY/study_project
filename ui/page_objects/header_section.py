from selenium.webdriver.common.by import By
from ui.helper import BaseMethods
from ui.locators import MenuBarLocators, HeaderLocators


class MenuBar(BaseMethods):
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

