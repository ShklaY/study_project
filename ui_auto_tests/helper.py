from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseMethods:
    """це допоміжний клас, що містить базові методи для взаємодії з веб-елементами"""
    def __init__(self, chrome_driver):
        self.driver = chrome_driver
        self.wait = WebDriverWait(self.driver, timeout=15)

    def wait_for_visibility_of_el(self, locator_type: str, locator: str) -> WebElement:
        """Цей метод очікує, поки е-нт стане видимим на стрінці"""
        return self.wait.until(EC.visibility_of_element_located((locator_type, locator)))

    def wait_for_visibility_of_all_elements(self, locator_type: str, locator: str) -> list:
        """Цей метод очікує, поки ЕЛЕМЕНТИ стануть видимии на стрінці"""
        return self.wait.until(EC.visibility_of_all_elements_located((locator_type, locator)))

    def scroll_js(self, wait_for_: WebElement) -> None:
        """Цей метод переміщує курсор миші до заданого ел-та за доп JS"""
        self.driver.execute_script('arguments[0].scrollIntoView();', wait_for_)

    def remove_advertising_in_footer(self) -> None:
        """Цей метод видаляє рекламу в футері, яка перекриває веб-елементи"""
        self.driver.execute_script('document.getElementById("adplus-anchor").remove();')
        self.driver.execute_script('document.getElementsByTagName("footer")[0].remove();')
        self.driver.execute_script('document.getElementById("close-fixedban").remove();')

