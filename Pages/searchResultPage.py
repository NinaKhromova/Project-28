import time

from selenium.webdriver.common.by import By
import selenium.webdriver.chrome.webdriver


def get_sub_category_xpath(name):
    return f"//div[contains(@class, 'categories')]//*[contains(text(), '{name}')]/ancestor::a"


def get_current_category_xpath(name):
    return f"//div[contains(@class, 'currentCategory')]//*[contains(text(), '{name}')]"


class SearchResultPage:
    def __init__(self, driver: selenium.webdriver.chrome.webdriver.WebDriver):
        self.driver = driver
        self.header_xpath = '//*[text() = "Результаты поиска"]'
        self.items_card_xpath = '//div[contains(@class, "itemCardList")]'
        self.show_photos_button_xpath = '//*[contains(@class, "actionButtons")]//button[@title="Показать фотографии"]'
        self.watch_button_xpath = '//*[contains(@class, "actionButtons")]//button[@title = "Наблюдать"]'
        self.items_photos_class_name = 'm-item-card-image'
        self.filter_button_xpath = '//*[@id="app"]/div/div[5]/div[2]/div[1]/div/div/div[1]/div[2]/div/div[1]/div[2]' \
                                   '/button[2]'
        self.filter_category_xpath = '//*[text() = "Дешевле"]'
        self.price_xpath = '//div[contains(@class, "itemCardList")]//div[contains(@class, "price_")]'

    def find_search_results(self):
        self.driver.find_element(By.XPATH, self.header_xpath)

    def sub_category_click(self, name):
        self.driver.find_element(By.XPATH, get_sub_category_xpath(name)).click()

    def check_current_category(self, name):
        self.driver.find_element(By.XPATH, get_current_category_xpath(name)).click()

    def find_photos_button_in_items_cards(self):
        return len(self.driver.find_elements(By.XPATH, self.show_photos_button_xpath))

    def find_items_cards(self):
        return len(self.driver.find_elements(By.XPATH, self.items_card_xpath))

    def find_watch_button_in_items_cards(self):
        return len(self.driver.find_elements(By.XPATH, self.watch_button_xpath))

    def find_item_images(self):
        return len(self.driver.find_elements(By.CLASS_NAME, self.items_photos_class_name))

    def check_filter(self):
        self.driver.find_element(By.XPATH, self.filter_button_xpath).click()
        self.driver.find_element(By.XPATH, self.filter_category_xpath).click()

    def item_prices(self):
        return self.driver.find_elements(By.XPATH, self.price_xpath)






