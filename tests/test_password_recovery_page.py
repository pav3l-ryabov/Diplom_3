import allure
import pytest

from data.data import URL_MAIN_PAGE, URL_FORGOT_PASSWORD_PAGE, URL_LOGIN_PAGE, TEST_MAIL
from locators.password_recovery_locators import PasswordRecoveryPageLocators
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecoveryPage:
    @allure.title('Тест перехода на страницу восстановления пароля')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_open_password_recovery_page(self,driver):
        driver.get(f'{URL_MAIN_PAGE}{URL_LOGIN_PAGE}')

        login_page = LoginPage(driver)
        login_page.click_password_recovery_button()

        assert login_page.get_current_url() == f'{URL_MAIN_PAGE}{URL_FORGOT_PASSWORD_PAGE}', "Переход на страницу восстановления пароля не произошел"

    @allure.title('Тест перехода на страницу восстановления пароля, ввода почты и клика по кнопке "Восстановить"')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_open_password_recovery_page_and_click_recovery_button(self,driver):
        driver.get(f'{URL_MAIN_PAGE}{URL_FORGOT_PASSWORD_PAGE}')

        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.enter_email_on_pass_recovery_page(TEST_MAIL)
        password_recovery_page.click_on_recovery_button()

        assert password_recovery_page.get_text_from_element(PasswordRecoveryPageLocators.CODE_FROM_MAIL_INPUT) == 'Введите код из письма', \
            'Страница не перешла в состояние, когда отображается поле ввода Введите код из письма'

    @allure.title('Тест проверяющий, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_show_password_recovery_page(self, driver):
        driver.get(f'{URL_MAIN_PAGE}{URL_FORGOT_PASSWORD_PAGE}')

        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.enter_email_on_pass_recovery_page(TEST_MAIL)
        password_recovery_page.click_on_recovery_button()
        password_recovery_page.click_on_show_hide_password_button()

        assert password_recovery_page.find_element_with_wait(PasswordRecoveryPageLocators.PASSWORD_IS_DISPLAYED), "Пароль не отобразился"
        assert password_recovery_page.find_element_with_wait(PasswordRecoveryPageLocators.PASSWORD_BUTTON_IS_ACTIVE), "Инпут ввода пароля не подсветился"
