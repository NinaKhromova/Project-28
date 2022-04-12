from selenium import webdriver

import time
import unittest
from Pages.mainPage import MainPage
from Pages.settingsPage import SettingsPage

from utils import get_random_string, get_random_number


class SellerPageTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/chromedriver')
    settings = SettingsPage(driver)
    main = MainPage(driver)

    @classmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://meshok.net")
        cls.main.login()
        cls.driver.get("https://meshok.net/profile/basic")

    def test_change_name(self):
        """Проверка возможности изменить имя """
        self.__test_field_change(self.settings.enter_name, get_random_string(12))

    def test_change_surname(self):
        """Проверка возможности изменить фамилию """
        self.__test_field_change(self.settings.enter_surname, get_random_string(12))

    def test_change_patronymic(self):
        """Проверка возможности изменить отчество """
        self.__test_field_change(self.settings.enter_patronymic, get_random_string(12))

    def test_change_address(self):
        """Проверка возможности изменить адрес """
        self.__test_field_change(self.settings.enter_address, get_random_string(12))

    def test_change_phone(self):
        """Проверка возможности изменить телефон """
        self.__test_field_change(self.settings.enter_phone, get_random_number(10000000, 99999999))

    def test_wrong_phone(self):
        """Проверка невозможности использовать текст в номере телефона """
        self.settings.enter_phone(get_random_string(10))
        self.settings.save_data()
        self.settings.get_wrong_phone_notification()

    def test_change_all(self):
        """Проверка возможности изменить все поля одновременно """
        self.settings.enter_name(get_random_string(5))
        self.settings.enter_surname(get_random_string(5))
        self.settings.enter_patronymic(get_random_string(5))
        self.settings.enter_address(get_random_string(5))
        self.settings.enter_phone(get_random_number(10000000, 99999999))
        self.settings.save_data()
        self.settings.get_success_notification()

    def test_change_all_with_wrong_phone(self):
        """Проверка невозможности изменить все поля одновременно, если в номере телефона ошибка """
        self.settings.enter_name(get_random_string(5))
        self.settings.enter_surname(get_random_string(5))
        self.settings.enter_patronymic(get_random_string(5))
        self.settings.enter_address(get_random_string(5))
        self.settings.enter_phone(get_random_string(5))
        self.settings.save_data()
        self.settings.get_wrong_phone_notification()

    def __test_field_change(self, action, value):
        action(value)
        self.settings.save_data()
        self.settings.get_success_notification()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')






