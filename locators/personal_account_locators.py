from selenium.webdriver.common.by import By

class PersonalAccountLocators:

    EMAIL_INPUT_AUTH = (By.CSS_SELECTOR, "input.input__textfield[name='name']")
    PASSWORD_INPUT_AUTH = (By.CSS_SELECTOR, "input.input__textfield[name='Пароль']")
    AUTH_BUTTON = (By.XPATH, "//button[normalize-space(text())='Войти']")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[normalize-space(text())='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Выход']")