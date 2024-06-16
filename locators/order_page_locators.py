from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = By.XPATH, './/*[@placeholder="* Имя"]' # Поле Имя на форме заказа
    SURNAME_INPUT = By.XPATH, './/*[@placeholder="* Фамилия"]' # Поле Фамилия на форме заказа
    ADDRESS_INPUT = By.XPATH, './/*[@placeholder="* Адрес: куда привезти заказ"]' # Поле Адрес на форме заказа
    METRO = By.XPATH, './/*[@placeholder="* Станция метро"]' # Поле Метро на форме заказа
    PHONE = By.XPATH, './/*[@placeholder="* Телефон: на него позвонит курьер"]' # Поле Телефон на форме заказа

    NEXT_TO_ORDER_BUTTON = By.XPATH, './/*[text()="Далее"]' # Кнопка Далее на странице заказа

    TIME_TO_DELIVERY_CALENDAR = By.XPATH, './/*[@placeholder="* Когда привезти самокат"]' # Поле "Когда привезти заказ" на форме заказа
    CHOOSE_DAY_BRING_SCOOTER = By.XPATH, './/*[@aria-label="Choose четверг, 27-е июня 2024 г."]' # Дата в календаре поля "Когда привезти заказ" на форме заказа
    RENT_TIME_DROPDOWN = By.XPATH, './/div[text()="* Срок аренды"]' # Выпадающий список в поле Срок аренды на форме заказа
    CHOOSE_RENT_TIME = By.XPATH, './/div[text() = "четверо суток"]' # Значание выпадающего списка Срок аренды на форме заказа
    CHOOSE_SCOOTER_COLOR = By.XPATH, './/input[@id="grey"]' # Чекбокс в поле Цвет самоката на форме заказа
    COMMENT_FOR_COURIER = By.XPATH, './/*[@placeholder="Комментарий для курьера"]' # Поле Комментарий для курьера на форме заказа

    ORDER_BUTTON_IN_THE_END_ORDER = By.XPATH, ".//*[contains(@class, 'Order_Buttons')]/*[text()='Заказать']" # Кнопка Заказать на последней странице формы заказа
    CONFIRM_ORDER_BUTTON_ORDER_PAGE = By.XPATH, ".//*[text()='Да']" # Кнопка "Да" в модальном окне подтверждения заказа

    ORDER_COMPLETE_HEADER = By.XPATH, ".//*[text()='Посмотреть статус']" # Кнопка "Посмотреть статус" в модальном окне сформированного заказа

    METRO_LOCATOR = By.XPATH, '//*[@data-index="{}"]' # локартор для значений выпадающего списка Метро, используется функцией для генерации рандомных значений станций


