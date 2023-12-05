from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from interaction_with_web_pages.user_model import UserModel
from typing import Self


class MethodsToInteractWithPages:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15)

    def wait_for_visibility_of_el(self, locator: tuple) -> WebElement:
        """Цей метод очікує, поки е-нт стане видимим на стрінці"""
        return self.wait.until(EC.visibility_of_element_located(locator))

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

