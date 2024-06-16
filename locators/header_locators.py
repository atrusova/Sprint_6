from selenium.webdriver.common.by import By

class HeaderLocators:
    YANDEX_LOGO = By.XPATH, ".//*[@alt='Yandex']" # Логотип Яндекса в шапке
    SCOOTER_LOGO = By.XPATH, ".//*[contains(@class, 'Header_LogoScoote')]" # Логотип Самокат в шапке
    DZEN_HEADER = By.XPATH, "//button[text()='Найти']" # Элемент Найти на странцие Дзен
