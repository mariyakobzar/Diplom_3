from selenium.webdriver.common.by import By

from page_object.pages.base_page import BasePage


class RestorePassPassLocators(BasePage):

    BUTTON_SHOW_HIDE_PASS = By.CSS_SELECTOR, 'fieldset>div>div>div>svg[xmlns="http://www.w3.org/2000/svg"]>path'
    INPUT_PASS_ACTIVE = By.XPATH, '//div[@class = "input pr-6 pl-6 input_type_text input_size_default input_status_active"]'


