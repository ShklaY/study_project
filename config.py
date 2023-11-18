import os

# TODO global constants usually are defined with caps lock
current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(current_file_path)
database_path = os.path.join(project_root, 'study_db.sqlite3')
