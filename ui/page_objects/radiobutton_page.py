from ui.page_objects.header_section import MenuBar
from selenium.webdriver.common.by import By
from ui.locators import RadioButtonPageLocators


class RadioButtonPage(MenuBar):
    def click_on_radio_buttons_and_get_output_text(self) -> tuple:
        """цей метод повертає списки: 1й містить усі назви клікнутих радіобатонів,
        2й список - назви радіобатонів, що відображались на сторінці після тексту 'You have selected' """
        list_of_radio_buttons = self.wait_for_visibility_of_all_elements(By.XPATH, RadioButtonPageLocators.RADIO_BUTTONS)
        list_of_clicked_radiobutt = []
        list_of_output_radiobutt = []
        for i in list_of_radio_buttons:
            find_a_preceding_sibling = i.find_element(By.XPATH, RadioButtonPageLocators.PRECEDING_SIBLING_FOR_RADIO_BTNS)
            if find_a_preceding_sibling.is_enabled():
                list_of_clicked_radiobutt.append(i.text)
                i.click()
                list_of_output_radiobutt.append(
                    self.get_text(By.CSS_SELECTOR, RadioButtonPageLocators.OUTPUT_TEXT))
        return list_of_clicked_radiobutt, list_of_output_radiobutt


