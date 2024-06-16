import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Клик на вопрос, получение текста ответа")
    def click_question_get_answer(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.find_element_with_wait(locator_q_formatted)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    def click_order_in_header(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_in_middle_page(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_IN_MIDDLE_PAGE)

    def find_logo_with_wait(self):
        self.find_element_with_wait(MainPageLocators.SCOOTER_IMAGE)

    def find_header_in_main_page(self):
        return self.find_element_with_wait(MainPageLocators.HEAD_MAIN_PAGE)

    def scroll_to_last_element_in_page(self):
        self.scroll_to_element(MainPageLocators.LAST_ELEMENT_IN_PAGE_TO_SCROLL)

    def scroll_to_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_IN_MIDDLE_PAGE)
