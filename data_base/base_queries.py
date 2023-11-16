from data_base.helper_db import DataBaseConnection


class BaseQueries(DataBaseConnection):
    def select_all(self, table_name: str) -> list:
        return self.get_all_rows(f'SELECT * FROM {table_name}')

    def select_id_by_name(self, table_name: str, tc_name: str) -> int:
        return self.get_one_row(f'SELECT id FROM {table_name} WHERE name="{tc_name}"')

    def insert(self, table_name: str, data: tuple) -> None:
        self.commit_changes(f"INSERT INTO {table_name} (description, author_id, name) VALUES {data};")

    def update(self, table_name: str, old_descrip: str, new_descrip: str) -> None:
        self.commit_changes(f"UPDATE {table_name} SET description='{new_descrip}' WHERE description='{old_descrip}';")

    def delete_row(self, table_name: str, tc_name: str) -> None:
        self.commit_changes(f"DELETE from {table_name} WHERE name='{tc_name}';")

