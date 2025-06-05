from selenium.webdriver.common.by import By

class MainFuncLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[normalize-space(text())='Конструктор']]")
    CONSTRUCT_BURGER_TEXT = (By.XPATH, "//h1[normalize-space(text())='Соберите бургер']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[.//p[normalize-space(text())='Лента Заказов']]")
    FIRST_ORDER_BUTTON = (By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r.mb-6")
    BULKA = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]//p[text()='Флюоресцентная булка R2-D3']")
    ORDER_MODAL_WINDOW = (By.CSS_SELECTOR, "div.Modal_orderBox__1xWdi.Modal_modal__contentBox__sCy8X.p-10")
    CLOSE_ORDER_MODAL_WINDOW_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS")
    ORDER_CONSTRUCTOR = (By.XPATH, "//span[text()='Перетяните булочку сюда (верх)']/ancestor::li")
    PRICE_1976 = (By.XPATH, "//p[@class='text text_type_digits-medium mr-3' and text()='1976']")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_ID_LABEL = (By.XPATH, "//p[text()='идентификатор заказа']")
