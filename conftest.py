import pytest
from selenium import webdriver
from locators import *
import random
from constants import Constants

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(Constants.URL)
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