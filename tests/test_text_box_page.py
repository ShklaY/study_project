import pytest
from assertpy import assert_that


@pytest.mark.elements_section
class TestTextBoxPage:
    def test_correct_output_is_displayed_submitting_form_with_valid_values(self, all_pages, input_user_data, record_property):
        record_property('testrail_result_comment', '1. Open text box page')
        all_pages.textbox_pg.open_page()

        record_property('testrail_result_comment', '3. Fill text boxes by valid data')
        all_pages.textbox_pg.fill_text_boxes(
            full_name=input_user_data.full_name,
            email=input_user_data.email,
            current_address=input_user_data.current_address,
            permanent_address=input_user_data.permanent_address
        )
        all_pages.textbox_pg.click_on_submit_btn()

        output_user_data = all_pages.textbox_pg.get_output_user_data()

        record_property('testrail_result_comment', '4. Check the output data == input data')
        assert_that(output_user_data.full_name).is_equal_to(input_user_data.full_name) \
            .described_as("input name != output")
        assert_that(output_user_data.email).is_equal_to(input_user_data.email) \
             .described_as("email != output")
        assert_that(output_user_data.current_address).is_equal_to(input_user_data.current_address) \
             .described_as("curr_address != output")
        assert_that(output_user_data.permanent_address).is_equal_to(input_user_data.permanent_address) \
             .described_as("perman_address != output")

    def test_validation_error_is_displayed_submitting_form_with_invalid_email(self, all_pages, input_user_data, record_property):
        text_box_pg = all_pages.textbox_pg
        record_property('testrail_result_comment', '1. Open text box page')
        text_box_pg.open_page()

        record_property('testrail_result_comment', '3. Fill text boxes by valid data')
        text_box_pg.fill_text_boxes(
            full_name=input_user_data.full_name,
            email=input_user_data.invalid_email,
            current_address=input_user_data.current_address,
            permanent_address=input_user_data.permanent_address
        )
        text_box_pg.click_on_submit_btn()
        text_box_pg.check_email_field_has_validation_error()

    def test_validation_error_is_displayed_submitting_empty_form(self, all_pages, input_user_data, record_property):
        text_box_pg = all_pages.textbox_pg
        record_property('testrail_result_comment', '1. Open text box page')
        text_box_pg.open_page()

        text_box_pg.click_on_submit_btn()
        text_box_pg.check_full_name_field_has_validation_error()
        text_box_pg.check_email_field_has_validation_error()

