import pytest
from selenium import webdriver
from locators import *
import random

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()


@pytest.fixture
def generate_login():
    login = random.randint(111, 999)
    return f"alexmatus19{login}@mail.ru"

@pytest.fixture
def generate_password():
    password = random.randint(111111, 9999999)
    return password

class Constants:
    URL = 'https://stellarburgers.nomoreparties.site/'
    URL_REG = 'https://stellarburgers.nomoreparties.site/register'
    URL_LOGIN = 'https://stellarburgers.nomoreparties.site/login'
    URL_PROFILE = 'https://stellarburgers.nomoreparties.site/account/profile'
    NAME = 'Alex'
    EMAIL = 'Alex19111@mail.ru'
    PASSWORD = '123456'

@pytest.fixture
def constants():
    return Constants()

@pytest.fixture
def login(driver):
    def _login():
        driver.find_element(*LOGIN_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*LOGIN_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*LOGIN_BUTTON).click()
    return _login