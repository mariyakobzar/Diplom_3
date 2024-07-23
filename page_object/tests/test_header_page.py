import allure

from page_object.locators.header_page_locators import HeaderPageLocators
from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.orders_page_locators import OrdersPageLocators
from page_object.pages.header_page import HeaderPage
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrdersPage


class TestHeaderPage():

    @allure.title('Переход в конструктор')
    def test_enter_constructor(self, driver):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        main_page.get_account_access()
        header_page.enter_constructor()

        assert main_page.find_element_with_wait(MainPageLocators.TEXT_COLLECT_BURGER)

    @allure.title('Переход в ленту заказов')
    def test_enter_orders(self, driver):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        orders_page = OrdersPage(driver)
        main_page.get_account_access()
        header_page.enter_orders()

        assert orders_page.get_header_name() == "Лента заказов"
