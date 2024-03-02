from helpers.methods_to_interact_with_pages import MethodsToInteractWithPages
from interaction_with_web_pages.page_objects.menu_bar import MenuBar
from selenium.webdriver.common.by import By
import random


class CheckBoxPage(MethodsToInteractWithPages):
    BTN_EXPAND_ALL = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    TITLES_OF_CHECKBOXES = (By.CSS_SELECTOR, '[class="rct-title"]')
    ICON_CHECK = (By.CSS_SELECTOR, '[class="rct-icon rct-icon-check"]')
    ancestor_for_checked_checkboxes = (By.XPATH, './/ancestor::span[@class="rct-text"]')
    RESULT_ROW_OF_SELECTED_CHECKBOXES = (By.XPATH, '//div/span[@class="text-success"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.menu_bar = MenuBar(self.driver)
        self.url = f'{self.base_url}/checkbox'

    def click_on_expand_all_btn(self) -> None:
        self.click_on(CheckBoxPage.BTN_EXPAND_ALL)

    def click_on_random_checkboxes(self) -> None:
        """Клік рандомну непарну к-сть разів на рандомні чекбокси"""
        self.remove_advertising_in_footer()
        list_of_all_checkboxes = self.wait_for_visibility_of_all_elements(CheckBoxPage.TITLES_OF_CHECKBOXES)
        for i in range(3, 9, 2):
            random_number = random.randint(1, 16)
            random_checkbox = list_of_all_checkboxes[random_number]
            random_checkbox.click()

    def get_titles_of_checked_checkboxes(self) -> list[str]:
        checked_checkboxes = self.wait_for_visibility_of_all_elements(CheckBoxPage.ICON_CHECK)

        titles_of_checked_checkboxes = []
        for checked_checkbox in checked_checkboxes:
            find_ancestor = checked_checkbox.find_element(*CheckBoxPage.ancestor_for_checked_checkboxes)
            titles_of_checked_checkboxes.append(find_ancestor.text.lower().replace(".doc", '').replace(" ", ''))
        return titles_of_checked_checkboxes

    def get_output_result(self) -> list[str]:
        """повертає назви чекбоксів, що виводяться в рядку 'You have selected' """
        result_row_of_selected_checkboxes = self.wait_for_visibility_of_all_elements(CheckBoxPage.RESULT_ROW_OF_SELECTED_CHECKBOXES)
        list_of_selected_checkboxes = [selected_checkbox.text.lower().replace(" ", '')
                                       for selected_checkbox in result_row_of_selected_checkboxes]
        return list_of_selected_checkboxes
