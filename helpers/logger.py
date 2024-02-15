import logging
from config import WEB_PAGES_LOGFILE_PATH

log = logging.getLogger(__name__)
handler = logging.FileHandler(encoding='utf-8', filename=WEB_PAGES_LOGFILE_PATH, mode='w')
formatter = logging.Formatter(fmt="%(asctime)s : %(levelname)s : %(module)s : %(message)s")

handler.setFormatter(fmt=formatter)
log.addHandler(hdlr=handler)
log.setLevel(level=logging.INFO)


