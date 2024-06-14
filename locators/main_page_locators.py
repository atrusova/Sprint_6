from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]' # Вопрос на главной странице, используется функцией для подстановки номера вопроса
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]' # Ответ на главной странице, используется функцией для подстановки номера ответа

    SCOOTER_IMAGE = By.XPATH, ".//*[@alt='Scooter blueprint']" # Ссылка "Самокат" в шапке ведущая на главную самоката
    LAST_ELEMENT_IN_PAGE_TO_SCROLL = By.XPATH, ".//*[text()='Я жизу за МКАДом, привезёте?']" # Последний вопрос на главной, для прокрутки страницы

    ORDER_BUTTON_HEADER = By.XPATH, ".//*[contains(@class, 'Header')]/*[text()='Заказать']" # Кнопка Заказать в шапке
    ORDER_BUTTON_IN_MIDDLE_PAGE = By.XPATH, ".//*[contains(@class, 'Home_FinishButton')]/*[text()='Заказать']" # Кнопка
    HEAD_MAIN_PAGE = By.XPATH, ".//*[text()='Самокат ']" # Заголовок главной страницы

    COOKIE_BUTTON = By.XPATH, ".//*[text()='да все привыкли']" # Кнопка принятия куки
