from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import ChromiumDriver

from config import BASE_URL
from helpers.logger import log
from interaction_with_web_pages.user_model import UserModel
from typing import Self


class MethodsToInteractWithPages:
    def __init__(self, driver):
        self.driver: ChromiumDriver = driver
        self.wait = WebDriverWait(driver, timeout=15)
        self.base_url = BASE_URL
        self.url = f'{self.base_url}/'

    def open_page(self):
        self.driver.get(self.url)

    def wait_for_visibility_of_el(self, locator: tuple) -> WebElement:
        """Цей метод очікує, поки е-нт стане видимим на стрінці"""
        try:
            wait_until = self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            log.error(f'TimeoutException. {e}')
            raise TimeoutException(f"Element '{locator}' not found.")
        else:
            return wait_until

    def click_on(self, locator: tuple) -> Self:
        self.wait_for_visibility_of_el(locator).click()
        return self

    def set_data(self, locator: tuple, user: UserModel) -> Self:
        self.wait_for_visibility_of_el(locator).send_keys(user)
        return self

    def get_text(self, locator: tuple) -> str:
        return self.wait_for_visibility_of_el(locator).text

    def clear_field(self, locator: tuple) -> Self:
        self.wait_for_visibility_of_el(locator).clear()
        return self

    def wait_for_visibility_of_all_elements(self, locator: tuple) -> list:
        """Цей метод очікує, поки ЕЛЕМЕНТИ стануть видимии на стрінці"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def scroll_js(self, locator: tuple) -> Self:
        """Цей метод переміщує курсор миші до заданого ел-та за доп JS"""
        self.driver.execute_script('arguments[0].scrollIntoView();', self.wait_for_visibility_of_el(locator))
        return self

    def remove_advertising_in_footer(self) -> Self:
        """Цей метод видаляє рекламу в футері, яка перекриває веб-елементи"""
        self.driver.execute_script('document.getElementById("adplus-anchor").remove();')
        self.driver.execute_script('document.getElementsByTagName("footer")[0].remove();')
        self.driver.execute_script('document.getElementById("close-fixedban").remove();')
        return self

