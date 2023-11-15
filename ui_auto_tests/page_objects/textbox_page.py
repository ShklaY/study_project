from ui_auto_tests.page_objects.header_section_and_menu_bar import HeaderSectionAndMenuBar
from selenium.webdriver.common.by import By
from ui_auto_tests.locators import TextBoxPageLocators
from ui_auto_tests.data import TestData


class TextBoxPage(HeaderSectionAndMenuBar):
    def fill_all_text_boxes(self) -> tuple:
        fill_full_name = self.set_data(By.CSS_SELECTOR, TextBoxPageLocators.TXT_FULL_NAME, TestData.full_name)
        fill_email = self.set_data(By.CSS_SELECTOR, TextBoxPageLocators.TXT_EMAIL, TestData.email)
        fill_current_address = self.set_data(By.CSS_SELECTOR, TextBoxPageLocators.TXT_CURRENT_ADDRESS, TestData.current_address)
        fill_permanent_address = self.set_data(By.CSS_SELECTOR, TextBoxPageLocators.TXT_PERMANENT_ADDRESS, TestData.permanent_address)
        return fill_full_name, fill_email, fill_current_address, fill_permanent_address

    def click_on_btn_submit(self) -> None:
        self.remove_advertising_in_footer()
        self.scroll_js(By.CSS_SELECTOR, TextBoxPageLocators.BTN_SUBMIT)
        self.click_on(By.CSS_SELECTOR, TextBoxPageLocators.BTN_SUBMIT)

    def get_output_user_data(self) -> tuple:
        split_full_name = self.get_text(By.CSS_SELECTOR, TextBoxPageLocators.OUTPUT_FULL_NAME).split(sep=':')
        split_email = self.get_text(By.CSS_SELECTOR, TextBoxPageLocators.OUTPUT_EMAIL).split(sep=':')
        split_curr_address = self.get_text(By.CSS_SELECTOR, TextBoxPageLocators.OUTPUT_CURRENT_ADDRESS).split(sep=':')
        split_perm_address = self.get_text(By.CSS_SELECTOR, TextBoxPageLocators.OUTPUT_PERMANENT_ADDRESS).split(sep=':')
        return split_full_name[1], split_email[1], split_curr_address[1], split_perm_address[1]


