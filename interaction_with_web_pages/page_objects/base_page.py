from interaction_with_web_pages.methods_to_interact_with_pages import MethodsToInteractWithPages
from selenium.webdriver.common.by import By


class BasePage(MethodsToInteractWithPages):
    BTN_ELEMENTS = '//*[@id="app"]/div/div/div[2]/div/div[1]'
    BTN_FORMS = '//*[@id="app"]/div/div/div[2]/div/div[2]'

    # TODO 3 Page should not have driver interactions methods, it should use associations for this
    def click_on_btn_elements(self) -> None:
        self.click_on(By.XPATH, BasePage.BTN_ELEMENTS)

    def click_on_btn_forms(self) -> None:
        self.click_on(By.XPATH, BasePage.BTN_FORMS)

