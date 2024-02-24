import os
from dotenv import load_dotenv
from helpers.file_system import FileSystem


load_dotenv()

BASE_URL = os.getenv('BASE_URL', default='NOT_DEFINED')
DIR_TEST_LOGS_PATH = FileSystem.make_dir('test_logs')
DIR_REPORTS_PATH = FileSystem.make_dir("reports")
WEB_PAGES_LOGFILE_PATH = str(DIR_TEST_LOGS_PATH / 'web_pages_logfile.log')
