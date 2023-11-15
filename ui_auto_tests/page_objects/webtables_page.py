from ui_auto_tests.data import TestData
from ui_auto_tests.page_objects.header_section_and_menu_bar import HeaderSectionAndMenuBar
from selenium.webdriver.common.by import By
from ui_auto_tests.locators import WebTablesPageLocators
from selenium.webdriver.support.select import Select


class WebTablesPage(HeaderSectionAndMenuBar):
    def click_on_btn_add(self) -> None:
        """цей метод відкриває Registration form"""
        self.click_on(By.CSS_SELECTOR, WebTablesPageLocators.BTN_ADD)

    def fill_in_fields_on_the_registration_form(self) -> str:
        """цей метод дозволяє заповнити поля в Registration form"""
        self.set_data(By.CSS_SELECTOR, WebTablesPageLocators.TXT_FIRST_NAME, TestData.first_name)
        self.set_data(By.CSS_SELECTOR, WebTablesPageLocators.TXT_LAST_NAME, TestData.last_name)
        self.set_data(By.CSS_SELECTOR, WebTablesPageLocators.TXT_USER_EMAIL, TestData.email)
        self.set_data(By.CSS_SELECTOR, WebTablesPageLocators.TXT_AGE, TestData.age)
        self.set_data(By.CSS_SELECTOR, WebTablesPageLocators.TXT_SALARY, TestData.salary)
        self.set_data(By.CSS_SELECTOR, WebTablesPageLocators.TXT_DEPARTMENT, TestData.department)
        return f'{TestData.first_name} {TestData.last_name} {TestData.age} {TestData.email} {TestData.salary} {TestData.department}'

    def click_on_btn_submit(self) -> None:
        self.click_on(By.CSS_SELECTOR, WebTablesPageLocators.BTN_SUBMIT)

    def get_text_from_rows(self) -> list:
        """цей метод повертає список значень всіх рядків таблиці"""
        list_rows = self.wait_for_visibility_of_all_elements(By.CSS_SELECTOR, WebTablesPageLocators.ROWS)
        txt_from_rows = []
        for i in list_rows:
            txt_from_rows.append(i.text.replace('\n', ' '))
        return txt_from_rows

    def search_by_email(self, email=TestData.email) -> str:
        """цей метод виконує пошук за ел адресою"""
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.TXT_SEARCH).clear()
        self.set_data(By.CSS_SELECTOR, WebTablesPageLocators.TXT_SEARCH, email)
        return email

    def set_new_email(self) -> str:
        """апдейт емейлу"""
        self.click_on(By.CSS_SELECTOR, WebTablesPageLocators.BTN_EDIT)
        self.clear_field(By.CSS_SELECTOR, WebTablesPageLocators.TXT_USER_EMAIL)
        self.set_data(By.CSS_SELECTOR, WebTablesPageLocators.TXT_USER_EMAIL, TestData.new_email)
        self.click_on_btn_submit()
        return TestData.new_email

    def remove_record(self) -> None:
        """цей метод видаляє новий запис з таблиці"""
        self.click_on(By.CSS_SELECTOR, WebTablesPageLocators.BTN_DELETE)

    def get_the_checking_text(self) -> str:
        """цей метод повертає текст, який підтверджує, що рядок з заданим емейлом не знайдено """
        return self.get_text(By.CSS_SELECTOR, WebTablesPageLocators.THE_CHECKING_TEXT)

    def quantity_of_rows(self) -> tuple:
        """цей метод: 1)змінює к-сть рядків таблиці що відображаються на сторінці;
        2) підраховує к-сть рядків, що фактично відображено в таблиці"""
        wait_for_btn_the_quantity_of_rows = self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.BTN_THE_QUANTITY_OF_ROWS)
        select = Select(wait_for_btn_the_quantity_of_rows)
        list_of_options = select.options
        list_of_clicked_options = []
        list_of_counted_rows = []

        for i in list_of_options:
            self.scroll_js(By.CSS_SELECTOR, WebTablesPageLocators.BTN_THE_QUANTITY_OF_ROWS)
            i.click()
            list_of_clicked_options.append(i.text.replace(' rows', ''))
            actual_quantity_rows = self.wait_for_visibility_of_all_elements(By.CSS_SELECTOR, WebTablesPageLocators.ROWS)
            list_of_counted_rows.append(str(len(actual_quantity_rows)))
        return list_of_clicked_options, list_of_counted_rows



