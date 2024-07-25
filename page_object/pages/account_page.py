import allure

from page_object.data import Urls
from page_object.locators.account_page_locators import AccountPageLocators
from page_object.pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step("Перейти в Историю заказов")
    def move_to_order_history(self):
        self.find_element_with_wait(AccountPageLocators.BUTTON_ORDER_HISTORY)
        self.click_to_element(AccountPageLocators.BUTTON_ORDER_HISTORY)

    @allure.step("Выйти из аккаунта")
    def exit_account(self):
        self.find_element_with_wait(AccountPageLocators.BUTTON_EXIT)
        self.click_to_element(AccountPageLocators.BUTTON_EXIT)

    @allure.step("Поиск последнего заказа")
    def find_last_order(self):
        self.find_element_with_wait(AccountPageLocators.NUMBER_OF_LAST_ORDER)
        return self.get_text_to_element(AccountPageLocators.NUMBER_OF_LAST_ORDER)

    @allure.step("Получение текста кнопки Профиль")
    def text_button_profile(self):
        self.find_element_with_wait(AccountPageLocators.BUTTON_PROFILE)
        return self.get_text_to_element(AccountPageLocators.BUTTON_PROFILE)

    @allure.step("Получение урла кнопки История заказов")
    def url_button_orders_history(self):
        return self.get_current_url()




