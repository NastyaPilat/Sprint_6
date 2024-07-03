import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage
import data
import allure


class TestHomePage:

    @allure.title('test_question_{index}')
    @pytest.mark.parametrize("index, expected_text", data.ANSWERS)
    def test_question(self, driver: WebDriver, index, expected_text):
        home_page = HomePage(driver)
        home_page.go_to(data.HOME_PAGE_URL)
        home_page.accept_cookies()
        home_page.get_question(index).click()
        answer = home_page.get_answer(index)
        assert not home_page.is_answer_hidden(index) and expected_text == answer.text
