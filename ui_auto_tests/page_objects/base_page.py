from ui_auto_tests.helper import BaseMethods
from selenium.webdriver.common.by import By
from ui_auto_tests.locators import InitPageLocators


class BasePage(BaseMethods):
    def click_on_btn_elements(self) -> None:
        self.click_on(By.XPATH, InitPageLocators.BTN_ELEMENTS)

    def click_on_btn_forms(self) -> None:
        self.click_on(By.XPATH, InitPageLocators.BTN_FORMS)

