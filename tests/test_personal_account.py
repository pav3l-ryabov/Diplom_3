import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

import allure
import pytest

from data.data import URL_MAIN_PAGE, URL_FORGOT_PASSWORD_PAGE, URL_LOGIN_PAGE, URL_RESET_PASSWORD_PAGE, TEST_MAIL, \
    TEST_PASS, URL_PERSONAL_ACCOUNT_PAGE, URL_ORDER_HISTORY_PAGE
from locators.password_recovery_locators import PasswordRecoveryPageLocators
from pages import main_page
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    @allure.title('Тест перехода в личный кабинет')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_open_personal_account_page(self, driver):
        driver.get(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email_on_authorization_page(TEST_MAIL)
        personal_account_page.enter_password_on_authorization_page(TEST_PASS)
        personal_account_page.click_on_auth_button()

        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        main_page.wait_for_url_to_be(f'{URL_MAIN_PAGE}{URL_PERSONAL_ACCOUNT_PAGE}')

        assert main_page.get_current_url() == f'{URL_MAIN_PAGE}{URL_PERSONAL_ACCOUNT_PAGE}', "Переход в личный кабинет не произошел"

    @allure.title('Тест перехода на страницу "История заказов"')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_open_order_history_page(self, driver):
        driver.get(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email_on_authorization_page(TEST_MAIL)
        personal_account_page.enter_password_on_authorization_page(TEST_PASS)
        personal_account_page.click_on_auth_button()

        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        main_page.wait_for_url_to_be(f'{URL_MAIN_PAGE}{URL_PERSONAL_ACCOUNT_PAGE}')

        personal_account_page.click_on_order_history_button()
        main_page.wait_for_url_to_be(f'{URL_MAIN_PAGE}{URL_ORDER_HISTORY_PAGE}')

        assert main_page.get_current_url() == f'{URL_MAIN_PAGE}{URL_ORDER_HISTORY_PAGE}', "Переход в историю заказов не произошел"

    @allure.title('Тест авторизации и последующего логаута')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_login_and_logout(self, driver):
        driver.get(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email_on_authorization_page(TEST_MAIL)
        personal_account_page.enter_password_on_authorization_page(TEST_PASS)
        personal_account_page.click_on_auth_button()

        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        main_page.wait_for_url_to_be(f'{URL_MAIN_PAGE}{URL_PERSONAL_ACCOUNT_PAGE}')

        personal_account_page.click_on_logout_button()
        main_page.wait_for_url_to_be(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')

        assert main_page.get_current_url() == f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}', "Логаут не произошел"
