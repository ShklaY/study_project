from selenium.webdriver.common.by import By
from ui_auto_tests.helper import BaseMethods
from ui_auto_tests.locators import MenuBarLocators, HeaderLocators


class HeaderSectionAndMenuBar(BaseMethods):
    """хедер сайту і панель меню"""

    def get_header_name(self) -> str:
        return self.wait_for_visibility_of_el(By.CSS_SELECTOR, HeaderLocators.header).text

    def click_on_btn_text_box(self) -> None:
        self.wait_for_visibility_of_el(By.XPATH, MenuBarLocators.menu_btn_text_box).click()

    def click_on_btn_check_box(self) -> None:
        self.wait_for_visibility_of_el(By.XPATH, MenuBarLocators.menu_btn_check_box).click()

    def click_on_btn_radio_button(self) -> None:
        self.wait_for_visibility_of_el(By.XPATH, MenuBarLocators.menu_btn_radio_button).click()

    def click_on_btn_web_tables(self) -> None:
        self.wait_for_visibility_of_el(By.XPATH, MenuBarLocators.menu_btn_web_tables).click()

    def click_on_btn_practice_form(self) -> None:
        self.wait_for_visibility_of_el(By.XPATH, MenuBarLocators.menu_btn_practice_form).click()

