from selenium.webdriver.common.by import By


class MainPageLocators():

    BUTTON_ACCOUNT = By.XPATH, '//nav/a/p[@class = "AppHeader_header__linkText__3q_va ml-2"]'

    TEXT_COLLECT_BURGER = By.XPATH, '//h1[@class = "text text_type_main-large mb-5 mt-10"]'

    BUN_1 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    MODAL_INGR = By.XPATH, '//section[@class = "Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]'

    BUN_1 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    BUN_2 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa6c"]'
    SOUCE_1 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa72"]'
    SOUCE_2 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa73"]'
    SOUCE_3 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa74"]'
    SOUCE_4 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa75"]'
    MAIN_1 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa6f"]'
    MAIN_2 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa70"]'
    MAIN_3 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa71"]'
    MAIN_4 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa6e"]'
    MAIN_5 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa76"]'
    MAIN_6 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa77"]'
    MAIN_7 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa78"]'
    MAIN_8 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa79"]'
    MAIN_9 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa7a"]'

    CROSS = By.XPATH, '//section[@class = "Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/div/button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'
    CROSS_CLOSE = By.XPATH, '//section[@class = "Modal_modal__P3_V5"][1]'

    BASKET = By.XPATH, '//ul[@class = "BurgerConstructor_basket__list__l9dp_"]'

    BUN_1_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa6d"]/div/p[@class = "counter_counter__num__3nue1"]'
    BUN_2_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa6c"]/div/p[@class = "counter_counter__num__3nue1"]'
    SOUCE_1_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa72"]/div/p[@class = "counter_counter__num__3nue1"]'
    SOUCE_2_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa73"]/div/p[@class = "counter_counter__num__3nue1"]'
    SOUCE_3_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa74"]/div/p[@class = "counter_counter__num__3nue1"]'
    SOUCE_4_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa75"]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_1_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa6f"]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_2_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa70"]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_3_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa71"]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_4_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa6e"]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_5_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa76"]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_6_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa77"]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_7_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa78"]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_8_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa79"]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_9_NUM = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa7a"]/div/p[@class = "counter_counter__num__3nue1"]'

    MODAL_ORDER = By.XPATH, '//div[@class = "Modal_modal__contentBox__sCy8X pt-30 pb-30"]'

    BUTTON_MAKE_ORDER = By.XPATH, '//button[contains(@class, "button_button_size_large")]'
    ID_ORDER = By.XPATH, '//p[@class = "undefined text text_type_main-medium mb-15"]'
    NUMBER_OF_ORDER = By.XPATH, '//h2[@class = "Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'

    CROSS_MODAL_ORDER = By.XPATH, '//button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'

    NUMBER_OF_ORDER_MODAL = By.XPATH, '//h2[@class = "Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'

    BUNS = By.XPATH, '//h2[@class = "text text_type_main-medium mb-6 mt-10" and text() = "Булки"]'
