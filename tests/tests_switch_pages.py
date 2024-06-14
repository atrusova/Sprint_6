import allure
from conftest import driver
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.header_page import HeaderPage


class TestSwitchPages:

    @allure.title('Переход со страницы зазказа на главную по клику на Самокат в лого')
    def test_click_scooter_in_header_open_main_page_scooter(self, driver):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        main_page.click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
        header_page.click_scooter_logo()
        assert main_page.find_element_with_wait(MainPageLocators.HEAD_MAIN_PAGE)

    @allure.title('Переход со страницы зазказа на Дзен по клику на Яндекс в лого')
    def test_click_yandex_go_to_dzen(self, driver):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        main_page.find_element_with_wait(MainPageLocators.SCOOTER_IMAGE)
        main_page.allow_cookie()
        main_page.click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
        header_page.click_yandex_logo()
        header_page.switch_to_next_browser_tab(driver)
        assert header_page.find_element_in_dzen_page()
