import allure

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

        assert main_page.text_form_collect_burger() == 'Соберите бургер'

    @allure.title('Переход в ленту заказов')
    def test_enter_orders(self, driver):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        orders_page = OrdersPage(driver)
        main_page.get_account_access()
        header_page.enter_orders()

        assert orders_page.get_header_name() == "Лента заказов"
