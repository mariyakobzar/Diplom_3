import allure

from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.account_page import AccountPage
from page_object.pages.enter_page import EnterPage
from page_object.pages.header_page import HeaderPage
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrdersPage


class TestOrderPage():

    @allure.title('Появление всплывающего окна с деталями заказа')
    def test_modal_with_order_details(self, driver, return_data_pass):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        orders_page = OrdersPage(driver)
        header_page = HeaderPage(driver)
        main_page.get_account_access()
        enter_page.enter_account(return_data_pass)
        main_page.add_ingredient(MainPageLocators.BUN_1)
        main_page.add_ingredient(MainPageLocators.SOUCE_2)
        main_page.add_ingredient(MainPageLocators.MAIN_3)
        main_page.make_order_user_login()
        main_page.close_modal_order()
        header_page.enter_orders()
        result = orders_page.modal_with_order_details()

        assert result == 'Cостав'

    @allure.title('Заказ пользователя отображается в ленте заказов')
    def test_modal_with_order_details(self, driver, return_data_pass):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        orders_page = OrdersPage(driver)
        header_page = HeaderPage(driver)
        account_page = AccountPage(driver)
        main_page.get_account_access()
        enter_page.enter_account(return_data_pass)
        main_page.add_ingredient(MainPageLocators.BUN_1)
        main_page.add_ingredient(MainPageLocators.SOUCE_3)
        main_page.add_ingredient(MainPageLocators.MAIN_4)
        main_page.make_order_user_login()
        main_page.close_modal_order()
        main_page.get_account_access()
        account_page.move_to_order_history()
        n = account_page.find_last_order()
        header_page.enter_orders()
        m = orders_page.get_number_of_last_order()

        assert n == m

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_modal_with_order_details(self, driver, return_data_pass):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        orders_page = OrdersPage(driver)
        header_page = HeaderPage(driver)
        main_page.get_account_access()
        enter_page.enter_account(return_data_pass)
        header_page.enter_orders()
        before = orders_page.get_number_of_orders()
        header_page.press_logo()
        main_page.add_ingredient(MainPageLocators.BUN_1)
        main_page.add_ingredient(MainPageLocators.SOUCE_2)
        main_page.add_ingredient(MainPageLocators.MAIN_4)
        main_page.make_order_user_login()
        main_page.close_modal_order()
        header_page.enter_orders()
        after = orders_page.get_number_of_orders()

        assert int(after) == (int(before) + 1)

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_modal_with_order_details(self, driver, return_data_pass):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        orders_page = OrdersPage(driver)
        header_page = HeaderPage(driver)
        main_page.get_account_access()
        enter_page.enter_account(return_data_pass)
        header_page.enter_orders()
        before = orders_page.get_number_of_orders_today()
        header_page.press_logo()
        main_page.add_ingredient(MainPageLocators.BUN_1)
        main_page.add_ingredient(MainPageLocators.SOUCE_2)
        main_page.add_ingredient(MainPageLocators.MAIN_4)
        main_page.make_order_user_login()
        main_page.close_modal_order()
        header_page.enter_orders()
        after = orders_page.get_number_of_orders_today()

        assert int(after) == (int(before) + 1)

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_modal_with_order_details(self, driver, return_data_pass):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        orders_page = OrdersPage(driver)
        header_page = HeaderPage(driver)
        main_page.get_account_access()
        enter_page.enter_account(return_data_pass)
        main_page.find_buns()
        main_page.add_ingredient(MainPageLocators.BUN_1)
        main_page.add_ingredient(MainPageLocators.SOUCE_2)
        main_page.add_ingredient(MainPageLocators.MAIN_4)
        main_page.make_order_user_login()
        number = main_page.get_number_of_order()
        main_page.close_modal_order()
        header_page.enter_orders()
        in_work = orders_page.get_number_of_orders_in_work()

        assert in_work == f'0{number}'

