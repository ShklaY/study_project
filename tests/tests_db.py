from data_base.base_queries import BaseQueries
from data_base.data_db import Data


class TestDataBase:
    testcase_id = None

    def test_get_all_test_cases(self, get_db):
        all_test_cases = BaseQueries().select_all(Data.table_name)
        assert len(all_test_cases) == 12, "quantity of test cases != 12"

    def test_add_new_record(self, get_db):
        BaseQueries().insert(Data.table_name, (Data.tc_description, Data.tc_author_id, Data.tc_name))
        id_test_case = BaseQueries().select_id_by_name(Data.table_name, Data.tc_name)
        tests_after = BaseQueries().select_all(Data.table_name)
        assert (id_test_case, Data.tc_description, Data.tc_author_id, Data.tc_name) in tests_after, "new record isnt added"
        TestDataBase.testcase_id = id_test_case

    def test_update(self, get_db):
        BaseQueries().update(Data.table_name, Data.tc_description, Data.new_description)
        tests_after = BaseQueries().select_all(Data.table_name)
        assert (TestDataBase.testcase_id, Data.new_description, Data.tc_author_id, Data.tc_name) in tests_after, "new record isnt updated"

    def test_delete(self, get_db):
        BaseQueries().delete_row(Data.table_name, Data.tc_name)
        tests_after = BaseQueries().select_all(Data.table_name)
        assert (TestDataBase.testcase_id, Data.new_description, Data.tc_author_id, Data.tc_name) not in tests_after, "new record isnt deleted"

