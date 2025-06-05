from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC

import allure
from selenium.common import TimeoutException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_func_locators import MainFuncLocators
from locators.password_recovery_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    @allure.step('Узнаем число каунтера Выполнено за все время и возвращаем его')
    def get_counter_all_time_done(self):
        return int(self.get_text_from_element(MainFuncLocators.ALL_TIME_COUNTER_ORDER))

    @allure.step('Узнаем число каунтера Выполнено за сегодня и возвращаем его')
    def get_counter_one_day_time_done(self):
        return int(self.get_text_from_element(MainFuncLocators.ONE_DAY_TIME_COUNTER_ORDER))

    @allure.step('Узнаем трек номер заказа возвращаем его')
    def get_track_num_order(self):
        self.wait_until_element_invisibility(MainFuncLocators.LOADING_IMAGE)
        return int(self.get_text_from_element(MainFuncLocators.ORDER_TRACK_NUMBER))

    @allure.step('Ищем трек номер заказа в списке и возвращаем его')
    def get_track_num_order_from_list(self):
        return int(self.get_text_from_element(MainFuncLocators.LIST_ORDER_TRACK_NUMBERS))



