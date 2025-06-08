import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    @allure.step('Клик на кнопку "Восстановить пароль')
    def click_password_recovery_button(self):
        self.click_to_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)