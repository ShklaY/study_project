import logging


log = logging.getLogger(__name__)
# rewrite filename path
handler = logging.FileHandler(encoding='utf-8', filename=r"C:\Users\Користувач\PycharmProjects\18_11\study_project\logs\web_pages_logfile.log", mode='w')
formatter = logging.Formatter(fmt="%(asctime)s : %(levelname)s : %(module)s : %(message)s")

handler.setFormatter(fmt=formatter)
log.addHandler(hdlr=handler)
log.setLevel(level=logging.INFO)


