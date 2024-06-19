from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    input_first_name = [By.XPATH, '//input[@placeholder="* Имя"]']
    input_second_name = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    input_address = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    input_metro_station = [By.XPATH, '//input[@placeholder="* Станция метро"]']
    input_phone_number = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    input_date = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    input_rental_period = [By.XPATH, '//div[text()="* Срок аренды"]']
    input_comment = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']
    dropdown_option = [By.CLASS_NAME, 'Dropdown-option']
    next_button = [By.XPATH, '//div[contains(@class,"Order_NextButton__1_rCA")]/button[text()="Далее"]']
    order_button = [By.XPATH, '//div[contains(@class,"Order_Buttons__1xGrp")]/button[text()="Заказать"]']
    modal = [By.CLASS_NAME, 'Order_Modal__YZ-d3']
    header = [By.CLASS_NAME, 'Order_Header__BZXOb']

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
    
    def fill_order_form_1(self, first_name, second_name, address, metro_station, phone_number):
        self.driver.find_element(*self.input_first_name).send_keys(first_name)
        self.driver.find_element(*self.input_second_name).send_keys(second_name)
        self.driver.find_element(*self.input_address).send_keys(address)
        self.driver.find_element(*self.input_metro_station).click()
        self.driver.find_element(By.XPATH, f"//button[contains(div[@class='Order_Text__2broi'], '{metro_station}')]").click()
        self.driver.find_element(*self.input_phone_number).send_keys(phone_number)

    def fill_order_form_2(self, date, rental_period, comment):
        self.driver.find_element(*self.input_date).send_keys(date)
        self.driver.find_element(*self.header).click()
        self.driver.find_element(*self.input_rental_period).click()
        rental_period_option_locator = (By.XPATH, f"//div[@class='Dropdown-option' and contains(text(), '{rental_period}')]")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(rental_period_option_locator)).click()
        self.driver.find_element(*self.input_comment).send_keys(comment)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def is_modal(self):
        return self.driver.find_element(*self.modal) is not None