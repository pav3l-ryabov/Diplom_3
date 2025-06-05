import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

import allure
import pytest

from data.data import URL_MAIN_PAGE, URL_FORGOT_PASSWORD_PAGE, URL_LOGIN_PAGE, URL_RESET_PASSWORD_PAGE, TEST_MAIL, \
    TEST_PASS, URL_PERSONAL_ACCOUNT_PAGE, URL_ORDER_HISTORY_PAGE, URL_ORDER_FEED_PAGE
from locators.main_func_locators import MainFuncLocators
from locators.password_recovery_locators import PasswordRecoveryPageLocators
from pages import main_page
from pages.login_page import LoginPage
from pages.main_func_page import MainFuncPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.password_recovery_page import PasswordRecoveryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.personal_account_page import PersonalAccountPage


class TestOrderFeed:
    @allure.title('Тест открытия всплывающего окна с деталями заказа')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_details_order(self, driver):
        driver.get(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email_on_authorization_page(TEST_MAIL)
        personal_account_page.enter_password_on_authorization_page(TEST_PASS)
        personal_account_page.click_on_auth_button()

        main_func_page = MainFuncPage(driver)
        main_func_page.click_on_constructor_button()
        main_func_page.add_ingredient_into_order(MainFuncLocators.BULKA, MainFuncLocators.ORDER_CONSTRUCTOR)
        main_func_page.click_create_order_button()
        driver.get(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')
        main_func_page.click_on_order_button()

        assert main_func_page.find_element_with_wait(MainFuncLocators.INGREDIENTS_TITLE), 'Окно с деталями заказа не отобразилось'
        # тест проверяет два кейса
        # 1.если кликнуть на заказ, откроется всплывающее окно с деталями,
        # 2.заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»

    @allure.title('Тест увеличения каунтера "Выполнено за всё время"')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_all_time_counter_order(self, driver):
        driver.get(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')
        order_feed_page = OrderFeedPage(driver)
        counter = order_feed_page.get_counter_all_time_done()

        driver.get(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email_on_authorization_page(TEST_MAIL)
        personal_account_page.enter_password_on_authorization_page(TEST_PASS)
        personal_account_page.click_on_auth_button()

        main_func_page = MainFuncPage(driver)
        main_func_page.click_on_constructor_button()
        main_func_page.add_ingredient_into_order(MainFuncLocators.BULKA, MainFuncLocators.ORDER_CONSTRUCTOR)
        main_func_page.click_create_order_button()
        driver.get(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')

        assert order_feed_page.get_counter_all_time_done() == counter + 1, 'Каунтер "Выполнено за всё время" не увеличился'

    @allure.title('Тест увеличения каунтера "Выполнено за сегодня"')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_one_day_time_counter_order(self, driver):
        driver.get(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')
        order_feed_page = OrderFeedPage(driver)
        counter = order_feed_page.get_counter_one_day_time_done()

        driver.get(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email_on_authorization_page(TEST_MAIL)
        personal_account_page.enter_password_on_authorization_page(TEST_PASS)
        personal_account_page.click_on_auth_button()

        main_func_page = MainFuncPage(driver)
        main_func_page.click_on_constructor_button()
        main_func_page.add_ingredient_into_order(MainFuncLocators.BULKA, MainFuncLocators.ORDER_CONSTRUCTOR)
        main_func_page.click_create_order_button()
        driver.get(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')

        assert order_feed_page.get_counter_one_day_time_done() == counter + 1, 'Каунтер "Выполнено за сегодня" не увеличился'

    @allure.title('Тест появления номера заказа в работе"')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_one_day_time_counter_order(self, driver):
        driver.get(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email_on_authorization_page(TEST_MAIL)
        personal_account_page.enter_password_on_authorization_page(TEST_PASS)
        personal_account_page.click_on_auth_button()

        main_func_page = MainFuncPage(driver)
        main_func_page.click_on_constructor_button()
        main_func_page.add_ingredient_into_order(MainFuncLocators.BULKA, MainFuncLocators.ORDER_CONSTRUCTOR)
        main_func_page.click_create_order_button()

        order_feed_page = OrderFeedPage(driver)
        track_num = order_feed_page.get_track_num_order()
        driver.get(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')

        assert order_feed_page.get_track_num_order_from_list() == track_num, 'Номер созданного заказа отображается в списке заказов'