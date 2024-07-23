import allure

from page_object.locators.enter_page_locators import EnterPageLocators
from page_object.locators.header_page_locators import HeaderPageLocators
from page_object.pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step("Переход в конструктор")
    def enter_constructor(self):
        self.find_element_with_wait(HeaderPageLocators.CONSTRUCTOR)
        self.click_to_element(HeaderPageLocators.CONSTRUCTOR)

    @allure.step("Переход в ленту заказов")
    def enter_orders(self):
        self.find_element_with_wait(HeaderPageLocators.ORDERS)
        self.click_to_element(HeaderPageLocators.ORDERS)

    @allure.step("Переход по Лого")
    def press_logo(self):
        self.find_element_with_wait(HeaderPageLocators.LOGO)
        self.click_to_element(HeaderPageLocators.LOGO)
