from helpers.file_system import FileSystem

DATABASE_PATH = FileSystem.get_absolute_path_for_file('study_db.sqlite3')

WEB_PAGES_LOGFILE_PATH = FileSystem.get_absolute_path_for_file(r'logs\web_pages_logfile.log')
