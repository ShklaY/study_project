from assertpy import assert_that


class TestTextBoxPage:
    def test_send_text_boxes(self, all_pages, input_user_data):
        all_pages.base_pg.click_on_btn_elements()
        all_pages.elements_pg.menu_bar.click_on_btn_text_box()
        all_pages.textbox_pg.fill_text_boxes(
            full_name=input_user_data.full_name,
            email=input_user_data.email,
            current_address=input_user_data.current_address,
            permanent_address=input_user_data.permanent_address)
        all_pages.textbox_pg.click_on_btn_submit()

        output_full_name, output_email, output_current_address, output_permanent_address = all_pages.textbox_pg.get_output_user_data()
        assert_that(output_full_name).is_equal_to(input_user_data.full_name).described_as("input name != output")
        assert_that(output_email).is_equal_to(input_user_data.email).described_as("email != output")
        assert_that(output_current_address).is_equal_to(input_user_data.current_address).described_as("curr_address != output")
        assert_that(output_permanent_address).is_equal_to(input_user_data.permanent_address).described_as("perman_address != output")


class TestCheckBoxPage:
    def test_click_on_check_boxes(self, all_pages):
        all_pages.base_pg.click_on_btn_elements()
        all_pages.elements_pg.menu_bar.click_on_btn_check_box()
        all_pages.checkbox_pg.click_on_btn_expand_all()
        all_pages.checkbox_pg.click_on_random_checkboxes()
        titles_of_checked_checkboxes = all_pages.checkbox_pg.get_titles_of_checked_checkboxes()
        """назви чекбоксів, що виводяться в рядку 'You have selected' """
        output_result = all_pages.checkbox_pg.get_output_result()
        assert_that(titles_of_checked_checkboxes).is_equal_to(output_result).described_as("clicked checkboxes != result")


class TestRadioButtonPage:
    def test_click_on_radio_buttons(self, all_pages):
        all_pages.base_pg.click_on_btn_elements()
        all_pages.elements_pg.menu_bar.click_on_btn_radio_button()
        """асьорт списків, де 1й список містить усі назви клікнутих радіобатонів , 
        а 2й список - назви радіобатонів, що відображались на сторінці після тексту 'You have selected' """
        list_of_clicked_radiobutt, list_of_output_radiobutt = all_pages.radiobutton_pg.click_on_radio_buttons_and_get_output_text()
        assert_that(list_of_clicked_radiobutt).is_equal_to(list_of_output_radiobutt).described_as("clicked radio buttons =! result")


class TestWebTablesPage:
    def test_add_new_record(self, all_pages, input_user_data):
        all_pages.base_pg.click_on_btn_elements()
        all_pages.elements_pg.menu_bar.click_on_btn_web_tables()
        """додавання нового запису в таблицю"""
        all_pages.web_tables_pg.click_on_btn_add()
        new_record = all_pages.web_tables_pg.fill_all_fields(
            first_name=input_user_data.full_name,
            last_name=input_user_data.last_name,
            email=input_user_data.email,
            age=input_user_data.age,
            salary=input_user_data.salary,
            department=input_user_data.department)
        all_pages.web_tables_pg.click_on_btn_submit()
        all_records = all_pages.web_tables_pg.get_text_from_rows()
        """перевірка чи новий запис додано в таблицю"""
        assert_that(all_records).contains(new_record).described_as("table dont contain new record")

    def test_search_new_record_by_email(self, all_pages, input_user_data):
        all_pages.web_tables_pg.set_email_in_search_field(input_user_data.email)
        search_result = all_pages.web_tables_pg.get_text_from_rows()
        first_field_in_search_result = search_result[0]
        assert_that(first_field_in_search_result).contains(input_user_data.email).described_as("results dont contain search email")

    def test_update_email(self, all_pages, input_user_data):
        all_pages.web_tables_pg.update_email(input_user_data.new_email)
        """пошук по новому емейлу, перевірка чи є він в першому рядку результату пошуку"""
        all_pages.web_tables_pg.set_email_in_search_field(input_user_data.new_email)
        search_result = all_pages.web_tables_pg.get_text_from_rows()
        first_field_in_search_result = search_result[0]
        assert_that(first_field_in_search_result).contains(input_user_data.new_email).described_as("results dont contain new_email")

    def test_remove_new_record(self, all_pages, input_user_data):
        all_pages.web_tables_pg.remove_new_record()
        checking_text = all_pages.web_tables_pg.get_the_checking_text()
        assert_that(checking_text).is_equal_to('No rows found').described_as('new_record doesnt deleted')

    def test_quantity_of_rows(self, all_pages):
        """перевірка чи обрані опції к-сті рядків відповідають фактичній к-сті рядків відображених на сторінці"""
        all_pages.base_pg.click_on_btn_elements()
        all_pages.elements_pg.menu_bar.click_on_btn_web_tables()
        list_of_clicked_options, list_of_counted_rows = all_pages.web_tables_pg.quantity_of_rows()
        assert_that(list_of_clicked_options).is_equal_to(list_of_counted_rows).described_as("quantity of_clicked_options != quantity of_counted_rows")


class TestPracticeFormPage:
    def test_registration_new_student(self, all_pages, input_user_data):
        all_pages.base_pg.click_on_btn_forms()
        all_pages.forms_pg.menu_bar.click_on_btn_practice_form()

        """заповнення форми реєстрації студента"""
        inp_gender, inp_hobby = all_pages.practice_form_pg.set_new_student(
            first_name=input_user_data.first_name,
            last_name=input_user_data.last_name,
            email=input_user_data.email,
            phone_number=input_user_data.phone_number,
            subject=input_user_data.subject,
            current_address=input_user_data.current_address,
            state=input_user_data.state,
            city=input_user_data.city)
        """вихідні дані з підтверджувальної таблиці"""
        list_with_data_of_registered_student = all_pages.practice_form_pg.get_data_of_registered_student()
        res_full_name, res_email, res_gender, res_mobile, res_date, res_subject, res_hobby, res_picture, res_address, \
            res_state_and_city = list_with_data_of_registered_student

        assert_that(f'{input_user_data.first_name} {input_user_data.last_name}').is_equal_to(res_full_name).described_as('name error')
        assert_that(input_user_data.email).is_equal_to(res_email).described_as('email error')
        assert_that(inp_gender).is_equal_to(res_gender).described_as('gender error')
        assert_that(str(input_user_data.phone_number)).is_equal_to(res_mobile).described_as('mobile error')
        assert_that(input_user_data.subject).is_equal_to(res_subject).described_as('subject error')
        assert_that(inp_hobby).is_equal_to(res_hobby).described_as('hobby error')
        assert_that(input_user_data.current_address).is_equal_to(res_address).described_as('address error')
        assert_that(f'{input_user_data.state} {input_user_data.city}').is_equal_to(res_state_and_city).described_as('state/city error')


