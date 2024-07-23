import allure

from page_object.locators.restore_pass_email_locators import RestorePassEmailLocators
from page_object.pages.base_page import BasePage


class RestorePassEmailPage(BasePage):

    @allure.step("ввод email для восстановления пароля")
    def input_email_for_restore_pass(self):
        self.find_element_with_wait(RestorePassEmailLocators.TEXT_RESTORE_PASS)
        self.find_element_with_wait(RestorePassEmailLocators.INPUT_EMAIL)
        self.click_to_element(RestorePassEmailLocators.INPUT_EMAIL)
        self.add_text_to_element(RestorePassEmailLocators.INPUT_EMAIL, "mariakobzar9@gmail.com")
        self.find_element_with_wait(RestorePassEmailLocators.BUTTON_RESTORE)
        self.click_to_element(RestorePassEmailLocators.BUTTON_RESTORE)

