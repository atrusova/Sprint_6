import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from conftest import driver


class HeaderPage(BasePage):
    YANDEX_LOGO = By.XPATH, ".//*[@alt='Yandex']"
    SCOOTER_LOGO = By.XPATH, ".//*[contains(@class, 'Header_LogoScoote')]"
    DZEN_HEADER = By.XPATH, "//button[text()='Найти']"

    @allure.step('Клик на лого Яндекс в шапке')
    def click_yandex_logo(self):
        self.click_to_element(self.YANDEX_LOGO)

    @allure.step('Клик на лого Самокат в шапке')
    def click_scooter_logo(self):
        self.click_to_element(self.SCOOTER_LOGO)

    @allure.step('Найти элемент на странице Дзен')
    def find_element_in_dzen_page(self):
        return self.find_element_with_wait(self.DZEN_HEADER)

    @allure.step('Перейти на следующую вкладку')
    def switch_to_next_browser_tab(self, driver):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
