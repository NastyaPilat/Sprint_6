from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class HomePage:
    question = [By.CLASS_NAME, 'accordion__item']
    panel = [By.CLASS_NAME, 'accordion__panel']
    paragraph = [By.TAG_NAME, 'p']
    order_button = [By.XPATH, '//div[contains(@class, "Home_FinishButton__1_cWm")]//button[contains(@class, "Button_Button__ra12g")]']

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_question(self, index: int):
        return self.driver.find_elements(*self.question)[index]
    
    def is_answer_hidden(self, index: int):
        question = self.get_question(index)
        panel = question.find_element(*self.panel)
        return panel.get_attribute('hidden') is not None

    def check_answer_text(self, index: int, expected_text: str):
        question = self.get_question(index)
        paragraph = question.find_element(*self.paragraph)
        return expected_text == paragraph.text
    
    def check_question(self, index: int, expected_text: str):
        self.get_question(index).click()
        return not self.is_answer_hidden(index) and self.check_answer_text(index, expected_text)
    
    def click_order_button(self):
        button = self.driver.find_element(*self.order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()