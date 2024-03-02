from selenium.webdriver.common.by import By
from helpers.methods_to_interact_with_pages import MethodsToInteractWithPages


class MenuBar(MethodsToInteractWithPages):
    BTN_TEXT_BOX = (By.XPATH, '//span[text()="Text Box"]')
    BTN_CHECK_BOX = (By.XPATH, '//span[text()="Check Box"]')
    BTN_RADIO_BUTTON = (By.XPATH, '//span[text()="Radio Button"]')
    BTN_WEB_TABLES = (By.XPATH, '//span[text()="Web Tables"]')
    BTN_PRACTICE_FORM = (By.XPATH, '//span[text()="Practice Form"]')

    def click_on_text_box_btn(self) -> None:
        self.click_on(MenuBar.BTN_TEXT_BOX)

    def click_on_check_box_btn(self) -> None:
        self.click_on(MenuBar.BTN_CHECK_BOX)

    def click_on_radio_btn(self) -> None:
        self.click_on(MenuBar.BTN_RADIO_BUTTON)

    def click_on_web_tables_btn(self) -> None:
        self.click_on(MenuBar.BTN_WEB_TABLES)

    def click_on_practice_form_btn(self) -> None:
        self.click_on(MenuBar.BTN_PRACTICE_FORM)

