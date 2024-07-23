from selenium.webdriver.common.by import By


class OrdersPageLocators():

    TEXT_ORDERS = By.XPATH, '//h1[@class = "text text_type_main-large mt-10 mb-5"]'

    ORDER_IN_LIST = By.XPATH, '//div[@class = "OrderHistory_dataBox__1mkxK"][1]'

    CONTAINS = By.XPATH, '//p[@class = "text text_type_main-medium mb-8"]'

    NUMBER_OF_ORDER_IN_LIST = By.XPATH, '//p[@class = "text text_type_digits-default"]'

    WHOLE_ORDERS = By.XPATH, '//div[@class = "undefined mb-15"]/p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"]'
    TODAY_ORDERS = By.XPATH, '//div[3]/p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"]'

    NUMBER_OF_ORDER_IN_WORK = By.XPATH, '//ul[@class = "OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[@class = "text text_type_digits-default mb-2"][1]'