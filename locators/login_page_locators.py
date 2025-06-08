from selenium.webdriver.common.by import By

class LoginPageLocators:

    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")  # кнопка "Восстановить пароль" на странице логина