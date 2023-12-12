import time

from selenium.common import StaleElementReferenceException
from interaction_with_web_pages.page_objects.menu_bar import MenuBar
from selenium.webdriver.common.by import By
from helpers.logger import log


class RadioButtonPage(MenuBar):
    RADIO_BUTTONS = (By.XPATH, "//label[contains(@class, 'custom-control-label')]")
    OUTPUT_TEXT = (By.CSS_SELECTOR, '[class="text-success"]')
    PRECEDING_SIBLING_FOR_RADIO_BTNS = (By.XPATH, ".//preceding-sibling::input")

    def click_on_radio_buttons_and_get_output_text(self) -> tuple:
        """цей метод повертає списки: 1й містить усі назви клікнутих радіобатонів,
        2й список - назви радіобатонів, що відображались на сторінці після тексту 'You have selected' """
        list_of_clicked_radiobutt = []
        list_of_output_radiobutt = []
        len_list_of_radio_buttons = len(self.wait_for_visibility_of_all_elements(RadioButtonPage.RADIO_BUTTONS))
        for i in range(len_list_of_radio_buttons):
            try:
                list_of_radio_buttons = self.wait_for_visibility_of_all_elements(RadioButtonPage.RADIO_BUTTONS)
                radio_button = list_of_radio_buttons[i]
                find_a_preceding_sibling = radio_button.find_element(*RadioButtonPage.PRECEDING_SIBLING_FOR_RADIO_BTNS)
                if find_a_preceding_sibling.is_enabled():
                    list_of_clicked_radiobutt.append(radio_button.text)
                    time.sleep(3)
                    radio_button.click()
                    log.info(f'Clicked on "{radio_button.text}" radio button')
                    list_of_output_radiobutt.append(self.get_text(RadioButtonPage.OUTPUT_TEXT))
            except StaleElementReferenceException as e:
                log.warning(f'StaleElementReferenceException. {e}', exc_info=True)
        return list_of_clicked_radiobutt, list_of_output_radiobutt


