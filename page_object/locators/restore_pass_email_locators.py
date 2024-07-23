from selenium.webdriver.common.by import By

from page_object.pages.base_page import BasePage


class RestorePassEmailLocators(BasePage):

    TEXT_RESTORE_PASS = By.XPATH, '//h2[text() = "Восстановление пароля"]'

    INPUT_EMAIL = By.XPATH, '//input[@class = "text input__textfield text_type_main-default"]'

    BUTTON_RESTORE = By.XPATH, '//button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'

