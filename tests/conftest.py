import time
import pytest
from selenium import webdriver
from faker import Faker
import random
from helpers.file_system import FileSystem
from interaction_with_web_pages.page_objects.all_pages import AllPages
from interaction_with_web_pages.user_model import UserModel


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver


@pytest.fixture(scope="class")
def all_pages(driver):
    driver.maximize_window()
    driver.get('https://demoqa.com/')
    all_pages = AllPages(driver)
    yield all_pages
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    driver = item.funcargs.get('driver', None)  # Отримання фікстури 'driver' з контексту

    if report.when == "call":
        extra.append(pytest_html.extras.url(""))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = str(int(round(time.time() * 1000))) + ".png"
            destinationFile = FileSystem.get_absolute_path_for_file('repots', file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html_content = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"' \
                               'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html_content))
        report.extras = extra


def pytest_html_report_title(report):
    report.title = "Test Web pages Report"
