from ui.page_objects.checkbox_page import CheckBoxPage
from ui.page_objects.forms_page import FormsPage
from ui.page_objects.base_page import BasePage
from ui.page_objects.elements_page import ElementsPage
from ui.page_objects.practiceform_page import PracticeFormPage
from ui.page_objects.radiobutton_page import RadioButtonPage
from ui.page_objects.textbox_page import TextBoxPage
from ui.page_objects.webtables_page import WebTablesPage


class TestTextBoxPage:
    def test_send_text_boxes(self, driver_chrome):
        BasePage(driver_chrome).click_on_btn_elements()
        ElementsPage(driver_chrome).click_on_btn_text_box()
        textbox_pg = TextBoxPage(driver_chrome)

        input_full_name, input_email, input_current_addr, input_permanent_addr = textbox_pg.fill_all_text_boxes()
        textbox_pg.click_on_btn_submit()
        output_full_name, output_email, output_current_address, output_permanent_address = textbox_pg.get_output_user_data()

        assert output_full_name == input_full_name, f"input:'{input_full_name}' =! output:'{output_full_name}' "
        assert output_email == input_email, f"input:'{input_email}' =! output:'{output_email}' "
        assert output_current_address == input_current_addr, f"input:'{input_current_addr}' =! output:'{output_current_address}' "
        assert output_permanent_address == input_permanent_addr, f"input:'{input_permanent_addr}' =! output:'{output_permanent_address}' "


class TestCheckBoxPage:
    def test_check_boxes(self, driver_chrome):
        BasePage(driver_chrome).click_on_btn_elements()
        ElementsPage(driver_chrome).click_on_btn_check_box()
        checkbox_pg = CheckBoxPage(driver_chrome)

        checkbox_pg.click_on_btn_expand_all()
        checkbox_pg.click_on_random_checkboxes()
        """назви всіх відмічених чекбоксів"""
        titles_of_checked_checkboxes = checkbox_pg.get_titles_of_checked_checkboxes()
        """назви чекбоксів, що виводяться в рядку 'You have selected' """
        output_result = checkbox_pg.get_output_result()
        assert titles_of_checked_checkboxes == output_result


class TestRadioButtonPage:
    def test_radio_buttons(self, driver_chrome):
        BasePage(driver_chrome).click_on_btn_elements()
        ElementsPage(driver_chrome).click_on_btn_radio_button()
        radiobutton_pg = RadioButtonPage(driver_chrome)

        """асьорт списків, де 1й список містить усі назви клікнутих радіобатонів , 
        а 2й список - назви радіобатонів, що відображались на сторінці після тексту 'You have selected' """
        list_of_clicked_radiobutt, list_of_output_radiobutt = radiobutton_pg.click_on_radio_buttons_and_get_output_text()
        assert list_of_clicked_radiobutt == list_of_output_radiobutt, f" clicked radio buttons =! outputed radio buttons"


class TestWebTablesPage:
    def test_add_record(self, driver_chrome):
        BasePage(driver_chrome).click_on_btn_elements()
        ElementsPage(driver_chrome).click_on_btn_web_tables()
        web_tables_pg = WebTablesPage(driver_chrome)

        """додавання нового запису в таблицю"""
        web_tables_pg.click_on_btn_add()
        input_data = web_tables_pg.fill_all_fields()
        web_tables_pg.click_on_btn_submit()
        output_data = web_tables_pg.get_text_from_rows()
        """перевірка чи новий запис додано в таблицю"""
        assert input_data in output_data, f"{input_data} is not in {output_data}"

    def test_search_new_record_by_email(self, driver_chrome):
        web_tables_pg = WebTablesPage(driver_chrome)
        search_email = web_tables_pg.set_email_in_search_field()
        search_result = web_tables_pg.get_text_from_rows()
        first_field_in_search_result = search_result[0]
        """перевірка чи є емейл в першому рядку результату пошуку"""
        assert search_email in first_field_in_search_result, f"{search_email} != email in the result search"

    def test_update_email(self, driver_chrome):
        web_tables_pg = WebTablesPage(driver_chrome)
        new_email = web_tables_pg.set_new_email()
        """пошук по новому емейлу, перевірка чи є він в першому рядку результату пошуку"""
        web_tables_pg.set_email_in_search_field(new_email)
        search_result = web_tables_pg.get_text_from_rows()
        first_field_in_search_result = search_result[0]
        assert new_email in first_field_in_search_result, f"{new_email} != new email in the new result search"

    def test_remove_new_record(self, driver_chrome):
        web_tables_pg = WebTablesPage(driver_chrome)
        web_tables_pg.remove_record()
        the_checking_text = web_tables_pg.get_the_checking_text()
        assert the_checking_text == 'No rows found', 'new_record doesnt deleted'

    def test_quantity_of_rows(self, driver_chrome):
        """перевірка чи обрані опції к-сті рядків відповідають фактичній к-сті рядків відображених на сторінці"""
        web_tables_pg = WebTablesPage(driver_chrome)
        list_of_clicked_options, list_of_counted_rows = web_tables_pg.quantity_of_rows()
        assert list_of_clicked_options == list_of_counted_rows, "quantity of_clicked_options != quantity of_counted_rows"


class TestPracticeFormPage:
    def test_registration_new_student(self, driver_chrome):
        BasePage(driver_chrome).click_on_btn_forms()
        FormsPage(driver_chrome).click_on_btn_practice_form()
        practice_form_pg = PracticeFormPage(driver_chrome)

        """заповнення форми реєстрації студента"""
        inp_first_name, inp_last_name, inp_email, inp_gender, inp_mobile, inp_subject, inp_hobby, inp_address, \
        inp_state, inp_city = practice_form_pg.set_student_registration_form()

        """дані з підтверджувальної таблиці"""
        res_name, res_email, res_gender, res_mobile, res_date, res_subject, res_hobby, res_picture, res_address, \
        res_state_and_city = practice_form_pg.get_data_result()

        assert f'{inp_first_name} {inp_last_name}' == res_name, 'name error'
        assert inp_email == res_email, 'email error'
        assert inp_gender == res_gender, 'gender error'
        assert inp_mobile == res_mobile, 'mobile error'
        assert inp_subject == res_subject, 'subject error'
        assert inp_hobby == res_hobby, 'hobby error'
        assert inp_address == res_address, 'address error'
        assert f'{inp_state} {inp_city}' == res_state_and_city, 'state/city error'
