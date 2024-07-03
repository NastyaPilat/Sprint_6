from selenium.webdriver.common.by import By


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

def get_rental_period_option_locator(rental_period):
    return (By.XPATH, f"//div[@class='Dropdown-option' and contains(text(), '{rental_period}')]")

def get_metro_station_option_locator(metro_station):
    return (By.XPATH, f"//button[contains(div[@class='Order_Text__2broi'], '{metro_station}')]")
