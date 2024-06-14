import pytest
import options
import random as r
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    option = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=option)
    option.add_argument('--window-size=1920,1080')
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()