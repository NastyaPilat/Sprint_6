from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBasePage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_logo_yandex(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        base_page = BasePage(self.driver)
        base_page.click_logo_yandex()
        WebDriverWait(self.driver, 3).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "https://dzen.ru/?yredirect=true" == self.driver.current_url

    def test_logo_scooter(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")
        base_page = BasePage(self.driver)
        base_page.click_logo_scooter()
        WebDriverWait(self.driver, 3).until(EC.url_changes)
        assert "https://qa-scooter.praktikum-services.ru/" == self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 