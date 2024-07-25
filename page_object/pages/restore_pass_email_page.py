import allure

from page_object.data import Data_for_tests
from page_object.locators.restore_pass_email_locators import RestorePassEmailLocators
from page_object.pages.base_page import BasePage


class RestorePassEmailPage(BasePage):

    @allure.step("ввод email для восстановления пароля")
    def input_email_for_restore_pass(self):
        self.find_element_with_wait(RestorePassEmailLocators.TEXT_RESTORE_PASS)
        self.find_element_with_wait(RestorePassEmailLocators.INPUT_EMAIL)
        self.click_to_element(RestorePassEmailLocators.INPUT_EMAIL)
        self.add_text_to_element(RestorePassEmailLocators.INPUT_EMAIL, Data_for_tests.EMAIL)
        self.find_element_with_wait(RestorePassEmailLocators.BUTTON_RESTORE)
        self.click_to_element(RestorePassEmailLocators.BUTTON_RESTORE)

