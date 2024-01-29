import json
from uuid import uuid4
import pytest
from selenium import webdriver
from faker import Faker
import random
from config import DIR_REPORTS_PATH
from interaction_with_web_pages.page_objects.all_pages import AllPages
from interaction_with_web_pages.user_model import UserModel


@pytest.fixture(scope="function")
def all_pages(request, record_property):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/')
    all_pages = AllPages(driver)
    yield all_pages
    save_failure_artifacts(driver, request, record_property)
    driver.quit()


@pytest.fixture(scope="class")
def input_user_data():
    fake = Faker(locale='uk_UA')
    list_departments = [
        'Insurance',
        'Compliance',
        'Legal'
    ]
    list_subjects = [
                "Hindi",
                "English",
                "Maths",
                "Physics",
                "Chemistry",
                "Biology",
                "Computer Science",
                "Commerce",
                "Accounting",
                "Economics",
                "Arts",
                "Social Studies",
                "History",
                "Civics"
            ]
    dict_state_city = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
    }
    list_states = list(dict_state_city.keys())
    random_state = list_states[random.randint(0, 3)]
    cities_in_the_random_state = dict_state_city[random_state]
    length_of_the_cities_list = len(cities_in_the_random_state)
    random_city = cities_in_the_random_state[random.randint(0, length_of_the_cities_list - 1)]

    user_data = UserModel(
        full_name=fake.first_name(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address(),
        new_email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=random.randint(18, 79),
        salary=random.randint(1000, 20000),
        department=list_departments[random.randint(0, 2)],
        phone_number=random.randint(9347822912, 9947822913),
        subject=list_subjects[random.randint(0, 13)],
        state=random_state,
        city=random_city,
    )
    return user_data


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

        except Exception as ex:
            print(ex)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
