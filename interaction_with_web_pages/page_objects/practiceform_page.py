from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from interaction_with_web_pages.user_model import UserModel
from interaction_with_web_pages.page_objects.menu_bar import MenuBar
import random


class PracticeFormPage(MenuBar):
    TXT_FIRST_NAME = '[id="firstName"]'
    TXT_LAST_NAME = '[id="lastName"]'
    TXT_EMAIL = '[id="userEmail"]'
    RADIO_BTN_GENDER = f'[for="gender-radio-{random.randint(1, 3)}"]'
    TXT_MOBILE_NUMBER = '[id="userNumber"]'
    DATE_OF_BIRTH = '[id="dateOfBirthInput"]'
    TXT_SUBJECTS = 'input[id="subjectsInput"]'
    HOBBIES = f'[for="hobbies-checkbox-{random.randint(1, 3)}"]'
    PICTURE = ''
    TXT_CURRENT_ADDRESS = '[id="currentAddress"]'

    SELECT_STATE = 'div[id="state"]'
    LOCATOR_INPUT_STATE = 'input[id="react-select-3-input"]'
    SELECT_CITY = 'div[id="city"]'
    LOCATOR_INPUT_CITY = 'input[id="react-select-4-input"]'
    BTN_SUBMIT = '[id="submit"]'

    RESULT_TABLE = '//tr/td[2]'

    def set_new_student(self,
                        first_name: UserModel,
                        last_name: UserModel,
                        email: UserModel,
                        phone_number: UserModel,
                        subject: UserModel,
                        current_address: UserModel,
                        state: UserModel,
                        city: UserModel) -> tuple:
        self.remove_advertising_in_footer()
        self.set_data(By.CSS_SELECTOR, PracticeFormPage.TXT_FIRST_NAME, first_name)
        self.set_data(By.CSS_SELECTOR, PracticeFormPage.TXT_LAST_NAME, last_name)
        self.set_data(By.CSS_SELECTOR, PracticeFormPage.TXT_EMAIL, email)

        self.click_on(By.CSS_SELECTOR, PracticeFormPage.RADIO_BTN_GENDER)
        chosen_gender = self.get_text(By.CSS_SELECTOR, PracticeFormPage.RADIO_BTN_GENDER)

        self.set_data(By.CSS_SELECTOR, PracticeFormPage.TXT_MOBILE_NUMBER, phone_number)
        """вибір предмету* """
        self.helper(PracticeFormPage.TXT_SUBJECTS, subject)
        """вибір хоббі, введення адреси"""
        self.click_on(By.CSS_SELECTOR, PracticeFormPage.HOBBIES)
        chosen_hobby = self.get_text(By.CSS_SELECTOR, PracticeFormPage.HOBBIES)

        self.set_data(By.CSS_SELECTOR, PracticeFormPage.TXT_CURRENT_ADDRESS, current_address)
        """вибір штату* """
        self.click_on(By.CSS_SELECTOR, PracticeFormPage.SELECT_STATE)
        self.helper(PracticeFormPage.LOCATOR_INPUT_STATE, state)
        """вибір міста* """
        self.click_on(By.CSS_SELECTOR, PracticeFormPage.SELECT_CITY)
        self.helper(PracticeFormPage.LOCATOR_INPUT_CITY, city)
        """клік на кнпку submit"""
        self.click_on(By.CSS_SELECTOR, PracticeFormPage.BTN_SUBMIT)
        return chosen_gender, chosen_hobby

    def helper(self, locator: str, data: UserModel) -> None:
        """допоміжний метод для взаємодії з полями Subjects, State and City"""
        self.set_data(By.CSS_SELECTOR, locator, data)
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, locator).send_keys(Keys.ENTER)

    def get_data_of_registered_student(self) -> list:
        """цей метод повертає дані з підтверджувальної таблиці"""
        table = self.wait_for_visibility_of_all_elements(By.XPATH, PracticeFormPage.RESULT_TABLE)
        list_with_data_of_registered_student = []
        for row in table:
            list_with_data_of_registered_student.append(row.text)
        return list_with_data_of_registered_student


