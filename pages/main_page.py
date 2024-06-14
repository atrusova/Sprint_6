import time
import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class MainPage(BasePage):

    @allure.step("Клик на вопрос, получение текста ответа")
    def click_question_get_answer(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)
