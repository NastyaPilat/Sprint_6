from selenium import webdriver
from pages.home_page import HomePage
from pages.base_page import BasePage


class TestHomePage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_question_1(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        BasePage.accept_cookies(self.driver)
        home_page = HomePage(self.driver)
        assert home_page.check_question(0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')

    def test_question_2(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        BasePage.accept_cookies(self.driver)
        home_page = HomePage(self.driver)
        assert home_page.check_question(1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')

    def test_question_3(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        BasePage.accept_cookies(self.driver)
        home_page = HomePage(self.driver)
        assert home_page.check_question(2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')

    def test_question_4(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        BasePage.accept_cookies(self.driver)
        home_page = HomePage(self.driver)
        assert home_page.check_question(3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')

    def test_question_5(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        BasePage.accept_cookies(self.driver)
        home_page = HomePage(self.driver)
        assert home_page.check_question(4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')

    def test_question_6(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        BasePage.accept_cookies(self.driver)
        home_page = HomePage(self.driver)
        assert home_page.check_question(5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')

    def test_question_7(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        BasePage.accept_cookies(self.driver)
        home_page = HomePage(self.driver)
        assert home_page.check_question(6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')

    def test_question_8(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        BasePage.accept_cookies(self.driver)
        home_page = HomePage(self.driver)
        assert home_page.check_question(7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 