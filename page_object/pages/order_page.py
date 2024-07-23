import allure

from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.orders_page_locators import OrdersPageLocators
from page_object.pages.base_page import BasePage


class OrdersPage(BasePage):

    @allure.step("Получение заголовка раздела")
    def get_header_name(self):
        self.find_element_with_wait(OrdersPageLocators.TEXT_ORDERS)
        return self.get_text_to_element(OrdersPageLocators.TEXT_ORDERS)

    @allure.step("Появление всплывающего окна с деталями заказа")
    def modal_with_order_details(self):
        self.find_element_with_wait(OrdersPageLocators.ORDER_IN_LIST)
        self.click_to_element(OrdersPageLocators.ORDER_IN_LIST)
        return self.get_text_to_element(OrdersPageLocators.CONTAINS)

    @allure.step("Получение номера последнего заказа")
    def get_number_of_last_order(self):
        self.find_element_with_wait(OrdersPageLocators.NUMBER_OF_ORDER_IN_LIST)
        return self.get_text_to_element(OrdersPageLocators.NUMBER_OF_ORDER_IN_LIST)

    @allure.step("Получение количества заказов Всего")
    def get_number_of_orders(self):
        self.find_element_with_wait(OrdersPageLocators.WHOLE_ORDERS)
        return self.get_text_to_element(OrdersPageLocators.WHOLE_ORDERS)

    @allure.step("Получение количества заказов за сегодня")
    def get_number_of_orders_today(self):
        self.find_element_with_wait(OrdersPageLocators.TODAY_ORDERS)
        return self.get_text_to_element(OrdersPageLocators.TODAY_ORDERS)

    @allure.step("Появление номера заказа в разделе В работе")
    def get_number_of_orders_in_work(self):
        self.find_element_with_wait(OrdersPageLocators.NUMBER_OF_ORDER_IN_WORK)
        return self.get_text_to_element(OrdersPageLocators.NUMBER_OF_ORDER_IN_WORK)


