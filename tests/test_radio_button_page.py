import pytest
from assertpy import assert_that


@pytest.mark.elements_section
class TestRadioButtonPage:
    def test_click_on_radio_buttons(self, all_pages, record_property):
        record_property('testrail_result_comment', '1. Click on button Elements')
        all_pages.start_pg.click_on_elements_btn()
        record_property('testrail_result_comment', '2. Click on button Radio Button')
        all_pages.elements_pg.menu_bar.click_on_radio_btn()

        record_property('testrail_result_comment', '3. Click on all radio buttons sequentially')
        results = all_pages.radiobutton_pg.click_on_radio_buttons_and_get_output_text()

        record_property('testrail_result_comment', '4. Check the names of clicked radio buttons == names of radio buttons on the output')
        assert_that(results['expected']).is_equal_to(results['actual']).described_as("clicked radio buttons =! output_radio_buttons")

