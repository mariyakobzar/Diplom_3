from selenium.webdriver.common.by import By


class HeaderPageLocators():

    CONSTRUCTOR = By.XPATH, '//p[@class = "AppHeader_header__linkText__3q_va ml-2" and text() = "Конструктор"]'

    ORDERS = By.XPATH, '//p[@class = "AppHeader_header__linkText__3q_va ml-2" and text() = "Лента Заказов"]'

    LOGO = By.CSS_SELECTOR, 'div>a>svg[xmlns = "http://www.w3.org/2000/svg"]'