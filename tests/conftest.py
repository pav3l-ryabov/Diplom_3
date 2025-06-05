import pytest
from selenium import webdriver


@pytest.fixture
def driver(request): # фикстура для запуска "поддерживаемого" браузера в зависимости от того, что передаем. Любой другой браузер выдаст ошибку
    browser = request.param
    if browser == "chrome":
        driver_instance = webdriver.Chrome()
    elif browser == "firefox":
        driver_instance = webdriver.Firefox()
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser}") # ошибка на случай, если будет передан "не поддерживаемый" браузер
    yield driver_instance
    driver_instance.quit()