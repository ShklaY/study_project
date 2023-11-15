from ui_auto_tests.data import TestData
from ui_auto_tests.page_objects.header_section_and_menu_bar import HeaderSectionAndMenuBar
from selenium.webdriver.common.by import By
from ui_auto_tests.locators import WebTablesPageLocators
from selenium.webdriver.support.select import Select


class WebTablesPage(HeaderSectionAndMenuBar):
    """сторінка Web Tables: містить локатори веб елементів та методи для взаємодії з ними"""

    def click_on_btn_add(self) -> None:
        """цей метод відкриває Registration form"""
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.btn_add).click()

    def fill_in_fields_on_the_registration_form(self) -> str:
        """цей метод дозволяє заповнити поля в Registration form"""
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.txt_first_name).send_keys(TestData.first_name)
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.txt_last_name).send_keys(TestData.last_name)
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.txt_user_email).send_keys(TestData.email)
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.txt_age).send_keys(TestData.age)
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.txt_salary).send_keys(TestData.salary)
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.txt_department).send_keys(TestData.department)
        return f'{TestData.first_name} {TestData.last_name} {TestData.age} {TestData.email} {TestData.salary} {TestData.department}'

    def click_on_btn_submit(self) -> None:
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.btn_submit).click()

    def get_text_from_rows(self) -> list:
        """цей метод повертає список значень всіх рядків таблиці"""
        list_rows = self.wait_for_visibility_of_all_elements(By.CSS_SELECTOR, WebTablesPageLocators.rows)
        txt_from_rows = []
        for i in list_rows:
            txt_from_rows.append(i.text.replace('\n', ' '))
        return txt_from_rows

    def perform_search_by_email(self, email=TestData.email) -> str:
        """цей метод виконує пошук за ел адресою"""
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.txt_search).clear()
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.txt_search).send_keys(email)
        return email

    def set_new_email(self) -> str:
        """апдейт емейлу"""
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.btn_edit).click()
        user_email = self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.txt_user_email)
        user_email.clear()
        user_email.send_keys(TestData.new_email)
        self.click_on_btn_submit()
        return TestData.new_email

    def remove_record(self) -> None:
        """цей метод видаляє новий запис з таблиці"""
        self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.btn_delete).click()

    def get_the_checking_text(self) -> str:
        """цей метод повертає текст, який підтверджує, що рядок з заданим емейлом не знайдено """
        return self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.the_checking_text).text

    def quantity_of_rows(self) -> tuple:
        """цей метод: 1)змінює к-сть рядків таблиці що відображаються на сторінці;
        2) підраховує к-сть рядків, що фактично відображено в таблиці"""
        wait_for_btn_the_quantity_of_rows = self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPageLocators.btn_the_quantity_of_rows)
        select = Select(wait_for_btn_the_quantity_of_rows)
        list_of_options = select.options
        list_of_clicked_options = []
        list_of_counted_rows = []

        for i in list_of_options:
            self.scroll_js(wait_for_btn_the_quantity_of_rows)
            i.click()
            list_of_clicked_options.append(i.text.replace(' rows', ''))
            actual_quantity_rows = self.wait_for_visibility_of_all_elements(By.CSS_SELECTOR, WebTablesPageLocators.rows)
            list_of_counted_rows.append(str(len(actual_quantity_rows)))
        return list_of_clicked_options, list_of_counted_rows



