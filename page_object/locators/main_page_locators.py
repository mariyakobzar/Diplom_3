from selenium.webdriver.common.by import By


class MainPageLocators():

    BUTTON_ACCOUNT = By.XPATH, '//nav/a/p[@class = "AppHeader_header__linkText__3q_va ml-2"]'

    TEXT_COLLECT_BURGER = By.XPATH, '//h1[@class = "text text_type_main-large mb-5 mt-10"]'

    BUN_1 = By.XPATH, '//a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href = "/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    MODAL_INGR = By.XPATH, '//section[@class = "Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]'

    BUN_1 = By.XPATH, '//ul[1]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][1]'
    BUN_2 = By.XPATH, '//ul[1]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][2]'
    SOUCE_1 = By.XPATH, '//ul[2]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][1]'
    SOUCE_2 = By.XPATH, '//ul[2]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][2]'
    SOUCE_3 = By.XPATH, '//ul[2]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][3]'
    SOUCE_4 = By.XPATH, '//ul[2]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][4]'
    MAIN_1 = By.XPATH, '//ul[3]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][1]'
    MAIN_2 = By.XPATH, '//ul[3]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][2]'
    MAIN_3 = By.XPATH, '//ul[3]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][3]'
    MAIN_4 = By.XPATH, '//ul[3]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][4]'
    MAIN_5 = By.XPATH, '//ul[3]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][5]'
    MAIN_6 = By.XPATH, '//ul[3]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][6]'
    MAIN_7 = By.XPATH, '//ul[3]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][7]'
    MAIN_8 = By.XPATH, '//ul[3]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][8]'
    MAIN_9 = By.XPATH, '//ul[3]/a[@class = "BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][9]'

    CROSS = By.XPATH, '//section[1]/div/button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'
    CROSS_CLOSE = By.XPATH, '//section[@class = "Modal_modal__P3_V5"][1]'

    BASKET = By.XPATH, '//ul[@class = "BurgerConstructor_basket__list__l9dp_"]'

    BUN_1_NUM = By.XPATH, '//ul[1]/a[1]/div/p[@class = "counter_counter__num__3nue1"]'
    BUN_2_NUM = By.XPATH, '//ul[1]/a[2]/div/p[@class = "counter_counter__num__3nue1"]'
    SOUCE_1_NUM = By.XPATH, '//ul[2]/a[1]/div/p[@class = "counter_counter__num__3nue1"]'
    SOUCE_2_NUM = By.XPATH, '//ul[2]/a[2]/div/p[@class = "counter_counter__num__3nue1"]'
    SOUCE_3_NUM = By.XPATH, '//ul[2]/a[3]/div/p[@class = "counter_counter__num__3nue1"]'
    SOUCE_4_NUM = By.XPATH, '//ul[2]/a[4]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_1_NUM = By.XPATH, '//ul[3]/a[1]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_2_NUM = By.XPATH, '//ul[3]/a[2]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_3_NUM = By.XPATH, '//ul[3]/a[3]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_4_NUM = By.XPATH, '//ul[3]/a[4]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_5_NUM = By.XPATH, '//ul[3]/a[5]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_6_NUM = By.XPATH, '//ul[3]/a[6]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_7_NUM = By.XPATH, '//ul[3]/a[7]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_8_NUM = By.XPATH, '//ul[3]/a[8]/div/p[@class = "counter_counter__num__3nue1"]'
    MAIN_9_NUM = By.XPATH, '//ul[3]/a[9]/div/p[@class = "counter_counter__num__3nue1"]'

    MODAL_ORDER = By.XPATH, '//div[@class = "Modal_modal__contentBox__sCy8X pt-30 pb-30"]'
    BUTTON_MAKE_ORDER = By.XPATH, '//button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
    NUMBER_OF_ORDER = By.XPATH, '//h2[@class = "Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'

    CROSS_MODAL_ORDER = By.XPATH, '//button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'

    NUMBER_OF_ORDER_MODAL = By.XPATH, '//h2[@class = "Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'

