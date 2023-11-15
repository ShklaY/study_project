import random


class InitPageLocators:
    btn_elements = '//*[@id="app"]/div/div/div[2]/div/div[1]'
    btn_forms = '//*[@id="app"]/div/div/div[2]/div/div[2]'


class HeaderLocators:
    header = 'div[class="main-header"]'


class MenuBarLocators:
    menu_btn_text_box = '//span[text()="Text Box"]'
    menu_btn_check_box = '//span[text()="Check Box"]'
    menu_btn_radio_button = '//span[text()="Radio Button"]'
    menu_btn_web_tables = '//span[text()="Web Tables"]'
    menu_btn_practice_form = '//span[text()="Practice Form"]'


class TextBoxPageLocators:
    txt_full_name = 'input[id="userName"]'
    txt_email = 'input[id="userEmail"]'
    txt_current_address = 'textarea[id="currentAddress"]'
    txt_permanent_address = 'textarea[id="permanentAddress"]'
    btn_submit = 'button[id="submit"]'

    output_full_name = 'p[id="name"]'
    output_email = 'p[id="email"]'
    output_current_address = 'p[id="currentAddress"]'
    output_permanent_address = 'p[id="permanentAddress"]'


class CheckBoxPageLocators:
    btn_expand_all = 'button[title="Expand all"]'
    titles_of_checkboxes = '[class="rct-title"]'


class RadioButtonPageLocators:
    radio_buttons = "//label[contains(@class, 'custom-control-label')]"
    output_text = '[class="text-success"]'

    preceding_sibling_for_radio_btns = ".//preceding-sibling::input"


class WebTablesPageLocators:
    btn_add = 'button[id="addNewRecordButton"]'
    txt_first_name = 'input[id="firstName"]'
    txt_last_name = 'input[id="lastName"]'
    txt_user_email = 'input[id="userEmail"]'
    txt_age = 'input[id="age"]'
    txt_salary = 'input[id="salary"]'
    txt_department = 'input[id="department"]'
    btn_submit = 'button[id="submit"]'
    rows = 'div[class="rt-tr-group"]'

    txt_search = 'input[id="searchBox"]'
    btn_edit = '[title="Edit"]'
    btn_delete = '[title="Delete"]'
    the_checking_text = '[class="rt-noData"]'

    btn_the_quantity_of_rows = 'select[aria-label="rows per page"]'


class PracticeFormPageLocators:
    txt_first_name = '[id="firstName"]'
    txt_last_name = '[id="lastName"]'
    txt_email = '[id="userEmail"]'
    radio_btn_gender = f'[for="gender-radio-{random.randint(1,3)}"]'
    txt_mobile_number = '[id="userNumber"]'
    date_of_birth = '[id="dateOfBirthInput"]'
    txt_subjects = 'input[id="subjectsInput"]'
    hobbies = f'[for="hobbies-checkbox-{random.randint(1,3)}"]'
    picture = ''
    txt_current_address = '[id="currentAddress"]'

    select_state = 'div[id="state"]'
    locator_input_state = 'input[id="react-select-3-input"]'
    select_city = 'div[id="city"]'
    locator_input_city = 'input[id="react-select-4-input"]'
    btn_submit = '[id="submit"]'

    result_table = '//tr/td[2]'



