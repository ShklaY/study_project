import pytest
from selenium import webdriver
from data_base.helper_db import DataBaseConnection


@pytest.fixture(scope="class")
def driver_chrome():
    # TODO 1 should be reimplemented with selenium wrapper
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/')
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def get_db():
    db = DataBaseConnection()
    yield db
    db.close()
