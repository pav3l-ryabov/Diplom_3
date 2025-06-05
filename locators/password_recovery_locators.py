from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")
    CODE_FROM_MAIL_INPUT = (By.XPATH, "//label[text()='Введите код из письма']")
    RECOVERY_BUTTON = (By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Восстановить']")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Введите новый пароль']")
    SHOW_HIDE_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".input__icon.input__icon-action")
    PASSWORD_IS_DISPLAYED = (By.CSS_SELECTOR, "div.input.input_type_text.input_size_default.input_status_active")
    PASSWORD_BUTTON_IS_ACTIVE = (By.CSS_SELECTOR, "label.input__placeholder.text.noselect.text_type_main-default.input__placeholder-focused")