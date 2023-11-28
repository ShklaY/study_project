from selenium.webdriver.common.by import By
from interaction_with_web_pages.methods_to_interact_with_pages import MethodsToInteractWithPages


class MenuBar(MethodsToInteractWithPages):
    BTN_TEXT_BOX = '//span[text()="Text Box"]'
    BTN_CHECK_BOX = '//span[text()="Check Box"]'
    BTN_RADIO_BUTTON = '//span[text()="Radio Button"]'
    BTN_WEB_TABLES = '//span[text()="Web Tables"]'
    BTN_PRACTICE_FORM = '//span[text()="Practice Form"]'

    def click_on_btn_text_box(self) -> None:
        self.click_on(By.XPATH, MenuBar.BTN_TEXT_BOX)

    def click_on_btn_check_box(self) -> None:
        self.click_on(By.XPATH, MenuBar.BTN_CHECK_BOX)

    def click_on_btn_radio_button(self) -> None:
        self.click_on(By.XPATH, MenuBar.BTN_RADIO_BUTTON)

    def click_on_btn_web_tables(self) -> None:
        self.click_on(By.XPATH, MenuBar.BTN_WEB_TABLES)

    def click_on_btn_practice_form(self) -> None:
        self.click_on(By.XPATH, MenuBar.BTN_PRACTICE_FORM)

