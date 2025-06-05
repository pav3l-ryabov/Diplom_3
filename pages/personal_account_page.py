import allure

from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators
from locators.password_recovery_locators import PasswordRecoveryPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):
    @allure.step('Ввод email в поле email на странице авторизации')
    def enter_email_on_authorization_page(self, email):
        self.add_text_to_element(PersonalAccountLocators.EMAIL_INPUT_AUTH, email)

    @allure.step('Ввод пароля в поле пароля на странице авторизации')
    def enter_password_on_authorization_page(self, password):
        self.add_text_to_element(PersonalAccountLocators.PASSWORD_INPUT_AUTH, password)

    @allure.step('Клик на кнопку Войти на странице авторизации')
    def click_on_auth_button(self):
        self.wait_for_element_to_be_clickable(PersonalAccountLocators.AUTH_BUTTON)
        self.click_to_element(PersonalAccountLocators.AUTH_BUTTON)

    @allure.step('Клик по кнопке История заказов в личном кабинете')
    def click_on_order_history_button(self):
        self.click_to_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Клик по кнопке Выход в личном кабинете')
    def click_on_logout_button(self):
        self.click_to_element(PersonalAccountLocators.LOGOUT_BUTTON)
