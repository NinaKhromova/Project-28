import time

import selenium.webdriver.chrome.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_tab_link_xpath(page_url):
    return f"//div[contains(@class, 'tabsHeaderWrapper')]/a[@href='{page_url}']"


def get_main_info_icon_xpath(data_icon):
    return f"//div[contains(@class, 'infoBlock')]//*[name()='svg'][@data-icon='{data_icon}']"


class SellerPage:
    def __init__(self, driver: selenium.webdriver.chrome.webdriver.WebDriver):
        self.driver = driver

        self.add_to_favorites_button_xpath = "//div[contains(@class, 'actions')]//*[name()='svg'][@data-icon=" \
                                             "'star_outline']/ancestor::button"
        self.remove_from_favorites_button_xpath = "//div[contains(@class, 'actions')]//*[name()='svg']" \
                                                  "[@data-icon='star']/ancestor::button"
        self.favorite_button_xpath = "//div[contains(@class, 'actions')]//*[name()='svg'][@data-icon='star' " \
                                     "or @data-icon='star_outline']/ancestor::button"
        self.added_to_favorites_notification_xpath = '//*[text() = "Продавец добавлен в избранное"]'
        self.removed_from_favorites_notification_xpath = '//*[text() = "Продавец удален из избранных"]'
        self.undo_success_notification_xpath = '//*[text() = "Продавец восстановлен"]'
        self.undo_button_xpath = "//*[name()='svg'][@data-icon='undo']/ancestor::button"

        self.more_button_xpath = "//div[contains(@class, 'actions')]//*[name()='svg'][@data-icon='more_vert']" \
                                 "/ancestor::button"
        self.add_to_black_list_button_xpath = '//*[text() = "Добавить в черный список"]'
        self.remove_from_black_list_button_xpath = '//*[text() = "Убрать из черного списка"]'
        self.removed_from_black_list_notification_xpath = '//*[contains(text(), "удален из Вашего черного списка")]'
        self.added_to_black_list_notification_xpath = '//*[contains(text(), "добавлен в Ваш черный список")]'
        self.black_list_icon_xpath = "//div[contains(@class, 'avatarContainer')]/*[name()='svg']" \
                                     "[@data-icon='account_off']"
        self.news_block_xpath = "//div[contains(@class, 'card')]//span[contains(text(), 'Новости')]"

    def add_seller_to_favorites(self):
        self.__wait_for_favorite_button()
        if self.__is_seller_favorite():
            self.__click_remove_from_favorites_button()

        self.__click_add_to_favorites_button()

    def remove_seller_from_favorites(self):
        self.__wait_for_favorite_button()
        if not self.__is_seller_favorite():
            self.__click_add_to_favorites_button()

        self.__click_remove_from_favorites_button()

    def get_added_to_favorites_notification(self):
        self.driver.find_element(By.XPATH, self.added_to_favorites_notification_xpath)

    def get_removed_from_favorites_notification(self):
        self.driver.find_element(By.XPATH, self.removed_from_favorites_notification_xpath)

    def get_undo_success_notification(self):
        self.driver.find_element(By.XPATH, self.undo_success_notification_xpath)

    def click_undo_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.undo_button_xpath))
        )
        self.driver.find_element(By.XPATH, self.undo_button_xpath).click()

    def add_to_black_list(self):
        if self.__is_seller_in_black_list():
            self.__open_add_menu()
            self.__click_remove_from_black_list()
            self.get_removed_from_black_list_success_notification()

        self.__open_add_menu()
        self.__click_add_to_black_list()

    def remove_from_black_list(self):
        if not self.__is_seller_in_black_list():
            self.__open_add_menu()
            self.__click_add_to_black_list()
            self.get_added_to_black_list_success_notification()

        self.__open_add_menu()
        self.__click_remove_from_black_list()

    def get_added_to_black_list_success_notification(self):
        self.driver.find_element(By.XPATH, self.added_to_black_list_notification_xpath)

    def get_removed_from_black_list_success_notification(self):
        self.driver.find_element(By.XPATH, self.removed_from_black_list_notification_xpath)

    def check_sub_page_link_exist(self, url):
        self.driver.find_element(By.XPATH, get_tab_link_xpath(url))

    def check_info_block_exist(self, data_icon):
        self.driver.find_element(By.XPATH, get_main_info_icon_xpath(data_icon))

    def check_news_block_exist(self):
        self.driver.find_element(By.XPATH, self.news_block_xpath)

    def __is_seller_favorite(self):
        if len(self.driver.find_elements(By.XPATH, self.remove_from_favorites_button_xpath)) > 0:
            return True
        else:
            return False

    def __click_add_to_favorites_button(self):
        self.__wait_for_favorite_button()
        self.driver.find_element(By.XPATH, self.add_to_favorites_button_xpath).click()

    def __click_remove_from_favorites_button(self):
        self.__wait_for_favorite_button()
        self.driver.find_element(By.XPATH, self.remove_from_favorites_button_xpath).click()

    def __wait_for_favorite_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.favorite_button_xpath))
        )

    def __open_add_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.more_button_xpath))
        )

        self.driver.find_element(By.XPATH, self.more_button_xpath).click()

    def __is_seller_in_black_list(self):
        time.sleep(2)
        if len(self.driver.find_elements(By.XPATH, self.black_list_icon_xpath)) > 0:
            return True
        else:
            return False

    def __click_add_to_black_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_black_list_button_xpath))
        )

        self.driver.find_element(By.XPATH, self.add_to_black_list_button_xpath).click()

    def __click_remove_from_black_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.remove_from_black_list_button_xpath))
        )

        self.driver.find_element(By.XPATH, self.remove_from_black_list_button_xpath).click()






