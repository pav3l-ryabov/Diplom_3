import allure

from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Клик на кнопку "Личный кабинет')
    def click_personal_account_button(self):
        self.click_to_element(BasePageLocators.PERSONAL_ACCOUNT)