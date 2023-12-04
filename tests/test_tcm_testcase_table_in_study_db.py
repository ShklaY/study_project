from interaction_with_db.testcase_model import TestCaseModel
from assertpy import assert_that


class TestTcmTestcaseTable:

    def test_get_all_test_cases(self, queries_for_tcm_testcase_table):
        all_test_cases = queries_for_tcm_testcase_table.select_all()
        assert_that(len(all_test_cases), "quantity of test cases != 12").is_equal_to(12)

    def test_add_update_delete_new_record(self, queries_for_tcm_testcase_table):
        new_tc_data = TestCaseModel('description for test_case_8', 3, 'test_case_8', 'new description')
        queries_for_tcm_testcase_table.insert(new_tc_data.tc_description, new_tc_data.tc_author_id, new_tc_data.tc_name)
        id_tc = queries_for_tcm_testcase_table.select_id_by_name(new_tc_data.tc_name)
        new_test_case = id_tc, new_tc_data.tc_description, new_tc_data.tc_author_id, new_tc_data.tc_name
        all_test_cases = queries_for_tcm_testcase_table.select_all()
        assert_that(all_test_cases).contains(new_test_case)

        # update new_record
        queries_for_tcm_testcase_table.update(new_tc_data.tc_description, new_tc_data.new_description)
        all_test_cases = queries_for_tcm_testcase_table.select_all()
        updated_tc = id_tc, new_tc_data.new_description, new_tc_data.tc_author_id, new_tc_data.tc_name
        assert_that(all_test_cases).contains(updated_tc)

        # delete new_record
        queries_for_tcm_testcase_table.delete_row(new_tc_data.tc_name)
        all_test_cases = queries_for_tcm_testcase_table.select_all()
        assert_that(all_test_cases).does_not_contain(updated_tc).described_as("new test case isn't deleted")

