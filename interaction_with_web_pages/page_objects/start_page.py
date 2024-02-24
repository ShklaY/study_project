from interaction_with_web_pages.methods_to_interact_with_pages import MethodsToInteractWithPages
from selenium.webdriver.common.by import By


class StartPage(MethodsToInteractWithPages):
    BTN_ELEMENTS = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    BTN_FORMS = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]')

    def click_on_btn_elements(self) -> None:
        self.click_on(StartPage.BTN_ELEMENTS)

    def click_on_btn_forms(self) -> None:
        self.click_on(StartPage.BTN_FORMS)

