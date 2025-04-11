from conftest import Constants
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestLKToConstructorNavigation:
    # Проверка перехода из Личного кабинета в конструктор по клику на "Конструктор"
    def test_open_constructor_from_lk(self, driver, login):
        driver.find_element(*LK_BUTTON).click()
        login()
        driver.find_element(*LK_BUTTON).click()
        driver.find_element(*CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(Constants.URL))
        assert driver.current_url == Constants.URL

    # Проверка перехода из Личного кабинета в конструктор по клику на логотип "Stellar Burgers"
    def test_open_constructor_from_lk_via_logo(self, driver, login):
        driver.find_element(*LK_BUTTON).click()
        login()
        driver.find_element(*LK_BUTTON).click()
        driver.find_element(*LOGO).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(Constants.URL))
        assert driver.current_url == Constants.URL