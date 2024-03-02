import json
from uuid import uuid4
from config import DIR_REPORTS_PATH, WEB_PAGES_LOGFILE_PATH


def save_failure_artifacts(driver, request, record_property):
    """Saves screenshot and browser logs for failed tests"""
    if request.node.rep_setup.failed or request.node.rep_call.failed:
        try:
            failure_id = uuid4()

            # Save screenshot
            screenshot_path = str(DIR_REPORTS_PATH / f'{failure_id}_screenshot.png')
            driver.save_screenshot(screenshot_path)
            record_property("testrail_attachment", screenshot_path)

            # Save browser logs
            browser_logs_path = DIR_REPORTS_PATH / f'{failure_id}_browser_logs.json'
            with open(browser_logs_path, "x") as file:
                file.write(json.dumps(driver.get_log("browser"), indent=4))
            record_property("testrail_attachment", browser_logs_path)

            # Save web_pages_logfile
            record_property("testrail_attachment", WEB_PAGES_LOGFILE_PATH)

        except Exception as ex:
            print(ex)
