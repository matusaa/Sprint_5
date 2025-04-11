import pytest
from conftest import Constants
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

# Проверка выхода из аккаунта  по кнопке "Выйти" в личном кабинете
class TestLogout:
    def test_logout_from_lk(self, driver, login):
        driver.find_element(*LK_BUTTON).click()
        login()
        driver.find_element(*LK_BUTTON).click()
        logout_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(LOGOUT_BUTTON))
        logout_button.click()
        WebDriverWait(driver, 5).until(EC.url_to_be(Constants.URL_LOGIN))
        assert driver.current_url == Constants.URL_LOGIN
