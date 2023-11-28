from interaction_with_web_pages.page_objects.menu_bar import MenuBar
from selenium.webdriver.common.by import By
from interaction_with_web_pages.user_model import UserModel


class TextBoxPage(MenuBar):
    TXT_FULL_NAME = 'input[id="userName"]'
    TXT_EMAIL = 'input[id="userEmail"]'
    TXT_CURRENT_ADDRESS = 'textarea[id="currentAddress"]'
    TXT_PERMANENT_ADDRESS = 'textarea[id="permanentAddress"]'
    BTN_SUBMIT = 'button[id="submit"]'

    OUTPUT_FULL_NAME = 'p[id="name"]'
    OUTPUT_EMAIL = 'p[id="email"]'
    OUTPUT_CURRENT_ADDRESS = 'p[id="currentAddress"]'
    OUTPUT_PERMANENT_ADDRESS = 'p[id="permanentAddress"]'

    def fill_text_boxes(self, full_name: UserModel, email: UserModel, current_address: UserModel, permanent_address: UserModel) -> None:
        # TODO 3 wrong data import, data should be get as method argument
        self.set_data(By.CSS_SELECTOR, TextBoxPage.TXT_FULL_NAME, full_name)
        self.set_data(By.CSS_SELECTOR, TextBoxPage.TXT_EMAIL, email)
        self.set_data(By.CSS_SELECTOR, TextBoxPage.TXT_CURRENT_ADDRESS, current_address)
        self.set_data(By.CSS_SELECTOR, TextBoxPage.TXT_PERMANENT_ADDRESS, permanent_address)

    def click_on_btn_submit(self) -> None:
        self.remove_advertising_in_footer()
        self.scroll_js(By.CSS_SELECTOR, TextBoxPage.BTN_SUBMIT)
        self.click_on(By.CSS_SELECTOR, TextBoxPage.BTN_SUBMIT)

    def get_output_user_data(self) -> tuple:
        split_full_name = self.get_text(By.CSS_SELECTOR, TextBoxPage.OUTPUT_FULL_NAME).split(sep=':')
        split_email = self.get_text(By.CSS_SELECTOR, TextBoxPage.OUTPUT_EMAIL).split(sep=':')
        split_curr_address = self.get_text(By.CSS_SELECTOR, TextBoxPage.OUTPUT_CURRENT_ADDRESS).split(sep=':')
        split_perm_address = self.get_text(By.CSS_SELECTOR, TextBoxPage.OUTPUT_PERMANENT_ADDRESS).split(sep=':')
        return split_full_name[1], split_email[1], split_curr_address[1], split_perm_address[1]


