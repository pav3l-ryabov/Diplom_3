from selenium.webdriver import ActionChains, Keys

import allure
from locators.main_func_locators import MainFuncLocators
from pages.base_page import BasePage

class MainFuncPage(BasePage):
    @allure.step('Клик на кнопку Конструктор')
    def click_on_constructor_button(self):
        self.wait_for_element_to_be_clickable(MainFuncLocators.CONSTRUCTOR_BUTTON)
        self.click_to_element(MainFuncLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на кнопку Лента заказов')
    def click_on_order_feed_button(self):
        self.wait_for_element_to_be_clickable(MainFuncLocators.ORDER_FEED_BUTTON)
        self.click_to_element(MainFuncLocators.ORDER_FEED_BUTTON)

    @allure.step('Клик на кнопку заказа')
    def click_on_order_button(self):
        self.wait_for_element_to_be_clickable(MainFuncLocators.FIRST_ORDER_BUTTON)
        self.click_to_element(MainFuncLocators.FIRST_ORDER_BUTTON)

    @allure.step('Клик на кнопку закрытия модального окна заказа через ActionChains')
    def click_on_close_order_button(self):
        self.click_to_element_with_actionchains(MainFuncLocators.CLOSE_ORDER_MODAL_WINDOW_BUTTON)

    @allure.step('Закрывает всплывающее окно через escape')
    def press_esc(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()

    @allure.step('Перетаскивание ингредиента в заказ')
    def add_ingredient_into_order(self, source_locator, target_locator):
        self.drag_and_drop(source_locator, target_locator)

    @allure.step('Клик на кнопку создания заказа')
    def click_create_order_button(self):
        self.click_to_element_with_actionchains(MainFuncLocators.CREATE_ORDER_BUTTON)