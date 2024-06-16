import allure
from conftest import driver
from pages.main_page import MainPage
from pages.header_page import HeaderPage


class TestSwitchPages:

    @allure.title('Переход со страницы зазказа на главную по клику на Самокат в лого')
    def test_click_scooter_in_header_open_main_page_scooter(self, driver):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        main_page.click_order_in_header()
        header_page.click_scooter_logo()
        assert main_page.find_header_in_main_page()

    @allure.title('Переход со страницы зазказа на Дзен по клику на Яндекс в лого')
    def test_click_yandex_go_to_dzen(self, driver):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        main_page.find_logo_with_wait()
        main_page.allow_cookie()
        main_page.click_order_in_header()
        header_page.click_yandex_logo()
        header_page.switch_to_next_browser_tab()
        assert header_page.find_element_in_dzen_page()
