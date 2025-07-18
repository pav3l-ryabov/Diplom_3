## Дипломный проект. Задание 3: UI-тесты

### Автотесты для проверки работы с юзерами и заказами в Stellar Burgers

### Структура проекта

- `data.data.py` - хранит константы

- `locators/base_page_locators.py` - хранит базовые локаторы
- `locators/login_page_locators.py` - хранит локаторы страницы логина
- `locators/main_func_locators.py` - хранит локаторы страницы основных функций
- `locators/password_recovery_locators.py` - хранит локаторы страницы восстановления пароля
- `locators/personal_account_locators.py` - хранит локаторы страницы личного кабинета

- `pages/base_page.py` - хранит базовые методы
- `pages/login_page.py` - хранит методы страницы авторизации
- `pages/main_func_page.py` - хранит методы основных функций
- `pages/main_page.py` - хранит методы главной страницы
- `pages/order_feed_page.py` - хранит методы страницы ленты заказов
- `pages/password_recovery_page.py` - хранит методы восстановления пароля
- `pages/personal_account_page.py` - хранит методы личного кабинета

- `tests/conftest.py` - хранит фикстуру запуска браузеров
- `tests/test_main_func.py` - хранит тесты основной функциональности
- `tests/test_order_feed.py` - хранит тесты ленты заказов
- `tests/test_password_recovery_page.py` - хранит тесты восстановления пароля
- `tests/test_personal_account.py` - хранит тесты личного кабинета


### Запуск автотестов

> `$ pytest --alluredir=reports`

**Установка зависимостей**

> `$ pip install -r requirements.txt`