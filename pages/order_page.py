from pages.base_page import BasePage
from locators import order_page_locators
from locators import base_page_locators
import allure


class OrderPage(BasePage):

    @allure.step('fill_order_form_1')
    def fill_order_form_1(self, first_name, second_name, address, metro_station, phone_number):
        self.find_element(order_page_locators.input_first_name).send_keys(first_name)
        self.find_element(order_page_locators.input_second_name).send_keys(second_name)
        self.find_element(order_page_locators.input_address).send_keys(address)
        self.find_element(order_page_locators.input_metro_station).click()
        metro_station_option_locator = order_page_locators.get_metro_station_option_locator(metro_station)
        self.find_element(metro_station_option_locator).click()
        self.find_element(order_page_locators.input_phone_number).send_keys(phone_number)

    @allure.step('fill_order_form_2')
    def fill_order_form_2(self, date, rental_period, comment):
        self.find_element(order_page_locators.input_date).send_keys(date)
        self.find_element(order_page_locators.header).click()
        self.find_element(order_page_locators.input_rental_period).click()
        rental_period_option_locator = order_page_locators.get_rental_period_option_locator(rental_period)
        self.wait_for_element_to_be_clickable(rental_period_option_locator)
        self.click_element(rental_period_option_locator)
        self.find_element(order_page_locators.input_comment).send_keys(comment)

    @allure.step('click_logo_scooter')
    def click_logo_scooter(self):
        self.click_element(base_page_locators.logo_scooter)

    @allure.step('click_next_button')
    def click_next_button(self):
        self.click_element(order_page_locators.next_button)

    @allure.step('click_order_button')
    def click_order_button(self):
        self.click_element(order_page_locators.order_button)

    @allure.step('is_modal')
    def is_modal(self):
        return self.find_element(order_page_locators.modal) is not None
