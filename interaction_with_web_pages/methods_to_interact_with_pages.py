from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from interaction_with_web_pages.user_model import UserModel


class MethodsToInteractWithPages:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15)

    def wait_for_visibility_of_el(self, locator_type: str, locator: str) -> WebElement:
        """Цей метод очікує, поки е-нт стане видимим на стрінці"""
        return self.wait.until(EC.visibility_of_element_located((locator_type, locator)))

    def click_on(self, locator_type: str, locator: str) -> None:
        self.wait_for_visibility_of_el(locator_type, locator).click()

    def set_data(self, locator_type: str, locator: str, user: UserModel):
        self.wait_for_visibility_of_el(locator_type, locator).send_keys(user)
        return user

    def get_text(self, locator_type: str, locator: str) -> str:
        return self.wait_for_visibility_of_el(locator_type, locator).text

    def clear_field(self, locator_type: str, locator: str) -> None:
        self.wait_for_visibility_of_el(locator_type, locator).clear()

    def wait_for_visibility_of_all_elements(self, locator_type: str, locator: str) -> list:
        """Цей метод очікує, поки ЕЛЕМЕНТИ стануть видимии на стрінці"""
        return self.wait.until(EC.visibility_of_all_elements_located((locator_type, locator)))

    def scroll_js(self, locator_type: str, locator: str) -> None:
        """Цей метод переміщує курсор миші до заданого ел-та за доп JS"""
        self.driver.execute_script('arguments[0].scrollIntoView();', self.wait_for_visibility_of_el(locator_type, locator))

    def remove_advertising_in_footer(self) -> None:
        """Цей метод видаляє рекламу в футері, яка перекриває веб-елементи"""
        self.driver.execute_script('document.getElementById("adplus-anchor").remove();')
        self.driver.execute_script('document.getElementsByTagName("footer")[0].remove();')
        self.driver.execute_script('document.getElementById("close-fixedban").remove();')

