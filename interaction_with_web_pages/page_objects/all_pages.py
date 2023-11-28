from interaction_with_web_pages.page_objects.base_page import BasePage
from interaction_with_web_pages.page_objects.checkbox_page import CheckBoxPage
from interaction_with_web_pages.page_objects.elements_page import ElementsPage
from interaction_with_web_pages.page_objects.forms_page import FormsPage
from interaction_with_web_pages.page_objects.practiceform_page import PracticeFormPage
from interaction_with_web_pages.page_objects.radiobutton_page import RadioButtonPage
from interaction_with_web_pages.page_objects.textbox_page import TextBoxPage
from interaction_with_web_pages.page_objects.webtables_page import WebTablesPage


class AllPages:
    def __init__(self, driver):
        self.base_pg = BasePage(driver)
        self.elements_pg = ElementsPage(driver)
        self.textbox_pg = TextBoxPage(driver)
        self.checkbox_pg = CheckBoxPage(driver)
        self.radiobutton_pg = RadioButtonPage(driver)
        self.web_tables_pg = WebTablesPage(driver)
        self.forms_pg = FormsPage(driver)
        self.practice_form_pg = PracticeFormPage(driver)


