from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from ui_auto_tests.locators import PracticeFormPageLocators
from ui_auto_tests.data import TestData, DataStateAndCity
from ui_auto_tests.page_objects.header_section_and_menu_bar import HeaderSectionAndMenuBar


class PracticeFormPage(HeaderSectionAndMenuBar):
    """сторінка Practice Form: містить локатори веб елементів та методи для взаємодії з ними"""

    def set_student_registration_form(self) -> tuple:
        """введення імені, прізвища, емейлу, №тел; вибір гендеру"""
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, PracticeFormPageLocators.txt_first_name).send_keys(TestData.first_name)
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, PracticeFormPageLocators.txt_last_name).send_keys(TestData.last_name)
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, PracticeFormPageLocators.txt_email).send_keys(TestData.email)

        wait_for_radio_btn_gender = self.wait_for_visibility_of_el(By.CSS_SELECTOR, PracticeFormPageLocators.radio_btn_gender)
        wait_for_radio_btn_gender.click()
        chosen_gender = wait_for_radio_btn_gender.text

        self.wait_for_visibility_of_el(By.CSS_SELECTOR, PracticeFormPageLocators.txt_mobile_number).send_keys(TestData.phone_number)
        """вибір предмету* """
        self.helper(PracticeFormPageLocators.txt_subjects, TestData.subject)
        """вибір хоббі, введення адреси"""
        wait_for_hobbies = self.wait_for_visibility_of_el(By.CSS_SELECTOR, PracticeFormPageLocators.hobbies)
        wait_for_hobbies.click()
        chosen_hobby = wait_for_hobbies.text

        self.wait_for_visibility_of_el(By.CSS_SELECTOR, PracticeFormPageLocators.txt_current_address).send_keys(TestData.current_address)
        """вибір штату* """
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, PracticeFormPageLocators.select_state).click()
        self.helper(PracticeFormPageLocators.locator_input_state, DataStateAndCity.random_state)
        """вибір міста* """
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, PracticeFormPageLocators.select_city).click()
        self.helper(PracticeFormPageLocators.locator_input_city, DataStateAndCity.random_city)
        """клік на кнпку submit"""
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, PracticeFormPageLocators.btn_submit).click()
        return TestData.first_name, TestData.last_name, TestData.email, chosen_gender, str(TestData.phone_number), \
               TestData.subject, chosen_hobby, TestData.current_address, DataStateAndCity.random_state, DataStateAndCity.random_city

    def helper(self, locator: str, data: str or int) -> None:
        """допоміжний метод для взаємодії з полями Subjects, State and City"""
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, locator).send_keys(data)
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, locator).send_keys(Keys.ENTER)

    def get_data_result(self) -> list:
        """цей метод повертає дані з підтверджувальної таблиці"""
        table = self.wait_for_visibility_of_all_elements(By.XPATH, PracticeFormPageLocators.result_table)
        list_with_data_result = []
        for i in table:
            list_with_data_result.append(i.text)
        return list_with_data_result


