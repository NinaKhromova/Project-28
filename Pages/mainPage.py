from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import selenium.webdriver.chrome.webdriver


class MainPage:
    def __init__(self, driver: selenium.webdriver.chrome.webdriver.WebDriver):
        self.driver = driver

        self.account_button_id = 'desktop-profile-button'
        self.login_mode_button_xpath = '//*[contains(text(), "Вход в систему")]'
        self.email_field_name = 'email'
        self.password_field_xpath = '/html/body/div[4]/div/div/div/div/div[1]/div[1]/form/div[2]/div[2]/div[1]/div[1]/'\
                                    'input'
        self.login_button_xpath = '/html/body/div[4]/div/div/div/div/div[1]/div[2]/button[1]/span'
        self.logout_button_xpath = '//*[@id="app"]/div/div[6]/div[1]/div[2]/div/div/div[5]/div/b'
        self.functional_menu_button_id = 'desktop-functional-menu-button'
        self.functional_menu_cart_button_xpath = '//*[@id="app"]/div/div[6]/div[2]/div[2]/div/div/div[2]'
        self.search_field_id = 'desktop-search-field'
        self.red_badge_xpath = '//*[@id="desktop-cart-button"]/button/span'
        self.invalid_creds_error_notification_xpath = '//*[contains(text(), "неверный адрес электронной почты ' \
                                                      'или пароль")]'
        self.light_error_incorrect_email_format_xpath = '//*[contains(text(), "К сожалению, Вы указали адрес ' \
                                                        'электронной почты в неверном формате")]'
        self.secondary_toolbar_button_xpath = '//*[contains(text(), "Себе и любимым")]'
        self.category_link_xpath = '//*[contains(text(), "Драгоценности и украшения"]'
        self.category_menu_button_xpath = '//*[contains (text(), "Бытовая техника"]'
        self.category_logo_button_xpath = '//*[@id="app"]/div/div[4]/nav/div/div[1]/div/a'
        self.inner_category_menu_link_xpath = '//*[contains(text(),  "Вентиляторы"]'
        self.unsuccessful_search_notification_xpath = '//*[contains(text(), "не удалось найти ни одного лота")]'
        self.scroll_top_button_xpath = '//button[contains(@class, "goTopButton")]'
        self.product_card_xpath = '//div[contains(@class, "itemCardList")]'
        self.show_photos_button_xpath = '//*[contains(@class, "actionButtons")]//button[@title="Показать фотографии"]'
        self.watch_button_xpath = '//*[contains(@class, "actionButtons")]//button[@title = "Наблюдать"]'

    def login(self):
        self.click_account_button()
        self.click_login_mode_button()
        self.enter_email("falling2@yandex.ru")
        self.enter_password("kakadu1")
        self.click_login_button()
        time.sleep(1)

    def click_scroll_top_button(self):
        self.driver.find_element(By.XPATH, self.scroll_top_button_xpath).click()

    def click_account_button(self):
        self.driver.find_element(By.ID, self.account_button_id).click()

    def click_login_mode_button(self):
        self.driver.find_element(By.XPATH, self.login_mode_button_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.NAME, self.email_field_name ).clear()
        self.driver.find_element(By.NAME, self.email_field_name).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def open_profile_menu(self):
        self.driver.find_element(By.ID, self.account_button_id).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()

    def open_functional_menu(self):
        self.driver.find_element(By.ID, self.functional_menu_button_id).click()

    def find_functional_menu_cart_button(self):
        self.driver.find_element(By.XPATH, self.functional_menu_cart_button_xpath)

    def search_field_exist(self):
        self.driver.find_element(By.ID, self.search_field_id)

    def search(self, text):
        self.driver.find_element(By.ID, self.search_field_id).clear()
        self.driver.find_element(By.ID, self.search_field_id).send_keys(text + Keys.RETURN)

    def check_badge(self):
        self.driver.find_element(By.XPATH, self.red_badge_xpath)

    def check_error_notification_invalid_password(self, invalid_password):
        self.driver.find_element(By.XPATH, self.password_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(invalid_password)
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        self.driver.find_element(By.XPATH, self.invalid_creds_error_notification_xpath)

    def check_error_notification_invalid_email(self, invalid_email):
        self.driver.find_element(By.NAME, self.email_field_name ).clear()
        self.driver.find_element(By.NAME, self.email_field_name).send_keys(invalid_email)
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        self.driver.find_element(By.XPATH, self.invalid_creds_error_notification_xpath)

    def check_light_error_incorrect_email_format(self, invalid_email):
        self.driver.find_element(By.NAME, self.email_field_name).clear()
        self.driver.find_element(By.NAME, self.email_field_name).send_keys(invalid_email)
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        self.driver.find_element(By.XPATH, self.light_error_incorrect_email_format_xpath)

    def app_secondary_toolbar(self):
        self.driver.find_element(By.XPATH, self.secondary_toolbar_button_xpath).click()
        self.driver.find_element(By.XPATH, self.category_link_xpath)

    def category_menu_button(self):
        self.driver.find_element(By.XPATH, self.category_menu_button_xpath).click()
        self.driver.find_element(By.XPATH, self.inner_category_menu_link_xpath)

    def logo_button(self):
        self.driver.find_element(By.XPATH, self.category_logo_button_xpath).click()
        self.driver.find_element(By.XPATH, self.category_menu_button_xpath)

    def search_unexisted_item(self, text):
        self.driver.find_element(By.ID, self.search_field_id).clear()
        self.driver.find_element(By.ID, self.search_field_id).send_keys(text + Keys.RETURN)
        self.driver.find_element(By.XPATH, self.unsuccessful_search_notification_xpath)










