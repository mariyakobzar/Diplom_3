from selenium.webdriver.common.by import By

from page_object.pages.base_page import BasePage


class RestorePassPassLocators(BasePage):

    BUTTON_SHOW_HIDE_PASS = By.CSS_SELECTOR, 'fieldset>div>div>div>svg[xmlns="http://www.w3.org/2000/svg"]'
    INPUT_PASS_ACTIVE = By.CSS_SELECTOR, 'div>label[class="input__placeholder text noselect text_type_main-default input__placeholder-focused"]'



