from dataclasses import dataclass


@dataclass()
class Data:
    table_name: str = 'tcm_testcase'
    tc_name: str = 'test_case_3'
    tc_description: str = 'description for test_case_3'
    tc_author_id: int = 3
    new_description: str = "new description for test_case_3"


