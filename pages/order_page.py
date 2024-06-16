import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Заполнение полей заказа, переход на вторую страницу заказа')
    def set_order_first_page(self, order_info_dict):
        self.click_to_element(OrderPageLocators.NAME_INPUT)
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, order_info_dict['name'])
        self.click_to_element(OrderPageLocators.SURNAME_INPUT)
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT, order_info_dict['surname'])
        self.click_to_element(OrderPageLocators.ADDRESS_INPUT)
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT, order_info_dict['address'])
        self.click_to_element(OrderPageLocators.METRO)
        locator_v_formatted = self.format_locators(OrderPageLocators.METRO_LOCATOR, order_info_dict['metro'])
        self.click_to_element(locator_v_formatted)
        self.click_to_element(OrderPageLocators.PHONE)
        self.add_text_to_element(OrderPageLocators.PHONE, order_info_dict['phone'])
        self.click_to_element(OrderPageLocators.NEXT_TO_ORDER_BUTTON)

    @allure.step('Заполнение полей на второй странице, завершение заказа')
    def set_order_last_page(self, order_info_dict):
        self.click_to_element(OrderPageLocators.TIME_TO_DELIVERY_CALENDAR)
        self.click_to_element(OrderPageLocators.CHOOSE_DAY_BRING_SCOOTER)
        self.click_to_element(OrderPageLocators.RENT_TIME_DROPDOWN)
        self.click_to_element(OrderPageLocators.CHOOSE_RENT_TIME)
        self.click_to_element(OrderPageLocators.CHOOSE_SCOOTER_COLOR)
        self.click_to_element(OrderPageLocators.COMMENT_FOR_COURIER)
        self.add_text_to_element(OrderPageLocators.COMMENT_FOR_COURIER, order_info_dict['comment'])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_IN_THE_END_ORDER)
        self.click_to_element(OrderPageLocators.CONFIRM_ORDER_BUTTON_ORDER_PAGE)
        self.find_element_with_wait(OrderPageLocators.ORDER_COMPLETE_HEADER)
        return self.get_text_from_element(OrderPageLocators.ORDER_COMPLETE_HEADER)

    @allure.step('Форматирование и возврат локатора для поля Метро в виде значения с рандомным индексом')
    def reformat_metro_locator(self, order_dict_info):
        locator_x_formatted = self.format_locators(OrderPageLocators.METRO_LOCATOR, order_dict_info['metro'])
        return locator_x_formatted
