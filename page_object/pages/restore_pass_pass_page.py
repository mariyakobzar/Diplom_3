import allure

from page_object.locators.restore_pass_pass_locators import RestorePassPassLocators
from page_object.pages.base_page import BasePage


class RestorePassPassPage(BasePage):

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_hide_pass_button(self):
        self.find_element_with_wait(RestorePassPassLocators.BUTTON_SHOW_HIDE_PASS)
        self.click_to_element(RestorePassPassLocators.BUTTON_SHOW_HIDE_PASS)

    @allure.step("Получение текста Пароль")
    def text_input_password(self):
        self.find_element_with_wait(RestorePassPassLocators.INPUT_PASS_ACTIVE)
        return self.get_text_to_element(RestorePassPassLocators.INPUT_PASS_ACTIVE)