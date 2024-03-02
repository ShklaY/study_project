import pytest
from assertpy import assert_that


@pytest.mark.forms_section
class TestPracticeFormPage:
    def test_registration_new_student(self, all_pages, input_user_data, record_property):
        record_property('testrail_result_comment', '1. Click on button Forms')
        all_pages.start_pg.click_on_forms_btn()
        record_property('testrail_result_comment', '2. Click on button Practice Form')
        all_pages.forms_pg.menu_bar.click_on_practice_form_btn()

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

