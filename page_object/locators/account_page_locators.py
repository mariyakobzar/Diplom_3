from selenium.webdriver.common.by import By


class AccountPageLocators():

    BUTTON_PROFILE = By.XPATH, '//a[@class = "Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]'

    BUTTON_ORDER_HISTORY = By.XPATH, '//a[@class = "Account_link__2ETsJ text text_type_main-medium text_color_inactive"]'
    BUTTON_ORDER_HISTORY_ACTIVE = By.XPATH, '//a[contains(@class, "Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active")]'

    BUTTON_EXIT = By.XPATH, '//button[text() = "Выход"]'

    NUMBER_OF_LAST_ORDER = By.XPATH, '//ul/li[last()]/a[@class = "OrderHistory_link__1iNby"]/div/p[@class = "text text_type_digits-default"]'