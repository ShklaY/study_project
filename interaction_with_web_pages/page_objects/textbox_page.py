import dataclasses

from helpers.methods_to_interact_with_pages import MethodsToInteractWithPages
from interaction_with_web_pages.page_objects.menu_bar import MenuBar
from selenium.webdriver.common.by import By
from helpers.custom_types import UserModel


@dataclasses.dataclass
class OutputUserData:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


class TextBoxPage(MethodsToInteractWithPages):
    TXT_FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    TXT_FULL_NAME_WITH_VALIDATION_ERROR = (By.CSS_SELECTOR, 'input[id="userName"].field-error')
    TXT_EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    TXT_EMAIL_WITH_VALIDATION_ERROR = (By.CSS_SELECTOR, 'input[id="userEmail"].field-error')
    TXT_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    TXT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    BTN_SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    OUTPUT_FULL_NAME = (By.CSS_SELECTOR, 'p[id="name"]')
    OUTPUT_EMAIL = (By.CSS_SELECTOR, 'p[id="email"]')
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="currentAddress"]')
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="permanentAddress"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.menu_bar = MenuBar(self.driver)
        self.url = f'{self.base_url}/text-box'

    def fill_text_boxes(self,
                        full_name: UserModel,
                        email: UserModel,
                        current_address: UserModel,
                        permanent_address: UserModel) -> None:
        self.set_data(TextBoxPage.TXT_FULL_NAME, full_name)\
            .set_data(TextBoxPage.TXT_EMAIL, email)\
            .set_data(TextBoxPage.TXT_CURRENT_ADDRESS, current_address)\
            .set_data(TextBoxPage.TXT_PERMANENT_ADDRESS, permanent_address)

    def click_on_submit_btn(self) -> None:
        self.remove_advertising_in_footer()\
            .scroll_js(TextBoxPage.BTN_SUBMIT)\
            .click_on(TextBoxPage.BTN_SUBMIT)

    def get_output_user_data(self) -> OutputUserData:
        split_full_name = self.get_text(TextBoxPage.OUTPUT_FULL_NAME).split(sep=':')
        split_email = self.get_text(TextBoxPage.OUTPUT_EMAIL).split(sep=':')
        split_curr_address = self.get_text(TextBoxPage.OUTPUT_CURRENT_ADDRESS).split(sep=':')
        split_perm_address = self.get_text(TextBoxPage.OUTPUT_PERMANENT_ADDRESS).split(sep=':')
        return OutputUserData(split_full_name[1], split_email[1], split_curr_address[1], split_perm_address[1])

    def check_email_field_has_validation_error(self) -> None:
        self.wait_for_visibility_of_el(self.TXT_EMAIL_WITH_VALIDATION_ERROR)

    def check_full_name_field_has_validation_error(self) -> None:
        self.wait_for_visibility_of_el(self.TXT_FULL_NAME_WITH_VALIDATION_ERROR)


