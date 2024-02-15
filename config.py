from helpers.file_system import FileSystem

DIR_TEST_LOGS_PATH = FileSystem.make_dir('test_logs')
DIR_REPORTS_PATH = FileSystem.make_dir("reports")
WEB_PAGES_LOGFILE_PATH = str(DIR_TEST_LOGS_PATH / 'web_pages_logfile.log')
