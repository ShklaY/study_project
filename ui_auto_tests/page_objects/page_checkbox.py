from ui_auto_tests.page_objects.header_section_and_menu_bar import HeaderSectionAndMenuBar
from selenium.webdriver.common.by import By
from ui_auto_tests.locators import CheckBoxPageLocators
import random


class CheckBoxPage(HeaderSectionAndMenuBar):
    """сторінка Check Box: містить локатори веб елементів та методи для взаємодії з ними"""

    def click_on_btn_expand_all(self) -> None:
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, CheckBoxPageLocators.btn_expand_all).click()

    def click_on_random_checkboxes(self) -> None:
        """Клік рандомну непарну к-сть разів на рандомні чекбокси"""
        list_of_all_checkboxes = self.wait_for_visibility_of_all_elements(By.CSS_SELECTOR, CheckBoxPageLocators.titles_of_checkboxes)
        for i in range(3, 9, 2):
            random_number = random.randint(1, 16)
            random_checkbox = list_of_all_checkboxes[random_number]
            self.scroll_js(random_checkbox)
            random_checkbox.click()

    def get_titles_of_checked_checkboxes(self) -> list:
        """цей метод повертає назви всіх відмічених чекбоксів"""
        checked_checkboxes = self.wait_for_visibility_of_all_elements(By.CSS_SELECTOR, '[class="rct-icon rct-icon-check"]')
        ancestor_for_checked_checkboxes = './/ancestor::span[@class="rct-text"]'
        titles_of_checked_checkboxes = []
        for i in checked_checkboxes:
            find_ancestor = i.find_element(By.XPATH, ancestor_for_checked_checkboxes)
            titles_of_checked_checkboxes.append(find_ancestor.text.lower().replace(".doc", '').replace(" ", ''))
        return titles_of_checked_checkboxes

    def get_output_result(self) -> list:
        """цей метод повертає назви чекбоксів, що виводяться в рядку 'You have selected' """
        row_of_selected_checkboxes = self.wait_for_visibility_of_all_elements(By.XPATH, '//div/span[@class="text-success"]')
        list_of_selected_checkboxes = []
        for i in row_of_selected_checkboxes:
            list_of_selected_checkboxes.append(i.text.lower().replace(" ", ''))
        return list_of_selected_checkboxes
