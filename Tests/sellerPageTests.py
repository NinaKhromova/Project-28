from selenium import webdriver

import time
import unittest
from Pages.mainPage import MainPage
from Pages.sellerPage import SellerPage


class SellerPageTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/chromedriver')
    seller = SellerPage(driver)
    main = MainPage(driver)

    @classmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://meshok.net/info/549857")

        cls.main.login()

    def test_add_favorite_seller(self):
        """Проверка добавления продавца в избранные """
        self.seller.add_seller_to_favorites()
        self.seller.get_added_to_favorites_notification()

    def test_remove_favorite_seller(self):
        """Проверка удаления продавца из избранных """
        self.seller.remove_seller_from_favorites()
        self.seller.get_removed_from_favorites_notification()

    def test_undo_favorite_seller(self):
        """Проверка UNDO """
        self.seller.remove_seller_from_favorites()
        self.seller.get_removed_from_favorites_notification()
        self.seller.click_undo_button()
        self.seller.get_undo_success_notification()

    def test_add_to_black_list(self):
        """Проверка добавления в черный список """
        self.seller.add_to_black_list()
        self.seller.get_added_to_black_list_success_notification()

    def test_remove_from_black_list(self):
        """Проверка удаления из черного списка """
        self.seller.remove_from_black_list()
        self.seller.get_removed_from_black_list_success_notification()

    def test_lots_list_link(self):
        """Проверка наличия ссылки на страницу лотов """
        self.seller.check_sub_page_link_exist('/info/549857/lots')

    def test_info_page_link(self):
        """Проверка наличия ссылки на страницу информации """
        self.seller.check_sub_page_link_exist('/info/549857/lots')

    def test_buyers_reviews_link(self):
        """Проверка наличия ссылки на страницу отзывов покупателей """
        self.seller.check_sub_page_link_exist('/info/549857/salesman')

    def test_sellers_reviews_link(self):
        """Проверка наличия ссылки на страницу отзывов продавцов """
        self.seller.check_sub_page_link_exist('/info/549857/buyer')

    def test_forum_link(self):
        """Проверка наличия ссылки на страницу форума """
        self.seller.check_sub_page_link_exist('/info/549857/forum')

    def test_city_info_block_01(self):
        """Проверка наличия информации о городе """
        self.seller.check_info_block_exist('location_city')

    def test_city_info_block_02(self):
        """Проверка наличия информации о регистрации """
        self.seller.check_info_block_exist('person')

    def test_city_info_block_03(self):
        """Проверка наличия информации о последнем визите """
        self.seller.check_info_block_exist('clock_outline')

    def test_city_info_block_04(self):
        """Проверка наличия информации об избранных """
        self.seller.check_info_block_exist('star_outline')

    def test_city_info_block_05(self):
        """Проверка наличия информации о рейтинге """
        self.seller.check_info_block_exist('chartLine')

    def test_city_info_block_06(self):
        """Проверка наличия информации об ID """
        self.seller.check_info_block_exist('vpn_key')

    def test_news_block(self):

        """Проверка наличия блока новостей """
        self.seller.check_news_block_exist()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')






