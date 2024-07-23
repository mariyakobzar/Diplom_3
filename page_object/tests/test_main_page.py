
import allure
import pytest

from page_object.conftest import return_data_pass
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.enter_page import EnterPage
from page_object.pages.main_page import MainPage


class TestMainPage():
    @pytest.mark.parametrize(
        'num',
        [
            (MainPageLocators.BUN_1),
            (MainPageLocators.BUN_2),
            (MainPageLocators.SOUCE_1),
            (MainPageLocators.SOUCE_2),
            (MainPageLocators.SOUCE_3),
            (MainPageLocators.SOUCE_4),
            (MainPageLocators.MAIN_1),
            (MainPageLocators.MAIN_2),
            (MainPageLocators.MAIN_3),
            (MainPageLocators.MAIN_4),
            (MainPageLocators.MAIN_5),
            (MainPageLocators.MAIN_6),
            (MainPageLocators.MAIN_7),
            (MainPageLocators.MAIN_8),
            (MainPageLocators.MAIN_9)
        ]
    )
    @allure.title('Появление встплывающего окна с деталями ингредиента')
    def test_modal_window_with_ingr_details(self, driver, num):
        main_page = MainPage(driver)
        main_page.modal_window_with_ingr_details(num)

        assert main_page.find_element_with_wait(MainPageLocators.MODAL_INGR)

    @pytest.mark.parametrize(
        'num',
        [
            (MainPageLocators.BUN_1),
            (MainPageLocators.BUN_2),
            (MainPageLocators.SOUCE_1),
            (MainPageLocators.SOUCE_2),
            (MainPageLocators.SOUCE_3),
            (MainPageLocators.SOUCE_4),
            (MainPageLocators.MAIN_1),
            (MainPageLocators.MAIN_2),
            (MainPageLocators.MAIN_3),
            (MainPageLocators.MAIN_4),
            (MainPageLocators.MAIN_5),
            (MainPageLocators.MAIN_6),
            (MainPageLocators.MAIN_7),
            (MainPageLocators.MAIN_8),
            (MainPageLocators.MAIN_9)
        ]
    )
    @allure.title('Закрытие всплывающего окна с деталями ингредиента')
    def test_modal_window_with_ingr_details_close(self, driver, num):
        main_page = MainPage(driver)
        main_page.modal_window_with_ingr_details_close(num)

        assert main_page.find_element_with_wait(MainPageLocators.CROSS_CLOSE)

    @pytest.mark.parametrize(
        'num, result',
        [
            (MainPageLocators.BUN_1, MainPageLocators.BUN_1_NUM),
            (MainPageLocators.BUN_2, MainPageLocators.BUN_2_NUM)
        ]
    )
    @allure.title('Добавить ингредиент в заказ')
    def test_add_ingredient_bun(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.add_ingredient(num)
        main_page.find_element_with_wait(result)
        value = int(main_page.get_text_to_element(result)) * 2

        assert value == 4

    @pytest.mark.parametrize(
        'num, result',
        [
            (MainPageLocators.SOUCE_1, MainPageLocators.SOUCE_1_NUM),
            (MainPageLocators.SOUCE_2, MainPageLocators.SOUCE_2_NUM),
            (MainPageLocators.SOUCE_3, MainPageLocators.SOUCE_3_NUM),
            (MainPageLocators.SOUCE_4, MainPageLocators.SOUCE_4_NUM),
            (MainPageLocators.MAIN_1, MainPageLocators.MAIN_1_NUM),
            (MainPageLocators.MAIN_2, MainPageLocators.MAIN_2_NUM),
            (MainPageLocators.MAIN_3, MainPageLocators.MAIN_3_NUM),
            (MainPageLocators.MAIN_4, MainPageLocators.MAIN_4_NUM),
            (MainPageLocators.MAIN_5, MainPageLocators.MAIN_5_NUM),
            (MainPageLocators.MAIN_6, MainPageLocators.MAIN_6_NUM),
            (MainPageLocators.MAIN_7, MainPageLocators.MAIN_7_NUM),
            (MainPageLocators.MAIN_8, MainPageLocators.MAIN_8_NUM),
            (MainPageLocators.MAIN_9, MainPageLocators.MAIN_9_NUM)
        ]
    )
    @allure.title('Добавить ингредиент в заказ')
    def test_add_ingredient(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.add_ingredient(num)
        main_page.find_element_with_wait(result)
        value = int(main_page.get_text_to_element(result)) * 2

        assert value == 2

    @allure.title('Оформить заказ, пользователь залогинен')
    def test_make_order_user_login(self, driver, return_data_pass):
        main_page = MainPage(driver)
        enter_page = EnterPage(driver)
        main_page.get_account_access()
        enter_page.enter_account(return_data_pass)
        driver.implicitly_wait(3)
        main_page.add_ingredient(MainPageLocators.BUN_1)
        main_page.add_ingredient(MainPageLocators.SOUCE_2)
        main_page.add_ingredient(MainPageLocators.MAIN_3)
        main_page.make_order_user_login()

        assert main_page.find_element_with_wait(MainPageLocators.MODAL_ORDER)

