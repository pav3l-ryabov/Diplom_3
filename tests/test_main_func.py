import allure
import pytest

from data.data import URL_MAIN_PAGE, URL_LOGIN_PAGE, TEST_MAIL, \
    TEST_PASS, URL_ORDER_FEED_PAGE
from locators.main_func_locators import MainFuncLocators
from pages.main_func_page import MainFuncPage
from pages.personal_account_page import PersonalAccountPage


class TestMainFunc:
    @allure.title('Тест перехода в конструктор')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_open_constructor_page(self, driver):
        main_func_page = MainFuncPage(driver)
        main_func_page.get_url_page(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')
        main_func_page.click_on_constructor_button()

        assert main_func_page.find_element_with_wait(MainFuncLocators.CONSTRUCT_BURGER_TEXT), "Переход в конструктор не произошел"

    @allure.title('Тест перехода в ленту заказов')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_open_order_feed_page(self, driver):
        main_func_page = MainFuncPage(driver)
        main_func_page.get_url_page(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')
        main_func_page.click_on_order_feed_button()

        assert main_func_page.get_current_url() == f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}', "Переход на страницу ленты заказов не произошел"

    @allure.title('Тест отображения всплывающего окна с деталями')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_open_order_feed_page(self, driver):
        main_func_page = MainFuncPage(driver)
        main_func_page.get_url_page(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')
        main_func_page.click_on_order_button()

        assert main_func_page.find_element_with_wait(MainFuncLocators.ORDER_MODAL_WINDOW), "Всплывающее окно с деталями заказа не отобразилось"

    @allure.title('Тест закрытия всплывающего окна с деталями')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_open_order_feed_page(self, driver):
        main_func_page = MainFuncPage(driver)
        main_func_page.get_url_page(f'{URL_MAIN_PAGE}{URL_ORDER_FEED_PAGE}')
        main_func_page.click_on_order_button()
        main_func_page.press_esc()

        assert driver.find_elements(*MainFuncLocators.ORDER_MODAL_WINDOW), "Модальное окно всё ещё отображается"

    @allure.title('Тест при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_add_ingredient_into_order(self, driver):
        main_func_page = MainFuncPage(driver)
        main_func_page.get_url_page(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')
        main_func_page.click_on_constructor_button()
        main_func_page.add_ingredient_into_order(MainFuncLocators.BULKA, MainFuncLocators.ORDER_CONSTRUCTOR)

        assert main_func_page.find_element_with_wait(MainFuncLocators.PRICE_1976), "Каунтер не содержит нужную цену"

    @allure.title('Тест создания заказа авторизованным пользователем')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_create_order(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.get_url_page(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')
        personal_account_page.enter_email_on_authorization_page(TEST_MAIL)
        personal_account_page.enter_password_on_authorization_page(TEST_PASS)
        personal_account_page.click_on_auth_button()

        main_func_page = MainFuncPage(driver)
        main_func_page.click_on_constructor_button()
        main_func_page.add_ingredient_into_order(MainFuncLocators.BULKA, MainFuncLocators.ORDER_CONSTRUCTOR)
        main_func_page.click_create_order_button()

        assert main_func_page.find_element_with_wait(MainFuncLocators.ORDER_ID_LABEL), "Заказ не создался"