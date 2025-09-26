import allure

from page_object.pages.enter_page import EnterPage
from page_object.pages.main_page import MainPage
from page_object.pages.restore_pass_email_page import RestorePassEmailPage
from page_object.pages.restore_pass_pass_page import RestorePassPassPage


class TestRestorePassPassPage():
    @allure.title('Восстановление пароля')
    def test_click_show_hide_pass_button(self, driver):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        restore_pass_email = RestorePassEmailPage(driver)
        restore_pass_pass = RestorePassPassPage(driver)
        main_page.get_account_access()
        enter_page.press_button_restore_pass()
        restore_pass_email.input_email_for_restore_pass()
        restore_pass_pass.click_show_hide_pass_button()

        assert restore_pass_pass.text_input_password() == 'Пароль'
