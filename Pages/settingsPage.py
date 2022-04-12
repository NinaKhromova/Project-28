import time

import selenium.webdriver.chrome.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SettingsPage:
    def __init__(self, driver: selenium.webdriver.chrome.webdriver.WebDriver):
        self.driver = driver

        self.name_input_xpath = "//input[@aria-label='Имя']"
        self.surname_input_xpath = "//input[@aria-label='Фамилия']"
        self.patronymic_input_xpath = "//input[@aria-label='Отчество']"
        self.address_input_xpath = "//input[@aria-label='Адрес']"
        self.phone_input_xpath = "//input[@aria-label='Телефон']"

        self.save_form_button_xpath = "//form[contains(@class, 'form')]//*[contains(text(), 'Сохранить изменения')]" \
                                      "/ancestor::button"
        self.success_notification_xpath = '//*[contains(text(), "Информация обновлена")]'
        self.wrong_phone_xpath = '//*[contains(text(), "используйте такой формат номера")]'

    def enter_name(self, name):
        self.__enter_field_data(self.name_input_xpath, name)

    def enter_surname(self, surname):
        self.__enter_field_data(self.surname_input_xpath, surname)

    def enter_patronymic(self, patronymic):
        self.__enter_field_data(self.patronymic_input_xpath, patronymic)

    def enter_address(self, address):
        self.__enter_field_data(self.address_input_xpath, address)

    def enter_phone(self, phone):
        self.__enter_field_data(self.phone_input_xpath, phone)

    def save_data(self):
        self.driver.find_element(By.XPATH, self.save_form_button_xpath).click()

    def get_success_notification(self):
        self.driver.find_element(By.XPATH, self.success_notification_xpath)

    def get_wrong_phone_notification(self):
        self.driver.find_element(By.XPATH, self.wrong_phone_xpath)

    def __enter_field_data(self, field_xpath, data):
        field = self.driver.find_element(By.XPATH, field_xpath)
        field.clear()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(data)








