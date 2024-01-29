import logging
from config import DIR_TEST_LOGS_PATH

log = logging.getLogger(__name__)
handler = logging.FileHandler(encoding='utf-8', filename=str(DIR_TEST_LOGS_PATH / 'web_pages_logfile.log'), mode='w')
formatter = logging.Formatter(fmt="%(asctime)s : %(levelname)s : %(module)s : %(message)s")

handler.setFormatter(fmt=formatter)
log.addHandler(hdlr=handler)
log.setLevel(level=logging.INFO)


