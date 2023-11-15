import time
from ui_auto_tests.page_objects.page_checkbox import CheckBoxPage
from ui_auto_tests.page_objects.page_forms import FormsPage
from ui_auto_tests.page_objects.page_base import InitPage
from ui_auto_tests.page_objects.page_elements import ElementsPage
from ui_auto_tests.page_objects.page_practiceform import PracticeFormPage
from ui_auto_tests.page_objects.page_radiobutton import RadioButtonPage
from ui_auto_tests.page_objects.page_textbox import TextBoxPage
from ui_auto_tests.page_objects.page_webtables import WebTablesPage


class TestTextBoxPage:
    def test_text_box_page(self, driver_chrome):
        InitPage(driver_chrome).click_on_btn_elements()
        """відклилась стрінка Elements"""
        ElementsPage(driver_chrome).click_on_btn_text_box()
        """відкрилась стрінка TextBox після кліку на кнпку text_box в меню на стрінці Elements"""
        textbox_pg = TextBoxPage(driver_chrome)
        textbox_pg_header_name = textbox_pg.get_header_name()
        """перевірка тайтлу сторінки: """
        assert textbox_pg_header_name == 'Text Box', f" title 'Text Box' =! '{textbox_pg_header_name}' "
        """заповнення полей: ім'я, емейл, адреса та клік submit"""
        input_full_name = textbox_pg.set_full_name()
        input_email = textbox_pg.set_email()
        input_current_address = textbox_pg.set_current_address()
        input_permanent_address = textbox_pg.set_permanent_address()
        textbox_pg.remove_advertising_in_footer()
        textbox_pg.scroll_and_click_on_btn_submit()
        """поміщаю в змінні вихідні дані: ім'я, емейл, адреси"""
        output_full_name = textbox_pg.get_output_full_name()
        output_email = textbox_pg.get_output_email()
        output_current_address = textbox_pg.get_output_current_address()
        output_permanent_address = textbox_pg.get_output_permanent_address()

        assert output_full_name == input_full_name, f"input:'{input_full_name}' =! output:'{output_full_name}' "
        assert output_email == input_email, f"input:'{input_email}' =! output:'{output_email}' "
        assert output_current_address == input_current_address, f"input:'{input_current_address}' =! output:'{output_current_address}' "
        assert output_permanent_address == input_permanent_address, f"input:'{input_permanent_address}' =! output:'{output_permanent_address}' "
        print(output_full_name, output_email, output_current_address, output_permanent_address)

class TestCheckBoxPage:
    def test_check_box_page(self, driver_chrome):
        InitPage(driver_chrome).click_on_btn_elements()
        ElementsPage(driver_chrome).click_on_btn_check_box()
        time.sleep(3)
        checkbox_pg = CheckBoxPage(driver_chrome)
        checkbox_pg_header_name = checkbox_pg.get_header_name()
        """перевірка тайтлу сторінки: """
        assert checkbox_pg_header_name == 'Check Box', f" title 'Check Box' =! '{checkbox_pg_header_name}' "
        checkbox_pg.click_on_btn_expand_all()
        checkbox_pg.click_on_random_checkboxes()
        """назви всіх відмічених чекбоксів"""
        titles_of_checked_checkboxes = checkbox_pg.get_titles_of_checked_checkboxes()
        """назви чекбоксів, що виводяться в рядку 'You have selected' """
        output_result = checkbox_pg.get_output_result()

        assert titles_of_checked_checkboxes == output_result


class TestRadioButtonPage:
    def test_radio_button_page(self, driver_chrome):
        InitPage(driver_chrome).click_on_btn_elements()
        ElementsPage(driver_chrome).click_on_btn_radio_button()
        radiobutton_pg = RadioButtonPage(driver_chrome)
        radiobutton_pg_header_name = radiobutton_pg.get_header_name()
        """перевірка тайтлу сторінки: """
        assert radiobutton_pg_header_name == 'Radio Button', f" title 'Radio Button' =! '{radiobutton_pg_header_name}' "

        """асьорт списків, де 1й список містить усі назви клікнутих радіобатонів , 
        а 2й список - назви радіобатонів, що відображались на сторінці після тексту 'You have selected' """
        list_of_clicked_radiobutt, list_of_output_radiobutt = radiobutton_pg.click_on_radio_buttons_and_get_output_text()
        assert list_of_clicked_radiobutt == list_of_output_radiobutt, f" clicked radio buttons =! outputed radio buttons"


class TestWebTablesPage:
    def test_web_tables_page(self, driver_chrome):
        InitPage(driver_chrome).click_on_btn_elements()
        ElementsPage(driver_chrome).click_on_btn_web_tables()
        web_tables_pg = WebTablesPage(driver_chrome)
        web_tables_pg_header_name = web_tables_pg.get_header_name()
        """перевірка тайтлу сторінки: """
        assert web_tables_pg_header_name == "Web Tables", f" title 'Web Tables' =! '{web_tables_pg_header_name}' "

        """додавання нового запису в таблицю"""
        web_tables_pg.click_on_btn_add()
        input_data = web_tables_pg.fill_in_fields_on_the_registration_form()
        web_tables_pg.click_on_btn_submit()
        output_data = web_tables_pg.get_text_from_rows()
        """перевірка чи новий запис додано в таблицю"""
        assert input_data in output_data, f"{input_data} is not in {output_data}"

        """виконання пошуку по емейлу"""
        search_email = web_tables_pg.perform_search_by_email()
        time.sleep(3)
        output_data_after_performing_the_search = web_tables_pg.get_text_from_rows()
        first_result_field = output_data_after_performing_the_search[0]
        """перевірка чи є емейл в першому рядку результату пошуку"""
        assert search_email in first_result_field, f"{search_email} != email in the result search"

        """апдейт емейлу"""
        new_email = web_tables_pg.set_new_email()

        """пошук по новому емейлу, перевірка чи є він в першому рядку результату пошуку"""
        web_tables_pg.perform_search_by_email(new_email)
        output_data_after_performing_the_search_with_a_new_email = web_tables_pg.get_text_from_rows()
        first_result_field_with_a_new_email = output_data_after_performing_the_search_with_a_new_email[0]
        assert new_email in first_result_field_with_a_new_email, f"{new_email} != new email in the new result search"

        """видалення реклами в футері"""
        web_tables_pg.remove_advertising_in_footer()
        """видалення нового запису з таблиці"""
        web_tables_pg.remove_record()
        the_checking_text = web_tables_pg.get_the_checking_text()
        assert the_checking_text == 'No rows found', 'after removing a new record, the message "No rows found" does not appear'

        """перевірка чи обрані опції к-сті рядків відповідають фактичній к-сті рядків відображених на сторінці"""
        list_of_clicked_options, list_of_counted_rows = web_tables_pg.quantity_of_rows()
        assert list_of_clicked_options == list_of_counted_rows, "quantity of_clicked_options != quantity of_counted_rows"


class TestForms:
    def test_practice_form(self, driver_chrome):
        InitPage(driver_chrome).click_on_btn_forms()
        """відклилась стрінка Forms"""
        FormsPage(driver_chrome).click_on_btn_practice_form()
        """відклилась стрінка Practice Form"""
        practice_form_pg = PracticeFormPage(driver_chrome)
        practice_form_pg_header_name = practice_form_pg.get_header_name()
        assert practice_form_pg_header_name == 'Practice Form', f" title 'Practice Form' =! '{practice_form_pg_header_name}' "

        """видалення реклами в футері, що перекриває кнопку submit; заповнення форми реєстрації студента"""
        practice_form_pg.remove_advertising_in_footer()
        inp_first_name, inp_last_name, inp_email, inp_gender, inp_mobile, inp_subject, inp_hobby, inp_address, inp_state, inp_city = practice_form_pg.set_student_registration_form()

        """дані з підтверджувальної таблиці"""
        res_name, res_email, res_gender, res_mobile, res_date, res_subject, res_hobby, res_picture, res_address, res_state_and_city = practice_form_pg.get_data_result()

        assert f'{inp_first_name} {inp_last_name}' == res_name, 'name error'
        assert inp_email == res_email, 'email error'
        assert inp_gender == res_gender, 'gender error'
        assert inp_mobile == res_mobile, 'mobile error'
        assert inp_subject == res_subject, 'subject error'
        assert inp_hobby == res_hobby, 'hobby error'
        assert inp_address == res_address, 'address error'
        assert f'{inp_state} {inp_city}' == res_state_and_city, 'state/city error'
