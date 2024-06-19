import pytest
from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @pytest.mark.parametrize("first_name, second_name, address, metro_station, phone_number, date, rental_period, comment", [
        ("Иван", "Иванов", "ул. Пушкина, дом Колотушкина", "Южная", "+79998887766", "20.06.2024", "двое суток", "Не звоните, напишите")
    ])
    def test_order_from_base_page(self, first_name, second_name, address, metro_station, phone_number, date, rental_period, comment):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        base_page = BasePage(self.driver)
        base_page.click_order_button()
        order_page = OrderPage(self.driver)
        order_page.fill_order_form_1(first_name, second_name, address, metro_station, phone_number)
        order_page.click_next_button()
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.driver.find_element(*order_page.order_button)))
        order_page.fill_order_form_2(date, rental_period, comment)
        order_page.click_order_button()
        assert order_page.is_modal()

    @pytest.mark.parametrize("first_name, second_name, address, metro_station, phone_number, date, rental_period, comment", [
        ("Петр", "Петров", "ул. Лермонтова, дом 1", "Лубянка", "+79997776655", "21.06.2024", "трое суток", "Звоните заранее")
    ])
    def test_order_from_home_page(self, first_name, second_name, address, metro_station, phone_number, date, rental_period, comment):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        home_page = HomePage(self.driver)
        home_page.click_order_button()
        order_page = OrderPage(self.driver)
        order_page.fill_order_form_1(first_name, second_name, address, metro_station, phone_number)
        order_page.click_next_button()
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.driver.find_element(*order_page.order_button)))
        order_page.fill_order_form_2(date, rental_period, comment)
        order_page.click_order_button()
        assert order_page.is_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 