from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from ui_auto_tests.locators import PracticeFormPageLocators
from ui_auto_tests.data import TestData, DataStateAndCity
from ui_auto_tests.page_objects.header_section_and_menu_bar import HeaderSectionAndMenuBar


class PracticeFormPage(HeaderSectionAndMenuBar):
    def set_student_registration_form(self) -> tuple:
        """введення імені, прізвища, емейлу, №тел; вибір гендеру"""
        self.remove_advertising_in_footer()
        self.set_data(By.CSS_SELECTOR, PracticeFormPageLocators.TXT_FIRST_NAME, TestData.first_name)
        self.set_data(By.CSS_SELECTOR, PracticeFormPageLocators.TXT_LAST_NAME, TestData.last_name)
        self.set_data(By.CSS_SELECTOR, PracticeFormPageLocators.TXT_EMAIL, TestData.email)

        self.click_on(By.CSS_SELECTOR, PracticeFormPageLocators.RADIO_BTN_GENDER)
        chosen_gender = self.get_text(By.CSS_SELECTOR, PracticeFormPageLocators.RADIO_BTN_GENDER)

        self.set_data(By.CSS_SELECTOR, PracticeFormPageLocators.TXT_MOBILE_NUMBER, TestData.phone_number)
        """вибір предмету* """
        self.helper(PracticeFormPageLocators.TXT_SUBJECTS, TestData.subject)
        """вибір хоббі, введення адреси"""
        self.click_on(By.CSS_SELECTOR, PracticeFormPageLocators.HOBBIES)
        chosen_hobby = self.get_text(By.CSS_SELECTOR, PracticeFormPageLocators.HOBBIES)

        self.set_data(By.CSS_SELECTOR, PracticeFormPageLocators.TXT_CURRENT_ADDRESS, TestData.current_address)
        """вибір штату* """
        self.click_on(By.CSS_SELECTOR, PracticeFormPageLocators.SELECT_STATE)
        self.helper(PracticeFormPageLocators.LOCATOR_INPUT_STATE, DataStateAndCity.random_state)
        """вибір міста* """
        self.click_on(By.CSS_SELECTOR, PracticeFormPageLocators.SELECT_CITY)
        self.helper(PracticeFormPageLocators.LOCATOR_INPUT_CITY, DataStateAndCity.random_city)
        """клік на кнпку submit"""
        self.click_on(By.CSS_SELECTOR, PracticeFormPageLocators.BTN_SUBMIT)
        return TestData.first_name, TestData.last_name, TestData.email, chosen_gender, str(TestData.phone_number), \
               TestData.subject, chosen_hobby, TestData.current_address, DataStateAndCity.random_state, DataStateAndCity.random_city

    def helper(self, locator: str, data: str or int) -> None:
        """допоміжний метод для взаємодії з полями Subjects, State and City"""
        self.set_data(By.CSS_SELECTOR, locator, data)
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, locator).send_keys(Keys.ENTER)

    def get_data_result(self) -> list:
        """цей метод повертає дані з підтверджувальної таблиці"""
        table = self.wait_for_visibility_of_all_elements(By.XPATH, PracticeFormPageLocators.RESULT_TABLE)
        list_with_data_result = []
        for i in table:
            list_with_data_result.append(i.text)
        return list_with_data_result


