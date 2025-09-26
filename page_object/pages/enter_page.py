import allure

from page_object.locators.enter_page_locators import EnterPageLocators
from page_object.pages.base_page import BasePage


class EnterPage(BasePage):

    @allure.step("Переход по кнопке 'Восстановить пароль")
    def press_button_restore_pass(self):
        self.find_element_with_wait(EnterPageLocators.BUTTON_RESTORE_PASS)
        self.click_to_element(EnterPageLocators.BUTTON_RESTORE_PASS)

    @allure.step("Вход в аккаунт")
    def enter_account(self, return_data_pass):
        self.find_element_with_wait(EnterPageLocators.INPUT_EMAIL)
        self.add_text_to_element(EnterPageLocators.INPUT_EMAIL, return_data_pass['email'])
        self.find_element_with_wait(EnterPageLocators.INPUT_PASSWORD)
        self.add_text_to_element(EnterPageLocators.INPUT_PASSWORD, return_data_pass['password'])
        self.find_element_with_wait(EnterPageLocators.BUTTON_ENTER)
        self.click_to_element(EnterPageLocators.BUTTON_ENTER)

    @allure.step("Получение текста заголовка формы логина")
    def text_form_enter_account(self):
        self.find_element_with_wait(EnterPageLocators.TEXT_ENTER)
        return self.get_text_to_element(EnterPageLocators.TEXT_ENTER)

