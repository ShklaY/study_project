import pytest
from assertpy import assert_that


@pytest.mark.elements_section
class TestWebTablesPage:
    @staticmethod
    def test_add_new_record(all_pages, input_user_data, record_property):
        record_property('testrail_result_comment', '1. Click on button Elements')
        all_pages.start_pg.click_on_elements_btn()
        record_property('testrail_result_comment', '2. Click on button Web Tables')
        all_pages.elements_pg.menu_bar.click_on_web_tables_btn()
        record_property('testrail_result_comment', '3. Click on button Add')
        all_pages.web_tables_pg.click_on_add_btn()
        record_property('testrail_result_comment', '4. Add a new record to the table')
        new_record = all_pages.web_tables_pg.fill_all_fields(
            first_name=input_user_data.full_name,
            last_name=input_user_data.last_name,
            email=input_user_data.email,
            age=input_user_data.age,
            salary=input_user_data.salary,
            department=input_user_data.department)
        all_pages.web_tables_pg.click_on_submit_btn()
        all_records = all_pages.web_tables_pg.get_text_from_rows()

        record_property('testrail_result_comment', '5. Check the new record was added to the table')
        assert_that(all_records).contains(new_record).described_as("table doesnt contain new record")

    def test_search_new_record_by_email(self, all_pages, input_user_data, record_property):
        self.test_add_new_record(all_pages, input_user_data, record_property)

        record_property('testrail_result_comment', '6. input the email in the search field')
        all_pages.web_tables_pg.set_email_in_search_field(input_user_data.email)

        search_result = all_pages.web_tables_pg.get_text_from_rows()
        first_field_in_search_result = search_result[0]

        record_property('testrail_result_comment', '7. Check the email is in the search results')
        assert_that(first_field_in_search_result).contains(input_user_data.email).described_as("result doesnt contain search email")

    def test_update_email(self, all_pages, input_user_data, record_property):
        self.test_add_new_record(all_pages, input_user_data, record_property)
        record_property('testrail_result_comment', '6. Update email')
        all_pages.web_tables_pg.update_email(input_user_data.new_email)

        record_property('testrail_result_comment', '7. input the new email in the search field')
        all_pages.web_tables_pg.set_email_in_search_field(input_user_data.new_email)
        search_result = all_pages.web_tables_pg.get_text_from_rows()
        first_field_in_search_result = search_result[0]

        record_property('testrail_result_comment', '8. Check the new email is in the search results')
        assert_that(first_field_in_search_result).contains(input_user_data.new_email).described_as("result doesnt contain new_email")

    def test_remove_new_record(self, all_pages, input_user_data, record_property):
        self.test_update_email(all_pages, input_user_data, record_property)

        record_property('testrail_result_comment', '9. Click on the trash can icon')
        all_pages.web_tables_pg.remove_new_record()

        checking_text = all_pages.web_tables_pg.get_the_checking_text()

        record_property('testrail_result_comment', '10. Check the text "No rows found" has appeared')
        assert_that(checking_text).is_equal_to('No rows found').described_as('new_record doesnt deleted')

    def test_quantity_of_rows(self, all_pages, record_property):
        record_property('testrail_result_comment', '1. Click on button Elements')
        all_pages.start_pg.click_on_elements_btn()

        record_property('testrail_result_comment', '2. Click on button Web Tables')
        all_pages.elements_pg.menu_bar.click_on_web_tables_btn()

        record_property('testrail_result_comment', '3. Click on the "10 rows" option in the dropdown menu and other options sequentially')
        results = all_pages.web_tables_pg.quantity_of_rows()

        record_property('testrail_result_comment', '4. Check the number of rows in the table for each option sequentially')
        assert_that(results['expected']).is_equal_to(results['actual']).described_as("expected_quantity_of_rows != actual_quantity_of_rows")

