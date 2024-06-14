import allure
from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helpers import generate_order_info
from locators.main_page_locators import MainPageLocators


class TestOrderPage:

    @allure.title('Создание заказа по кнопке Заказать из шапки')
    def test_create_order_from_header(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_info = generate_order_info()
        main_page.find_element_with_wait(MainPageLocators.SCOOTER_IMAGE)
        main_page.allow_cookie()
        main_page.click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
        assert order_page.set_order(order_info) == 'Посмотреть статус'

    @allure.title('Создание заказа по кнопке Заказать из блока Как это работает')
    def test_create_order_from_button_in_the_middle_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_info = generate_order_info()
        main_page.find_element_with_wait(MainPageLocators.SCOOTER_IMAGE)
        main_page.allow_cookie()
        main_page.scroll_to_element(MainPageLocators.ORDER_BUTTON_IN_MIDDLE_PAGE)
        main_page.click_to_element(MainPageLocators.ORDER_BUTTON_IN_MIDDLE_PAGE)
        assert order_page.set_order(order_info) == 'Посмотреть статус'
