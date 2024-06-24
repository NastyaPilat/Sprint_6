from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage
from pages.order_page import OrderPage
import data
import allure


class TestBasePage:

    @allure.title('test_logo_yandex')
    def test_logo_yandex(self, driver: WebDriver):
        home_page = HomePage(driver)
        home_page.go_to(data.HOME_PAGE_URL)
        home_page.click_logo_yandex()
        home_page.wait_for_number_of_windows_to_be(2)
        home_page.switch_to_window(1)
        assert data.DZEN_PAGE_URL == home_page.get_current_url()

    @allure.title('test_logo_scooter')
    def test_logo_scooter(self, driver: WebDriver):
        order_page = OrderPage(driver)
        order_page.go_to(data.ORDER_PAGE_URL)
        order_page.click_logo_scooter()
        assert data.HOME_PAGE_URL == order_page.get_current_url()
