import allure
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators


class HeaderPage(BasePage):

    @allure.step('Клик на лого Яндекс в шапке')
    def click_yandex_logo(self):
        self.click_to_element(HeaderLocators.YANDEX_LOGO)

    @allure.step('Клик на лого Самокат в шапке')
    def click_scooter_logo(self):
        self.click_to_element(HeaderLocators.SCOOTER_LOGO)

    @allure.step('Найти элемент на странице Дзен')
    def find_element_in_dzen_page(self):
        return self.find_element_with_wait(HeaderLocators.DZEN_HEADER)
