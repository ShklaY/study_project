from interaction_with_db.methods_to_help_interact_with_db import MethodsToHelpInteractWithDB
from interaction_with_db.testcase_model import TestCaseModel


class QueriesForTcmTestcaseTable(MethodsToHelpInteractWithDB):
    def select_all(self) -> list:
        return self.get_all_rows('SELECT * FROM tcm_testcase')

    def get_id(self, query: str) -> int:
        return self.execute_query(query).fetchone()[0]

    def select_id_by_name(self, tc_name: TestCaseModel) -> int:
        return self.get_id(f'SELECT id FROM tcm_testcase WHERE name="{tc_name}"')

    def insert(self, description: TestCaseModel, author_id: TestCaseModel, name: TestCaseModel) -> None:
        self.commit_changes(f"INSERT INTO tcm_testcase (description, author_id, name) VALUES ('{description}', '{author_id}', '{name}');")

    def update(self, old_descrip: TestCaseModel, new_descrip: TestCaseModel) -> None:
        self.commit_changes(f"UPDATE tcm_testcase SET description='{new_descrip}' WHERE description='{old_descrip}';")

    def delete_row(self, tc_name: TestCaseModel) -> None:
        self.commit_changes(f"DELETE from tcm_testcase WHERE name='{tc_name}';")
