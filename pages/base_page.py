from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    cookie_button = [By.CLASS_NAME, 'App_CookieButton__3cvqF']
    logo_yandex = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    logo_scooter = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    order_button = [By.XPATH, '//div[contains(@class, "Header_Header__214zg")]//button[contains(@class, "Button_Button__ra12g")]']

    @classmethod
    def accept_cookies(cls, driver: WebDriver):
        try:
            driver.find_element(*cls.cookie_button).click()
        except:
            pass

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_logo_yandex(self):
        self.driver.find_element(*self.logo_yandex).click()

    def click_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()