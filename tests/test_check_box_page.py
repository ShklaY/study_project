import pytest
from assertpy import assert_that


@pytest.mark.elements_section
class TestCheckBoxPage:
    def test_click_on_check_boxes(self, all_pages, record_property):
        record_property('testrail_result_comment', '1. Click on button Elements')
        all_pages.start_pg.click_on_elements_btn()
        record_property('testrail_result_comment', '2. Click on button Check Box')
        all_pages.elements_pg.menu_bar.click_on_check_box_btn()

        record_property('testrail_result_comment', '3. Click on button "+"("Expand All")')
        all_pages.checkbox_pg.click_on_expand_all_btn()
        record_property('testrail_result_comment', '4. Click on some random checkboxes')
        all_pages.checkbox_pg.click_on_random_checkboxes()
        titles_of_checked_checkboxes = all_pages.checkbox_pg.get_titles_of_checked_checkboxes()

        """назви чекбоксів, що виводяться в рядку 'You have selected' """
        output_result = all_pages.checkbox_pg.get_output_result()

        record_property('testrail_result_comment', "5. Check the names of clicked checkboxes == names of checkboxes in the 'You have selected' block")
        assert_that(titles_of_checked_checkboxes).is_equal_to(output_result).described_as("clicked checkboxes != result")

