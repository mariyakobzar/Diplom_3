import allure

from page_object.data import Urls
from page_object.pages.account_page import AccountPage
from page_object.pages.enter_page import EnterPage
from page_object.pages.main_page import MainPage


class TestAccountPage():

    @allure.title('Вход в личный кабинет')
    def test_enter_account(self, driver, return_data_pass):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        account_page = AccountPage(driver)
        main_page.get_account_access()
        enter_page.enter_account(return_data_pass)
        main_page.get_account_access()

        assert account_page.text_button_profile == 'Личный Кабинет'

    @allure.title('Переход в историю заказов')
    def test_enter_account(self, driver, return_data_pass):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        account_page = AccountPage(driver)
        main_page.get_account_access()
        enter_page.enter_account(return_data_pass)
        main_page.get_account_access()
        account_page.move_to_order_history()

        assert account_page.url_button_orders_history() == Urls.URL_ORDERS_HISTORY

    @allure.title('Выход из аккаунта')
    def test_exit_account(self, driver, return_data_pass):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        account_page = AccountPage(driver)
        main_page.get_account_access()
        enter_page.enter_account(return_data_pass)
        main_page.get_account_access()
        account_page.exit_account()

        assert enter_page.text_form_enter_account() == 'Вход'


