from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import base_page_locators
import allure


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    @allure.step
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step
    def execute_script(self, script, *args):
        self.driver.execute_script(script, *args)

    @allure.step
    def wait_for_element_to_be_clickable(self, locator, timeout=3):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    @allure.step
    def wait_for_number_of_windows_to_be(self, num_windows, timeout=3):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(num_windows))

    @allure.step
    def wait_for_element_to_be_visible(self, locator, timeout=3):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step
    def switch_to_window(self, window_index: int):
        self.driver.switch_to.window(self.driver.window_handles[window_index])
    
    @allure.step
    def accept_cookies(self):
        try:
            self.click_element(base_page_locators.cookie_button)
        except:
            pass