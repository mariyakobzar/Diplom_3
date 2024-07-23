import allure

from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Переход на страницу входа в аккаунт по кнопке Личный кабинет")
    def get_account_access(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_ACCOUNT)
        self.click_to_element(MainPageLocators.BUTTON_ACCOUNT)

    @allure.step("Появление встплывающего окна с деталями ингредиента")
    def modal_window_with_ingr_details(self, ingr):
        self.scroll_to_element(ingr)
        self.find_element_with_wait(ingr)
        self.click_to_element(ingr)

    @allure.step("Закрытие всплывающего окна с деталями ингредиента")
    def modal_window_with_ingr_details_close(self, ingr):
        self.scroll_to_element(ingr)
        self.find_element_with_wait(ingr)
        self.click_to_element(ingr)
        self.find_element_with_wait(MainPageLocators.CROSS)
        self.click_to_element(MainPageLocators.CROSS)

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient(self, ingr):
        self.scroll_to_element(ingr)
        self.drag_and_drop(ingr, MainPageLocators.BASKET)

    @allure.step("Оформить заказ, пользователь залогинен")
    def make_order_user_login(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_MAKE_ORDER)
        self.click_to_element(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step("Получение номера заказа")
    def get_number_of_order(self):
        self.find_element_with_wait(MainPageLocators.NUMBER_OF_ORDER_MODAL)
        return self.get_text_to_element(MainPageLocators.NUMBER_OF_ORDER_MODAL)


    @allure.step("Закрыть окно заказа")
    def close_modal_order(self):
        self.find_element_with_wait(MainPageLocators.CROSS_MODAL_ORDER)
        self.click_to_element(MainPageLocators.CROSS_MODAL_ORDER)