from interaction_with_web_pages.page_objects.menu_bar import MenuBar
from selenium.webdriver.common.by import By


class RadioButtonPage(MenuBar):
    RADIO_BUTTONS = (By.XPATH, "//label[contains(@class, 'custom-control-label')]")
    OUTPUT_TEXT = (By.CSS_SELECTOR, '[class="text-success"]')
    PRECEDING_SIBLING_FOR_RADIO_BTNS = (By.XPATH, ".//preceding-sibling::input")

    def click_on_radio_buttons_and_get_output_text(self) -> tuple:
        """цей метод повертає списки: 1й містить усі назви клікнутих радіобатонів,
        2й список - назви радіобатонів, що відображались на сторінці після тексту 'You have selected' """
        list_of_radio_buttons = self.wait_for_visibility_of_all_elements(RadioButtonPage.RADIO_BUTTONS)
        list_of_clicked_radiobutt = []
        list_of_output_radiobutt = []
        for radio_button in list_of_radio_buttons:
            find_a_preceding_sibling = radio_button.find_element(*RadioButtonPage.PRECEDING_SIBLING_FOR_RADIO_BTNS)
            if find_a_preceding_sibling.is_enabled():
                list_of_clicked_radiobutt.append(radio_button.text)
                radio_button.click()
                list_of_output_radiobutt.append(
                    self.get_text(RadioButtonPage.OUTPUT_TEXT))
        return list_of_clicked_radiobutt, list_of_output_radiobutt


