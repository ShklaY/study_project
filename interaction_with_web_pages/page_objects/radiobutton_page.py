from selenium.common import StaleElementReferenceException
from interaction_with_web_pages.methods_to_interact_with_pages import MethodsToInteractWithPages
from interaction_with_web_pages.page_objects.menu_bar import MenuBar
from selenium.webdriver.common.by import By
from helpers.logger import log
from interaction_with_web_pages.results_helper import ResultsHelper


class RadioButtonPage(MethodsToInteractWithPages):
    RADIO_BUTTONS = (By.XPATH, "//label[contains(@class, 'custom-control-label')]")
    OUTPUT_TEXT = (By.CSS_SELECTOR, '[class="text-success"]')
    PRECEDING_SIBLING_FOR_RADIO_BTNS = (By.XPATH, ".//preceding-sibling::input")
    RESULT_ROW_OF_SELECTED_CHECKBOXES = (By.XPATH, '//div/span[@class="text-success"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.menu_bar = MenuBar(self.driver)

    def click_on_radio_buttons_and_get_output_text(self) -> ResultsHelper:
        """ключ 'expected_res' містить усі назви клікнутих радіобатонів,
        ключ 'actual_res' містить назви радіобатонів, що відображались на сторінці після тексту 'You have selected' """
        results: ResultsHelper = {
            'expected': [],
            'actual': []
        }
        len_list_of_radio_buttons = len(self.wait_for_visibility_of_all_elements(RadioButtonPage.RADIO_BUTTONS))
        for i in range(len_list_of_radio_buttons):
            try:
                list_of_radio_buttons = self.wait_for_visibility_of_all_elements(RadioButtonPage.RADIO_BUTTONS)
                radio_button = list_of_radio_buttons[i]
                find_a_preceding_sibling = radio_button.find_element(*RadioButtonPage.PRECEDING_SIBLING_FOR_RADIO_BTNS)
                if find_a_preceding_sibling.is_enabled():
                    results['expected'].append(radio_button.text)
                    radio_button.click()
                    log.info(f'Clicked on "{radio_button.text}" radio button')
                    results['actual'].append(self.get_text(RadioButtonPage.OUTPUT_TEXT))
            except StaleElementReferenceException as e:
                log.warning(f'StaleElementReferenceException. {e}', exc_info=True)
        return results


