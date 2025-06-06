import allure
import pytest

from data.data import URL_MAIN_PAGE, URL_LOGIN_PAGE, TEST_MAIL, \
    TEST_PASS, URL_ORDER_FEED_PAGE
from locators.main_func_locators import MainFuncLocators
from pages.main_func_page import MainFuncPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeed:
    @allure.title('Тест открытия всплывающего окна с деталями заказа')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_details_order(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.get_url_page(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')
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
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.get_url_page(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')
        counter = order_feed_page.get_counter_all_time_done()

        order_feed_page.get_url_page(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email_on_authorization_page(TEST_MAIL)
        personal_account_page.enter_password_on_authorization_page(TEST_PASS)
        personal_account_page.click_on_auth_button()

        main_func_page = MainFuncPage(driver)
        main_func_page.click_on_constructor_button()
        main_func_page.add_ingredient_into_order(MainFuncLocators.BULKA, MainFuncLocators.ORDER_CONSTRUCTOR)
        main_func_page.click_create_order_button()
        main_func_page.get_url_page(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')

        assert order_feed_page.get_counter_all_time_done() == counter + 1, 'Каунтер "Выполнено за всё время" не увеличился'

    @allure.title('Тест увеличения каунтера "Выполнено за сегодня"')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_one_day_time_counter_order(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.get_url_page(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')
        counter = order_feed_page.get_counter_one_day_time_done()

        order_feed_page.get_url_page(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email_on_authorization_page(TEST_MAIL)
        personal_account_page.enter_password_on_authorization_page(TEST_PASS)
        personal_account_page.click_on_auth_button()

        main_func_page = MainFuncPage(driver)
        main_func_page.click_on_constructor_button()
        main_func_page.add_ingredient_into_order(MainFuncLocators.BULKA, MainFuncLocators.ORDER_CONSTRUCTOR)
        main_func_page.click_create_order_button()
        main_func_page.get_url_page(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')

        assert order_feed_page.get_counter_one_day_time_done() == counter + 1, 'Каунтер "Выполнено за сегодня" не увеличился'

    @allure.title('Тест появления номера заказа в работе"')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_track_num_in_order_list(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.get_url_page(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')
        personal_account_page.enter_email_on_authorization_page(TEST_MAIL)
        personal_account_page.enter_password_on_authorization_page(TEST_PASS)
        personal_account_page.click_on_auth_button()

        main_func_page = MainFuncPage(driver)
        main_func_page.click_on_constructor_button()
        main_func_page.add_ingredient_into_order(MainFuncLocators.BULKA, MainFuncLocators.ORDER_CONSTRUCTOR)
        main_func_page.click_create_order_button()

        order_feed_page = OrderFeedPage(driver)
        track_num = order_feed_page.get_track_num_order()
        order_feed_page.get_url_page(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')

        assert order_feed_page.get_track_num_order_from_list() == track_num, 'Номер созданного заказа отображается в списке заказов'