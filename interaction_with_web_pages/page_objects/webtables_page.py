from helpers.methods_to_interact_with_pages import MethodsToInteractWithPages
from helpers.custom_types import UserModel
from interaction_with_web_pages.page_objects.menu_bar import MenuBar
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from helpers.custom_types import ActualAndExpectedResult


class WebTablesPage(MethodsToInteractWithPages):
    BTN_ADD = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    TXT_FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    TXT_LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    TXT_USER_EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    TXT_AGE = (By.CSS_SELECTOR, 'input[id="age"]')
    TXT_SALARY = (By.CSS_SELECTOR, 'input[id="salary"]')
    TXT_DEPARTMENT = (By.CSS_SELECTOR, 'input[id="department"]')
    BTN_SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')
    ROWS = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')

    TXT_SEARCH = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    BTN_EDIT = (By.CSS_SELECTOR, '[title="Edit"]')
    BTN_DELETE = (By.CSS_SELECTOR, '[title="Delete"]')
    THE_CHECKING_TEXT = (By.CSS_SELECTOR, '[class="rt-noData"]')

    BTN_THE_QUANTITY_OF_ROWS = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.menu_bar = MenuBar(self.driver)
        self.url = f'{self.base_url}/webtables'

    def click_on_add_btn(self) -> None:
        """цей метод відкриває Registration form"""
        self.remove_advertising_in_footer().\
            click_on(WebTablesPage.BTN_ADD)

    def fill_all_fields(self, first_name: UserModel, last_name: UserModel, email: UserModel, age: UserModel, salary: UserModel, department: UserModel) -> str:
        """цей метод дозволяє заповнити поля в Registration form"""
        self.set_data(WebTablesPage.TXT_FIRST_NAME, first_name)\
            .set_data(WebTablesPage.TXT_LAST_NAME, last_name)\
            .set_data(WebTablesPage.TXT_USER_EMAIL, email)\
            .set_data(WebTablesPage.TXT_AGE, age)\
            .set_data(WebTablesPage.TXT_SALARY, salary)\
            .set_data(WebTablesPage.TXT_DEPARTMENT, department)
        return f'{first_name} {last_name} {age} {email} {salary} {department}'

    def click_on_submit_btn(self) -> None:
        self.click_on(WebTablesPage.BTN_SUBMIT)

    def get_text_from_rows(self) -> list:
        """цей метод повертає список значень всіх рядків таблиці"""
        list_rows = self.wait_for_visibility_of_all_elements(WebTablesPage.ROWS)
        txt_from_rows = [row.text.replace('\n', ' ') for row in list_rows]
        return txt_from_rows

    def set_email_in_search_field(self, email: UserModel) -> None:
        """цей метод виконує пошук за ел адресою"""
        self.clear_field(WebTablesPage.TXT_SEARCH)\
            .set_data(WebTablesPage.TXT_SEARCH, email)

    def update_email(self, new_email: UserModel) -> None:
        self.click_on(WebTablesPage.BTN_EDIT)\
            .clear_field(WebTablesPage.TXT_USER_EMAIL)\
            .set_data(WebTablesPage.TXT_USER_EMAIL, new_email)\
            .click_on_submit_btn()

    def remove_new_record(self) -> None:
        """цей метод видаляє новий запис з таблиці"""
        self.click_on(WebTablesPage.BTN_DELETE)

    def get_the_checking_text(self) -> str:
        """цей метод повертає текст, який підтверджує, що рядок з заданим емейлом не знайдено """
        return self.get_text(WebTablesPage.THE_CHECKING_TEXT)

    def quantity_of_rows(self) -> ActualAndExpectedResult:
        """цей метод: 1)змінює к-сть рядків таблиці що відображаються на сторінці;
        2) підраховує к-сть рядків, що фактично відображено в таблиці"""
        wait_for_btn_the_quantity_of_rows = self.wait_for_visibility_of_el(WebTablesPage.BTN_THE_QUANTITY_OF_ROWS)
        select = Select(wait_for_btn_the_quantity_of_rows)
        list_of_options = select.options
        results: ActualAndExpectedResult = {
            'expected': [],
            'actual': []
        }

        for option in list_of_options:
            self.scroll_js(WebTablesPage.BTN_THE_QUANTITY_OF_ROWS)
            option.click()
            results['expected'].append(option.text.replace(' rows', ''))
            actual_quantity_rows = self.wait_for_visibility_of_all_elements(WebTablesPage.ROWS)
            results['actual'].append(str(len(actual_quantity_rows)))
        return results



