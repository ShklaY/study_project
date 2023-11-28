from interaction_with_web_pages.user_model import UserModel
from interaction_with_web_pages.page_objects.menu_bar import MenuBar
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class WebTablesPage(MenuBar):
    BTN_ADD = 'button[id="addNewRecordButton"]'
    TXT_FIRST_NAME = 'input[id="firstName"]'
    TXT_LAST_NAME = 'input[id="lastName"]'
    TXT_USER_EMAIL = 'input[id="userEmail"]'
    TXT_AGE = 'input[id="age"]'
    TXT_SALARY = 'input[id="salary"]'
    TXT_DEPARTMENT = 'input[id="department"]'
    BTN_SUBMIT = 'button[id="submit"]'
    ROWS = 'div[class="rt-tr-group"]'

    TXT_SEARCH = 'input[id="searchBox"]'
    BTN_EDIT = '[title="Edit"]'
    BTN_DELETE = '[title="Delete"]'
    THE_CHECKING_TEXT = '[class="rt-noData"]'

    BTN_THE_QUANTITY_OF_ROWS = 'select[aria-label="rows per page"]'

    def click_on_btn_add(self) -> None:
        """цей метод відкриває Registration form"""
        self.click_on(By.CSS_SELECTOR, WebTablesPage.BTN_ADD)

    def fill_all_fields(self, first_name: UserModel, last_name: UserModel, email: UserModel, age: UserModel, salary: UserModel, department: UserModel) -> str:
        """цей метод дозволяє заповнити поля в Registration form"""
        self.set_data(By.CSS_SELECTOR, WebTablesPage.TXT_FIRST_NAME, first_name)
        self.set_data(By.CSS_SELECTOR, WebTablesPage.TXT_LAST_NAME, last_name)
        self.set_data(By.CSS_SELECTOR, WebTablesPage.TXT_USER_EMAIL, email)
        self.set_data(By.CSS_SELECTOR, WebTablesPage.TXT_AGE, age)
        self.set_data(By.CSS_SELECTOR, WebTablesPage.TXT_SALARY, salary)
        self.set_data(By.CSS_SELECTOR, WebTablesPage.TXT_DEPARTMENT, department)
        return f'{first_name} {last_name} {age} {email} {salary} {department}'

    def click_on_btn_submit(self) -> None:
        self.click_on(By.CSS_SELECTOR, WebTablesPage.BTN_SUBMIT)

    def get_text_from_rows(self) -> list:
        """цей метод повертає список значень всіх рядків таблиці"""
        list_rows = self.wait_for_visibility_of_all_elements(By.CSS_SELECTOR, WebTablesPage.ROWS)
        txt_from_rows = []
        for row in list_rows:
            txt_from_rows.append(row.text.replace('\n', ' '))
        return txt_from_rows

    def set_email_in_search_field(self, email: UserModel) -> None:
        """цей метод виконує пошук за ел адресою"""
        self.clear_field(By.CSS_SELECTOR, WebTablesPage.TXT_SEARCH)
        self.set_data(By.CSS_SELECTOR, WebTablesPage.TXT_SEARCH, email)

    def update_email(self, new_email: UserModel) -> None:
        self.click_on(By.CSS_SELECTOR, WebTablesPage.BTN_EDIT)
        self.clear_field(By.CSS_SELECTOR, WebTablesPage.TXT_USER_EMAIL)
        self.set_data(By.CSS_SELECTOR, WebTablesPage.TXT_USER_EMAIL, new_email)
        self.click_on_btn_submit()

    def remove_new_record(self) -> None:
        """цей метод видаляє новий запис з таблиці"""
        self.remove_advertising_in_footer()
        self.click_on(By.CSS_SELECTOR, WebTablesPage.BTN_DELETE)

    def get_the_checking_text(self) -> str:
        """цей метод повертає текст, який підтверджує, що рядок з заданим емейлом не знайдено """
        return self.get_text(By.CSS_SELECTOR, WebTablesPage.THE_CHECKING_TEXT)

    def quantity_of_rows(self) -> tuple:
        """цей метод: 1)змінює к-сть рядків таблиці що відображаються на сторінці;
        2) підраховує к-сть рядків, що фактично відображено в таблиці"""
        wait_for_btn_the_quantity_of_rows = self.wait_for_visibility_of_el(By.CSS_SELECTOR, WebTablesPage.BTN_THE_QUANTITY_OF_ROWS)
        select = Select(wait_for_btn_the_quantity_of_rows)
        list_of_options = select.options
        list_of_clicked_options = []
        list_of_counted_rows = []

        for option in list_of_options:
            self.scroll_js(By.CSS_SELECTOR, WebTablesPage.BTN_THE_QUANTITY_OF_ROWS)
            option.click()
            list_of_clicked_options.append(option.text.replace(' rows', ''))
            actual_quantity_rows = self.wait_for_visibility_of_all_elements(By.CSS_SELECTOR, WebTablesPage.ROWS)
            list_of_counted_rows.append(str(len(actual_quantity_rows)))
        return list_of_clicked_options, list_of_counted_rows



