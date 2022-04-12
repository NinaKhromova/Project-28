from selenium import webdriver
import time
import unittest
from Pages.mainPage import MainPage
from Pages.searchResultPage import SearchResultPage
from Pages.cartPage import CartPage


class LoginTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/chromedriver')
    main = MainPage(driver)
    cart = CartPage(driver)
    searchResults = SearchResultPage(driver)


    @classmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        """Проверка регистрации пользователя, входа на сайт и выхода с сайта """
        self.driver.get("https://meshok.net/")

        self.main.click_account_button()
        self.main.click_login_mode_button()
        self.main.enter_email("falling2@yandex.ru")
        self.main.enter_password("kakadu1")
        self.main.click_login_button()
        time.sleep(1)
        self.main.open_profile_menu()
        self.main.click_logout_button()

    def test_check_functional_menu(self):
        """Проверка появления фунционального меню после клика на кнопку меню """
        self.driver.get("https://meshok.net/")
        self.main.open_functional_menu()
        self.main.find_functional_menu_cart_button()

    def test_search_field_exist(self):
        """Проверка наличия поля поиска на главной странице"""
        self.driver.get("https://meshok.net/")
        self.main.open_functional_menu()
        self.main.search_field_exist()

    def test_scroll_top_button(self):
        """Проверка кнопки прокрутки к началу"""
        self.driver.get("https://meshok.net/")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        self.main.click_scroll_top_button()
        time.sleep(1)
        self.assertEqual(self.driver.execute_script("return window.pageYOffset"), 0)

    def test_app_secondary_toolbar(self):
        """Проверка кликабельности кнопки в верхнем меню и перехода в раздел категорий товаров"""
        self.driver.get("https://meshok.net/")
        self.main.app_secondary_toolbar()

    def test_category_menu_button(self):
        """Проверка кликабельности кнопок в меню категорий на главной странице"""
        self.driver.get("https://meshok.net/")
        self.main.category_menu_button()

    def test_logo_button(self):
        """Проверка кликабельности кнопки-лого и возврата на главную страницу сайта"""
        self.driver.get("https://meshok.net/good/10")
        self.main.logo_button()

    def test_search(self):
        """Проверка осуществления поиска через поле поиск"""
        self.driver.get("https://meshok.net/")
        self.main.search("брошь")
        time.sleep(2)
        self.searchResults.find_search_results()

    def test_item_cards_exist(self):
        """Проверка наличия карточек товаров на странице поиска"""
        self.driver.get("https://meshok.net/")
        self.main.search("брошь")
        time.sleep(1)
        items_card_count = self.searchResults.find_items_cards()
        self.assertNotEqual(items_card_count, 0)

    def test_show_photos_button_exists_in_item_cards(self):
        """Проверка наличия кнопки просмотр фото в карточках товаров"""
        self.driver.get("https://meshok.net/")
        self.main.search("брошь")
        time.sleep(1)
        photos_buttons_count = self.searchResults.find_photos_button_in_items_cards()
        items_card_count = self.searchResults.find_items_cards()
        self.assertNotEqual(photos_buttons_count, 0)
        self.assertNotEqual(items_card_count, 0)
        self.assertEqual(photos_buttons_count, items_card_count)

    def test_watch_button_exists_in_items_cards(self):
        """Проверка наличия кнопки наблюдать в карточках товаров"""
        self.driver.get("https://meshok.net/")
        self.main.search("брошь")
        time.sleep(1)
        watch_buttons_count = self.searchResults.find_watch_button_in_items_cards()
        items_card_count = self.searchResults.find_items_cards()
        self.assertNotEqual(watch_buttons_count, 0)
        self.assertNotEqual(items_card_count, 0)
        self.assertEqual(watch_buttons_count, items_card_count)

    def test_images_exists_in_items_cards(self):
        """Проверка наличия фотографий во всех карточках товаров при поиске"""
        self.driver.get("https://meshok.net/")
        self.main.search("брошь")
        time.sleep(1)
        images_count = self.searchResults.find_item_images()
        items_card_count = self.searchResults.find_items_cards()
        self.assertNotEqual(images_count, 0)
        self.assertNotEqual(items_card_count, 0)
        self.assertEqual(images_count, items_card_count)

    def test_select_sub_category(self):
        """Проверка возможности уточнить категорию на списке лотов"""
        self.driver.get("https://meshok.net/listing?good=115")
        self.searchResults.sub_category_click('Газеты, журналы')
        self.searchResults.check_current_category('Газеты, журналы')

    def test_filter(self):
        """Проверка сортировки с помощью фильтра"""
        self.driver.get("https://meshok.net/listing?search=%D0%B1%D1%80%D0%BE%D1%88%D1%8C")
        self.searchResults.check_filter()
        elems = self.searchResults.item_prices()
        texts = list(map(lambda x: x.text, elems))
        rubbles_only = list(filter(lambda x: '₽' in x, texts))
        numbers = list(map(lambda x: float(x.replace(' ', '').replace(',', '.').replace('₽', '')), rubbles_only))
        print(numbers)
        assert numbers == sorted(numbers), "Sort by price doesn't work!"

    def test_add_to_the_cart(self):
        """Проверка возможности добавления товаров в корзину кликом по значку в  карточке товара"""
        self.driver.get("https://meshok.net/listing?opt=3&search=%D0%B1%D1%80%D0%BE%D1%88%D1%8C")
        time.sleep(5)
        self.cart.add_to_cart()

    def test_red_badge(self):
        """Проверка появления красного кружка с количеством добавленного товара возле значка корзины
        после добавления товаров в корзину"""
        self.test_add_to_the_cart()
        self.main.check_badge()

    def test_clear_cart(self):
        """Проверка кнопки очистить корзину"""
        self.test_add_to_the_cart()
        self.driver.get("https://meshok.net/buying/cart")
        time.sleep(1)
        self.cart.clear_cart()

    def test_select_item_in_cart(self):
        """Проверка возможности выбора и выделения одного лота в корзине для оформления заказа"""
        self.driver.get("https://meshok.net/")
        self.main.click_account_button()
        self.main.click_login_mode_button()
        self.main.enter_email("falling2@yandex.ru")
        self.main.enter_password("kakadu1")
        self.main.click_login_button()
        time.sleep(1)
        self.test_add_to_the_cart()

        self.cart.select_item_in_cart()


    def test_delete_item_from_the_cart(self):
        """Проверка возможности удаления одного лота из корзины"""
        self.test_add_to_the_cart()
        self.driver.get("https://meshok.net/buying/cart")
        time.sleep(1)
        self.cart.delete_the_item_from_cart()

    def test_the_order_button(self):
        """Проверка кликабельности кнопки Оформить в корзине и перехода к форме с кнопкой купить"""
        self.test_select_item_in_cart()
        time.sleep(1)
        self.cart.order_button()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')






