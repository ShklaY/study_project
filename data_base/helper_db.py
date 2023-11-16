import sqlite3
from config import database_path


class DataBaseConnection:
    def __init__(self):
        self.path = database_path
        self.connection = sqlite3.connect(self.path)

    def execute_query(self, query: str):
        my_cursor = self.connection.cursor()
        my_cursor.execute(query)
        return my_cursor

    def get_all_rows(self, query: str):
        return self.execute_query(query).fetchall()

    def get_one_row(self, query: str):
        return self.execute_query(query).fetchone()[0]

    def commit_changes(self, query: str):
        self.execute_query(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


