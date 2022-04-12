import time

import selenium.webdriver.chrome.webdriver
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver: selenium.webdriver.chrome.webdriver.WebDriver):
        self.driver = driver
        self.clear_the_cart_button_xpath = '//*[contains(text(), "Очистить корзину")]'
        self.clear_the_cart_notification_xpath = '//*[text() = "Лот удален" or text() = "Все лоты удалены"]'
        self.delete_the_item_from_cart_button_xpath = "//*[@title='Удалить лот']"
        self.select_the_item_in_cart_xpath = "//div[contains(@class, 'cartList')]//div[contains(@class, 'checkBox')]"
        self.order_button_xpath = '//*[@id="app"]/div/div[5]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/button/div'
        self.buy_button_xpath = '//*[contains(text(), "Купить")]'
        self.open_the_cart_xpath = '//*[@id="desktop-cart-button"]/button'
        self.cart_button_xpath = "//button[@title='Добавить в корзину']"
        self.added_to_cart_xpath = '//*[text() = "Лот добавлен в корзину"]'

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.cart_button_xpath).click()
        self.driver.find_element(By.XPATH, self.added_to_cart_xpath)

    def clear_cart(self):
        self.driver.find_element(By.XPATH, self.clear_the_cart_button_xpath).click()
        self.driver.find_element(By.XPATH, self.clear_the_cart_notification_xpath)

    def delete_the_item_from_cart(self):
        self.driver.find_element(By.XPATH, self.delete_the_item_from_cart_button_xpath).click()
        self.driver.find_element(By.XPATH, self.clear_the_cart_notification_xpath)

    def select_item_in_cart(self):
        self.driver.find_element(By.XPATH, self.open_the_cart_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_the_item_in_cart_xpath).click()
        self.driver.find_element(By.XPATH, self.order_button_xpath)

    def order_button(self):
        self.driver.find_element(By.XPATH, self.order_button_xpath).click()
        self.driver.find_element(By.XPATH, self.buy_button_xpath)



