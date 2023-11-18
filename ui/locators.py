import random


class InitPageLocators:
    # TODO 3 locators should be defined in page object
    BTN_ELEMENTS = '//*[@id="app"]/div/div/div[2]/div/div[1]'
    BTN_FORMS = '//*[@id="app"]/div/div/div[2]/div/div[2]'


class MenuBarLocators:
    BTN_TEXT_BOX = '//span[text()="Text Box"]'
    BTN_CHECK_BOX = '//span[text()="Check Box"]'
    BTN_RADIO_BUTTON = '//span[text()="Radio Button"]'
    BTN_WEB_TABLES = '//span[text()="Web Tables"]'
    BTN_PRACTICE_FORM = '//span[text()="Practice Form"]'


class TextBoxPageLocators:
    TXT_FULL_NAME = 'input[id="userName"]'
    TXT_EMAIL = 'input[id="userEmail"]'
    TXT_CURRENT_ADDRESS = 'textarea[id="currentAddress"]'
    TXT_PERMANENT_ADDRESS = 'textarea[id="permanentAddress"]'
    BTN_SUBMIT = 'button[id="submit"]'

    OUTPUT_FULL_NAME = 'p[id="name"]'
    OUTPUT_EMAIL = 'p[id="email"]'
    OUTPUT_CURRENT_ADDRESS = 'p[id="currentAddress"]'
    OUTPUT_PERMANENT_ADDRESS = 'p[id="permanentAddress"]'


class CheckBoxPageLocators:
    BTN_EXPAND_ALL = 'button[title="Expand all"]'
    TITLES_OF_CHECKBOXES = '[class="rct-title"]'
    ICON_CHECK = '[class="rct-icon rct-icon-check"]'
    ancestor_for_checked_checkboxes = './/ancestor::span[@class="rct-text"]'
    SELECTED_CHECKBOXES = '//div/span[@class="text-success"]'


class RadioButtonPageLocators:
    RADIO_BUTTONS = "//label[contains(@class, 'custom-control-label')]"
    OUTPUT_TEXT = '[class="text-success"]'

    PRECEDING_SIBLING_FOR_RADIO_BTNS = ".//preceding-sibling::input"


class WebTablesPageLocators:
    BTN_ADD = 'button[id="addNewRecordButton"]'
    TXT_FIRST_NAME = 'input[id="firstName"]'
    TXT_LAST_NAME = 'input[id="lastName"]'
    TXT_USER_EMAIL = 'input[id="userEmail"]'
    TXT_AGE = 'input[id="age"]'
    TXT_SALARY = 'input[id="salary"]'
    TXT_DEPARTMENT = 'input[id="department"]'
    BTN_SUBMIT = 'button[id="submit"]'
    ROWS = 'div[class="rt-tr-group"]'

    TXT_SEARCH = 'input[id="searchBox"]'
    BTN_EDIT = '[title="Edit"]'
    BTN_DELETE = '[title="Delete"]'
    THE_CHECKING_TEXT = '[class="rt-noData"]'

    BTN_THE_QUANTITY_OF_ROWS = 'select[aria-label="rows per page"]'


class PracticeFormPageLocators:
    TXT_FIRST_NAME = '[id="firstName"]'
    TXT_LAST_NAME = '[id="lastName"]'
    TXT_EMAIL = '[id="userEmail"]'
    RADIO_BTN_GENDER = f'[for="gender-radio-{random.randint(1, 3)}"]'
    TXT_MOBILE_NUMBER = '[id="userNumber"]'
    DATE_OF_BIRTH = '[id="dateOfBirthInput"]'
    TXT_SUBJECTS = 'input[id="subjectsInput"]'
    HOBBIES = f'[for="hobbies-checkbox-{random.randint(1, 3)}"]'
    PICTURE = ''
    TXT_CURRENT_ADDRESS = '[id="currentAddress"]'

    SELECT_STATE = 'div[id="state"]'
    LOCATOR_INPUT_STATE = 'input[id="react-select-3-input"]'
    SELECT_CITY = 'div[id="city"]'
    LOCATOR_INPUT_CITY = 'input[id="react-select-4-input"]'
    BTN_SUBMIT = '[id="submit"]'

    RESULT_TABLE = '//tr/td[2]'



