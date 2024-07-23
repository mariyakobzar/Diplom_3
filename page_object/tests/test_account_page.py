import allure

from page_object.locators.account_page_locators import AccountPageLocators
from page_object.locators.enter_page_locators import EnterPageLocators
from page_object.locators.restore_pass_pass_locators import RestorePassPassLocators
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

        assert account_page.find_element_with_wait(AccountPageLocators.BUTTON_PROFILE)

    @allure.title('Переход в историю заказов')
    def test_enter_account(self, driver, return_data_pass):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        account_page = AccountPage(driver)
        main_page.get_account_access()
        enter_page.enter_account(return_data_pass)
        main_page.get_account_access()
        account_page.move_to_order_history()

        assert account_page.find_element_with_wait(AccountPageLocators.BUTTON_ORDER_HISTORY_ACTIVE)

    @allure.title('Выход из аккаунта')
    def test_exit_account(self, driver, return_data_pass):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        account_page = AccountPage(driver)
        main_page.get_account_access()
        enter_page.enter_account(return_data_pass)
        main_page.get_account_access()
        account_page.exit_account()

        assert enter_page.find_element_with_wait(EnterPageLocators.TEXT_ENTER)


