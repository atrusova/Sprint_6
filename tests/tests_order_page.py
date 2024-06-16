import allure
from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helpers import generate_order_info


class TestOrderPage:

    @allure.title('Создание заказа по кнопке Заказать из шапки')
    def test_create_order_from_header(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_info = generate_order_info()
        main_page.find_logo_with_wait()
        main_page.allow_cookie()
        main_page.click_order_in_header()
        order_page.set_order_first_page(order_info)
        assert order_page.set_order_last_page(order_info) == 'Посмотреть статус'


    @allure.title('Создание заказа по кнопке Заказать из блока Как это работает')
    def test_create_order_from_button_in_the_middle_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_info = generate_order_info()
        main_page.find_logo_with_wait()
        main_page.allow_cookie()
        main_page.scroll_to_order_button()
        main_page.click_order_in_middle_page()
        order_page.set_order_first_page(order_info)
        assert order_page.set_order_last_page(order_info) == 'Посмотреть статус'
