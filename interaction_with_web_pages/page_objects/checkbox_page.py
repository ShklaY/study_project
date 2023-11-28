from interaction_with_web_pages.page_objects.menu_bar import MenuBar
from selenium.webdriver.common.by import By
import random


class CheckBoxPage(MenuBar):
    BTN_EXPAND_ALL = 'button[title="Expand all"]'
    TITLES_OF_CHECKBOXES = '[class="rct-title"]'
    ICON_CHECK = '[class="rct-icon rct-icon-check"]'
    ancestor_for_checked_checkboxes = './/ancestor::span[@class="rct-text"]'
    RESULT_ROW_OF_SELECTED_CHECKBOXES = '//div/span[@class="text-success"]'

    def click_on_btn_expand_all(self) -> None:
        self.click_on(By.CSS_SELECTOR, CheckBoxPage.BTN_EXPAND_ALL)

    def click_on_random_checkboxes(self) -> None:
        """Клік рандомну непарну к-сть разів на рандомні чекбокси"""
        self.remove_advertising_in_footer()
        list_of_all_checkboxes = self.wait_for_visibility_of_all_elements(By.CSS_SELECTOR, CheckBoxPage.TITLES_OF_CHECKBOXES)
        for i in range(3, 9, 2):
            random_number = random.randint(1, 16)
            random_checkbox = list_of_all_checkboxes[random_number]
            random_checkbox.click()

    def get_titles_of_checked_checkboxes(self) -> list:
        checked_checkboxes = self.wait_for_visibility_of_all_elements(By.CSS_SELECTOR, CheckBoxPage.ICON_CHECK)

        titles_of_checked_checkboxes = []
        # TODO i - bad naming for temp variable, checked_checkbox - is better
        for checked_checkbox in checked_checkboxes:
            find_ancestor = checked_checkbox.find_element(By.XPATH, self.ancestor_for_checked_checkboxes)
            titles_of_checked_checkboxes.append(find_ancestor.text.lower().replace(".doc", '').replace(" ", ''))
        return titles_of_checked_checkboxes

    def get_output_result(self) -> list:
        """повертає назви чекбоксів, що виводяться в рядку 'You have selected' """
        result_row_of_selected_checkboxes = self.wait_for_visibility_of_all_elements(By.XPATH, CheckBoxPage.RESULT_ROW_OF_SELECTED_CHECKBOXES)
        list_of_selected_checkboxes = []
        # TODO i - bad naming for temp variable
        for selected_checkbox in result_row_of_selected_checkboxes:
            list_of_selected_checkboxes.append(selected_checkbox.text.lower().replace(" ", ''))
        return list_of_selected_checkboxes
