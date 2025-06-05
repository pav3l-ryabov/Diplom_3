from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locator(self, locator_template, num):
        method, locator = locator_template
        return (method, locator.format(num))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def click_to_remove_focus(self):
        self.driver.execute_script("document.body.click();")

    def switch_to(self):
        # Переключаемся на последнюю вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_url_to_be(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def click_to_element_with_actionchains(self, locator):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).click(element).perform()

    def drag_and_drop(self, source_locator, target_locator, timeout=10):
        source = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(source_locator)
        )
        target = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(target_locator)
        )
        ActionChains(self.driver).drag_and_drop(source, target).perform()


