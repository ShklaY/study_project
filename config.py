import os

# TODO global constants usually are defined with caps lock
CURRENT_FILE_PATH = os.path.abspath(__file__)
PROJECT_ROOT = os.path.dirname(CURRENT_FILE_PATH)
DATABASE_PATH = os.path.join(PROJECT_ROOT, 'study_db.sqlite3')
