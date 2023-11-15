from ui_auto_tests.page_objects.header_section_and_menu_bar import HeaderSectionAndMenuBar
from selenium.webdriver.common.by import By
from ui_auto_tests.locators import TextBoxPageLocators
from ui_auto_tests.data import TestData


class TextBoxPage(HeaderSectionAndMenuBar):
    """сторінка Text Box: містить локатори веб елементів та методи для взаємодії з ними"""

    def set_full_name(self) -> str:
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, TextBoxPageLocators.txt_full_name).send_keys(TestData.full_name)
        return TestData.full_name

    def set_email(self) -> str:
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, TextBoxPageLocators.txt_email).send_keys(TestData.email)
        return TestData.email

    def set_current_address(self) -> str:
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, TextBoxPageLocators.txt_current_address).send_keys(TestData.current_address)
        return TestData.current_address

    def set_permanent_address(self) -> str:
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, TextBoxPageLocators.txt_permanent_address).send_keys(TestData.permanent_address)
        return TestData.permanent_address

    def scroll_and_click_on_btn_submit(self) -> None:
        button_submit = self.wait_for_visibility_of_el(By.CSS_SELECTOR, TextBoxPageLocators.btn_submit)
        self.scroll_js(button_submit)
        button_submit.click()

    def get_output_full_name(self) -> str:
        full_name = self.wait_for_visibility_of_el(By.CSS_SELECTOR, TextBoxPageLocators.output_full_name).text
        split_full_name = full_name.split(sep=':')
        return split_full_name[1]

    def get_output_email(self) -> str:
        email = self.wait_for_visibility_of_el(By.CSS_SELECTOR, TextBoxPageLocators.output_email).text
        split_email = email.split(sep=':')
        return split_email[1]

    def get_output_current_address(self) -> str:
        current_address = self.wait_for_visibility_of_el(By.CSS_SELECTOR, TextBoxPageLocators.output_current_address).text
        split_current_address = current_address.split(sep=':')
        return split_current_address[1]

    def get_output_permanent_address(self) -> str:
        permanent_address = self.wait_for_visibility_of_el(By.CSS_SELECTOR, TextBoxPageLocators.output_permanent_address).text
        split_permanent_address = permanent_address.split(sep=':')
        return split_permanent_address[1]

