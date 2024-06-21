from pages.base_page import BasePage
from locators import home_page_locators
from locators import base_page_locators
import allure


class HomePage(BasePage):

    @allure.step
    def get_question(self, index: int):
        return self.find_elements(home_page_locators.question)[index]
    
    @allure.step
    def get_answer(self, index: int):
        question = self.get_question(index)
        return question.find_element(*home_page_locators.answer)
    
    @allure.step
    def is_answer_hidden(self, index: int):
        question = self.get_question(index)
        panel = question.find_element(*home_page_locators.answer_container)
        return panel.get_attribute('hidden') is not None
    
    @allure.step
    def click_top_order_button(self):
        button = self.find_element(home_page_locators.order_button)
        self.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    @allure.step
    def click_bottom_order_button(self):
        button = self.find_element(home_page_locators.order_button)
        self.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    @allure.step
    def click_logo_yandex(self):
        self.click_element(base_page_locators.logo_yandex)