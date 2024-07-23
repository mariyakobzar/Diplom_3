from selenium.webdriver.common.by import By


class EnterPageLocators():

    TEXT_ENTER = By.XPATH, '//h2[text() = "Вход"]'

    BUTTON_RESTORE_PASS = By.XPATH, '//a[@class = "Auth_link__1fOlj" and text() = "Восстановить пароль"]'

    INPUT_EMAIL = By.XPATH, '//input[@class = "text input__textfield text_type_main-default" and @name = "name"]'
    INPUT_PASSWORD = By.XPATH, '//input[@class = "text input__textfield text_type_main-default" and @name = "Пароль"]'

    BUTTON_ENTER = By.XPATH, '//button[text() = "Войти"]'

