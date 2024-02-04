from assertpy import assert_that


class TestTextBoxPage:
    def test_send_text_boxes(self, all_pages, input_user_data, record_property):
        record_property('testrail_result_comment', '1. Click on button Elements')
        all_pages.base_pg.click_on_btn_elements()
        record_property('testrail_result_comment', '2. Click on button Text Box')
        all_pages.elements_pg.menu_bar.click_on_btn_text_box()

        record_property('testrail_result_comment', '3. Fill text boxes by valid data')
        all_pages.textbox_pg.fill_text_boxes(
            full_name=input_user_data.full_name,
            email=input_user_data.email,
            current_address=input_user_data.current_address,
            permanent_address=input_user_data.permanent_address)
        all_pages.textbox_pg.click_on_btn_submit()

        output_full_name, output_email, output_current_address, output_permanent_address = all_pages.textbox_pg.get_output_user_data()

        record_property('testrail_result_comment', '4. Check the output data == input data')
        assert_that(output_full_name).is_equal_to(input_user_data.full_name).described_as("input name != output")
        assert_that(output_email).is_equal_to(input_user_data.email).described_as("email != output")
        assert_that(output_current_address).is_equal_to(input_user_data.current_address).described_as("curr_address != output")
        assert_that(output_permanent_address).is_equal_to(input_user_data.permanent_address).described_as("perman_address != output")


class TestCheckBoxPage:
    def test_click_on_check_boxes(self, all_pages, record_property):
        record_property('testrail_result_comment', '1. Click on button Elements')
        all_pages.base_pg.click_on_btn_elements()
        record_property('testrail_result_comment', '2. Click on button Check Box')
        all_pages.elements_pg.menu_bar.click_on_btn_check_box()

        record_property('testrail_result_comment', '3. Click on button "+"("Expand All")')
        all_pages.checkbox_pg.click_on_btn_expand_all()
        record_property('testrail_result_comment', '4. Click on some random checkboxes')
        all_pages.checkbox_pg.click_on_random_checkboxes()
        titles_of_checked_checkboxes = all_pages.checkbox_pg.get_titles_of_checked_checkboxes()

        """назви чекбоксів, що виводяться в рядку 'You have selected' """
        output_result = all_pages.checkbox_pg.get_output_result()

        record_property('testrail_result_comment', "5. Check the names of clicked checkboxes == names of checkboxes in the 'You have selected' block")
        assert_that(titles_of_checked_checkboxes).is_equal_to(output_result).described_as("clicked checkboxes != result")


class TestRadioButtonPage:
    def test_click_on_radio_buttons(self, all_pages, record_property):
        record_property('testrail_result_comment', '1. Click on button Elements')
        all_pages.base_pg.click_on_btn_elements()
        record_property('testrail_result_comment', '2. Click on button Radio Button')
        all_pages.elements_pg.menu_bar.click_on_btn_radio_button()

        record_property('testrail_result_comment', '3. Click on all radio buttons in sequential order')
        results = all_pages.radiobutton_pg.click_on_radio_buttons_and_get_output_text()

        record_property('testrail_result_comment', '4. Check the names of clicked radio buttons == names of radio buttons on the output')
        assert_that(results['expected_res']).is_equal_to(results['actual_res']).described_as("clicked radio buttons =! output_radio_buttons")


class TestWebTablesPage:
    @staticmethod
    def test_add_new_record(all_pages, input_user_data, record_property):
        record_property('testrail_result_comment', '1. Click on button Elements')
        all_pages.base_pg.click_on_btn_elements()
        record_property('testrail_result_comment', '2. Click on button Web Tables')
        all_pages.elements_pg.menu_bar.click_on_btn_web_tables()
        record_property('testrail_result_comment', '3. Click on button Add')
        all_pages.web_tables_pg.click_on_btn_add()
        record_property('testrail_result_comment', '4. Add a new record to the table')
        new_record = all_pages.web_tables_pg.fill_all_fields(
            first_name=input_user_data.full_name,
            last_name=input_user_data.last_name,
            email=input_user_data.email,
            age=input_user_data.age,
            salary=input_user_data.salary,
            department=input_user_data.department)
        all_pages.web_tables_pg.click_on_btn_submit()
        all_records = all_pages.web_tables_pg.get_text_from_rows()

        record_property('testrail_result_comment', '5. Check the new record was added to the table')
        assert_that(all_records).contains(new_record).described_as("table doesnt contain new record")

    def test_search_new_record_by_email(self, all_pages, input_user_data, record_property):
        record_property('testrail_result_comment', '1. Add a new record to the table')
        self.test_add_new_record(all_pages, input_user_data, record_property)

        record_property('testrail_result_comment', '2. input the email in the search field')
        all_pages.web_tables_pg.set_email_in_search_field(input_user_data.email)

        search_result = all_pages.web_tables_pg.get_text_from_rows()
        first_field_in_search_result = search_result[0]

        record_property('testrail_result_comment', '3. Check the email is in the search result')
        assert_that(first_field_in_search_result).contains(input_user_data.email).described_as("result doesnt contain search email")

    def test_update_email(self, all_pages, input_user_data, record_property):
        record_property('testrail_result_comment', '1. Add a new record to the table')
        self.test_add_new_record(all_pages, input_user_data, record_property)
        record_property('testrail_result_comment', '2. Update email')
        all_pages.web_tables_pg.update_email(input_user_data.new_email)

        """пошук по новому емейлу, перевірка чи є він в першому рядку результату пошуку"""
        record_property('testrail_result_comment', '3. input the new email in the search field')
        all_pages.web_tables_pg.set_email_in_search_field(input_user_data.new_email)
        search_result = all_pages.web_tables_pg.get_text_from_rows()
        first_field_in_search_result = search_result[0]

        record_property('testrail_result_comment', '4. Check the new email is in the search result')
        assert_that(first_field_in_search_result).contains(input_user_data.new_email).described_as("result doesnt contain new_email")

    def test_remove_new_record(self, all_pages, input_user_data, record_property):
        record_property('testrail_result_comment', '1. Add a new record to the table')
        self.test_update_email(all_pages, input_user_data, record_property)

        record_property('testrail_result_comment', '2. Click on the trash can icon')
        all_pages.web_tables_pg.remove_new_record()

        checking_text = all_pages.web_tables_pg.get_the_checking_text()

        record_property('testrail_result_comment', '3. Check the text "No rows found" has appeared')
        assert_that(checking_text).is_equal_to('No rows found').described_as('new_record doesnt deleted')

    def test_quantity_of_rows(self, all_pages, record_property):
        record_property('testrail_result_comment', '1. Click on button Elements')
        all_pages.base_pg.click_on_btn_elements()

        record_property('testrail_result_comment', '2. Click on button Web Tables')
        all_pages.elements_pg.menu_bar.click_on_btn_web_tables()

        record_property('testrail_result_comment', '3. Click on the "10 rows" option in the dropdown menu and other options sequentially')
        results = all_pages.web_tables_pg.quantity_of_rows()

        record_property('testrail_result_comment', '4. Check the number of rows on the page')
        assert_that(results['expected_quantity']).is_equal_to(results['actual_quantity']).described_as("expected_quantity_of_rows != actual_quantity_of_rows")


class TestPracticeFormPage:
    def test_registration_new_student(self, all_pages, input_user_data, record_property):
        record_property('testrail_result_comment', '1. Click on button Forms')
        all_pages.base_pg.click_on_btn_forms()
        record_property('testrail_result_comment', '2. Click on button Practice Form')
        all_pages.forms_pg.menu_bar.click_on_btn_practice_form()

        """заповнення форми реєстрації студента"""
        record_property('testrail_result_comment', '3. Fill "Student Registration Form" by valid data')
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

        record_property('testrail_result_comment', '4. Check the input data == the data in the submitted form')
        assert_that(f'{input_user_data.first_name} {input_user_data.last_name}').is_equal_to(res_full_name).described_as('name error')
        assert_that(input_user_data.email).is_equal_to(res_email).described_as('email error')
        assert_that(inp_gender).is_equal_to(res_gender).described_as('gender error')
        assert_that(str(input_user_data.phone_number)).is_equal_to(res_mobile).described_as('mobile error')
        assert_that(input_user_data.subject).is_equal_to(res_subject).described_as('subject error')
        assert_that(inp_hobby).is_equal_to(res_hobby).described_as('hobby error')
        assert_that(input_user_data.current_address).is_equal_to(res_address).described_as('address error')
        assert_that(f'{input_user_data.state} {input_user_data.city}').is_equal_to(res_state_and_city).described_as('state/city error')

