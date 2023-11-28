import sqlite3


class MethodsToHelpInteractWithDB:
    def __init__(self, connect):
        self.connection = connect

    def execute_query(self, query: str) -> sqlite3.Cursor:
        my_cursor = self.connection.cursor()
        my_cursor.execute(query)
        return my_cursor

    def get_all_rows(self, query: str) -> list:
        return self.execute_query(query).fetchall()

    def commit_changes(self, query: str) -> None:
        self.execute_query(query)
        self.connection.commit()


