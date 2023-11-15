from ui_auto_tests.helper import BaseMethods
from selenium.webdriver.common.by import By
from ui_auto_tests.locators import InitPageLocators


class InitPage(BaseMethods):
    """початкова сторінка: містить локатори веб елементів та методи для взаємодії з ними"""

    def click_on_btn_elements(self) -> None:
        self.wait_for_visibility_of_el(By.XPATH, InitPageLocators.btn_elements).click()

    def click_on_btn_forms(self) -> None:
        self.wait_for_visibility_of_el(By.XPATH, InitPageLocators.btn_forms).click()

