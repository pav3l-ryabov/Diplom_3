from selenium.webdriver.common.by import By

class BasePageLocators:

    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет" на главной странице