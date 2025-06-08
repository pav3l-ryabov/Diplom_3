import allure

from locators.password_recovery_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage

class PasswordRecoveryPage(BasePage):
    @allure.step('Ввод email в поле email на странице восстановления пароля')
    def enter_email_on_pass_recovery_page(self, email):
        self.add_text_to_element(PasswordRecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик на кнопку Восстановить на странице восстановления пароля')
    def click_on_recovery_button(self):
        self.wait_for_element_to_be_clickable(PasswordRecoveryPageLocators.RECOVERY_BUTTON)
        self.click_to_element(PasswordRecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Клик по кнопке show/hide пароля на странице восстановления пароля')
    def click_on_show_hide_password_button(self):
        self.click_to_element(PasswordRecoveryPageLocators.SHOW_HIDE_PASSWORD_BUTTON)
