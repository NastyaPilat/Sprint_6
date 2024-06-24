import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators import order_page_locators
import data
import allure


class TestOrderPage:

    @allure.title('test_order_with_top_button')
    @pytest.mark.parametrize("first_name, second_name, address, metro_station, phone_number, date, rental_period, comment", [
        ("Иван", "Иванов", "ул. Пушкина, дом Колотушкина", "Южная", "+79998887766", "20.06.2024", "двое суток", "Не звоните, напишите")
    ])
    def test_order_with_top_button(self, driver: WebDriver, first_name, second_name, address, metro_station, phone_number, date, rental_period, comment):
        home_page = HomePage(driver)
        home_page.go_to(data.HOME_PAGE_URL)
        home_page.click_top_order_button()
        order_page = OrderPage(driver)
        order_page.fill_order_form_1(first_name, second_name, address, metro_station, phone_number)
        order_page.click_next_button()
        order_page.wait_for_element_to_be_clickable(order_page_locators.order_button)
        order_page.fill_order_form_2(date, rental_period, comment)
        order_page.click_order_button()
        assert order_page.is_modal()

    @allure.title('test_order_with_bottom_button')
    @pytest.mark.parametrize("first_name, second_name, address, metro_station, phone_number, date, rental_period, comment", [
        ("Петр", "Петров", "ул. Лермонтова, дом 1", "Лубянка", "+79997776655", "21.06.2024", "трое суток", "Звоните заранее")
    ])
    def test_order_with_bottom_button(self, driver: WebDriver, first_name, second_name, address, metro_station, phone_number, date, rental_period, comment):
        home_page = HomePage(driver)
        home_page.go_to(data.HOME_PAGE_URL)
        home_page.click_bottom_order_button()
        order_page = OrderPage(driver)
        order_page.fill_order_form_1(first_name, second_name, address, metro_station, phone_number)
        order_page.click_next_button()
        order_page.wait_for_element_to_be_clickable(order_page_locators.order_button)
        order_page.fill_order_form_2(date, rental_period, comment)
        order_page.click_order_button()
        assert order_page.is_modal()
