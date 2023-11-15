from ui_auto_tests.page_objects.header_section_and_menu_bar import HeaderSectionAndMenuBar
from selenium.webdriver.common.by import By
from ui_auto_tests.locators import RadioButtonPageLocators


class RadioButtonPage(HeaderSectionAndMenuBar):
    """сторінка Radio Button: містить локатори веб елементів та методи для взаємодії з ними"""

    def click_on_radio_buttons_and_get_output_text(self) -> tuple:
        """цей метод повертає списки: 1й містить усі назви клікнутих радіобатонів,
        2й список - назви радіобатонів, що відображались на сторінці після тексту 'You have selected' """
        list_of_radio_buttons = self.wait_for_visibility_of_all_elements(By.XPATH, RadioButtonPageLocators.radio_buttons)
        list_of_clicked_radiobutt = []
        list_of_output_radiobutt = []
        for i in list_of_radio_buttons:
            find_a_preceding_sibling = i.find_element(By.XPATH, RadioButtonPageLocators.preceding_sibling_for_radio_btns)
            if find_a_preceding_sibling.is_enabled():
                list_of_clicked_radiobutt.append(i.text)
                i.click()
                list_of_output_radiobutt.append(
                    self.wait_for_visibility_of_el(By.CSS_SELECTOR, RadioButtonPageLocators.output_text).text)
        return list_of_clicked_radiobutt, list_of_output_radiobutt


