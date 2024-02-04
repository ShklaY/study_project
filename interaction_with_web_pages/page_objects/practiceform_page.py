from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from interaction_with_web_pages.methods_to_interact_with_pages import MethodsToInteractWithPages
from interaction_with_web_pages.user_model import UserModel
from interaction_with_web_pages.page_objects.menu_bar import MenuBar
import random
from typing import Self


class PracticeFormPage(MethodsToInteractWithPages):
    TXT_FIRST_NAME = (By.CSS_SELECTOR, '[id="firstName"]')
    TXT_LAST_NAME = (By.CSS_SELECTOR, '[id="lastName"]')
    TXT_EMAIL = (By.CSS_SELECTOR, '[id="userEmail"]')
    RADIO_BTN_GENDER = (By.CSS_SELECTOR, f'[for="gender-radio-{random.randint(1, 3)}"]')
    TXT_MOBILE_NUMBER = (By.CSS_SELECTOR, '[id="userNumber"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, '[id="dateOfBirthInput"]')
    TXT_SUBJECTS = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES = (By.CSS_SELECTOR, f'[for="hobbies-checkbox-{random.randint(1, 3)}"]')
    TXT_CURRENT_ADDRESS = (By.CSS_SELECTOR, '[id="currentAddress"]')

    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    LOCATOR_INPUT_STATE = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    LOCATOR_INPUT_CITY = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    BTN_SUBMIT = (By.CSS_SELECTOR, '[id="submit"]')

    RESULT_TABLE = (By.XPATH, '//tr/td[2]')

    def __init__(self, driver):
        super().__init__(driver)
        self.menu_bar = MenuBar(self.driver)

    def set_new_student(self,
                        first_name: UserModel,
                        last_name: UserModel,
                        email: UserModel,
                        phone_number: UserModel,
                        subject: UserModel,
                        current_address: UserModel,
                        state: UserModel,
                        city: UserModel) -> tuple[str, str]:
        self.remove_advertising_in_footer() \
            .set_data(PracticeFormPage.TXT_FIRST_NAME, first_name) \
            .set_data(PracticeFormPage.TXT_LAST_NAME, last_name) \
            .set_data(PracticeFormPage.TXT_EMAIL, email) \
            .click_on(PracticeFormPage.RADIO_BTN_GENDER) \
            .set_data(PracticeFormPage.TXT_MOBILE_NUMBER, phone_number) \
            .helper(PracticeFormPage.TXT_SUBJECTS, subject) \
            .click_on(PracticeFormPage.HOBBIES) \
            .set_data(PracticeFormPage.TXT_CURRENT_ADDRESS, current_address) \
            .click_on(PracticeFormPage.SELECT_STATE) \
            .helper(PracticeFormPage.LOCATOR_INPUT_STATE, state) \
            .click_on(PracticeFormPage.SELECT_CITY) \
            .helper(PracticeFormPage.LOCATOR_INPUT_CITY, city) \
            .click_on(PracticeFormPage.BTN_SUBMIT)

        chosen_gender = self.get_text(PracticeFormPage.RADIO_BTN_GENDER)
        chosen_hobby = self.get_text(PracticeFormPage.HOBBIES)
        return chosen_gender, chosen_hobby

    def helper(self, locator: tuple, data: UserModel) -> Self:
        """допоміжний метод для взаємодії з полями Subjects, State and City"""
        self.set_data(locator, data) \
            .wait_for_visibility_of_el(locator).send_keys(Keys.ENTER)
        return self

    def get_data_of_registered_student(self) -> list[str]:
        """цей метод повертає дані з підтверджувальної таблиці"""
        table = self.wait_for_visibility_of_all_elements(PracticeFormPage.RESULT_TABLE)
        list_with_data_of_registered_student = [row.text for row in table]
        return list_with_data_of_registered_student


