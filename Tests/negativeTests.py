from selenium import webdriver

import time
import unittest
from Pages.mainPage import MainPage


class LoginTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/chromedriver')
    main = MainPage(driver)

    @classmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_invalid_password(self):
        """Проверка появления сообщения об ошибке при попытке входа на сайт с неправильным паролем"""
        self.driver.get("https://meshok.net/")
        self.main.click_account_button()
        self.main.click_login_mode_button()
        self.main.enter_email("falling2@yandex.ru")
        self.main.check_error_notification_invalid_password("111")

        time.sleep(2)

    def test_login_invalid_email(self):
        """Проверка появления сообщения об ошибке при попытке входа на сайт с неправильным email"""
        self.driver.get("https://meshok.net/")
        self.main.click_account_button()
        self.main.click_login_mode_button()
        self.main.enter_password("kakadu1")
        self.main.check_error_notification_invalid_email("falling@yandex.ru")

        time.sleep(2)

    def test_login_incorrect_format_email(self):
        """Проверка появления сообщения об ошибке при попытке входа на сайт с вводом email в неправильном формате"""
        self.driver.get("https://meshok.net/")
        self.main.click_account_button()
        self.main.click_login_mode_button()
        self.main.enter_password("kakadu1")
        self.main.check_light_error_incorrect_email_format("111")

        time.sleep(2)

    def test_search_unexisted_item(self):
        self.driver.get("https://meshok.net/")
        self.main.search_unexisted_item("&&&&")

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')


